"""Optional real-browser smoke checks. Run: python tests/browser_smoke.py

Requires Playwright and Chromium. This is intentionally optional so the
website remains runnable without a browser-testing dependency.
"""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
PAGES=['index.html','lessons/01-how-ai-reads-words/index.html','lessons/02-word-embeddings/index.html','lessons/04-ai-context-memory/index.html','lessons/05-ai-retrieval/index.html']

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
          assert page.locator('#vectors .chip').count()==1
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
          page.locator('#factValue').fill('Milo')
          page.locator('#addFact').click()
          page.locator('#ask').click()
          assert 'Your dog’s name is Milo.' in page.locator('#messages').inner_text()
          page.locator('#clear').click()
          page.locator('#ask').click()
          assert 'I don’t know that from the current context.' in page.locator('#messages').inner_text()
          assert page.locator('#context .fact').count()==0
        if '05-' in path:
          assert 'How does AI use tools' in page.locator('h1').inner_text()
          page.locator('#userQuestion').fill('what is 5 x 2')
          page.locator('#askQuestion').click()
          assert '5 × 2 = 10' in page.locator('#toolChat').inner_text()
          page.locator('#runAgent').click()
          page.wait_for_timeout(5500)
          assert 'Goal reached' in page.locator('#agentChat').inner_text()
          page.locator('#agentScenario').select_option('headphones')
          page.locator('#runAgent').click()
          page.wait_for_timeout(5500)
          assert 'Goal reached' in page.locator('#agentChat').inner_text()
          page.locator('#restartAgent').click()
          assert 'Goal reached' not in page.locator('#agentChat').inner_text()
        page.close()
      print('Desktop checks passed' if width==1280 else 'Mobile checks passed')
    browser.close()
if __name__=='__main__':check()
