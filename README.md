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
- **Asset Management**: Automatic organization of generated documents.
- **Remote Ready**: Built-in support for Docker and GitHub Container Registry.

---

## 🎨 Showcase: AI Benefits Poster

The following assets were generated and used for the academic poster:

![AI Art for Poster](assets/ai_art_for_poster.png)
![AI Benefits Poster](assets/ai_benefits_poster.png)

### 🎬 Demo: Typst in Action
![Typst Demo Video](assets/tyspt_demo.mov)

---

## 🚀 Quick Start (Docker)

The fastest way to use this server is via Docker. No local installation of Typst is required.

### MCP Configuration

Add this snippet to your `mcp_config.json` (for Claude Desktop or VS Code):

```json
{
  "mcpServers": {
    "typst": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "ghcr.io/vvijayaragupathy-uno/typst-mcpserver:main"
      ]
    }
  }
}
```

### Local Build

```bash
docker build -t typst-mcp-server .
docker run -i --rm typst-mcp-server
```

---

## 🛠 Local Setup (Python)

If you prefer to run the server locally:

1. **Install Typst CLI**: [typst.app/docs/cli](https://typst.app/docs/cli/)
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Server**:
   ```bash
   python3 server.py
   ```

---

## 🚀 Impact & Career Value

### How to Add to Your Resume
Do not just list it as a GitHub link. Frame it as a technical achievement:
> "Built open-source MCP server enabling Claude AI to generate academic PDF posters through natural language. Implemented FastMCP tools for dynamic poster generation, section editing, and Typst compilation. Deployed via Docker on GitHub Container Registry."

### Why this project stands out:
1. **MCP is Cutting Edge**: Most engineers have never built one.
2. **Full Stack Architecture**: You built the server, client, and agent layers.
3. **Professional DevOps**: Uses Docker + GitHub Actions + GHCR.
4. **Real Output**: Generates actual PDF posters, not just "Hello World."
5. **Immediately Usable**: Works with Claude Desktop out of the box.

---

⚖️ **License**: MIT
