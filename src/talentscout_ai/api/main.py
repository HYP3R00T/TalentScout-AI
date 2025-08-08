from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from talentscout_ai.rag.engine import get_engine

app = FastAPI(title="TalentScout AI", version="0.1.0")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=2)
    top_k: int = Field(5, ge=1, le=10)


class ChatResponse(BaseModel):
    response: str


class EmployeeOut(BaseModel):
    id: int
    name: str
    skills: list[str]
    experience_years: int
    projects: list[str]
    availability: str


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> Any:
    eng = get_engine()
    results = eng.retrieve(req.message, top_k=req.top_k)
    resp = eng.generate_response(req.message, results)
    return ChatResponse(response=resp)


@app.get("/employees/search", response_model=list[EmployeeOut])
async def employee_search(
    skills: list[str] | None = None,
    min_experience: int | None = None,
) -> Any:
    eng = get_engine()
    emps = eng.search_structured(skills=skills or None, min_experience=min_experience)
    return [EmployeeOut(**eng.serialize_employee(e)) for e in emps]


@app.get("/healthz")
async def health() -> dict[str, str]:
    return {"status": "ok"}
