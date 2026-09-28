# Step 1: LLM Fundamentals & Your First API Call

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
In software engineering, you don't train huge models from scratch. You interact with them via APIs using a Python SDK (`google-genai`).

## 2. Key Code
```python
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Artificial Intelligence in one concise sentence."
)
print(response.text)
```

## 3. How to Run
```bash
python 01_hello_llm.py
```

## 4. Key Takeaways
- Always store your secret keys in `.env` and use `os.getenv()`.
- Never hardcode or commit keys to GitHub.
- `client.models.generate_content()` sends the prompt and returns a response object with `.text`.

## 5. Self-Check & Interview Question
* **Q**: *Why use `.env` instead of hardcoding API keys?*  
* **Answer**: Hardcoded keys get leaked into git history and compromised by automated bots. `.env` keeps secrets separated from source code.
