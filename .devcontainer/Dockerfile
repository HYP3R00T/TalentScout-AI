FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

COPY --from=jdxcode/mise /usr/local/bin/mise /usr/local/bin/

# Activate mise in shells
RUN echo 'eval "$(mise activate bash)"' >> /home/vscode/.bashrc && \
    echo 'eval "$(mise activate zsh)"' >> /home/vscode/.zshrc

# Optional: Install minimal NVIDIA CUDA runtime to enable GPU in container when host has GPUs
# Comment these lines if you don't need GPU.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 python3-venv python3-pip curl git ca-certificates && \
    rm -rf /var/lib/apt/lists/*
