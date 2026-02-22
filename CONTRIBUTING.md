# Contributing to Excaligen 🎨

First off, thank you for considering contributing to Excaligen! It's people like you that make open-source tools great. 

## How Can I Contribute?

* **Reporting Bugs:** Open an issue and describe the bug. Please include the Python version you are using and a code snippet that reproduces the issue.
* **Suggesting Enhancements:** Have an idea for a new shape, styling option, or feature? Open an issue and tell us about it!
* **Pull Requests:** If you want to fix a bug or add a feature, we gladly accept Pull Requests (PRs).

## Local Development Setup

To contribute code, you'll need to set up a local development environment.

### Fork the repository on GitHub and clone your fork locally:
   ```bash
   git clone https://github.com/milanpiskla/excaligen.git
   cd excaligen
```

### Create a virtual environment (recommended):

```Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install the package in editable mode

```Bash
pip install -e .
```

### Modifying the Code

The core logic for Excaligen is located inside the src/ directory.

Please follow standard PEP 8 style guidelines for Python.

### Generating Documentation

Excaligen uses a custom documentation generator to parse docstrings and generate Markdown.

If you add a new class, update a docstring, or add a method, you must regenerate the API documentation before submitting your PR.

Run the build script from the root of the project:

```Bash
python docs/build.py
```
This will automatically update the files in the docs/api/ directory.

### Submitting a Pull Request
Create a new branch for your feature: git checkout -b feature-name

Commit your changes: git commit -m "Add some feature"

Push to the branch: git push origin feature-name

Open a Pull Request against the main branch of the original repository.

Thank you for your help in making Excaligen better! 💙
