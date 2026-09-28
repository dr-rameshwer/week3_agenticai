# Generative AI & Agentic AI Engineering — Complete Practical Guide

**Prepared by Dr. Rameshwer**  
*Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*

---

## 📖 Table of Contents
1. [Course Overview & Learning Objectives](#1-course-overview--learning-objectives)
2. [📅 Week 3 Study Roadmap (How to Study This Week)](#2--week-3-study-roadmap-how-to-study-this-week)
3. [Python Fundamentals Required for the Code](#3-python-fundamentals-required-for-the-code)
4. [Generative AI & LLM Core Concepts](#4-generative-ai--llm-core-concepts)
5. [Pydantic & Data Validation Basics](#5-pydantic--data-validation-basics)
6. [Tool / Function Calling Basics (Agentic AI)](#6-tool--function-calling-basics-agentic-ai)
7. [FastAPI Microservices & Web APIs](#7-fastapi-microservices--web-apis)
8. [The 10-Step Code Roadmap](#8-the-10-step-code-roadmap)
9. [Quickstart Setup (Run in 2 Minutes)](#9-quickstart-setup-run-in-2-minutes)
10. [Automated Self-Testing](#10-automated-self-testing)

---

## 1. Course Overview & Learning Objectives

This repository is a practical, step-by-step developer handbook. It is designed to take you from writing your first LLM API call to building type-safe, tool-augmented, production-ready AI microservices in Python.

### What You Will Master:
- **API Invocation**: Programmatically connecting to Google Gemini with `google-genai`.
- **Token Economics**: Calculating prompt vs. completion tokens, context limits, and USD cost.
- **Generation Control**: Tuning temperature ($0.0 \to 1.0$), system instructions, and few-shot exemplars.
- **Structured Reasoning**: Forcing observable intermediate problem-solving steps before answers.
- **Data Validation**: Building zero-defect schemas with Pydantic v2 (`BaseModel`, `Field`, `ValidationError`).
- **Guaranteed JSON Output**: Constraining LLMs to return strict JSON matching Pydantic models.
- **Tool Calling (Agents)**: Empowering LLMs to query live Python functions and local databases.
- **FastAPI Microservices**: Serving asynchronous REST endpoints with interactive Swagger UI (`/docs`).

---

## 2. 📅 Week 3 Study Roadmap (How to Study This Week)

Follow this 5-Day structured study plan (approx. 45–60 minutes per day):

```mermaid
flowchart LR
    D1[Day 1: API & Tokens] --> D2[Day 2: Prompting & Personas]
    D2 --> D3[Day 3: Reasoning & Pydantic]
    D3 --> D4[Day 4: JSON & Tool Calling]
    D4 --> D5[Day 5: FastAPI Microservice]
```

### 🗓️ Day 1: API Foundations & Token Mechanics
* **Goal**: Master programmatic LLM calls, environment credentials, and token economics.
* **Code to Run**:
  * [`01_hello_llm.py`](file:///Users/rameshwer/week3_agenticai/01_hello_llm.py) — First API call, `.env` credentials, response extraction.
  * [`02_tokens_and_cost.py`](file:///Users/rameshwer/week3_agenticai/02_tokens_and_cost.py) — Tokens, context windows, and USD cost estimation.
* **Notes to Read**:
  * [`notes/01_hello_llm.md`](file:///Users/rameshwer/week3_agenticai/notes/01_hello_llm.md)
  * [`notes/02_tokens.md`](file:///Users/rameshwer/week3_agenticai/notes/02_tokens.md)
* **Hands-on Action**: Run both scripts. Modify the prompt in `01_hello_llm.py` with your own question. Calculate the USD cost for 10,000 requests in `02_tokens_and_cost.py`.

---

### 🗓️ Day 2: Prompt Engineering, Temperature & Personas
* **Goal**: Control model behavior, system personas, and multi-class classification without fine-tuning.
* **Code to Run**:
  * [`03_temperature.py`](file:///Users/rameshwer/week3_agenticai/03_temperature.py) — Compare deterministic ($T=0.0$) vs creative ($T=1.0$).
  * [`04_system_instructions.py`](file:///Users/rameshwer/week3_agenticai/04_system_instructions.py) — System personas and guardrails.
  * [`05_few_shot_prompting.py`](file:///Users/rameshwer/week3_agenticai/05_few_shot_prompting.py) — Few-shot multi-class ticket classification.
* **Notes to Read**:
  * [`notes/03_temperature.md`](file:///Users/rameshwer/week3_agenticai/notes/03_temperature.md)
  * [`notes/04_system_instructions.md`](file:///Users/rameshwer/week3_agenticai/notes/04_system_instructions.md)
  * [`notes/05_few_shot.md`](file:///Users/rameshwer/week3_agenticai/notes/05_few_shot.md)
* **Hands-on Action**: Change the persona in Step 4 to a "Senior Security Auditor" and test new ticket categories in Step 5.

---

### 🗓️ Day 3: Structured Reasoning & Pydantic Validation
* **Goal**: Master Chain-of-Thought problem solving and zero-defect runtime data validation.
* **Code to Run**:
  * [`06_step_by_step_reasoning.py`](file:///Users/rameshwer/week3_agenticai/06_step_by_step_reasoning.py) — Step-by-step arithmetic decomposition & verification.
  * [`07_pydantic_validation.py`](file:///Users/rameshwer/week3_agenticai/07_pydantic_validation.py) — Pydantic `BaseModel`, `Field` bounds, and `ValidationError`.
* **Notes to Read**:
  * [`notes/06_reasoning.md`](file:///Users/rameshwer/week3_agenticai/notes/06_reasoning.md)
  * [`notes/07_pydantic.md`](file:///Users/rameshwer/week3_agenticai/notes/07_pydantic.md)
* **Hands-on Action**: Add a new field (`is_honor_student: bool = False`) to the Pydantic schema in Step 7 and test invalid input strings to trigger a `ValidationError`.

---

### 🗓️ Day 4: Guaranteed JSON & Agentic Tool Calling
* **Goal**: Force LLMs to output guaranteed JSON schemas and connect models to live Python functions.
* **Code to Run**:
  * [`08_structured_output.py`](file:///Users/rameshwer/week3_agenticai/08_structured_output.py) — Constrained decoding with Pydantic `response_schema`.
  * [`09_tool_calling.py`](file:///Users/rameshwer/week3_agenticai/09_tool_calling.py) — 5-step tool calling loop with live database lookup.
* **Notes to Read**:
  * [`notes/08_structured_output.md`](file:///Users/rameshwer/week3_agenticai/notes/08_structured_output.md)
  * [`notes/09_tool_calling.md`](file:///Users/rameshwer/week3_agenticai/notes/09_tool_calling.md)
* **Hands-on Action**: Query an unknown student roll number in Step 9 to observe how the tool handles missing records and returns grounded answers without hallucinating.

---

### 🗓️ Day 5: Production FastAPI AI Microservice & Verification
* **Goal**: Wrap your AI system into an asynchronous REST API and run full automated verification.
* **Code to Run**:
  * [`10_fastapi_ai_service.py`](file:///Users/rameshwer/week3_agenticai/10_fastapi_ai_service.py) — FastAPI REST service with interactive Swagger UI at `/docs`.
  * [`test_all.py`](file:///Users/rameshwer/week3_agenticai/test_all.py) — Automated self-test suite for all 10 steps.
* **Notes to Read**:
  * [`notes/10_fastapi.md`](file:///Users/rameshwer/week3_agenticai/notes/10_fastapi.md)
* **Hands-on Action**: Start the server with `python 10_fastapi_ai_service.py`, open `http://127.0.0.1:8000/docs` in your browser, and test the `/api/v1/advisory` endpoint. Run `python test_all.py` to verify all 10 steps.

---

## 3. Python Fundamentals Required for the Code

You do not need to be an expert in advanced Python. Below are all the essential syntax features used across the 10 programs:

### 2.1. Importing Modules (`import` and `from ... import ...`)
In Python, libraries and helper modules are brought into your script using `import`:
```python
import os                       # Imports the built-in operating system module
from dotenv import load_dotenv  # Imports only the specific function load_dotenv
from google import genai        # Imports the Google GenAI SDK
from google.genai import types  # Imports configuration dataclasses
```

### 2.2. Environment Variables & `.env` Files
API keys should never be written directly inside your Python files.
* A `.env` file stores secrets as key-value pairs:
  ```env
  GEMINI_API_KEY=AIzaSyD-YourSecretKeyHere
  ```
* `load_dotenv()` reads the `.env` file and loads the keys into your operating system environment.
* `os.getenv("GEMINI_API_KEY")` retrieves the key safely.

### 2.3. Formatted String Literals (f-strings)
f-strings allow you to embed variables and expressions directly inside text:
```python
name = "Alice"
score = 3.8542
print(f"Student: {name}, GPA: {score:.2f}")  # Output: Student: Alice, GPA: 3.85
```

### 2.4. Python Lists & Dictionaries
* **List `[]`**: Ordered collection of items.
  ```python
  courses = ["Data Structures", "FastAPI", "Agentic AI"]
  ```
* **Dictionary `{}`**: Key-value pairs for structured lookups.
  ```python
  student = {"roll_no": "CS2026", "name": "Alice", "gpa": 3.9}
  print(student["name"])  # 'Alice'
  ```

### 2.5. Functions, Type Hints & Docstrings
Python 3 allows type annotations (`name: str`, `gpa: float`) and triple-quoted docstrings (`"""..."""`):
```python
def lookup_student(roll_no: str) -> dict:
    """Retrieves student details by roll number from the database.

    Args:
        roll_no: Unique student identification string (e.g. 'CS2026').
    """
    return {"roll_no": roll_no, "status": "Passed"}
```
> **Why this matters**: Google Gemini reads the **type hints** and **docstrings** to know how to call the function as a tool!

### 2.6. Error Handling (`try ... except ...`)
Prevents your program from crashing when an error occurs:
```python
try:
    # Code that might fail (e.g. network call, invalid data)
    result = client.models.generate_content(...)
except Exception as e:
    print(f"Operation failed safely: {e}")
```

---

## 3. Generative AI & LLM Core Concepts

### 3.1. What is an LLM and API?
* **Base Model**: The neural network weights trained on vast text data.
* **API (Application Programming Interface)**: The secure cloud service that runs the model on GPUs and sends you answers over HTTPS.
* **SDK (`google-genai`)**: The official Python package that makes HTTP requests in 3 lines of code.

### 3.2. What are Tokens?
LLMs do not read letters or words; they read **Tokens** (sub-word chunks).
* **Rule of thumb**: $100\text{ tokens} \approx 75\text{ words}$ (or 1 token $\approx$ 4 characters).
* **Input / Prompt Tokens**: Tokens you send to the model (cheaper).
* **Output / Candidate Tokens**: Tokens the model generates (more expensive).
* **Context Window**: Maximum tokens a model can remember in a single interaction.

### 3.3. Temperature ($T$)
Controls randomness in the token probability selection:
* **Low Temperature ($T = 0.0$)**: *Deterministic & Precise*. Always selects the most probable token. Use for code generation, math, SQL, and classification.
* **High Temperature ($T = 0.8\text{--}1.0$)**: *Creative & Exploratory*. Flattens probabilities. Use for brainstorming, storytelling, and copy generation.

### 3.4. System Instructions vs. User Prompts
* **System Instruction**: Persistent operating rules and persona (e.g. *"You are a strict programming mentor. Keep answers under 2 sentences."*).
* **User Prompt**: The immediate task or question (e.g. *"What is a Python dictionary?"*).

### 3.5. Few-Shot Prompting
Providing 2–4 solved examples (Input $\to$ Output pairs) inside the prompt. This anchors the model's pattern recognition to guarantee exact formatting and high classification accuracy without training weights.

### 3.6. Step-by-Step Reasoning (Chain-of-Thought)
Directly guessing the answer to a multi-step calculation often causes hallucinations. Instructing the model to output:
1. `STEP-BY-STEP CALCULATION`
2. `VERIFICATION`
3. `FINAL ANSWER`  
allows newly generated intermediate tokens to act as working memory in the context window.

---

## 4. Pydantic & Data Validation Basics

Python's built-in type hints are purely advisory and ignored at runtime. **Pydantic v2** enforces strict runtime validation.

### 4.1. Defining a `BaseModel`
```python
from pydantic import BaseModel, Field, ValidationError

class StudentProfile(BaseModel):
    roll_no: str = Field(min_length=4, max_length=10)
    name: str = Field(min_length=2)
    gpa: float = Field(ge=0.0, le=4.0)  # ge = greater than or equal, le = less than or equal
```

### 4.2. Validation & Serialization
* **Valid Data**:
  ```python
  student = StudentProfile(roll_no="CS2026", name="Alice", gpa=3.85)
  print(student.model_dump())       # Converts to Python dict
  print(student.model_dump_json())  # Converts to JSON string
  ```
* **Invalid Data**:
  ```python
  # Raises ValidationError: gpa cannot exceed 4.0
  bad_student = StudentProfile(roll_no="CS", name="A", gpa=4.95)
  ```

### 4.3. Constrained Structured Output
Instead of asking the LLM to *"please return JSON"* (which often breaks or includes markdown backticks), pass your Pydantic model directly to the API:
```python
config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=StudentProfile,
    temperature=0.0
)
```
The API uses **Constrained Decoding** (Context-Free Grammar masking) to guarantee 100% valid JSON matching the schema.

---

## 5. Tool / Function Calling Basics (Agentic AI)

LLMs do not have access to live databases, private student records, or arithmetic engines. **Tool Calling** gives models the ability to request external computation.

### The 5-Step Lifecycle:
```text
1. User asks question: "What is student CS2026's GPA?"
        ↓
2. LLM detects it needs private data and requests tool: lookup_student_record(roll_no="CS2026")
        ↓
3. Python application intercepts request and executes local Python function against database
        ↓
4. Application sends tool output (e.g. {"name": "Alice", "gpa": 3.9}) back to LLM
        ↓
5. LLM synthesizes ground-truth answer: "Student Alice has a GPA of 3.9."
```

```python
def lookup_student_record(roll_no: str) -> dict:
    """Retrieves student details by roll number."""
    return STUDENT_DB.get(roll_no.upper(), {"found": False})

# Bind tool to generation config
config = types.GenerateContentConfig(tools=[lookup_student_record])
```

---

## 6. FastAPI Microservices & Web APIs

FastAPI allows you to wrap your AI logic into a high-throughput web server.

### 6.1. Core Concepts:
* **Endpoint / Route**: A specific URL path (e.g., `POST /api/v1/advisory`).
* **Asynchronous Handlers (`async def`)**: LLM API calls take 0.5s–3s. Declaring routes with `async def` allows the web server to handle hundreds of other incoming requests concurrently while waiting for the LLM response.
* **OpenAPI / Swagger UI**: FastAPI automatically reads your Pydantic schemas and generates an interactive web interface at `/docs`.

```python
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="AI Advisory Service")

class QueryRequest(BaseModel):
    subject: str
    question: str

class QueryResponse(BaseModel):
    subject: str
    advice: str

@app.post("/api/v1/advisory", response_model=QueryResponse)
async def get_advisory(req: QueryRequest):
    return QueryResponse(subject=req.subject, advice="Practice coding daily.")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

---

## 7. The 10-Step Code Roadmap

Each Python program in the root directory is self-contained (15–40 lines) with fallback simulation mode:

| Step | Script | Concept Note | What It Demonstrates |
| :---: | :--- | :--- | :--- |
| **01** | [`01_hello_llm.py`](file:///Users/rameshwer/week3_agenticai/01_hello_llm.py) | [`notes/01_hello_llm.md`](file:///Users/rameshwer/week3_agenticai/notes/01_hello_llm.md) | Loading `.env`, connecting client, sending first prompt |
| **02** | [`02_tokens_and_cost.py`](file:///Users/rameshwer/week3_agenticai/02_tokens_and_cost.py) | [`notes/02_tokens.md`](file:///Users/rameshwer/week3_agenticai/notes/02_tokens.md) | Reading token counts (`usage_metadata`) & USD cost |
| **03** | [`03_temperature.py`](file:///Users/rameshwer/week3_agenticai/03_temperature.py) | [`notes/03_temperature.md`](file:///Users/rameshwer/week3_agenticai/notes/03_temperature.md) | Comparing Deterministic ($T=0.0$) vs Creative ($T=1.0$) |
| **04** | [`04_system_instructions.py`](file:///Users/rameshwer/week3_agenticai/04_system_instructions.py) | [`notes/04_system_instructions.md`](file:///Users/rameshwer/week3_agenticai/notes/04_system_instructions.md) | Defining mentor persona rules and guardrails |
| **05** | [`05_few_shot_prompting.py`](file:///Users/rameshwer/week3_agenticai/05_few_shot_prompting.py) | [`notes/05_few_shot.md`](file:///Users/rameshwer/week3_agenticai/notes/05_few_shot.md) | Classifying tickets using 3 solved demonstration pairs |
| **06** | [`06_step_by_step_reasoning.py`](file:///Users/rameshwer/week3_agenticai/06_step_by_step_reasoning.py) | [`notes/06_reasoning.md`](file:///Users/rameshwer/week3_agenticai/notes/06_reasoning.md) | GPA calculation with step-by-step verification |
| **07** | [`07_pydantic_validation.py`](file:///Users/rameshwer/week3_agenticai/07_pydantic_validation.py) | [`notes/07_pydantic.md`](file:///Users/rameshwer/week3_agenticai/notes/07_pydantic.md) | Pydantic v2 schemas, `Field` bounds, and error catching |
| **08** | [`08_structured_output.py`](file:///Users/rameshwer/week3_agenticai/08_structured_output.py) | [`notes/08_structured_output.md`](file:///Users/rameshwer/week3_agenticai/notes/08_structured_output.md) | Forcing guaranteed JSON output matching Pydantic schema |
| **09** | [`09_tool_calling.py`](file:///Users/rameshwer/week3_agenticai/09_tool_calling.py) | [`notes/09_tool_calling.md`](file:///Users/rameshwer/week3_agenticai/notes/09_tool_calling.md) | Python function tool registration & database lookup |
| **10** | [`10_fastapi_ai_service.py`](file:///Users/rameshwer/week3_agenticai/10_fastapi_ai_service.py) | [`notes/10_fastapi.md`](file:///Users/rameshwer/week3_agenticai/notes/10_fastapi.md) | Complete async REST microservice with `/docs` |

---

## 8. Quickstart Setup (Run in 2 Minutes)

### Step 1: Create and Activate Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key (Optional)
```bash
cp .env.example .env
```
Open `.env` and paste your free key from [Google AI Studio](https://aistudio.google.com/):
```env
GEMINI_API_KEY=your_actual_key_here
GEMINI_MODEL=gemini-2.5-flash
```
*(If no key is configured, all scripts automatically run in simulated mode so you can still learn without interruption!)*

### Step 4: Run Any Step
```bash
python 01_hello_llm.py
python 02_tokens_and_cost.py
python 07_pydantic_validation.py
python 09_tool_calling.py
python 10_fastapi_ai_service.py
```

---

## 9. Automated Self-Testing

Verify that all 10 programs and API endpoints execute properly with a single command:

```bash
python test_all.py
# or
pytest
```

---

## Author & Guide

* **Prepared by**: **Dr. Rameshwer**
* **Profile**: *Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*
* **Mission**: Training developers and students into production-ready Agentic AI engineers through clean, practical, and type-safe software development.
