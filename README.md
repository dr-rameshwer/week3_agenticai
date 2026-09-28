# Generative AI & Agentic AI Engineering — 10-Step Practical Guide

**Prepared by Dr. Rameshwer**  
*Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*

---

## Welcome!

This repository is a lightweight, step-by-step developer handbook designed to train software engineers and students in **Generative AI, Prompt Engineering, Pydantic Schema Validation, Tool/Function Calling, and FastAPI Microservices**.

Everything is structured in **10 clean, runnable steps**. Each step contains:
- A self-contained Python program (15–40 lines).
- In-place comments and clear terminal outputs.
- A matching concise note in [`notes/`](file:///Users/rameshwer/week3_agenticai/notes/) with interview Q&A.
- Fallback simulation so you can run and test even without an API key!

---

## 10-Step Learning Progression

| Step | Topic | Source Code | Concept Note | Key Takeaway |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **First LLM Call** | [`01_hello_llm.py`](file:///Users/rameshwer/week3_agenticai/01_hello_llm.py) | [`notes/01_hello_llm.md`](file:///Users/rameshwer/week3_agenticai/notes/01_hello_llm.md) | Loading `.env`, initializing `google-genai` client, sending prompts |
| **02** | **Tokens & Cost** | [`02_tokens_and_cost.py`](file:///Users/rameshwer/week3_agenticai/02_tokens_and_cost.py) | [`notes/02_tokens.md`](file:///Users/rameshwer/week3_agenticai/notes/02_tokens.md) | Measuring input/output tokens, calculating API cost in USD |
| **03** | **Temperature** | [`03_temperature.py`](file:///Users/rameshwer/week3_agenticai/03_temperature.py) | [`notes/03_temperature.md`](file:///Users/rameshwer/week3_agenticai/notes/03_temperature.md) | Deterministic ($T=0.0$) vs Creative ($T=1.0$) sampling |
| **04** | **System Prompts** | [`04_system_instructions.py`](file:///Users/rameshwer/week3_agenticai/04_system_instructions.py) | [`notes/04_system_instructions.md`](file:///Users/rameshwer/week3_agenticai/notes/04_system_instructions.md) | Setting personas, response rules, and safety guardrails |
| **05** | **Few-Shot Learning** | [`05_few_shot_prompting.py`](file:///Users/rameshwer/week3_agenticai/05_few_shot_prompting.py) | [`notes/05_few_shot.md`](file:///Users/rameshwer/week3_agenticai/notes/05_few_shot.md) | Multi-class classification using 2–3 solved exemplars |
| **06** | **Step-by-Step Reasoning** | [`06_step_by_step_reasoning.py`](file:///Users/rameshwer/week3_agenticai/06_step_by_step_reasoning.py) | [`notes/06_reasoning.md`](file:///Users/rameshwer/week3_agenticai/notes/06_reasoning.md) | Chain-of-Thought calculations & arithmetic verification |
| **07** | **Pydantic Validation** | [`07_pydantic_validation.py`](file:///Users/rameshwer/week3_agenticai/07_pydantic_validation.py) | [`notes/07_pydantic.md`](file:///Users/rameshwer/week3_agenticai/notes/07_pydantic.md) | `BaseModel`, `Field` constraints, and `ValidationError` |
| **08** | **Structured Output** | [`08_structured_output.py`](file:///Users/rameshwer/week3_agenticai/08_structured_output.py) | [`notes/08_structured_output.md`](file:///Users/rameshwer/week3_agenticai/notes/08_structured_output.md) | Guaranteed JSON schemas with `response_schema` |
| **09** | **Tool / Function Calling** | [`09_tool_calling.py`](file:///Users/rameshwer/week3_agenticai/09_tool_calling.py) | [`notes/09_tool_calling.md`](file:///Users/rameshwer/week3_agenticai/notes/09_tool_calling.md) | Connecting LLMs to Python functions and databases |
| **10** | **FastAPI AI Service** | [`10_fastapi_ai_service.py`](file:///Users/rameshwer/week3_agenticai/10_fastapi_ai_service.py) | [`notes/10_fastapi.md`](file:///Users/rameshwer/week3_agenticai/notes/10_fastapi.md) | Asynchronous REST endpoints with Swagger UI at `/docs` |

---

## Quickstart (Under 2 Minutes)

### 1. Setup Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# venv\Scripts\activate        # Windows

pip install -r requirements.txt
```

### 2. Configure API Key (Optional)
```bash
cp .env.example .env
# Open .env and insert your GEMINI_API_KEY from https://aistudio.google.com/
```
*(If no API key is provided, all programs automatically run in educational simulated mode!)*

### 3. Run Any Step Directly
```bash
python 01_hello_llm.py
python 02_tokens_and_cost.py
python 09_tool_calling.py
python 10_fastapi_ai_service.py
```

### 4. Run Automated Self-Tests
Verify all 10 steps in one command:
```bash
python test_all.py
# or
pytest
```

---

## Author & Guide

* **Prepared by**: **Dr. Rameshwer**
* **Profile**: *Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*
