import pathlib
import subprocess
import sys 
import shutil
import json
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Typst Developer Server")

# Helper to find typst executable
def get_typst_command() -> str:
    return shutil.which("typst") or "typst"

# Template directory
TEMPLATE_DIR = pathlib.Path(__file__).parent / "templates"

@mcp.prompt()
def typst_assistant_instructions() -> str:
    """
    Instructions for the Typst assistant.
    """
    return """\
You are a Typst typesetting expert. You help users create professional documents using Typst.

AVAILABLE TOOLS:
  compile_document  — compiles .typ to PDF/PNG/SVG
  query_metadata    — extracts metadata from .typ files
  list_fonts        — shows available fonts
  list_templates    — shows available document templates
  get_template      — gets the content of a template
  create_document   — creates a new document from a template
  edit_section      — edits a section marked with // SECTION: name
  read_section      — reads a section marked with // SECTION: name
  list_sections     — lists all marked sections in a file
  add_package_import — adds a package import (e.g., polylux, cetz)

WORKFLOW:
1. Ask the user what kind of document they want to create (e.g., Paper, CV, Poster, Data Report).
2. Use `list_templates` to see what's available.
3. Use `create_document` to start the file.
4. Use `edit_section` for targeted updates to specific parts of the document.
5. Use `add_package_import` if you need external capabilities like charts or slides.
6. Always `compile_document` after changes to verify correctness.
7. Use `query_metadata` to check for specific document properties if needed.

GUIDES:
- `guides/typst_guide.md`: Quick reference for Typst syntax (markup, math, scripting).
- `guides/advanced_typst.md`: Mastery guide for `set`/`show` rules, complex layout (grid, stack), and automation.
- `guides/mcp_usage_guide.md`: Best practices for using this MCP server and its tools.

TYPST MASTERY PRINCIPLES:
- **Styling**: Always use `#set` for defaults and `#show` for transformations. Never hardcode styles in every element.
- **Layout**: Use `#grid` for structured 2D layouts and `#stack` for 1D arrangements.
- **Data**: Recommend loading CSV/JSON for dynamic tables and reports.
- **Scripting**: Encapsulate repetitive elements into functions using `#let`.
- **Packages**: Search the Typst Universe for specialized tools (e.g., `@preview/cetz` for drawings).

TIPS:
- Use `// SECTION: Name` and `// END: Name` markers in your Typst code to make it easy to edit later.
- If the user has an existing .typ file, use `list_sections` to see if it's already marked up.
"""

@mcp.tool()
def add_package_import(path: str, package: str) -> str:
    """
    Add a package import to the top of a Typst file.
    package: The full import string (e.g., "@preview/polylux:0.3.1").
    """
    filepath = pathlib.Path(path)
    if not filepath.exists():
        return f"Error: {path} not found."
    
    content = filepath.read_text(encoding="utf-8")
    import_line = f'#import "{package}": *\n'
    if import_line in content:
        return f"Package {package} is already imported."
        
    updated_content = import_line + content
    filepath.write_text(updated_content, encoding="utf-8")
    return f"Imported {package} into {path}."

@mcp.tool()
def compile_document(path: str, format: str = "pdf", open_after: bool = False) -> str:
    """
    Compile a Typst document.
    path: Path to the .typ file.
    format: Output format (pdf, png, svg). Default is pdf.
    """
    typst_path = pathlib.Path(path)
    if not typst_path.exists():
        return f"Error: File {path} not found."
    
    cmd = [get_typst_command(), "compile", str(typst_path)]
    if format != "pdf":
        output_path = typst_path.with_suffix(f".{format}")
        cmd.append(str(output_path))
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        output_file = typst_path.with_suffix(".pdf") if format == "pdf" else typst_path.with_suffix(f".{format}")
        return f"Successfully compiled to {output_file}"
    return f"Compile error:\n{result.stderr}"

@mcp.tool()
def query_metadata(path: str, selector: str) -> str:
    """
    Query metadata from a Typst document using a selector.
    Example selectors: "heading", "figure", "<my-label>".
    """
    typst_path = pathlib.Path(path)
    if not typst_path.exists():
        return f"Error: File {path} not found."
    
    cmd = [get_typst_command(), "query", str(typst_path), selector, "--format", "json"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout
    return f"Query error:\n{result.stderr}"

@mcp.tool()
def list_fonts() -> str:
    """List all fonts available to Typst."""
    cmd = [get_typst_command(), "fonts"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    return f"Error listing fonts:\n{result.stderr}"

@mcp.tool()
def list_templates() -> List[str]:
    """List available document templates."""
    if not TEMPLATE_DIR.exists():
        return []
    return [f.stem for f in TEMPLATE_DIR.glob("*.typ")]

@mcp.tool()
def get_template(name: str) -> str:
    """Get the source code of a template."""
    template_path = TEMPLATE_DIR / f"{name}.typ"
    if not template_path.exists():
        return f"Error: Template '{name}' not found."
    return template_path.read_text(encoding="utf-8")

@mcp.tool()
def create_document(path: str, template_name: Optional[str] = None, content: str = "") -> str:
    """
    Create a new Typst document.
    path: Path to save the new .typ file.
    template_name: (Optional) Name of a template to use as a starting point.
    content: (Optional) Initial content to add to the document.
    """
    target_path = pathlib.Path(path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    file_content = ""
    if template_name:
        template_path = TEMPLATE_DIR / f"{template_name}.typ"
        if template_path.exists():
            file_content = template_path.read_text(encoding="utf-8") + "\n"
        else:
            return f"Warning: Template '{template_name}' not found. Creating empty file."
            
    file_content += content
    target_path.write_text(file_content, encoding="utf-8")
    return f"Document created at {path}"

@mcp.tool()
def edit_section(path: str, name: str, new_content: str) -> str:
    """
    Edit a specific section in a Typst file marked with // SECTION: name.
    """
    filepath = pathlib.Path(path)
    if not filepath.exists():
        return f"Error: {path} not found."
    
    content = filepath.read_text(encoding="utf-8")
    start_marker = f"// SECTION: {name}"
    end_marker = f"// END: {name}"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        return f"Error: Could not find markers for section '{name}'."
        
    updated_content = (
        content[:start_idx + len(start_marker)] + 
        "\n" + new_content + "\n" + 
        content[end_idx:]
    )
    
    filepath.write_text(updated_content, encoding="utf-8")
    return f"Section '{name}' in {path} updated."

@mcp.tool()
def read_section(path: str, name: str) -> str:
    """
    Read a specific section in a Typst file marked with // SECTION: name.
    """
    filepath = pathlib.Path(path)
    if not filepath.exists():
        return f"Error: {path} not found."
    
    content = filepath.read_text(encoding="utf-8")
    start_marker = f"// SECTION: {name}"
    end_marker = f"// END: {name}"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        return f"Error: Could not find markers for section '{name}'."
        
    return content[start_idx:end_idx + len(end_marker)]

@mcp.tool()
def list_sections(path: str) -> str:
    """
    List all sections in a Typst file marked with // SECTION: name.
    """
    filepath = pathlib.Path(path)
    if not filepath.exists():
        return f"Error: {path} not found."
    
    content = filepath.read_text(encoding="utf-8")
    sections = []
    lines = content.splitlines()
    for line in lines:
        if line.startswith("// SECTION:"):
            sections.append(line.replace("// SECTION:", "").strip())
            
    if not sections:
        return f"No marked sections found in {path}."
    return "Sections found:\n" + "\n".join(f"  - {s}" for s in sections)

if __name__ == "__main__":
    mcp.run(transport="stdio")