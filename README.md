# 📝 Typst MCP Server

A professional Model Context Protocol (MCP) server that brings **Typst's** high-quality document typesetting to your AI workflows.

---

## 🧐 The Problem
Creating academic posters requires LaTeX or design tools. Both are complex, slow, and hard to iterate on.

## 💡 The Solution
Talk to Claude in plain English:
*"Create a poster about AI in manufacturing with Introduction, Methods, Results sections."*

Claude uses this MCP server to generate, edit, and compile a professional PDF poster automatically.

---

## ✨ Features

- **Professional Templates**: Create CVs, Papers, Posters, and Reports instantly.
- **High-Quality Rendering**: Compile `.typ` files into PDF, PNG, or SVG.
- **Volume Map Support**: Work directly with your local files through Docker.
- **Remote Ready**: Support for Docker and GitHub Container Registry (GHCR).

---

## 🎨 Showcase: AI Benefits Poster

The following assets were generated and used for the academic poster:

![AI Art for Poster](assets/ai_art_for_poster.png)
![AI Benefits Poster](assets/ai_benefits_poster.png)

### 🎬 Demo: Typst in Action
![Typst Demo Video](assets/tyspt_demo.mov)

---

## 🚀 Getting Started (Docker)

The fastest and most stable way to use this server is via Docker. No local installation of Typst is required.

### 1. Configure MCP
Add this snippet to your `mcp_config.json` (Claude Desktop, IDEs, or other MCP Clients):

```json
{
  "mcpServers": {
    "typst": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-v", "/Users/yourname/Documents/TypstProjects:/app",
        "ghcr.io/vvijayaragupathy-uno/typst-mcpserver:main"
      ]
    }
  }
}
```

> [!TIP]
> **Easy Mode**: Create a default project folder at `~/Documents/TypstProjects` and update the path above with your Mac username.

> [!IMPORTANT]
> **Why the `-v` (Volume Mount) is required:**
> Docker containers are isolated. Without this "bridge" from your Mac to `/app` inside the container, the AI cannot see or compile your local files.

### 2. Verify Connection
Run this in your terminal to ensure the server is responding correctly:

```bash
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}' | docker run --rm -i ghcr.io/vvijayaragupathy-uno/typst-mcpserver:main
```

---

## 🛠 Available Tools

Once installed, your AI agent can use these powerful tools:

- `create_document`: Start a new `.typ` file (optionally from a template).
- `compile_document`: Turn your `.typ` source into a PDF, PNG, or SVG.
- `list_templates`: Browse built-in templates (CV, Resume, Poster, Paper, etc.).
- `list_fonts`: Check available system fonts for styling.
- `edit_section`: Update specific parts of a document marked with section tags.
- `query_metadata`: Extract data from Typst files for analysis.

---

## 🐍 Native Setup (Optional)

If you prefer to run the server without Docker:

1. **Install Typst CLI**: [typst.app/docs/cli](https://typst.app/docs/cli/)
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Server**:
   ```bash
   python3 server.py
   ```

⚖️ **License**: MIT
