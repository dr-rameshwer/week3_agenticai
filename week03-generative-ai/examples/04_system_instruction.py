"""
Program: 04_system_instruction.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: System instructions, persona steering, role separation,
         and behavioral guardrails.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 04_system_instruction.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("[NOTICE]: Running in educational simulation mode (No API Key).")
    print("--- Academic Mentor Persona Response ---")
    print("Think of a Python dictionary like a real-world address book where a name (key)")
    print("is paired with a phone number (value). It enables instant data lookups.")
    print("\nSyntax Example:")
    print('student_records = {"Alice": 95, "Bob": 88}')
    print("=" * 50)
    sys.exit(0)

try:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    # Define strict behavioral guidelines for the Academic Mentor persona
    system_instruction = """
    You are a university computer science programming mentor.
    Rules:
    1. Explain technical concepts using simple, everyday analogies.
    2. Keep explanations under 3 sentences.
    3. Always conclude with a one-line Python code snippet.
    4. Maintain an encouraging and professional academic tone.
    """

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2,
        max_output_tokens=200
    )

    question = "What is a Python dictionary?"
    print(f"Student Inquiry: {question}\n")

    response = client.models.generate_content(
        model=model_name,
        contents=question,
        config=config
    )

    print("--- Academic Mentor Response ---")
    print(response.text.strip())
    print("=" * 50)

except Exception as e:
    print(f"[ERROR]: Execution failed: {e}")
    sys.exit(1)
