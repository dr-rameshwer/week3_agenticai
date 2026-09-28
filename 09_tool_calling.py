"""
Step 9: Function / Tool Calling Lifecycle
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- The LLM does NOT guess database values; it requests tool execution
- Python functions with type hints & docstrings are converted to tools
- Automatic tool execution loop returns real-time grounded facts
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("Step 9: Function / Tool Calling")
print("Guide: Dr. Rameshwer")
print("=" * 50)

# Simulated Campus DB
STUDENT_DB = {
    "CS2026": {"name": "Alice Smith", "major": "Computer Science", "status": "Passed", "gpa": 3.9},
    "CS2027": {"name": "Bob Jones", "major": "Data Science", "status": "Academic Probation", "gpa": 2.4}
}

# 1. Define Tool function with docstring and type hints
def lookup_student_record(roll_no: str) -> dict:
    """Retrieves student academic standing and GPA by roll number.

    Args:
        roll_no: Student identification string (e.g. 'CS2026').
    """
    clean_roll = roll_no.strip().upper()
    print(f"  [Tool Call Executed]: Querying DB for {clean_roll}...")
    if clean_roll in STUDENT_DB:
        return {"found": True, "record": STUDENT_DB[clean_roll]}
    return {"found": False, "error": f"Student '{clean_roll}' not found."}

if not api_key:
    print("Simulated Output:")
    tool_res = lookup_student_record("CS2026")
    print(f"Student Alice Smith is in Good Standing with a GPA of 3.9.")
    exit(0)

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

# 2. Bind tool to generation config
config = types.GenerateContentConfig(
    tools=[lookup_student_record],
    temperature=0.0
)

query = "What is the academic standing and GPA of student CS2026?"
print(f"User Query: {query}\n")

# 3. Model automatically calls lookup_student_record and synthesizes answer
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=query,
    config=config
)

print("\n--- Grounded Answer from LLM ---")
print(response.text.strip())
print("=" * 50)
