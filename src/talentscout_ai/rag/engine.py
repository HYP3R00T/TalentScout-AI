from __future__ import annotations

from collections.abc import Iterable
from dataclasses import asdict
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from .data import SAMPLE_EMPLOYEES, Employee


class RAEngine:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> None:
        # Small, CPU-friendly by default; can be swapped for GPU if available
        self.model = SentenceTransformer(model_name)
        self._corpus: list[str] = [self._employee_to_text(e) for e in SAMPLE_EMPLOYEES]
        self._embeddings = self.model.encode(self._corpus, convert_to_numpy=True, show_progress_bar=False)

    @staticmethod
    def _employee_to_text(e: Employee) -> str:
        return (
            f"Name: {e.name}\n"
            f"Skills: {', '.join(e.skills)}\n"
            f"Experience: {e.experience_years} years\n"
            f"Projects: {', '.join(e.projects)}\n"
            f"Availability: {e.availability}"
        )

    def retrieve(self, query: str, top_k: int = 5) -> list[tuple[Employee, float]]:
        q_emb = self.model.encode([query], convert_to_numpy=True, show_progress_bar=False)
        sims = cosine_similarity(q_emb, self._embeddings)[0]
        idxs = np.argsort(-sims)[:top_k]
        return [(SAMPLE_EMPLOYEES[i], float(sims[i])) for i in idxs]

    def generate_response(self, query: str, results: list[tuple[Employee, float]], max_candidates: int = 3) -> str:
        if not results:
            return "I couldn't find matching employees. Could you rephrase or add more details?"
        lines: list[str] = []
        lines.append(f"Based on your query: '{query}', here are {min(max_candidates, len(results))} candidates:")
        for i, (emp, score) in enumerate(results[:max_candidates], start=1):
            lines.append(
                f"{i}. {emp.name} — {emp.experience_years} yrs; Skills: {', '.join(emp.skills)}; "
                f"Projects: {', '.join(emp.projects)}; Availability: {emp.availability} (score {score:.2f})"
            )
        lines.append(
            "Would you like me to check their availability for meetings or share more details about specific projects?"
        )
        return "\n".join(lines)

    def search_structured(
        self, *, skills: Iterable[str] | None = None, min_experience: int | None = None
    ) -> list[Employee]:
        out: list[Employee] = []
        for e in SAMPLE_EMPLOYEES:
            if skills and not all(s.lower() in (x.lower() for x in e.skills) for s in skills):
                continue
            if min_experience is not None and e.experience_years < min_experience:
                continue
            out.append(e)
        return out

    def serialize_employee(self, e: Employee) -> dict[str, Any]:
        return asdict(e)


# Singleton engine for simple use-cases
_engine: RAEngine | None = None


def get_engine() -> RAEngine:
    global _engine
    if _engine is None:
        _engine = RAEngine()
    return _engine
