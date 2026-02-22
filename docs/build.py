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
            
        doc_info.description = "\n".join(description_lines).strip()
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
        """Write documentation for a class."""
        content = []
        
        # Add class header
        content.append(f"# Class {class_name}\n")
        
        # Add class description if present
        if class_obj.__doc__:
            doc_info = DocstringParser.parse(class_obj.__doc__)
            if doc_info.description:
                content.append(f"{doc_info.description}\n")
        
        # Add methods section
        content.append("## Methods\n")
        
        # Document methods
        for method_name, method in inspect.getmembers(class_obj, predicate=inspect.isfunction):
            if not method_name.startswith('_') or method_name == '__init__':
                docstring = inspect.getdoc(method)
                doc_info = DocstringParser.parse(docstring) if docstring else None
                self._write_method_doc(method_name, method, doc_info, content)
        
        # Write to file
        output_file = os.path.join(self.output_dir, f"{class_name.lower()}.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(''.join(content))

    def _write_method_doc(self, method_name: str, method: object, doc_info: DocstringInfo, content: List[str]) -> None:
        """Write documentation for a method into the content list in Markdown format.
        This method processes the method's documentation and formats it as Markdown, including:
        - Method signature
        - Description
        - Arguments table
        - Return value information
        - Exceptions that may be raised
        Args:
            method_name (str): Name of the method being documented
            method (object): The method object to document
            doc_info (DocstringInfo): Parsed docstring information containing description, args, returns, and raises
            content (List[str]): List to append the formatted documentation to
        Returns:
            None: Documentation is appended directly to the content list
        """
        # Add method signature
        content.append(f"### {method_name}\n")
        content.append("```python\n")
        source_lines = inspect.getsource(method).splitlines()
        signature_line = next((line for line in source_lines if line.strip().startswith('def ')), source_lines[0])
        content.append(f"{signature_line}\n")
        content.append("```\n")
        
        if doc_info:
            # Add description
            if doc_info.description:
                content.append(f"{doc_info.description}\n\n")
            
            # Add arguments
            if doc_info.args:
                content.append("#### Arguments\n\n")
                content.append("| Name | Type | Description |\n")
                content.append("|------|------|-------------|\n")
                for arg in doc_info.args:
                    desc = arg.description
                    if desc.lower().startswith(f"{arg.name.lower()}:"):
                        desc = desc[len(arg.name) + 1:].strip()
                    content.append(f"| `{arg.name}` | `{arg.type_hint}` | {desc} |\n")
                content.append("\n")
            
            # Add returns
            if doc_info.returns:
                content.append("#### Returns\n\n")
                if doc_info.return_type:
                    content.append(f"**Type**: `{doc_info.return_type}`\n\n")
                content.append(f"{doc_info.returns}\n\n")
            
            # Add raises
            if doc_info.raises:
                content.append("#### Raises\n\n")
                for raise_info in doc_info.raises:
                    if raise_info.type:
                        content.append(f"**{raise_info.type}**: {raise_info.description}\n\n")
                    else:
                        content.append(f"{raise_info.description}\n\n")

    def write_toc(self, classes: List[Tuple[str, object, str]]) -> None:
        """Write table of contents for all documented classes to a markdown file.
        This method generates a structured table of contents for API documentation,
        organizing classes by their modules. The output is written to 'api.md' in
        the specified output directory.
        Args:
            classes (List[Tuple[str, object, str]]): List of tuples containing:
                - class name (str)
                - class object (object)
                - module path (str)
        Returns:
            None
        The generated TOC has the following structure:
        - Documentation header
        - Module sections with class entries grouped under each module
        - Classes listed with links to their documentation
        The output file is written in markdown format with UTF-8 encoding.
        """
        content = [self._get_doc_header()]
        modules = self._group_classes_by_module(classes)
        
        for full_module_name, module_classes in self._get_sorted_modules(modules):
            simple_module = full_module_name.split('.')[-1]
            content.append(f"## {simple_module}\n\n")
            content.extend(self._format_class_entries(module_classes))
        
        filepath = os.path.join(self.output_dir, "index.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("".join(content))

    def _get_doc_header(self) -> str:
        """Return the documentation header text."""
        return """# 🎨 Excaligen API Documentation\n\n
This is the API documentation for the Excaligen library\n\n
✨ The following classes are available:\n\n"""

    def _group_classes_by_module(self, classes: List[Tuple[str, object, str]]) -> Dict[str, List[Tuple[str, object]]]:
        """Group classes by their module names."""
        modules: Dict[str, List[Tuple[str, object]]] = {}
        for class_name, class_obj, module_name in classes:
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append((class_name, class_obj))
        return modules

    def _get_sorted_modules(self, modules: Dict[str, List[Tuple[str, object]]]) -> List[Tuple[str, List[Tuple[str, object]]]]:
        """Return modules sorted by hierarchy depth and name."""
        return sorted(modules.items(), key=lambda x: (len(x[0].split('.')), x[0].lower()))

    def _format_class_entries(self, module_classes: List[Tuple[str, object]]) -> List[str]:
        """Format class entries with their descriptions."""
        entries = []
        for class_name, class_obj in sorted(module_classes):
            link = f"{class_name.lower()}.md"
            entries.append(f"* [{class_name}]({link})\n")
            
            if class_obj.__doc__:
                doc_info = DocstringParser.parse(class_obj.__doc__)
                if doc_info.description:
                    brief_desc = doc_info.description.split('.')[0].strip()
                    entries.append(f"    {brief_desc}\n")
            entries.append("\n")
        return entries

class Generator:
    """Main documentation generator class."""

    def __init__(self, output_dir: str):
        """Initialize the generator.

        Args:
            output_dir: Directory where documentation will be written
        """
        self.output_dir = output_dir
        self.writer = MarkdownWriter(output_dir)

    def _import_module(self, module_name: str, abs_path: str) -> Optional[object]:
        """Import a module dynamically.
        
        Args:
            module_name: Full name of the module to import
            abs_path: Absolute path to the module file
            
        Returns:
            Imported module object or None if import fails
        """
        # Import parent package first
        package_name = module_name.rsplit('.', 1)[0]
        try:
            __import__(package_name)
        except ImportError:
            print(f"Could not import package: {package_name}")
            return None
        
        # Import the module dynamically
        spec = importlib.util.spec_from_file_location(module_name, abs_path)
        if not (spec and spec.loader):
            return None
            
        module = importlib.util.module_from_spec(spec)
        module.__package__ = package_name
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

    def _process_module_classes(self, module: object) -> List[Tuple[str, object, str]]:
        """Extract and process classes from a module.
        
        Args:
            module: Module object to process
            
        Returns:
            List of tuples containing (class_name, class_object, module_name)
        """
        classes = []
        module_classes = inspect.getmembers(
            module,
            lambda obj: inspect.isclass(obj) and obj.__module__ == module.__name__
        )
        
        for class_name, class_obj in module_classes:
            classes.append((class_name, class_obj, module.__name__))
            self.writer.write_class_doc(class_name, class_obj, module.__name__)
        
        return classes

    def generate(self, doc_targets: List[Tuple[str, str]]):
        """Generate documentation for the specified targets.
        
        Args:
            doc_targets: List of tuples containing (module_name, absolute_path)
        """
        classes = []
        
        for module_name, abs_path in doc_targets:
            try:
                module = self._import_module(module_name, abs_path)
                if module:
                    classes.extend(self._process_module_classes(module))
            except Exception as e:
                print(f"Failed to import {abs_path}: {e}")
                import traceback
                traceback.print_exc()

        # Generate table of contents
        self.writer.write_toc(classes)

if __name__ == "__main__":
    # Add the 'src' directory to sys.path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    src_path = os.path.join(project_root, 'src')
    sys.path.insert(0, src_path)
    
    DOC_TARGETS = [
        ("excaligen.SceneBuilder", "./src/excaligen/SceneBuilder.py"),
        ("excaligen.impl.elements.Arrow", "./src/excaligen/impl/elements/Arrow.py"),
        ("excaligen.impl.colors.Color", "./src/excaligen/impl/colors/Color.py"),
        ("excaligen.impl.elements.Diamond", "./src/excaligen/impl/elements/Diamond.py"),
        ("excaligen.impl.elements.Ellipse", "./src/excaligen/impl/elements/Ellipse.py"),
        ("excaligen.impl.elements.Frame", "./src/excaligen/impl/elements/Frame.py"),
        ("excaligen.impl.elements.Group", "./src/excaligen/impl/elements/Group.py"),
        ("excaligen.impl.elements.Image", "./src/excaligen/impl/elements/Image.py"),
        ("excaligen.impl.elements.Line", "./src/excaligen/impl/elements/Line.py"),
        ("excaligen.impl.elements.Rectangle", "./src/excaligen/impl/elements/Rectangle.py"),
        ("excaligen.impl.elements.Text", "./src/excaligen/impl/elements/Text.py"),
        ("excaligen.defaults.Defaults", "./src/excaligen/defaults/Defaults.py"),
    ]

    generator = Generator(os.path.join("docs", "api"))
    generator.generate(DOC_TARGETS)
