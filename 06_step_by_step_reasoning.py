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
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("Step 6: Step-by-Step Reasoning")
print("Guide: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("Simulated Output:")
    print("1. CALCULATION: Total Points = (4*4.0) + (3*3.0) + (3*4.0) + (2*2.0) = 41.0 / 12 = 3.4166")
    print("2. FINAL ANSWER: GPA = 3.42")
    exit(0)

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

problem = """
Courses:
- Data Structures: 4 credits, Grade A (4.0)
- Database Systems: 3 credits, Grade B (3.0)
- Discrete Math: 3 credits, Grade A (4.0)
- Tech Writing: 2 credits, Grade C (2.0)
Calculate the final GPA.
"""

prompt = f"""
Solve this academic problem carefully:
1. STEP-BY-STEP CALCULATION: Show credit-point products and sums.
2. VERIFICATION: Briefly check the math.
3. FINAL ANSWER: State 'FINAL ANSWER: GPA = X.XX'.

Problem:
{problem}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(temperature=0.0)
)

print(response.text.strip())
print("=" * 50)
