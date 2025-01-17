import os
import sys
import inspect
import importlib.util
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple
from enum import Enum
import re

class ArgumentInfo:
    def __init__(self, name: str, type_hint: Optional[str], description: str, optional: bool):
        self.name = name
        self.type_hint = type_hint
        self.description = description
        self.optional = optional

class RaiseInfo:
    def __init__(self, type: Optional[str], description: str):
        self.type = type
        self.description = description

class DocstringInfo:
    def __init__(self):
        self.description = ""
        self.args: List[ArgumentInfo] = []
        self.return_type: Optional[str] = None
        self.returns: Optional[str] = None
        self.raises: List[RaiseInfo] = []

def __post_init__(self):
    if self.args is None:
        self.args = []

class DocSection(Enum):
    DESCRIPTION = "description"
    ARGS = "args"
    RETURNS = "returns"
    RAISES = "raises"

class DocstringParser:
    """Parser for function and method docstrings."""

    TYPE_HINT_PATTERN = re.compile(r'(\w+)\s*\((.*?)\)')

    @staticmethod
    def parse(docstring: str) -> DocstringInfo:
        """Parse a docstring into structured information.

        Args:
            docstring: The docstring to parse.

        Returns:
            DocstringInfo object containing parsed information.
        """
        if not docstring:
            return DocstringInfo()
        
        doc_info = DocstringInfo()
        lines = [line.rstrip() for line in docstring.splitlines()]
        current_section = DocSection.DESCRIPTION
        description_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Section detection
            if line.lower().startswith(("parameters:", "args:")):
                current_section = DocSection.ARGS
                i += 1
                i = DocstringParser._parse_args(lines, i, doc_info)
            elif line.lower().startswith("returns:"):
                current_section = DocSection.RETURNS
                i = DocstringParser._parse_returns(lines, i, doc_info)
            elif line.lower().startswith("raises:"):
                current_section = DocSection.RAISES
                i = DocstringParser._parse_raises(lines, i, doc_info)
            elif current_section == DocSection.DESCRIPTION and line:
                description_lines.append(line)
            
            i += 1
            
        doc_info.description = " ".join(description_lines).strip()
        return doc_info

    @staticmethod
    def _parse_args(lines: List[str], i: int, doc_info: DocstringInfo) -> int:
        """Parse the arguments section."""
        if lines[i].lower().strip().startswith(("args:", "parameters:")):
            i += 1
            
        while i < len(lines):
            line = lines[i].strip()
            
            if not line or line.lower().startswith(("returns:", "raises:")):
                break
                
            if ":" in line:
                param_def, description = line.split(":", 1)
                param_def = param_def.strip()
                description = description.strip()
                
                match = DocstringParser.TYPE_HINT_PATTERN.match(param_def)
                if match:
                    param_name = match.group(1).strip()
                    type_hint = match.group(2).strip().replace("|", " or ")
                else:
                    param_name = param_def
                    type_hint = None
                    
                desc_lines = [description]
                next_i = i + 1
                while next_i < len(lines):
                    next_line = lines[next_i].strip()
                    if (not next_line or 
                        next_line.startswith(("returns:", "raises:")) or
                        DocstringParser.TYPE_HINT_PATTERN.match(next_line)):
                        break
                    desc_lines.append(next_line)
                    next_i += 1
                    
                full_desc = " ".join(desc_lines)
                optional = "optional" in full_desc.lower()
                
                doc_info.args.append(ArgumentInfo(
                    name=param_name,
                    type_hint=type_hint,
                    description=full_desc,
                    optional=optional
                ))
                
                i = next_i - 1
            i += 1
            
        return i

    @staticmethod
    def _parse_returns(lines: List[str], i: int, doc_info: DocstringInfo) -> int:
        """Parse the returns section."""
        line = lines[i].strip().lower()
        if line.startswith("returns:"):
            # Get description from first line if present
            if ":" in line:
                desc = line.split(":", 1)[1].strip()
                if desc:
                    doc_info.returns = desc
                    return i
            
            # Process subsequent lines
            i += 1
            while i < len(lines):
                line = lines[i].strip()
                if not line or line.lower().startswith("raises:"):
                    break
                    
                if ":" in line:
                    type_part, desc = line.split(":", 1)
                    doc_info.return_type = type_part.strip().replace("|", " or ")
                    doc_info.returns = desc.strip()
                else:
                    if doc_info.returns:
                        doc_info.returns += " " + line
                    else:
                        doc_info.returns = line
                i += 1
        return i

    @staticmethod
    def _parse_raises(lines: List[str], i: int, doc_info: DocstringInfo) -> int:
        """Parse the raises section."""
        # Skip Raises header
        line = lines[i].strip()
        if line.lower().startswith("raises:"):
            if ":" in line:
                _, desc = line.split(":", 1)
                if desc.strip():
                    doc_info.raises.append(RaiseInfo(None, desc.strip()))
                    return i
            
            # Multi-line raises
            next_i = i + 1
            while next_i < len(lines):
                line = lines[next_i].strip()
                if not line:
                    break
                if ":" in line:
                    type_part, desc = line.split(":", 1)
                    doc_info.raises.append(RaiseInfo(
                        type=type_part.strip(),
                        description=desc.strip()
                    ))
                next_i += 1
            i = next_i - 1
        
        return i

    @staticmethod
    def _extract_type_hint(arg_name_part: str) -> Tuple[Optional[str], str]:
        """Extract type hint and argument name."""
        arg_name_part = arg_name_part.strip()
        if "(" in arg_name_part and ")" in arg_name_part:
            name = arg_name_part[:arg_name_part.find("(")].strip()
            type_hint = arg_name_part[arg_name_part.find("(")+1:arg_name_part.find(")")].strip()
            return type_hint, name
        return None, arg_name_part

class MarkdownWriter:
    """Handles generation of Markdown documentation."""

    def __init__(self, output_dir: str):
        """Initialize the Markdown writer.

        Args:
            output_dir: Directory where markdown files will be written
        """
        self.output_dir = output_dir

    def write_class_doc(self, class_name: str, class_obj: object, module_name: str):
        """Generate markdown documentation for a class.

        Args:
            class_name: Name of the class
            class_obj: Class object
            module_name: Name of the module containing the class
        """
        content = []
        parser = DocstringParser()

        # Class header and description
        content.append(f"# Class {class_name}\n")
        if class_obj.__doc__:
            doc_info = parser.parse(class_obj.__doc__)
            if doc_info.description:
                content.append(f"{doc_info.description}\n\n")

        # Get methods
        methods = inspect.getmembers(class_obj, predicate=inspect.isfunction)
        
        if methods:
            content.append("## Methods\n")
            
            for method_name, method in methods:
                if not method_name.startswith('_') or method_name == '__init__':
                    content.append(f"### {method_name}\n")
                    self._write_method_doc(content, method_name, method, parser)

        # Write to file
        filename = f"{class_name.lower()}.md"
        filepath = os.path.join(self.output_dir, filename)
        
        os.makedirs(self.output_dir, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write("".join(content))

    def _write_method_doc(self, content: List[str], method_name: str, method: object, parser: DocstringParser):
        """Write documentation for a method.

        Args:
            content: List to append the documentation to
            method_name: Name of the method
            method: Method object
            parser: DocstringParser instance
        """
        # Add method signature
        signature = str(inspect.signature(method))
        content.append(f"```python\ndef {method_name}{signature}\n```\n")
        
        # Parse and add method documentation
        if method.__doc__:
            doc_info = parser.parse(method.__doc__)
            
            if doc_info.description:
                content.append(f"{doc_info.description}\n\n")
            
            if doc_info.args:
                content.append("#### Arguments\n\n")
                content.append("| Name | Type | Description |\n")
                content.append("|------|------|-------------|\n")
                
                for arg in doc_info.args:
                    # Clean up the description
                    desc = arg.description
                    if desc.lower().startswith(f"{arg.name.lower()}:"):
                        desc = desc[len(arg.name) + 1:].strip()
                    
                    content.append(
                        f"| `{arg.name}` | `{arg.type_hint}` | {desc} |\n"
                    )
                content.append("\n")
            
            if doc_info.returns:
                content.append("#### Returns\n\n")
                if doc_info.return_type:
                    content.append(f"**Type**: `{doc_info.return_type}`\n\n")
                content.append(f"{doc_info.returns}\n\n")
        else:
            # Handle missing docstring
            content.append("*No documentation available.*\n\n")
                        
    def write_toc(self, classes: List[tuple]):
        """Generate table of contents file.

        Args:
            classes: List of (class_name, class_obj, module_name) tuples
        """
        content = ["# API Documentation\n\n"]
        
        # Group classes by module
        modules: Dict[str, List[tuple]] = {}
        for class_name, class_obj, module_name in classes:
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append((class_name, class_obj))
        
        # Generate TOC
        for module_name, module_classes in sorted(modules.items()):
            content.append(f"## Module {module_name}\n\n")
            
            for class_name, class_obj in sorted(module_classes):
                link = f"{class_name.lower()}.md"
                content.append(f"* [{class_name}]({link})")
                
                if class_obj.__doc__:
                    doc_info = DocstringParser.parse(class_obj.__doc__)
                    if doc_info.description:
                        # Use only the first line of description
                        brief_desc = doc_info.description.split('.')[0]
                        content.append(f": {brief_desc}")
                
                content.append("\n")
            content.append("\n")
        
        # Write to file
        filepath = os.path.join(self.output_dir, "index.md")
        with open(filepath, 'w') as f:
            f.write("".join(content))

class Generator:
    """Main documentation generator class."""

    def __init__(self, output_dir: str):
        """Initialize the generator.

        Args:
            output_dir: Directory where documentation will be written
        """
        self.output_dir = output_dir
        self.writer = MarkdownWriter(output_dir)

    def _get_module_name(self, file_path: str) -> str:
        """Convert file path to full module name.

        Args:
            file_path: Path to Python file

        Returns:
            Full module name including package path
        """
        # Get the absolute path
        abs_path = os.path.abspath(file_path)
        
        # Find the root package directory (where the first __init__.py is found)
        current_dir = os.path.dirname(abs_path)
        package_parts = []
        
        while current_dir:
            if os.path.isfile(os.path.join(current_dir, '__init__.py')):
                package_parts.append(os.path.basename(current_dir))
                current_dir = os.path.dirname(current_dir)
            else:
                break
        
        # Reverse the package parts to get correct order
        package_parts.reverse()
        
        # Add the module name itself
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        package_parts.append(module_name)
        
        # Join all parts with dots
        return '.'.join(package_parts)

    def import_module_from_file(self, file_path: str) -> Optional[object]:
        """Import a Python module from file path.

        Args:
            file_path: Path to Python file

        Returns:
            Imported module object or None if import fails
        """
        try:
            # Get absolute path
            abs_path = os.path.abspath(file_path)
            
            # Find the package root directory
            current_dir = os.path.dirname(abs_path)
            package_root = None
            
            while current_dir:
                if os.path.isfile(os.path.join(current_dir, '__init__.py')):
                    package_root = os.path.dirname(current_dir)
                    current_dir = os.path.dirname(current_dir)
                else:
                    break
            
            if package_root:
                # Add package root to Python path
                if package_root not in sys.path:
                    sys.path.insert(0, package_root)
            
            # Get the full module name
            module_name = self._get_module_name(file_path)
            
            # Import the module
            spec = importlib.util.spec_from_file_location(module_name, abs_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                return module
                
        except Exception as e:
            print(f"Failed to import {file_path}: {e}")
            import traceback
            traceback.print_exc()  # This will help debug import issues
        return None

    def generate(self, file_paths: List[str]):
        """Generate documentation for specified Python files.

        Args:
            file_paths: List of paths to Python files to document
        """
        classes = []
        
        for file_path in file_paths:
            module = self.import_module_from_file(file_path)
            if not module:
                continue
            
            # Get all classes from the module
            module_classes = inspect.getmembers(
                module, 
                lambda obj: inspect.isclass(obj) and obj.__module__ == module.__name__
            )
            
            for class_name, class_obj in module_classes:
                classes.append((class_name, class_obj, module.__name__))
                self.writer.write_class_doc(class_name, class_obj, module.__name__)
        
        # Generate table of contents
        self.writer.write_toc(classes)

if __name__ == "__main__":
    files = [
        "./src/impl/elements/Arrow.py",
        "./src/impl/elements/Rectangle.py",
    ]

    generator = Generator("docs")
    generator.generate(files)
