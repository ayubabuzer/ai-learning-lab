"""Optional real-browser smoke checks. Run: python tests/browser_smoke.py

Requires Playwright and Chromium. This is intentionally optional so the
website remains runnable without a browser-testing dependency.
"""
from pathlib import Path
import random
from math import isclose
import shutil
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
PAGES=['index.html','lessons/01-how-ai-reads-words/index.html','lessons/02-word-embeddings/index.html','lessons/04-ai-context-memory/index.html','lessons/05-ai-retrieval/index.html']

def check_calculator_matrix(page):
  """Exercise calculator parser directly; UI only offers prepared questions."""
  good = {'What is 5 x 2?': 10.0,
   '5 * 2': 10.0,
   '5 × 2': 10.0,
   '5X2': 10.0,
   '12 + 8': 20.0,
   '7 - 12': -5.0,
   '-4 x 3': -12.0,
   '5 x -2': -10.0,
   '2.5 x 4': 10.0,
   '1,000 x 2': 2000.0,
   '1e3 * 2': 2000.0,
   '5 / 2': 2.5,
   '5 ÷ 2': 2.5,
   '5 divided by 2': 2.5,
   '5 x 2 plus 3': 13.0,
   'calculate 2 + 3 * 4': 14.0,
   '2 to the power of 3': 8.0,
   'What is 50% of 200?': 100.0,
   '0.1 + 0.2': 0.3,
   '5 / 0.5': 10.0,
   '5 - -2': 7.0,
   '2 * (3 + 4)': 14.0,
   '2 ^ 3 ^ 2': 512.0,
   'احسب ٥ × ٢': 10.0,
   'احسب 5 × 2': 10.0}
  rejects = {'5 / 0': 'zero',
   'five times two': 'unsupported',
   'calculate 2 +': 'unsupported',
   'calculate 2 + 3 *': 'unsupported',
   'calculate 2 + 3 * 4 and weather in London': 'unsupported',
   'calculate 2 + 3 and find recent news': 'unsupported'}
  for q,expected in good.items():
    result=page.evaluate('(q)=>parseMath(q)',q)
    assert 'value' in result and isclose(result['value'],expected,rel_tol=1e-9,abs_tol=1e-9),(q,result,expected)
  for q,reason in rejects.items():
    result=page.evaluate('(q)=>parseMath(q)',q)
    assert result.get('error')==reason,(q,result)
  # Only prepared questions are shown to students.
  assert page.locator('#userQuestion').count()==0
  page.locator('[data-example="math"]').click()
  assert '5 × 2 = 10' in page.locator('#toolChat').inner_text()
  page.locator('#configuredTools input').nth(1).uncheck()
  page.locator('[data-example="math"]').click()
  assert 'no matching enabled tool' in page.locator('#toolChat').inner_text()
  page.locator('#configuredTools input').nth(1).check()
  page.locator('#lang').click()
  page.locator('[data-example="math"]').click()
  assert '5 × 2 = 10' in page.locator('#toolChat').inner_text()
  page.locator('#lang').click()

def check_random_arithmetic(page):
  """Deterministic property-style browser checks for arithmetic precedence."""
  rng=random.Random(1729)
  for _ in range(240):
    a,b,c=[rng.randint(-30,30) for _ in range(3)]
    op=rng.choice(['+','-','*','/'])
    mode=rng.randrange(4)
    if op=='/' and b==0:b=1
    if mode==0:
      expression=f'{a} {op} {b}'
      expected={'+' :lambda:a+b, '-' :lambda:a-b, '*':lambda:a*b, '/':lambda:a/b}[op]()
    elif mode==1:
      expression=f'({a} + {b}) * {c}'
      expected=(a+b)*c
    elif mode==2:
      expression=f'{a} + {b} * {c}'
      expected=a+b*c
    else:
      expression=f'({a} - {b}) / {c or 1}'
      expected=(a-b)/(c or 1)
    result=page.evaluate('(q)=>parseMath(q)',expression)
    assert 'value' in result and isclose(result['value'],expected,abs_tol=1e-8,rel_tol=1e-8),(expression,expected,result)

def check():
  with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('google-chrome') or None)
    for width in [1280,390]:
      for path in PAGES:
        page=browser.new_page(viewport={'width':width,'height':820})
        failures=[]
        page.on('pageerror',lambda err: failures.append(str(err)))
        page.set_content((ROOT/path).read_text(encoding='utf-8'))
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1'),f'{path} overflow at {width}'
        assert not failures,f'{path} browser errors: {failures}'
        if '01-' in path:
          page.locator('#inputText').fill('Hello world!')
          assert page.locator('#pieces .chip').count()==2
          assert page.locator('#identifiers .chip').count()==2
          assert page.locator('#vectorCards .vector-card').count()==4
          assert page.locator('#vectorPlot circle').count()==4
        if '02-' in path:
          original=page.locator('#score').inner_text()
          page.locator('#wordB').select_option('car')
          changed=page.locator('#score').inner_text()
          assert original!=changed,(original,changed)
          assert 'car' in page.locator('#wordPair').inner_text()
          page.locator('#language').click()
          assert page.locator('html').get_attribute('dir')=='rtl'
          assert page.locator('#score').inner_text()==changed
        if '04-' in path:
          page.locator('#factPalette .fact-card').first.click()
          assert page.locator('#context .fact').count()==1
          page.locator('#ask').click()
          assert 'Your dog’s name is Milo.' in page.locator('#messages').inner_text()
          page.locator('#clear').click()
          page.locator('#ask').click()
          assert 'I don’t know that from the current context.' in page.locator('#messages').inner_text()
          assert page.locator('#context .fact').count()==0
          page.locator('#factPalette .fact-card').nth(1).drag_to(page.locator('#dropTarget'))
          assert page.locator('#context .fact').count()==1
        if '05-' in path:
          assert 'How does AI use tools' in page.locator('h1').inner_text()
          check_calculator_matrix(page)
          if width==1280:check_random_arithmetic(page)
          page.locator('#runAgent').click()
          page.wait_for_function("document.querySelector('#agentChat').textContent.includes('Goal reached')", timeout=15000)
          assert 'Goal reached' in page.locator('#agentChat').inner_text()
          if width==1280:
            page.locator('#agentScenario').select_option('headphones')
            page.locator('#runAgent').click()
            page.wait_for_function("document.querySelector('#agentChat').textContent.includes('Goal reached')", timeout=15000)
            assert 'Goal reached' in page.locator('#agentChat').inner_text()
          page.locator('#restartAgent').click()
          assert 'Goal reached' not in page.locator('#agentChat').inner_text()
        page.close()
      print('Desktop checks passed' if width==1280 else 'Mobile checks passed')
    browser.close()
if __name__=='__main__':check()
