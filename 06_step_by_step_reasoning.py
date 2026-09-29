"""
Step 6: Step-by-Step Structured Reasoning
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- Why direct guessing causes math/logic errors in LLMs
- Prompting for explicit calculation steps + verification before final answer
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 6: Step-by-Step Reasoning")
print("Guide: Dr. Rameshwer")
print("=" * 50)

def run_step():
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            problem = "Courses: Data Structures: 4 credits (4.0), Database: 3 credits (3.0), Math: 3 credits (4.0), Writing: 2 credits (2.0)."
            prompt = f"Solve step by step:\n1. STEP-BY-STEP CALCULATION\n2. VERIFICATION\n3. FINAL ANSWER: GPA = X.XX\nProblem: {problem}"
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.0)
            )
            print(response.text.strip())
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    print("1. STEP-BY-STEP CALCULATION:")
    print("  * Total Quality Points = (4*4.0) + (3*3.0) + (3*4.0) + (2*2.0) = 41.0")
    print("  * Total Credits = 12")
    print("  * GPA = 41.0 / 12 = 3.4166...")
    print("2. FINAL ANSWER: GPA = 3.42")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
