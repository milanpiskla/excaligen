import os
import sys
import inspect
import importlib.util
from dataclasses import dataclass
from typing import Dict, List, Optional, Set

@dataclass
class ArgumentInfo:
    """Information about a function/method argument."""
    name: str
    type_hint: str
    description: str
    optional: bool = False
    default_value: str = ""

@dataclass
class DocstringInfo:
    """Parsed information from a docstring."""
    description: str = ""
    args: List[ArgumentInfo] = None
    returns: Optional[str] = None
    return_type: Optional[str] = None

    def __post_init__(self):
        if self.args is None:
            self.args = []

class DocstringParser:
    """Parser for function and method docstrings."""

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

        lines = [line.strip() for line in docstring.split('\n')]
        doc_info = DocstringInfo()
        
        # Parse description
        description_lines = []
        current_section = "description"
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            if line.lower().startswith("args:"):
                current_section = "args"
            elif line.lower().startswith("returns:"):
                current_section = "returns"
            elif not line:
                # Skip empty lines
                pass
            elif current_section == "description":
                description_lines.append(line)
            elif current_section == "args":
                # Parse argument
                if ":" in line:
                    # Start of a new argument
                    arg_name_part, arg_desc = line.split(":", 1)
                    arg_name_part = arg_name_part.strip()
                    arg_desc_lines = [arg_desc.strip()]
                    
                    # Look ahead for continuation of the argument description
                    next_i = i + 1
                    while next_i < len(lines):
                        next_line = lines[next_i].strip()
                        if not next_line or next_line.find(":") == -1 or \
                           next_line.lower().startswith("args:") or \
                           next_line.lower().startswith("returns:"):
                            if next_line:
                                arg_desc_lines.append(next_line)
                            next_i += 1
                        else:
                            break
                    
                    # Extract type hint if present
                    type_hint = ""
                    if "(" in arg_name_part:
                        arg_name, type_hint = arg_name_part.split("(", 1)
                        type_hint = type_hint.rstrip(")")
                        arg_name = arg_name.strip()
                    else:
                        arg_name = arg_name_part

                    # Join all description lines
                    full_desc = " ".join(arg_desc_lines)
                    
                    # Check if optional and extract default value
                    optional = "optional" in full_desc.lower()
                    default_value = ""
                    if "defaults to" in full_desc.lower():
                        desc_parts = full_desc.split("defaults to", 1)
                        if len(desc_parts) > 1:
                            default_value = desc_parts[1].strip().strip('.').strip()
                        else:
                            default_value = ""
                        full_desc = desc_parts[0].strip()
                    
                    doc_info.args.append(ArgumentInfo(
                        name=arg_name,
                        type_hint=type_hint,
                        description=full_desc,
                        optional=optional,
                        default_value=default_value
                    ))
                    
                    i = next_i - 1  # Adjust index based on lookahead
            elif current_section == "returns":
                if not doc_info.returns:
                    if ":" in line:
                        return_parts = line.split(":", 1)
                        doc_info.return_type = return_parts[0].strip()
                        doc_info.returns = return_parts[1].strip()
                    else:
                        doc_info.returns = line
            
            i += 1
        
        doc_info.description = " ".join(description_lines)
        return doc_info
    
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
                            content.append("| Name | Type | Description | Default |\n")
                            content.append("|------|------|-------------|----------|\n")
                            
                            for arg in doc_info.args:
                                default = f"`{arg.default_value}`" if arg.default_value else "Required"
                                if arg.optional and not arg.default_value:
                                    default = "Optional"
                                
                                # Clean up the description
                                desc = arg.description
                                if desc.lower().startswith(f"{arg.name.lower()}:"):
                                    desc = desc[len(arg.name) + 1:].strip()
                                
                                content.append(
                                    f"| `{arg.name}` | `{arg.type_hint}` | {desc} | {default} |\n"
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

        # Write to file
        filename = f"{class_name.lower()}.md"
        filepath = os.path.join(self.output_dir, filename)
        
        os.makedirs(self.output_dir, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write("".join(content))
                        
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
    # Example usage:
    # python build.py file1.py file2.py file3.py
    # if len(sys.argv) < 2:
    #     print("Usage: python build.py <python_file1> [python_file2 ...]")
    #     sys.exit(1)

    files = [
        "./src/impl/elements/Arrow.py",
        "./src/impl/elements/Rectangle.py",
    ]

    generator = Generator("api")
    generator.generate(files)
