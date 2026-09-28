"""
Program: 06_reasoning.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: Structured problem-solving, observable step-by-step reasoning,
         intermediate calculations, and verification steps.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 06_reasoning.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("[NOTICE]: Running in educational simulation mode (No API Key).")
    print("1. STEP-BY-STEP CALCULATION:")
    print("  * Total Credits: 4 + 3 + 3 + 2 = 12 credits")
    print("  * Total Quality Points: (4*4.0) + (3*3.0) + (3*4.0) + (2*2.0) = 41.0")
    print("  * GPA: 41.0 / 12 = 3.4166...")
    print("2. VERIFICATION: Arithmetic checked and confirmed.")
    print("3. FINAL ANSWER: GPA = 3.42")
    print("=" * 50)
    sys.exit(0)

try:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    problem = """
A student is registered for 4 courses:
1. Data Structures: 4 credits, Grade A (4.0 points)
2. Database Systems: 3 credits, Grade B (3.0 points)
3. Discrete Mathematics: 3 credits, Grade A (4.0 points)
4. Technical Writing: 2 credits, Grade C (2.0 points)

Calculate the student's Grade Point Average (GPA).
"""

    prompt = f"""
Solve the following academic problem with precision.
You must follow this exact output structure:
1. STEP-BY-STEP CALCULATION: Show all credit-point products and sums.
2. VERIFICATION: Re-check the arithmetic.
3. FINAL ANSWER: State the numerical GPA rounded to 2 decimal places.

Problem:
{problem}
"""

    config = types.GenerateContentConfig(temperature=0.0)

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=config
    )

    print("--- Model Reasoning & Solution ---")
    print(response.text.strip())
    print("=" * 50)

except Exception as e:
    print(f"[ERROR]: Execution failed: {e}")
    sys.exit(1)
