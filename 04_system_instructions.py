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
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("Step 4: System Instructions")
print("Guide: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("Simulated Output:")
    print("Think of a Python dictionary like a real-world address book.")
    print("Syntax: student_grades = {'Alice': 95, 'Bob': 88}")
    exit(0)

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

# Define system rules
system_prompt = """
You are a friendly programming mentor.
Rules:
1. Explain technical concepts in 2 simple sentences using an everyday analogy.
2. End with a 1-line Python code example.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is a Python dictionary?",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0.2
    )
)

print(response.text.strip())
print("=" * 50)
