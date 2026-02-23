"""
Build PyPI README.md

This script generates a README.md file for PyPI by replacing relative links with absolute links.
"""

# Copyright (c) 2024 - 2026 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import re
import sys
from pathlib import Path

def generate_pypi_readme():
    input_file = Path("README.md")
    output_file = Path("README_PYPI.md")

    if not input_file.exists():
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)

    content = input_file.read_text(encoding="utf-8")

    # Base URLs for GitHub
    repo = "milanpiskla/excaligen"
    branch = "main"
    
    # For images, we need the raw content so they render correctly on PyPI
    raw_base_url = f"https://raw.githubusercontent.com/{repo}/{branch}/"
    # For document links, we use the blob URL so users are directed to the GitHub UI
    blob_base_url = f"https://github.com/{repo}/blob/{branch}/"

    # 1. Replace relative image links: ![alt](./path) or ![alt](path)
    def repl_image(match):
        alt_text = match.group(1)
        path = match.group(2)
        # Skip absolute URLs
        if path.startswith("http://") or path.startswith("https://"):
            return match.group(0)
        
        # Remove leading ./ if present
        if path.startswith("./"):
            path = path[2:]
            
        return f"![{alt_text}]({raw_base_url}{path})"

    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl_image, content)

    # 2. Replace relative document links: [text](./path) or [text](path)
    def repl_link(match):
        text = match.group(1)
        path = match.group(2)
        # Skip absolute URLs and anchor links
        if path.startswith("http://") or path.startswith("https://") or path.startswith("#"):
            return match.group(0)
        
        # Remove leading ./ if present
        if path.startswith("./"):
            path = path[2:]
            
        return f"[{text}]({blob_base_url}{path})"

    # Use negative lookbehind to avoid matching image links
    content = re.sub(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)', repl_link, content)

    output_file.write_text(content, encoding="utf-8")
    print(f"Successfully generated {output_file} from {input_file}")

if __name__ == "__main__":
    generate_pypi_readme()
