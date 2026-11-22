"""Lesson 05 regression: actual prepared questions, tool toggle combinations, agent replay.
Run: python tests/test_lesson05_browser.py (Playwright + Chromium required).
"""
from pathlib import Path
import itertools
import shutil
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / 'lessons/05-ai-retrieval/index.html').read_text(encoding='utf-8')


def ready(page):
    page.wait_for_function("!document.querySelector('[data-example=weather]').disabled", timeout=6000)


def answer(page, text):
    page.wait_for_function('(needle) => !!document.querySelector("#toolChat .from-ai")?.textContent.includes(needle)', arg=text, timeout=6000)
    ready(page)


def configure(page, weather=True, calc=True, search=True):
    for index, value in enumerate([weather, calc, search]):
        box = page.locator('#configuredTools input').nth(index)
        if box.is_checked() != value:
            (box.check if value else box.uncheck)()
    ready(page)


def run_agent(page, result):
    page.locator('#runAgent').click()
    page.wait_for_function('needle => !!document.querySelector("#agentChat .from-ai")?.textContent.includes(needle)',arg=result, timeout=7000)
    assert page.locator('#runAgent').is_enabled()


def check(page):
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.set_content(HTML)
    assert page.locator('#configuredTools input').count() == 3
    page.evaluate('''() => {
      window._originalLessonTimeout = window.setTimeout;
      window.setTimeout = (fn, delay, ...args) => window._originalLessonTimeout(fn, Math.min(delay, 32), ...args);
    }''')

    # Prepared weather question: when tool is OFF, no old result is retained.
    page.locator('[data-example=weather]').click()
    answer(page, 'cloudy and 14°C')
    assert page.locator('#toolChat .from-tool').count() == 1
    configure(page, weather=False)
    answer(page, 'can’t check a forecast')
    assert 'cloudy and 14°C' not in page.locator('#toolChat').inner_text()
    assert page.locator('#toolChat .from-tool').count() == 0
    configure(page, weather=True)
    answer(page, 'cloudy and 14°C')

    # Simple arithmetic remains answerable when calculator is turned OFF.
    page.locator('[data-example=math]').click()
    answer(page, '5 × 2 = 10')
    assert page.locator('#toolChat .from-tool').count() == 1
    configure(page, calc=False)
    answer(page, '5 × 2 = 10')
    assert page.locator('#toolChat .from-tool').count() == 0
    assert 'without calling a tool' in page.locator('#toolChat').inner_text()
    configure(page, calc=True)

    # A fact can be known without a lookup, but is no longer verified by search.
    page.locator('[data-example=search]').click()
    answer(page, '20 July 1969')
    assert page.locator('#toolChat .from-tool').count() == 1
    configure(page, search=False)
    answer(page, 'can’t verify a source')
    assert page.locator('#toolChat .from-tool').count() == 0
    configure(page, search=True)

    # Exhaustive truth-table of all tool settings, both scenarios, without clock cost.
    for w,c,s in itertools.product([False, True], repeat=3):
        outcome = page.evaluate('''({w,c,s}) => {
          const tools = new Set([...(w?['weather']:[]), ...(c?['calculator']:[]), ...(s?['search']:[])]);
          return { picnic: planFor('picnic','en',tools), headphones: planFor('headphones','en',tools) };
        }''', {'w':w,'c':c,'s':s})
        picnic, headphones = outcome['picnic']['steps'],outcome['headphones']['steps']
        pt = [step['body'] for step in picnic if step['type']=='tool']
        ht = [step['body'] for step in headphones if step['type']=='tool']
        assert all('weather_forecast' not in call for call in pt) == (not w)
        assert all('web_search' not in call for call in ht) == (not s)
        assert all('calculator' not in call for call in ht) == (not c or not s)
        assert len([x for x in ht if 'web_search' in x]) == (2 if s else 0)
        assert ('Sunday looks better' in picnic[-1]['body']) == w
        assert ('Option C' in headphones[-1]['body']) == s
        assert all('indoor' not in step['body'].lower() for step in picnic)

    # Actual on-screen agents animate and finish in all the important conditions.
    page.locator('#agentScenario').select_option('picnic')
    configure(page, weather=True, calc=False, search=False)
    run_agent(page, 'Sunday looks better')
    assert page.locator('#agentChat .from-tool').count() == 1
    assert 'web_search' not in page.locator('#agentChat').inner_text()
    page.locator('#restartAgent').click()
    assert page.locator('#agentChat .from-ai').count() == 0
    configure(page,weather=False)
    run_agent(page,'can’t check the weather')
    assert page.locator('#agentChat .from-tool').count()==0
    assert 'sunny' not in page.locator('#agentChat').inner_text()

    page.locator('#agentScenario').select_option('headphones')
    configure(page, weather=False, calc=True, search=False)
    run_agent(page,'can’t check current products')
    assert page.locator('#agentChat .from-tool').count()==0
    assert 'Option C' not in page.locator('#agentChat').inner_text()
    configure(page, calc=False,search=True)
    run_agent(page,'Option C is the best match')
    assert page.locator('#agentChat .from-tool').count()==2  # two searches, no calculator
    assert '£5' in page.locator('#agentChat').inner_text()
    configure(page, calc=True)
    run_agent(page,'Option C is the best match')
    assert page.locator('#agentChat .from-tool').count()==3

    # Arabic follows the same supported/unavailable logic.
    page.locator('#lang').click()
    assert page.locator('html').get_attribute('dir')=='rtl'
    page.locator('#agentScenario').select_option('picnic')
    configure(page,weather=False)
    run_agent(page,'لا أستطيع التحقق من طقس السبت')
    assert page.locator('#agentChat .from-tool').count()==0
    configure(page,weather=True)
    run_agent(page,'الأحد أفضل للنزهة')
    assert page.locator('#agentChat .from-tool').count()==1
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1')
    assert not errors, errors

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=shutil.which('chromium'), headless=True)
        for w in (1280,390):
            page = browser.new_page(viewport={'width':w,'height':820})
            check(page)
            print('Lesson 5 verified at', w,'px', flush=True)
            page.close()
        browser.close()
