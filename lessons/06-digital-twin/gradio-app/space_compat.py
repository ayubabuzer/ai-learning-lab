"""Offline configuration preflight; network resolver runs in CI.

Versions verified from the public Gradio 6.32.0 and Transformers 5.23.0
package metadata on 2026-11-21. The Hub 1.31+ range is shared by both.
"""
from __future__ import annotations
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GRADIO_VERSION = "6.32.0"
SPACE_VERSION = "0.52.1"
PYTHON_VERSION = "3.12"
REQUIREMENTS = {
    "torch": "2.9.1",
    "transformers": "5.23.0",
    "accelerate": "1.16.0",
}
MANAGED = {"gradio", "spaces", "huggingface-hub", "huggingface_hub"}


def check_config() -> list[str]:
    problems = []
    lines = (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
    found = {}
    for line in lines:
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        match = re.fullmatch(r"([A-Za-z0-9_-]+)==([0-9]+(?:\.[0-9]+){1,3})", line)
        if not match:
            problems.append(f"Unsupported or floating Space dependency: {line}")
            continue
        name, version = match.group(1).lower().replace("_", "-"), match.group(2)
        if name in MANAGED:
            problems.append(f"{name} is platform-managed and must not be in requirements.txt")
        found[name] = version
    if found != REQUIREMENTS:
        problems.append(f"Space dependencies must be {REQUIREMENTS!r}; found {found!r}")
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    deps = project["project"]["dependencies"]
    required_local = [f"{name}=={version}" for name, version in REQUIREMENTS.items()]
    required_local += [f"gradio=={GRADIO_VERSION}", f"spaces=={SPACE_VERSION}"]
    for pinned in required_local:
        if pinned not in deps:
            problems.append(f"Local pyproject.toml must contain {pinned}")
    if "huggingface_hub>=1.31,<3" not in deps:
        problems.append("Local Hub range must match Transformers 5.23 and Gradio 6.32")
    if project["project"].get("requires-python") != ">=3.12,<3.13":
        problems.append("Local Python must match the tested Space Python 3.12")
    # A dotfile can be omitted when copying the project (for example, via Finder).
    # It is a local uv convenience, not an artifact uploaded to the Space.
    # The generated Space README pins Python, and requires-python in pyproject.toml
    # constrains local uv even when .python-version is missing.
    version_file = ROOT / ".python-version"
    if version_file.is_file() and version_file.read_text(encoding="utf-8").strip() != PYTHON_VERSION:
        problems.append(f".python-version must be {PYTHON_VERSION} when present")
    return problems


def require_compatible() -> None:
    errors = check_config()
    if errors:
        raise RuntimeError("Deployment configuration mismatch:\n - " + "\n - ".join(errors))


if __name__ == "__main__":
    require_compatible()
    print("Pinned Space configuration matches release matrix (run the online CI resolver before publishing)")
