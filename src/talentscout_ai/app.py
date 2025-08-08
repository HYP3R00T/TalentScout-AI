from __future__ import annotations

import os

import httpx
import streamlit as st

API_URL = os.environ.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="TalentScout AI", page_icon="🧑‍💻", layout="wide")

st.title("TalentScout AI — HR Resource Query Chatbot")

with st.sidebar:
    st.header("Settings")
    api_url = st.text_input("Backend API URL", value=API_URL)
    top_k = st.slider("Top K", 1, 10, 5)

if "history" not in st.session_state:
    st.session_state.history = []

prompt = st.chat_input("Ask: e.g., Find Python developers with 3+ years experience")

if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.spinner("Thinking..."):
        try:
            resp = httpx.post(f"{api_url}/chat", json={"message": prompt, "top_k": top_k}, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            st.session_state.history.append({
                "role": "assistant",
                "content": data.get("response", ""),
            })
        except Exception as e:  # noqa: BLE001
            st.session_state.history.append({
                "role": "assistant",
                "content": f"Error: {e}",
            })

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

st.divider()

st.subheader("Structured Search")
col1, col2 = st.columns(2)
with col1:
    skills_csv = st.text_input("Skills (comma-separated)", value="Python, AWS")
with col2:
    min_exp = st.number_input("Min experience (years)", min_value=0, max_value=50, value=0)

if st.button("Search Employees"):
    with st.spinner("Searching..."):
        try:
            params: dict[str, object] = {}
            skills = [s.strip() for s in skills_csv.split(",") if s.strip()]
            if skills:
                for s in skills:
                    params.setdefault("skills", []).append(s)  # type: ignore[assignment]
            if min_exp:
                params["min_experience"] = int(min_exp)
            resp = httpx.get(f"{api_url}/employees/search", params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:  # noqa: BLE001
            st.error(f"Search failed: {e}")
            data = []

    if data:
        st.success(f"Found {len(data)} employees")
        for emp in data:
            with st.expander(f"{emp['name']} — {emp['experience_years']} yrs, {', '.join(emp['skills'])}"):
                st.write(emp)
    else:
        st.info("No employees matched your filters.")
