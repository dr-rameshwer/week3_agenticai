"""
Step 4: System Instructions & Persona Steering
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- System Instructions: Set persistent rules, tone, and guardrails
- Forcing the model to stay concise and maintain role boundaries
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 4: System Instructions")
print("Guide: Dr. Rameshwer")
print("=" * 50)

def run_step():
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            system_prompt = "You are a friendly programming mentor. Explain in 2 sentences with an analogy. End with 1-line Python code."
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents="What is a Python dictionary?",
                config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=0.2)
            )
            print(response.text.strip())
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    print("Think of a Python dictionary like a real-world address book.")
    print("It pairs unique keys with values for fast lookups.")
    print("Syntax: student_grades = {'Alice': 95, 'Bob': 88}")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
