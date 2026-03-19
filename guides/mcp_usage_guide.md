# MCP Typst Server Usage Guide

This server provides tools to help you create and manage Typst documents using an AI.

## Workflow Overview
1. **Initialize**: Ask the AI to "List available templates".
2. **Create**: "Create a resume using the `resume` template".
3. **Draft**: The AI will generate the initial content with `// SECTION` markers.
4. **Edit**: "Rewrite the Education section in my CV".
5. **Compile**: "Compile my CV to PDF".

## Available Tools
- `list_templates`: Shows you what document types are ready (CV, Paper, Poster, etc.).
- `create_document`: Starts a new file. You can specify a template.
- `edit_section`: Makes surgery-like edits to your file without rewriting everything.
- `compile_document`: Generates a PDF, PNG, or SVG.
- `query_metadata`: Useful for deep inspection of the document structure.
- `list_fonts`: Handy if you want to use a specific font.

## Best Practices
- **Use Markers**: Always wrap logical sections of your document in `// SECTION: Name` and `// END: Name`. This allows the AI to edit one part without touching the rest.
- **Incremental Changes**: Instead of asking for a whole document at once, ask for the structure first, then fill in sections one by one.
- **Compile Often**: Typst is fast! Compile your document frequently to catch syntax errors early.
