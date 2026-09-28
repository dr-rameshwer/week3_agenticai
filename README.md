# Generative AI Engineering — Practical Developer Guide & Training Repository

**Prepared by Dr. Rameshwer**  
*Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*  
*Self-Paced Training Resource | 100% Self-Evaluated Hands-On Engineering Handbook*

---

## 1. Resource Purpose

Welcome to the **Generative AI & Agentic AI Engineering Practical Guide**.

This repository is designed as a self-contained, self-paced, and self-evaluating engineering guide to bridge the gap between AI theory and production software development. Rather than treating Large Language Models (LLMs) as black-box chat interfaces, this guide trains you to build deterministic, type-safe, observable, and tool-augmented microservices in Python.

### Self-Paced Learning & Self-Evaluation
All exercises, laboratory problem sets, viva questions, and technical interview scenarios include **complete reference answers, runnable solution scripts, automated test cases, and self-verification rubrics**. You can test, benchmark, and evaluate your own solutions instantly without waiting for manual grading.

Every topic is presented through an unbroken progression:
$$\text{Core Concept} \longrightarrow \text{Micro-Program (10--40 lines)} \longrightarrow \text{Line-by-Line Breakdown} \longrightarrow \text{Execution} \longrightarrow \text{Self-Experiment} \longrightarrow \text{Self-Evaluation Task}$$

---

## 2. Who This Guide Is For

* **Software Engineers & Backend Developers** transitioning into Generative AI, RAG, and Agentic AI development.
* **Full-Stack Developers** looking to build AI-powered microservices using Python, Pydantic, and FastAPI.
* **Students & Self-Learners** preparing for technical interviews, viva voce examinations, and production portfolio projects.

---

## 3. Prerequisite Knowledge

This training is designed with progressive scaffolding. You do **not** need advanced Python knowledge before starting. When new Python language features appear (such as `import ... as ...`, f-strings, decorators, `*args/**kwargs`, Pydantic models, or `async/await`), they are clearly explained in-place before being utilized.

Basic familiarity with:
1. Fundamental programming concepts (variables, conditions, loops, functions).
2. Terminal / Command-line basics (navigating directories, running scripts).
3. Basic HTTP concepts (URLs, client-server model).

---

## 4. Key Learning Outcomes

Upon completing this practical guide, you will be able to:

1. **Interact Programmatically with Frontier LLMs**: Authenticate, configure, and invoke models using modern SDKs (`google-genai` and `openai`).
2. **Measure & Optimize Token Economics**: Inspect tokenization mechanics, analyze prompt vs. completion costs, and manage context limits.
3. **Control Output Behavior**: Tune temperature, top-p, and system personas for deterministic classification or creative generation.
4. **Engineer High-Performance Prompts**: Apply few-shot demonstrations and observable chain-of-thought problem decomposition.
5. **Enforce Type Safety with Pydantic**: Define schemas, custom validators, and serialization workflows to guarantee zero-defect data structures.
6. **Extract Structured Output**: Force LLMs to output guaranteed JSON matching Pydantic schemas for backend ingestion.
7. **Implement Function / Tool Calling**: Bind Python functions and simulated databases to LLMs to give models real-time computation and live data access.
8. **Build Production FastAPI Microservices**: Deploy asynchronous REST API endpoints with automated OpenAPI/Swagger documentation, schema validation, and health checks.
9. **Architect a Unified Capstone**: Assemble all components into an end-to-end Student Academic Advisory AI Service.
10. **Master Technical Interviews & Viva Voce**: Confidently answer theoretical and architectural questions on Generative AI systems.

---

## 5. Repository Structure

```text
week3_agenticai/
│
├── README.md                           # Master guide overview, self-paced learning model
├── COURSE_ROADMAP.md                   # Detailed learning trajectory & timelines
├── SETUP.md                            # Step-by-step installation and environment setup
├── TROUBLESHOOTING.md                  # Comprehensive error reference & debugging guide
├── INTERVIEW_QUESTIONS.md              # Technical interview questions and complete answers
├── VIVA_QUESTIONS.md                   # Viva voce oral examination preparation guide with answers
├── ASSIGNMENTS.md                      # Self-evaluated assignments with complete solution codes
├── PROJECT_IDEAS.md                    # Portfolio project ideas & extensions
├── requirements.txt                    # Project Python dependencies
├── .env.example                        # Template for environment variables
├── .gitignore                          # Standard git ignore rules
│
├── week03-generative-ai/
│   ├── README.md                       # Week 3 specific guide & learning path
│   │
│   ├── notes/                          # 21-section comprehensive theory & concept guides
│   │   ├── 01_llm_fundamentals.md      # API vs Model, Client initialization, authentication
│   │   ├── 02_tokens.md                # Tokenization, prompt/completion tokens, cost tracking
│   │   ├── 03_temperature.md           # Sampling, temperature, determinism vs creativity
│   │   ├── 04_system_instructions.md   # Behavioral boundaries, personas, role separation
│   │   ├── 05_few_shot_prompting.md    # Demonstration-based in-context learning
│   │   ├── 06_reasoning_prompting.md   # Step-by-step problem decomposition & verification
│   │   ├── 07_pydantic.md              # Type hints, BaseModel, Field validation, errors
│   │   ├── 08_structured_output.md     # Guaranteed JSON schemas with Pydantic
│   │   ├── 09_tool_calling.md          # Function signatures, execution loop, DB tools
│   │   ├── 10_fastapi.md               # Async routes, request/response models, Swagger
│   │   └── 11_capstone.md              # Architecture of the full AI Microservice
│   │
│   ├── examples/                       # Clean, verified, 10–40 line micro-programs
│   │   ├── 01_hello_llm.py             # Smallest working LLM call
│   │   ├── 02_token_inspector.py       # Inspecting token usage metadata
│   │   ├── 03_temperature.py           # Comparing temperature settings
│   │   ├── 04_system_instruction.py    # Academic mentor persona
│   │   ├── 05_few_shot.py              # Campus ticket classifier
│   │   ├── 06_reasoning.py             # Step-by-step academic problem solver
│   │   ├── 07_pydantic_basics.py       # Pydantic schema validation
│   │   ├── 08_structured_output.py     # Schema-enforced course feedback analyzer
│   │   ├── 09_tool_calling.py          # Student records lookup tool loop
│   │   └── 10_fastapi_ai.py            # FastAPI LLM microservice endpoint
│   │
│   ├── exercises/                      # Student starter exercises with TODOs
│   │   ├── ex01_first_call.py
│   │   ├── ex02_token_budget.py
│   │   ├── ex03_temp_experiment.py
│   │   ├── ex04_system_persona.py
│   │   ├── ex05_few_shot_classifier.py
│   │   ├── ex06_step_by_step_reasoner.py
│   │   ├── ex07_pydantic_validator.py
│   │   ├── ex08_json_extractor.py
│   │   ├── ex09_custom_tool.py
│   │   └── ex10_fastapi_endpoint.py
│   │
│   ├── solutions/                      # Fully tested reference solutions
│   │   ├── sol01_first_call.py
│   │   ├── sol02_token_budget.py
│   │   ├── sol03_temp_experiment.py
│   │   ├── sol04_system_persona.py
│   │   ├── sol05_few_shot_classifier.py
│   │   ├── sol06_step_by_step_reasoner.py
│   │   ├── sol07_pydantic_validator.py
│   │   ├── sol08_json_extractor.py
│   │   ├── sol09_custom_tool.py
│   │   └── sol10_fastapi_endpoint.py
│   │
│   ├── assignments/                    # 3 Self-contained assignments with solutions & rubrics
│   │   ├── assignment1_prompt_engineering.md
│   │   ├── assignment2_pydantic_structured_output.md
│   │   └── assignment3_fastapi_ai_service.md
│   │
│   ├── interview/                      # Deep-dive viva and technical interview guides
│   │   ├── technical_qa.md
│   │   └── viva_master_guide.md
│   │
│   ├── tests/                          # Automated Pytest suite (28 tests)
│   │   ├── test_examples.py
│   │   ├── test_exercises.py
│   │   └── test_capstone.py
│   │
│   └── capstone/                       # Production-grade Student Advisory Microservice
│       ├── README.md
│       ├── requirements.txt
│       ├── .env.example
│       ├── app/
│       │   ├── __init__.py
│       │   ├── config.py               # Pydantic Settings & environment loader
│       │   ├── schemas.py              # Request/Response & internal data models
│       │   ├── tools.py                # Live tool definitions (student DB lookup)
│       │   ├── services.py             # LLM orchestration & tool execution engine
│       │   └── main.py                 # FastAPI application & REST endpoints
│       └── tests/
│           ├── __init__.py
│           └── test_api.py             # TestClient integration tests
│
└── resources/
    ├── glossary.md                     # Comprehensive terminology reference
    ├── cheatsheet.md                   # Quick reference for Python, SDKs & APIs
    └── further_learning.md             # Academic papers, books, and documentation links
```

---

## 6. How to Use This Repository for Self-Training

Follow this sequential 6-step self-learning method:

1. **Step 1: Read the Concept Note**: Open `week03-generative-ai/notes/0X_topic.md`. Read the concept explanation, syntax breakdown, and real-world analogy.
2. **Step 2: Run the Micro-Example**: Execute `python week03-generative-ai/examples/0X_topic.py` in your terminal. Observe the output.
3. **Step 3: Perform Self-Experiments**: Modify temperature, system instructions, input formats, or validation schemas as suggested.
4. **Step 4: Solve the Exercise**: Open `week03-generative-ai/exercises/ex0X_topic.py`. Fill in the missing `TODO` blocks.
5. **Step 5: Self-Evaluate with Solutions & Automated Tests**: Compare your work against `week03-generative-ai/solutions/sol0X_topic.py` and run `pytest`.
6. **Step 6: Review Interview & Viva Questions**: Test your conceptual retention using the interview and oral exam questions provided in each module.

---

## 7. Quickstart Setup (Under 5 Minutes)

### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd week3_agenticai
```

### Step 2: Create and Activate a Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure API Credentials
Create a `.env` file from the provided template:
```bash
cp .env.example .env
```
Open `.env` and set your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

> **Note**: If you do not have an active API key, all examples and tests feature graceful fallback / offline mock capabilities so you can still study, test, and understand the logic!

### Step 5: Run Your First Program
```bash
python week03-generative-ai/examples/01_hello_llm.py
```

### Step 6: Run the Test Suite
```bash
pytest
```

---

## 8. Responsible Use of API Keys & Security Protocol

> [!IMPORTANT]
> 1. **Never commit `.env` or credentials to version control.**
> 2. The `.gitignore` in this repository is pre-configured to block `.env`, `venv/`, and cache directories.
> 3. Always use `os.getenv("KEY_NAME")` or `pydantic-settings` to read credentials dynamically.
> 4. If an API key is accidentally committed or pushed, revoke and regenerate it immediately in [Google AI Studio](https://aistudio.google.com/).

---

## 9. Author & Guide

* **Prepared by**: **Dr. Rameshwer**
* **Role**: *Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*
* **Specialization**: Enterprise AI Solutions, LLM Microservices, Tool Calling & Agentic Control Loops
