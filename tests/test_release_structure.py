"""Dependency-free checks for the six-lesson bilingual AI Learning Lab website.

Run from repository root: python -m unittest discover -s tests -v
These do not replace testing in a real school browser.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
import ast
import unittest

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"
FOLDERS = [
    "01-how-ai-reads-words",
    "02-word-embeddings",
    "03-next-word-prediction",
    "04-ai-context-memory",
    "05-ai-retrieval",  # Retain the stable URL; the page now teaches attention.
    "06-digital-twin",
]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.extend(value for key,value in attrs if key=="href" and value)

class TestRelease(unittest.TestCase):
    def test_one_folder_per_lesson(self):
        self.assertEqual(sorted(p.name for p in LESSONS.iterdir() if p.is_dir()), FOLDERS)

    def test_lesson_docs(self):
        for name in FOLDERS:
            with self.subTest(name=name):
                for fname in (("index.html", "README.md") if name == "06-digital-twin" else ("index.html", "README.md", "README.ar.md")):
                    self.assertTrue((LESSONS/name/fname).is_file())

    def test_root_docs(self):
        for fname in ("index.html","README.md","README.ar.md","TEACHERS.md","TEACHERS.ar.md","CHANGELOG.md","UPLOAD-INSTRUCTIONS.md"):
            with self.subTest(fname=fname):self.assertTrue((ROOT/fname).exists())

    def test_all_internal_links(self):
        pages=[ROOT/"index.html"]+[LESSONS/name/"index.html" for name in FOLDERS]
        for page in pages:
            links=Links();links.feed(page.read_text(encoding="utf-8"))
            for href in links.hrefs:
                parsed=urlsplit(href)
                if parsed.scheme or href.startswith("#") or "${" in href:continue
                target=(page.parent/unquote(parsed.path)).resolve()
                if parsed.path.endswith("/"):target=target/"index.html"
                with self.subTest(page=page.parent.name,href=href):
                    self.assertTrue(target.exists(),f"Missing link: {target}")

    def test_next_and_previous(self):
        for name in FOLDERS:
            t=(LESSONS/name/"index.html").read_text(encoding="utf-8")
            with self.subTest(name=name):
                if name == '06-digital-twin':
                    self.assertIn('href="../05-ai-retrieval/"', t)
                    self.assertIn('href="#finish"', t)
                    self.assertIn('Certificate of Completion', t)
                    self.assertIn('const translations=', t)
                else:
                    self.assertIn('class="lesson-trail"',t)
                    self.assertIn('class="only-ar"',t)

    def test_no_model_brand_required_for_pupils(self):
        for page in [ROOT/"index.html"]+[LESSONS/x/"index.html" for x in FOLDERS]:
            with self.subTest(page=page.parent.name):
                self.assertNotIn('Qwen',page.read_text(encoding="utf-8"))

    def test_king_equations_and_map_overlap(self):
        t=(LESSONS/FOLDERS[1]/"index.html").read_text(encoding="utf-8")
        self.assertIn('mathStep1',t);self.assertIn('mathStep2',t)
        self.assertIn('buckets=new Map()',t)
        self.assertIn('stroke-dasharray',t)
        self.assertEqual((3-1,1-1),(2,0))
        self.assertEqual((2+1,0+3),(3,3))

    def test_attention_explorer(self):
        t=(LESSONS/FOLDERS[4]/"index.html").read_text(encoding="utf-8")
        for value in ('How Does AI Know Which Words to Look At?',
                      'function softmax(', 'function compute(',
                      'function tokensOf(', 'id="lens"', 'id="sentence"',
                      'id="words"', 'id="weights"', 'data-t="honesty"'):
            with self.subTest(value=value):
                self.assertIn(value,t)
        self.assertIn("These are real calculations from a small teaching algorithm",t)
        self.assertIn("lang==='ar'?'rtl':'ltr'",t)

    def test_windows_mac_guides(self):
        for page in (ROOT/"index.html",LESSONS/FOLDERS[5]/"index.html"):
            t=page.read_text(encoding="utf-8")
            with self.subTest(page=page.name):
                for value in ('data-os-tab="windows"', 'data-os-tab="mac"',
                              'aria-selected="true" data-os-tab="windows"',
                              'data-os-panel="mac" hidden', 'uv python install 3.12',
                              'winget install --id Git.Git -e', 'git --version',
                              'brew install uv', 'uvx hf auth whoami',
                              'uv run gradio deploy', 'zero-a10g'):
                    self.assertIn(value,t)

    def test_english_only_lesson6_and_image(self):
        page=(LESSONS/FOLDERS[5]/"index.html").read_text(encoding="utf-8")
        app=(LESSONS/FOLDERS[5]/"gradio-app")
        self.assertNotIn('id="lang"', page)
        self.assertNotIn("ar:{previous:",page)
        self.assertNotIn('README.ar.md',page)
        self.assertIn('assets/digital-twin-hero.webp',page)
        self.assertTrue((LESSONS/FOLDERS[5]/"assets/digital-twin-hero.webp").is_file())
        self.assertIn('lessons/06-digital-twin/assets/digital-twin-hero.webp',(ROOT/"index.html").read_text())
        self.assertIn('in English only', (app/"twin_core.py").read_text())
        self.assertNotIn('Arabic', (app/"app.py").read_text())
        self.assertFalse((app/"README.ar.md").exists())

    def test_sparse_clone_guides(self):
        for page in (ROOT/"index.html",LESSONS/FOLDERS[5]/"index.html"):
            text=page.read_text(encoding="utf-8")
            self.assertEqual(text.count('git sparse-checkout set lessons/06-digital-twin'),4)
            self.assertEqual(text.count('git clone --depth 1 --filter=blob:none --sparse'),4)
            self.assertEqual(text.count('data-os-tab="windows"'),1)

    def test_homepage_deployment_guide(self):
        t=(ROOT/"index.html").read_text(encoding="utf-8")
        for val in ('deploy-guide','git clone','uv run app.py','uvx hf auth login','uv run gradio deploy','zero-a10g','huggingface.co/join'):
            self.assertIn(val,t)

    def test_gradio_project_valid(self):
        folder=LESSONS/FOLDERS[5]/"gradio-app"
        ast.parse((folder/"app.py").read_text(encoding="utf-8"))
        for fname in ('app.py','twin_core.py','pyproject.toml','.python-version','requirements.txt','README.md','about-me.txt'):
            self.assertTrue((folder/fname).is_file())
        self.assertIn('zero-a10g', (folder/'README.md').read_text(encoding='utf-8'))
        self.assertIn('@spaces.GPU', (folder/'app.py').read_text(encoding='utf-8'))
        # Gradio deploy first-run hardware prompt is intentionally preserved by NOT
        # checking in YAML metadata before the first deployment.
        self.assertFalse((folder/'README.md').read_text(encoding='utf-8').startswith('---\n'))

if __name__ == '__main__':unittest.main()
