"""Dependency-free structural smoke tests for AI Learning Lab.
Run: python -m unittest discover -s tests -v
Browser interactions need real Chromium; see TEST-REPORT.md.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
import ast
import unittest

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / 'lessons'
FOLDERS = [
    '01-how-ai-reads-words',
    '02-word-embeddings',
    '03-next-word-prediction',
    '04-ai-context-memory',
    '05-ai-retrieval',
    '06-digital-twin',
]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for key, value in attrs:
                if key == 'href' and value:
                    self.hrefs.append(value)


class TestRelease(unittest.TestCase):
    def test_one_folder_per_lesson(self):
        self.assertEqual(sorted(p.name for p in LESSONS.iterdir() if p.is_dir()), FOLDERS)

    def test_each_lesson_has_bilingual_documentation(self):
        for name in FOLDERS:
            with self.subTest(lesson=name):
                for filename in ('index.html', 'README.md', 'README.ar.md'):
                    self.assertTrue((LESSONS / name / filename).is_file())

    def test_root_documentation(self):
        for filename in ('index.html', 'README.md', 'README.ar.md',
                         'TEACHERS.md', 'TEACHERS.ar.md', 'CHANGELOG.md'):
            with self.subTest(filename=filename):
                self.assertTrue((ROOT / filename).is_file())

    def test_static_relative_links_exist(self):
        pages = [ROOT / 'index.html'] + [LESSONS / name / 'index.html' for name in FOLDERS]
        for page in pages:
            links = Links()
            links.feed(page.read_text(encoding='utf-8'))
            for href in links.hrefs:
                if (href.startswith(('https:', 'http:', '#', 'mailto:'))
                        or '${' in href):
                    continue  # JS-generated homepage cards are checked in Chromium
                dest = (page.parent / unquote(href.split('#')[0])).resolve()
                with self.subTest(page=page.name, href=href):
                    self.assertTrue(dest.exists(), f'Missing link destination: {dest}')

    def test_gradio_python_is_valid(self):
        path = LESSONS / '06-digital-twin' / 'gradio-app' / 'app.py'
        ast.parse(path.read_text(encoding='utf-8'))

    def test_model_honesty(self):
        for name in FOLDERS[2:]:
            page = (LESSONS / name / 'index.html').read_text(encoding='utf-8')
            self.assertTrue('not ' in page.lower() or 'ليس' in page,
                            f'{name} should explain it is not pretrained Qwen')


if __name__ == '__main__':
    unittest.main()
