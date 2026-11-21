"""Publish only the Digital Twin app files to a Hugging Face Space.

Run from any directory with: uv run python lessons/06-digital-twin/gradio-app/deploy.py
(or from this folder: uv run python deploy.py).
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

from huggingface_hub import HfApi
from huggingface_hub.errors import HfHubHTTPError

ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / '.space-deploy.json'  # Local only; deliberately not uploaded.
UPLOAD_FILES = ('app.py', 'twin_core.py', 'about-me.txt', 'requirements.txt')
ZERO_GPU_HARDWARE = 'zero-a10g'  # Free for eligible accounts; selected at creation, never inferred from README.
SPACE_README = '''---
title: {title}
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
app_file: app.py
pinned: false
---

# {title}

A fictional-character Digital Twin from AI Learning Lab. Do not publish personal information.
'''


def safe_slug(value: str) -> str:
    value = value.strip().lower().replace(' ', '-')
    if not re.fullmatch(r'[a-z0-9][a-z0-9._-]{1,94}', value):
        raise ValueError('Use 2–95 characters: lowercase letters, numbers, hyphens, underscores or dots.')
    return value


def stage_files(destination: Path, title: str) -> list[str]:
    """A strict allowlist, not a copy of the project tree."""
    missing = [name for name in UPLOAD_FILES if not (ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError('Missing app files: ' + ', '.join(missing))
    for name in UPLOAD_FILES:
        shutil.copyfile(ROOT / name, destination / name)
    (destination / 'README.md').write_text(SPACE_README.format(title=title), encoding='utf-8')
    return [*UPLOAD_FILES, 'README.md']


def main() -> int:
    print('AI Learning Lab · Safe Space deployment')
    try:
        api = HfApi()
        who = api.whoami()
        username = who['name']
    except Exception:
        print('Not logged in. First create a Hugging Face Write token, then run: uvx hf auth login')
        print('Verify your account with: uvx hf auth whoami')
        return 1
    print(f'✓ Connected to Hugging Face as {username}')
    try:
        saved = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    except (ValueError, OSError):
        saved = {}
    previous = saved.get('repo_id', '')
    default = previous.split('/', 1)[1] if previous.startswith(username + '/') else 'my-ai-digital-twin'
    if previous.startswith(username + '/'):
        print(f'Previously deployed Space: {previous}')
        raw = input(f'Space name [{default}]: ').strip() or default
    else:
        raw = input(f'Choose a Space name [{default}]: ').strip() or default
    try:
        slug = safe_slug(raw)
    except ValueError as err:
        print(f'Invalid name: {err}')
        return 1
    repo_id = f'{username}/{slug}'
    try:
        existing = api.repo_exists(repo_id, repo_type='space')
        if existing and repo_id != previous:
            print(f'A Space named {repo_id} already exists. Choose another name to avoid overwriting it.')
            return 1
        with tempfile.TemporaryDirectory(prefix='ai-lab-space-') as temp:
            files = stage_files(Path(temp), slug.replace('-', ' ').title())
            print('✓ Only these files will be uploaded: ' + ', '.join(files))
            print('✓ .venv, caches, tests, local secrets and Git history are excluded')
            if not existing:
                api.create_repo(
                    repo_id=repo_id, repo_type='space', space_sdk='gradio',
                    space_hardware=ZERO_GPU_HARDWARE, private=False, exist_ok=False,
                )
                print('✓ Created Gradio Space with ZeroGPU hardware (zero-a10g)')
            if existing:
                # Do not silently switch hardware on a Space that may incur charges.
                info = api.get_space_runtime(repo_id=repo_id)
                stage = str(getattr(info, 'hardware', '') or '')
                requested = str(getattr(info, 'requested_hardware', '') or '')
                if ZERO_GPU_HARDWARE not in (stage, requested):
                    print(f'Existing Space uses {stage or requested or 'unknown'} hardware; not changing it automatically.')
                    print('Select ZeroGPU in Space Settings, or choose a fresh eligible Space name.')
                    return 1
            api.upload_folder(repo_id=repo_id, repo_type='space', folder_path=temp, commit_message='Deploy AI Learning Lab Digital Twin')
        STATE_FILE.write_text(json.dumps({'repo_id': repo_id}, indent=2) + '\n', encoding='utf-8')
    except (HfHubHTTPError, OSError, ValueError) as err:
        print(f'Deployment failed: {err}', file=sys.stderr)
        status = getattr(getattr(err, 'response', None), 'status_code', None)
        if status in (402, 403):
            print('Hugging Face rejected creation or access. This script requested ZeroGPU (zero-a10g), not CPU Basic.', file=sys.stderr)
            print('Check your account eligibility: verified email, account older than 30 days, and fewer than two free ZeroGPU Spaces.', file=sys.stderr)
            print('If eligible and the problem persists, check the Hugging Face error and account settings; no payment is initiated.', file=sys.stderr)
        elif status == 401:
            print('Authentication failed. Verify your Write token with: uvx hf auth whoami', file=sys.stderr)
        else:
            print('Check the exact error above and the Space build logs. An older oversized Space can retain its tracked files.', file=sys.stderr)
        return 1
    print('\n✓ App files uploaded. Hugging Face may still be building your Space.')
    print(f'Open: https://huggingface.co/spaces/{repo_id}')
    print('Wait for Running, then open App and test your chatbot. If it fails, check Logs and Settings → Hardware.')
    print('ZeroGPU hardware was requested when this Space was created; check the Space hardware status if it fails to run.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
