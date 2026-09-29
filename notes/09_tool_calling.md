# Step 9: Function / Tool Calling Lifecycle

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
The LLM does **not** execute Python code or connect to your database directly.
Instead:
1. You register Python functions with docstrings & type hints.
2. The user asks a question requiring private campus data.
3. The LLM requests tool execution with structured arguments (`roll_no='AI-2026-001'`).
4. Your application runs the function against `STUDENTS_DB`.
5. You return the result to the LLM.
6. The LLM generates the final grounded answer.

## 2. Key Code
```python
# 1. Private Campus Database
STUDENTS_DB = {
    "AI-2026-001": {"name": "Aarav Sharma", "attendance": 88.5, "eligible": True},
    "AI-2026-002": {"name": "Priya Patel", "attendance": 64.0, "eligible": False}
}

# 2. Define function with docstring (Gemini reads this!)
def get_student_record(roll_no: str) -> dict:
    """Look up a student's official attendance percentage and exam eligibility."""
    clean_roll = roll_no.strip().upper()
    if clean_roll in STUDENTS_DB:
        return {"status": "SUCCESS", "record": STUDENTS_DB[clean_roll]}
    return {"status": "NOT_FOUND", "error": f"Student {clean_roll} was not found."}

# 3. Register tool in config
config = types.GenerateContentConfig(
    tools=[get_student_record],
    temperature=0.0
)

# 4. Automatic tool execution loop
res = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Is student AI-2026-001 eligible for exams?",
    config=config
)
```

## 3. How to Run
```bash
python 09_tool_calling.py
```

## 4. Key Takeaways
- Function docstrings and type hints are mandatory because the SDK converts them into OpenAPI JSON Schema for the LLM.
- Tool calling eliminates hallucinations on private or real-time data.

## 5. Self-Check & Interview Question
* **Q**: *Does the LLM execute Python functions directly on the server?*  
* **Answer**: No. The LLM outputs the tool name and JSON arguments; the local application intercepts, executes the function, and returns the result back to the model.
