# Use a lightweight Python image
FROM python:3.11-slim

# Install Typst
# We download the latest release from GitHub
RUN apt-get update && apt-get install -y curl xz-utils && \
    curl -L https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-musl.tar.xz | tar -xJ --strip-components=1 -C /usr/local/bin typst-x86_64-unknown-linux-musl/typst && \
    apt-get remove -y curl xz-utils && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy project configuration and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the server code, templates, and guides
COPY server.py .
COPY agent.py .
COPY client.py .
COPY templates/ ./templates/
COPY guides/ ./guides/

# Expose the port (though MCP usually uses stdio)
# No EXPOSE needed for stdio-based MCP

# Run the server
ENTRYPOINT ["python", "server.py"]
