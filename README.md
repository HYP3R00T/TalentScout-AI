# HR Resource Query Chatbot

An intelligent HR assistant that answers resource allocation queries like "Find Python developers with 3+ years experience" using a lightweight RAG pipeline. Backend is FastAPI; frontend is Streamlit.

## Setup & Installation

```pwsh
# Install uv (if needed) and dependencies
uv sync

# Run API (FastAPI)
uv run uvicorn talentscout_ai.api.main:app --reload --host 0.0.0.0 --port 8000

# In another terminal, run Streamlit app
uv run streamlit run src/talentscout_ai/app.py --server.port 8501
```

Devcontainer (optional): The workspace includes a devcontainer that forwards ports 8000 and 8501 and requests GPU access (`--gpus=all`). Ensure Docker has the NVIDIA container toolkit on the host. If you don't need GPU, remove `runArgs` in `.devcontainer/devcontainer.json`.

## API Documentation

- POST /chat: Submit a natural language query. Body: `{ "message": "Find Python devs", "top_k": 5 }`.
- GET /employees/search: Structured search with query params: `skills=Python&skills=AWS&min_experience=3`.
- GET /healthz: Health check.

Once the API is running, visit <http://localhost:8000/docs> for interactive docs.

## Architecture

- Data: In-memory sample dataset (15 employees) defined in `talentscout_ai/rag/data.py`.
- Retrieval: SentenceTransformers embeddings + cosine similarity.
- Augmentation: Concatenates relevant employee profiles.
- Generation: Template-based natural language response (no external LLM by default). Can be swapped to OpenAI or local LLM later.
- Backend: FastAPI, async endpoints.
- Frontend: Streamlit chat UI with structured search.

## Capabilities

- Chat-driven employee recommendations (RAG-lite)
- Structured filters (skills, min experience)
- Health endpoint and FastAPI docs
- Devcontainer with optional GPU, forwarded ports

## AI Development Process

- Assistants used: GitHub Copilot (primary), ChatGPT (planning), Copilot Chat in VS Code (inline edits).
- AI helped with: project scaffolding, API and Streamlit wiring, RAG structure, devcontainer GPU options.
- Code composition: ~70% AI-assisted, 30% hand-written/refined.
- Interesting AI outputs: Ready-to-run tasks.json for Windows pwsh; minimal RAG engine using sentence-transformers; optional GPU flags.
- Manual work: Repository integration, lint fixes, parameter validations, README authoring.

## Technical Decisions

- Started with embedding similarity + templated generation (no external LLM) to keep setup local and fast.
- SentenceTransformers all-MiniLM-L6-v2 for speed and acceptable semantic retrieval; can switch to more powerful models or GPU.
- FastAPI for robust typing and auto-docs; Streamlit for quick chat UI.
- Consider OpenAI or local LLM (Ollama) for higher-quality generation later; trade-offs: cost/latency/privacy.

## Future Improvements

- Swap templated generation with an LLM (OpenAI or Ollama) and add tool grounding.
- Persist vector index (FAISS) and dataset loading from JSON/CSV.
- Add more entity filters (availability, projects), and UI facets.
- Tests for RAG ranking and endpoint contracts.

## Demo

- Local: Run both API and app as shown above, then open <http://localhost:8501>

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please follow the coding standards defined in `.github/copilot-instructions.md`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
