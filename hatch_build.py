"""
Build hook for 'hatch build' command

This hook builds the documentation and generates the PyPI README.
"""

# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import sys
from pathlib import Path
import subprocess

class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        # 1. Generate PyPI README
        script_dir = Path(__file__).parent
        readme_script = script_dir / "build_pypi_readme.py"
        print(f"Running {readme_script}...")
        subprocess.run([sys.executable, str(readme_script)], cwd=str(script_dir), check=True)

        # 2. Build Documentation
        docs_script = script_dir / "docs" / "build.py"
        print(f"Running {docs_script}...")
        subprocess.run([sys.executable, str(docs_script)], cwd=str(script_dir), check=True)

