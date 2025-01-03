import os
import sys
import inspect
import importlib.util
from typing import Dict, List, Optional, Tuple

class Markdown:
    """Class for generating Markdown formatted documentation."""
    
    @staticmethod
    def header(text: str, level: int = 1) -> str:
        """Generate a Markdown header.
        
        Args:
            text: The header text
            level: The header level (1-6)
            
        Returns:
            Formatted Markdown header string
        """
        return f"{'#' * level} {text}\n\n"
    
    @staticmethod
    def code_block(text: str, language: str = "python") -> str:
        """Generate a Markdown code block.
        
        Args:
            text: The code content
            language: Programming language for syntax highlighting
            
        Returns:
            Formatted Markdown code block
        """
        return f"```{language}\n{text}\n```\n\n"
    
    @staticmethod
    def paragraph(text: str) -> str:
        """Generate a Markdown paragraph.
        
        Args:
            text: The paragraph text
            
        Returns:
            Formatted Markdown paragraph
        """
        return f"{text}\n\n"
    
    @staticmethod
    def link(text: str, anchor: str) -> str:
        """Generate a Markdown link to an anchor.
        
        Args:
            text: The link text
            anchor: The anchor name
            
        Returns:
            Formatted Markdown link
        """
        # Convert anchor to lowercase and replace spaces with hyphens
        anchor = anchor.lower().replace(' ', '-')
        return f"[{text}](#{anchor})"

class Generator:
    """Main documentation generator class."""
    
    def __init__(self, src_dir: str, output_dir: str, output_file: str = "api.md"):
        """Initialize the generator.
        
        Args:
            src_dir: Path to source code directory
            output_dir: Path to output documentation directory
            output_file: Name of the output markdown file
        """
        self.src_dir = os.path.abspath(src_dir)
        self.output_dir = os.path.abspath(output_dir)
        self.output_file = output_file
        self.markdown = Markdown()
        self.toc_entries: List[Tuple[str, int]] = []  # (title, level) pairs
        
        # Add source directory to Python path for relative imports
        if self.src_dir not in sys.path:
            sys.path.insert(0, os.path.dirname(self.src_dir))
    
    def _get_module_name(self, file_path: str) -> str:
        """Convert file path to module name.
        
        Args:
            file_path: Path to Python file
            
        Returns:
            Module name suitable for importing
        """
        rel_path = os.path.relpath(file_path, os.path.dirname(self.src_dir))
        module_name = os.path.splitext(rel_path)[0].replace(os.sep, '.')
        return module_name
    
    def get_python_files(self) -> List[str]:
        """Recursively find all Python files in the source directory.
        
        Returns:
            List of Python file paths
        """
        python_files = []
        for root, _, files in os.walk(self.src_dir):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))
        return python_files
    
    def import_module_from_file(self, file_path: str) -> Optional[object]:
        """Import a Python module from file path.
        
        Args:
            file_path: Path to Python file
            
        Returns:
            Imported module object or None if import fails
        """
        try:
            module_name = self._get_module_name(file_path)
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module  # Register module in sys.modules
                spec.loader.exec_module(module)
                return module
        except Exception as e:
            print(f"Failed to import {file_path}: {e}")
        return None
    
    def is_api_module(self, module: object) -> bool:
        """Check if module is marked as API with @api in its docstring.
        
        Args:
            module: Module object
            
        Returns:
            True if module contains @api tag, False otherwise
        """
        return bool(module.__doc__ and "@api" in module.__doc__)
    
    def add_toc_entry(self, title: str, level: int):
        """Add an entry to the table of contents.
        
        Args:
            title: Section title
            level: Header level
        """
        self.toc_entries.append((title, level))
    
    def generate_toc(self) -> str:
        """Generate table of contents from collected entries.
        
        Returns:
            Markdown formatted table of contents
        """
        content = [self.markdown.header("Table of Contents")]
        
        for title, level in self.toc_entries:
            indent = "    " * (level - 1)
            content.append(f"{indent}- {self.markdown.link(title, title)}\n")
        
        content.append("\n")  # Add extra newline after TOC
        return "".join(content)
    
    def generate_module_doc(self, module: object, rel_path: str) -> str:
        """Generate documentation for a module.
        
        Args:
            module: Module object
            rel_path: Relative path to module file
            
        Returns:
            Markdown formatted documentation string
        """
        content = []
        
        # Module header and docstring
        module_name = self._get_module_name(rel_path)
        module_title = f"Module {module_name}"
        content.append(self.markdown.header(module_title))
        self.add_toc_entry(module_title, 1)
        
        if module.__doc__:
            content.append(self.markdown.paragraph(module.__doc__.strip()))
            
        # Get all module members
        members = inspect.getmembers(module)
        
        # Document classes
        classes = [(name, obj) for name, obj in members 
                  if inspect.isclass(obj) and obj.__module__ == module.__name__]
        if classes:
            content.append(self.markdown.header("Classes", 2))
            self.add_toc_entry(f"{module_name} Classes", 2)
            
            for name, cls in classes:
                class_title = f"class {name}"
                content.append(self.markdown.header(class_title, 3))
                self.add_toc_entry(class_title, 3)
                
                if cls.__doc__:
                    content.append(self.markdown.paragraph(cls.__doc__.strip()))
                
                # Document methods
                methods = inspect.getmembers(cls, predicate=inspect.isfunction)
                for method_name, method in methods:
                    if not method_name.startswith('_') or method_name == '__init__':
                        method_title = f"{name}.{method_name}"
                        content.append(self.markdown.header(method_title, 4))
                        self.add_toc_entry(method_title, 4)
                        
                        if method.__doc__:
                            content.append(self.markdown.paragraph(method.__doc__.strip()))
                        
                        # Add method signature
                        signature = str(inspect.signature(method))
                        content.append(self.markdown.code_block(
                            f"def {method_name}{signature}:", "python"))
        
        # Document functions
        functions = [(name, obj) for name, obj in members 
                    if inspect.isfunction(obj) and obj.__module__ == module.__name__]
        if functions:
            content.append(self.markdown.header("Functions", 2))
            self.add_toc_entry(f"{module_name} Functions", 2)
            
            for name, func in functions:
                if not name.startswith('_'):
                    func_title = f"function {name}"
                    content.append(self.markdown.header(func_title, 3))
                    self.add_toc_entry(func_title, 3)
                    
                    if func.__doc__:
                        content.append(self.markdown.paragraph(func.__doc__.strip()))
                    
                    # Add function signature
                    signature = str(inspect.signature(func))
                    content.append(self.markdown.code_block(
                        f"def {name}{signature}:", "python"))
        
        return "".join(content)
    
    def generate(self):
        """Generate documentation for all Python files in source directory."""
        python_files = self.get_python_files()
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Collect documentation content
        content = []
        content.append(self.markdown.header("API Documentation"))
        
        # Process each Python file
        for file_path in python_files:
            # Import module
            module = self.import_module_from_file(file_path)
            if not module or not self.is_api_module(module):
                continue
            
            # Generate documentation
            doc_content = self.generate_module_doc(module, file_path)
            content.append(doc_content)
        
        # Insert table of contents at the beginning
        content.insert(1, self.generate_toc())
        
        # Write complete documentation to single file
        output_path = os.path.join(self.output_dir, self.output_file)
        with open(output_path, 'w') as f:
            f.write("".join(content))

if __name__ == "__main__":
    # Assuming script is run from the doc directory
    src_dir = os.path.join("..", "src")
    output_dir = "."
    
    generator = Generator(src_dir, output_dir)
    generator.generate()
