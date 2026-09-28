# Step 9: Function / Tool Calling Lifecycle

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
The LLM does **not** execute Python code or connect to your database directly.
Instead:
1. You register Python functions with docstrings & type hints.
2. The user asks a question requiring live or private data.
3. The LLM requests tool execution with structured arguments.
4. Your application runs the function against your database.
5. You return the result to the LLM.
6. The LLM generates the final grounded answer.

## 2. Key Code
```python
# 1. Define function with docstring
def lookup_student_record(roll_no: str) -> dict:
    """Retrieves student GPA and academic standing by roll number."""
    return STUDENT_DB.get(roll_no.upper(), {"found": False})

# 2. Register tool
config = types.GenerateContentConfig(
    tools=[lookup_student_record],
    temperature=0.0
)

# 3. Automatic tool execution loop
res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the GPA of student CS2026?",
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
