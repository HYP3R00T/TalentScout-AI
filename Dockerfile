FROM python:3.13-slim AS base

# Prevent Python from writing pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# System deps (curl for installing uv)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates git \
    && rm -rf /var/lib/apt/lists/*

# Install uv (fast Python package manager) and ensure it's on PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:/app/.venv/bin:${PATH}"

# Copy project metadata and docs required by build
COPY pyproject.toml uv.lock README.md LICENSE ./
COPY src ./src

# Install dependencies and the project into a local .venv (no dev deps)
RUN uv sync --frozen --no-dev

# Cache location for HF/Transformers models (mount a volume for persistence)
ENV HF_HOME=/hf-cache \
    TRANSFORMERS_CACHE=/hf-cache

# Default command runs the API; docker-compose overrides for the Streamlit app
EXPOSE 8000 8501
CMD ["uvicorn", "talentscout_ai.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
