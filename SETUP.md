# Developer Setup & Environment Guide

**Prepared by Dr. Rameshwer**  
*Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*  
*Local Environment Configuration & Quickstart Guide*

---

## 1. Prerequisites Checklist

Before running the code examples and exercises, ensure your system has:
1. **Python 3.10, 3.11, or 3.12** installed (`python3 --version` or `python --version`).
2. **Git** installed for version control (`git --version`).
3. A code editor such as **Visual Studio Code**, **Cursor**, or **PyCharm**.
4. An internet connection to query frontier LLM endpoints.

---

## 2. Step-by-Step Environment Setup

### Step 2.1: Open Your Terminal / Command Prompt
Navigate to your workspace directory:
```bash
cd /path/to/week3_agenticai
```

### Step 2.2: Create an Isolated Python Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv

# Windows
python -m venv venv
```

### Step 2.3: Activate the Virtual Environment
```bash
# macOS / Linux (bash/zsh)
source venv/bin/activate

# Windows (Command Prompt)
venv\Scripts\activate.bat

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```
*Your terminal prompt should now display `(venv)`.*

### Step 2.4: Upgrade Package Manager and Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 3. Configuring API Credentials

This guide uses modern SDKs (`google-genai` and `openai`).

### Step 3.1: Obtain an API Key
1. Visit Google AI Studio: [https://aistudio.google.com/](https://aistudio.google.com/)
2. Sign in with your Google account.
3. Click **"Get API key"** and create a new key.
4. Copy the generated API key string.

### Step 3.2: Create Your Local `.env` File
Run the following command to copy the template:
```bash
cp .env.example .env
```
Open `.env` in your text editor and insert your key:
```env
GEMINI_API_KEY=AIzaSyD-YourActualKeyHere123456789
GEMINI_MODEL=gemini-3.6-flash
```

> [!CAUTION]
> **Security Rule**: Never share your API key, commit it to GitHub, or paste it in public chat groups. The `.gitignore` file will prevent git from committing `.env`.

---

## 4. Validating Your Installation

Run the first micro-program to verify that your Python environment, network connectivity, and API keys are functioning properly:

```bash
python week03-generative-ai/examples/01_hello_llm.py
```

---

## 5. Running the Automated Test Suite

To run all automated tests and verify module functionality:
```bash
pytest
```

---

## 6. Offline / Mock Mode for Self-Study

If you are working in an environment without an active API key:
* All example programs and test suites contain **fallback mock implementations**.
* If `GEMINI_API_KEY` is not detected in `.env`, the programs will output a clear notice and return simulated model responses so that you can continue studying the syntax, schema validation, and FastAPI microservice architecture without interruption.
