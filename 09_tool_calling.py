"""
Step 9: Function / Tool Calling Lifecycle
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- The LLM does NOT guess private database values; it requests tool execution
- Python functions with type hints & docstrings are converted into tools
- Automatic tool execution loop returns real-time grounded facts
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 9: Function / Tool Calling")
print("Guide: Dr. Rameshwer")
print("=" * 50)

# Simulated Private Campus Database
STUDENTS_DB = {
    "AI-2026-001": {"name": "Aarav Sharma", "attendance": 88.5, "eligible": True},
    "AI-2026-002": {"name": "Priya Patel", "attendance": 64.0, "eligible": False}
}

def get_student_record(roll_no: str) -> dict:
    """Look up a student's official attendance percentage and exam eligibility.

    Args:
        roll_no: The student roll number, e.g. 'AI-2026-001' or 'AI-2026-002'.
    """
    clean_roll = roll_no.strip().upper()
    print(f"  [Tool Call Executed]: Querying database for {clean_roll}...")
    if clean_roll in STUDENTS_DB:
        return {"status": "SUCCESS", "record": STUDENTS_DB[clean_roll]}
    return {"status": "NOT_FOUND", "error": f"Student {clean_roll} was not found."}

query = "Can you check the attendance and exam eligibility for student AI-2026-001?"

def run_step():
    print(f"User Query: {query}\n")
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            config = types.GenerateContentConfig(
                system_instruction="You are the Campus AI Academic Advisor. Always call get_student_record when asked about student status.",
                tools=[get_student_record],
                temperature=0.0
            )
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents=query,
                config=config
            )
            print("--- Grounded Answer from LLM ---")
            print(response.text.strip())
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    tool_res = get_student_record("AI-2026-001")
    print("--- Grounded Answer from LLM (Simulated) ---")
    print("Student Aarav Sharma (AI-2026-001) has an attendance of 88.5% and is ELIGIBLE for exams.")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
