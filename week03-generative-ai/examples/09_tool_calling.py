"""
Program: 09_tool_calling.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: Function / Tool Calling lifecycle, registering Python callables
         with docstrings, local execution loop, and grounded responses.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 09_tool_calling.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

# Simulated Campus Academic Database
CAMPUS_DB = {
    "CS2026": {"name": "Alice Smith", "major": "Computer Science", "status": "Passed", "gpa": 3.9},
    "CS2027": {"name": "Bob Jones", "major": "Data Science", "status": "Pending", "gpa": 3.2}
}

# Step 1: Define Tool Function with Type Annotations and Docstrings
def get_student_exam_status(roll_no: str) -> dict:
    """Retrieves academic record and exam standing for a student by roll number.

    Args:
        roll_no: Unique student identification string (e.g., 'CS2026').

    Returns:
        A dictionary containing student name, major, exam status, and GPA.
    """
    clean_roll = roll_no.strip().upper()
    print(f"  --> [TOOL EXECUTION]: Querying campus database for '{clean_roll}'...")
    if clean_roll in CAMPUS_DB:
        return {"found": True, "data": CAMPUS_DB[clean_roll]}
    return {"found": False, "error": f"Roll number '{clean_roll}' not found in registry."}

if not api_key:
    print("[NOTICE]: Running in educational simulation mode (No API Key).")
    print("User Query: What is the exam standing of student CS2026?")
    tool_res = get_student_exam_status("CS2026")
    print(f"Tool Result: {tool_res}")
    print("\n--- Grounded LLM Response (Simulated) ---")
    print(f"Student {tool_res['data']['name']} ({tool_res['data']['major']}) has an exam status of '{tool_res['data']['status']}' with a GPA of {tool_res['data']['gpa']}.")
    print("=" * 50)
    sys.exit(0)

try:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    # Step 2: Register Tool in Generation Config
    config = types.GenerateContentConfig(
        tools=[get_student_exam_status],
        temperature=0.0
    )

    query = "What is the exam status and GPA for student CS2026?"
    print(f"User Query: {query}\n")

    # Step 3: Invoke model with automatic tool execution
    response = client.models.generate_content(
        model=model_name,
        contents=query,
        config=config
    )

    print("\n--- Grounded Model Response ---")
    print(response.text.strip())
    print("=" * 50)

except Exception as e:
    print(f"[ERROR]: Tool execution failed: {e}")
    sys.exit(1)
