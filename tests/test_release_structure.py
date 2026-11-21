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
    "05-ai-retrieval",  # Stable URL; the page now teaches tools, workflows and agents.
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
                    self.assertTrue('class="lesson-trail"' in t or 'class="trail"' in t)
                    self.assertTrue('class="only-ar"' in t or "language==='ar'" in t)

    def test_no_model_brand_required_for_pupils(self):
        for page in [ROOT/"index.html"]+[LESSONS/x/"index.html" for x in FOLDERS]:
            with self.subTest(page=page.parent.name):
                self.assertNotIn('Qwen',page.read_text(encoding="utf-8"))

    def test_guided_word_map_and_examples(self):
        t=(LESSONS/FOLDERS[1]/"index.html").read_text(encoding="utf-8")
        for value in ('id="plot"','id="wordA"','id="wordB"','id="score"','id="scoreFill"','id="presets"',
                      'Math.exp(-dist/160)', 'aria-pressed', 'attentionStory', 'smallSentence', 'bigSentence',
                      'analogyTitle', 'not a probability or a measurement from a real AI model'):
            with self.subTest(value=value):self.assertIn(value,t)
        self.assertNotIn('id="rebuild"',t)
        self.assertNotIn('id="examples"',t)

    def test_lesson01_tokens_and_vectors(self):
        t=(LESSONS/FOLDERS[0]/"index.html").read_text(encoding="utf-8")
        self.assertIn('id="pieces"',t)
        self.assertIn('id="identifiers"',t)
        self.assertIn('id="vectors"',t)
        self.assertNotIn('Optional deep dive · Unicode',t)

    def test_lesson05_tool_and_agent_chat(self):
        t=(LESSONS/FOLDERS[4]/"index.html").read_text(encoding="utf-8")
        for value in ('How Does AI Use Tools and Work Towards a Goal?',
                      'id="configuredTools"', 'id="toolChat"', 'id="agentChat"',
                      'data-example="math"', 'data-example="weather"', 'data-example="search"', 'id="runAgent"', 'id="agentScenario"',
                      'function selectTool(', 'function renderTools(',
                      'function renderAgent(', 'Illustrative', 'weather_forecast'):
            with self.subTest(value=value): self.assertIn(value,t)
        self.assertNotIn('function clueWeights(',t)
        self.assertNotIn('id="weights"',t)

    def test_deploy_requests_zerogpu(self):
        deploy = (ROOT / 'lessons/06-digital-twin/gradio-app/deploy.py').read_text(encoding='utf-8')
        self.assertIn("ZERO_GPU_HARDWARE = 'zero-a10g'", deploy)
        self.assertIn('space_hardware=ZERO_GPU_HARDWARE', deploy)
        self.assertIn('status in (402, 403)', deploy)

    def test_safe_deploy_allowlist(self):
        from importlib.util import spec_from_file_location, module_from_spec
        script=LESSONS/FOLDERS[5]/'gradio-app'/'deploy.py'
        self.assertTrue(script.is_file())
        text=script.read_text(encoding='utf-8')
        self.assertIn('UPLOAD_FILES',text)
        self.assertIn('TemporaryDirectory',text)
        self.assertIn('stage_files',text)
        self.assertNotIn('shutil.copytree',text)
        self.assertIn('uv run python deploy.py',(LESSONS/FOLDERS[5]/'gradio-app'/'README.md').read_text())

    def test_gradio_deployment_prompt_guidance(self):
        for p in (ROOT/'index.html', LESSONS/FOLDERS[5]/'index.html'):
            t=p.read_text(encoding='utf-8')
            for phrase in ('Add token as git credential?',
                           'Enter Spaces app title [gradio-app]:',
                           'Enter Gradio app file [app.py]:'):
                with self.subTest(page=p,phrase=phrase):self.assertIn(phrase,t)

    def test_lesson03_training_before_misleading_challenge(self):
        t=(LESSONS/FOLDERS[2]/"index.html").read_text(encoding="utf-8")
        for value in ('id="train"','id="predict"','id="training"',
                      'id="challengeExamples"','id="addChallenge"',
                      'function train()', 'function candidates()',
                      'The moon is made of rock'):
            with self.subTest(value=value):self.assertIn(value,t)
        self.assertLess(t.index('id="train"'),t.index('id="addChallenge"'))

    def test_lesson04_guided_chat_and_clear_context(self):
        t=(LESSONS/FOLDERS[3]/"index.html").read_text(encoding="utf-8")
        for value in ('id="messages"','id="context"','id="factPalette"','id="dropTarget"',
                      'draggable=true', 'id="question"','id="ask"','id="clear"','id="reset"',
                      'function addFact(key)', 'function ask()', 'facts.clear()', 'not a live AI model'):
            with self.subTest(value=value):self.assertIn(value,t)
        self.assertNotIn('id="message"',t) # No unreliable unrestricted chat box
        self.assertNotIn('id="factValue"',t) # No arbitrary values

    def test_homepage_unnecessary_demo_removed(self):
        t=(ROOT/'index.html').read_text(encoding='utf-8')
        self.assertNotIn('id="playground"',t)
        self.assertNotIn('Safe one-command deployment',t)

    def test_lesson05_multiplication_and_header(self):
        t=(LESSONS/FOLDERS[4]/'index.html').read_text(encoding='utf-8')
        for value in ('function parseMath(raw)', 'function normalizeMath(raw)', 'function mathIntent(q)', 'Division by zero is undefined.', 'LESSON 05 · TOOLS AND AGENTS', 'data-example="math"'):
            self.assertIn(value,t)

    def test_space_compatibility_preflight(self):
        import sys
        from importlib.util import spec_from_file_location, module_from_spec
        directory=LESSONS/FOLDERS[5]/'gradio-app'
        script=directory/'space_compat.py'
        self.assertTrue(script.exists())
        spec=spec_from_file_location('space_compat',script)
        module=module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.check_config(),[])
        self.assertIn('transformers==5.23.0', (directory/'requirements.txt').read_text())
        self.assertNotIn('huggingface_hub==', (directory/'requirements.txt').read_text())
        self.assertTrue((ROOT/'.github/workflows/validate.yml').exists())
        self.assertIn('uv pip compile',(ROOT/'.github/workflows/validate.yml').read_text())
        self.assertIn('sdk_version: {gradio_version}',(directory/'deploy.py').read_text())
        self.assertIn('python_version: "{python_version}"',(directory/'deploy.py').read_text())


    def test_deployment_preflight_without_hidden_python_dotfile(self):
        """A student who copied files without hidden dotfiles can still deploy."""
        from importlib.util import spec_from_file_location, module_from_spec
        from unittest.mock import patch
        import tempfile
        import shutil
        directory=LESSONS/FOLDERS[5]/'gradio-app'
        script=directory/'space_compat.py'
        spec=spec_from_file_location('space_compat_no_dotfile',script)
        module=module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmp:
            scratch=Path(tmp)
            for filename in ('requirements.txt','pyproject.toml'):
                shutil.copyfile(directory/filename,scratch/filename)
            # .python-version is intentionally absent.
            with patch.object(module,'ROOT',scratch):
                self.assertEqual(module.check_config(), [])
                (scratch/'.python-version').write_text('3.11\n',encoding='utf-8')
                self.assertTrue(any('.python-version' in problem for problem in module.check_config()))
                (scratch/'.python-version').write_text('3.12\n',encoding='utf-8')
                self.assertEqual(module.check_config(), [])

    def test_deploy_stages_only_five_files_and_version_metadata(self):
        import sys
        import tempfile
        from importlib.util import spec_from_file_location, module_from_spec
        directory=LESSONS/FOLDERS[5]/'gradio-app'
        sys.path.insert(0,str(directory))
        try:
            spec=spec_from_file_location('space_deployer_for_test',directory/'deploy.py')
            module=module_from_spec(spec)
            spec.loader.exec_module(module)
            with tempfile.TemporaryDirectory() as temp:
                files=module.stage_files(Path(temp),'Demo')
                self.assertEqual(set(files), {'app.py','twin_core.py','about-me.txt','requirements.txt','README.md'})
                self.assertEqual(set(p.name for p in Path(temp).iterdir()),set(files))
                meta=(Path(temp)/'README.md').read_text(encoding='utf-8')
                self.assertIn('sdk_version: 6.32.0',meta)
                self.assertIn('python_version: "3.12"',meta)
                self.assertNotIn('.venv',str(files))
        finally:
            sys.path.remove(str(directory))

    def test_no_unrestricted_questions_and_example_vectors(self):
        lesson1=(LESSONS/FOLDERS[0]/'index.html').read_text()
        lesson5=(LESSONS/FOLDERS[4]/'index.html').read_text()
        self.assertIn('id="vectorCards"',lesson1)
        self.assertIn('id="vectorPlot"',lesson1)
        self.assertIn('data-plotword="cat"',lesson1)
        self.assertNotIn('id="userQuestion"',lesson5)
        self.assertIn('agentDefinitionTitle',lesson5)

    def test_windows_mac_guides(self):
        for page in (ROOT/"index.html",LESSONS/FOLDERS[5]/"index.html"):
            t=page.read_text(encoding="utf-8")
            with self.subTest(page=page.name):
                for value in ('data-os-tab="windows"', 'data-os-tab="mac"',
                              'aria-selected="true" data-os-tab="windows"',
                              'data-os-panel="mac" hidden', 'uv python install 3.12',
                              'winget install --id Git.Git -e', 'git --version',
                              'brew install uv', 'uvx hf auth whoami',
                              'uv run python deploy.py', 'zero-a10g'):
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

    def test_full_clone_guides(self):
        for page in (ROOT/"index.html",LESSONS/FOLDERS[5]/"index.html"):
            text=page.read_text(encoding="utf-8")
            self.assertNotIn('git sparse-checkout set lessons/06-digital-twin',text)
            self.assertEqual(text.count('git clone https://github.com/ayubabuzer/ai-learning-lab.git'),4)
            self.assertEqual(text.count('data-os-tab="windows"'),1)

    def test_homepage_deployment_guide(self):
        t=(ROOT/"index.html").read_text(encoding="utf-8")
        for val in ('deploy-guide','git clone','uv run app.py','uvx hf auth login','uv run python deploy.py','zero-a10g','huggingface.co/join'):
            self.assertIn(val,t)

    def test_gradio_project_valid(self):
        folder=LESSONS/FOLDERS[5]/"gradio-app"
        ast.parse((folder/"app.py").read_text(encoding="utf-8"))
        for fname in ('app.py','twin_core.py','pyproject.toml','.python-version','requirements.txt','README.md','about-me.txt'):
            self.assertTrue((folder/fname).is_file())
        self.assertIn('zero-a10g', (folder/'README.md').read_text(encoding='utf-8'))
        self.assertIn('@spaces.GPU', (folder/'app.py').read_text(encoding='utf-8'))
        # Space metadata is generated from the pinned release matrix by deploy.py.
        self.assertIn('GRADIO_VERSION', (folder/'deploy.py').read_text())

if __name__ == '__main__':unittest.main()
