from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Availability = Literal["available", "unavailable", "busy", "on_leave"]


@dataclass
class Employee:
    id: int
    name: str
    skills: list[str]
    experience_years: int
    projects: list[str]
    availability: Availability


SAMPLE_EMPLOYEES: list[Employee] = [
    Employee(
        1,
        "Alice Johnson",
        ["Python", "React", "AWS"],
        5,
        ["E-commerce Platform", "Healthcare Dashboard"],
        "available",
    ),
    Employee(
        2,
        "Bob Smith",
        ["Java", "Docker", "Kubernetes"],
        7,
        ["Microservices Platform", "Banking API"],
        "busy",
    ),
    Employee(
        3,
        "Sarah Chen",
        ["Machine Learning", "TensorFlow", "PyTorch"],
        6,
        ["Medical Diagnosis Platform", "Image Analysis"],
        "available",
    ),
    Employee(
        4,
        "Michael Rodriguez",
        ["scikit-learn", "pandas", "HIPAA"],
        4,
        ["Patient Risk Prediction System", "EHR Integration"],
        "available",
    ),
    Employee(
        5,
        "Emma Davis",
        ["React Native", "TypeScript", "GraphQL"],
        3,
        ["Mobile Commerce App", "Social Media MVP"],
        "unavailable",
    ),
    Employee(
        6,
        "Liam Brown",
        ["AWS", "Docker", "Terraform"],
        5,
        ["Cloud Migration", "DevOps CI/CD"],
        "available",
    ),
    Employee(
        7,
        "Olivia Wilson",
        ["Python", "FastAPI", "PostgreSQL"],
        4,
        ["Internal HR Tool", "Analytics Service"],
        "busy",
    ),
    Employee(
        8,
        "Noah Miller",
        ["C#", ".NET", "Azure"],
        8,
        ["ERP System", "Inventory Management"],
        "available",
    ),
    Employee(
        9,
        "Ava Martinez",
        ["Data Science", "NLP", "SpaCy"],
        5,
        ["Customer Support Chatbot", "Text Analytics"],
        "available",
    ),
    Employee(
        10,
        "William Anderson",
        ["Go", "Docker", "AWS"],
        6,
        ["High-throughput API", "Monitoring Platform"],
        "on_leave",
    ),
    Employee(
        11,
        "Sophia Thomas",
        ["React", "Node.js", "AWS"],
        4,
        ["Real-time Dashboard", "Admin Portal"],
        "available",
    ),
    Employee(
        12,
        "James Lee",
        ["Python", "PyTorch", "Computer Vision"],
        5,
        ["Object Detection", "Video Analytics"],
        "busy",
    ),
    Employee(
        13,
        "Mia Harris",
        ["SQL", "dbt", "Snowflake"],
        6,
        ["Data Warehouse", "ETL Pipelines"],
        "available",
    ),
    Employee(
        14,
        "Ethan Clark",
        ["Rust", "WebAssembly", "Edge"],
        3,
        ["Edge Compute PoC", "Realtime Processing"],
        "available",
    ),
    Employee(
        15,
        "Isabella Lewis",
        ["Python", "AWS", "Docker"],
        4,
        ["ML Ops", "Model Serving"],
        "available",
    ),
]
