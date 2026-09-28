"""
Program: 05_few_shot.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: In-context learning, Few-Shot demonstrations, consistent
         format enforcement, and multi-class classification.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 05_few_shot.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("[NOTICE]: Running in educational simulation mode (No API Key).")
    print("Target Ticket: The server room cooling system failed.")
    print("CATEGORY: Infrastructure\nSEVERITY: High")
    print("=" * 50)
    sys.exit(0)

try:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    # Construct Few-Shot prompt with 3 balanced exemplars
    few_shot_prompt = """
You are an automated campus IT support ticket triage classifier.
Classify the given ticket into CATEGORY (Infrastructure, Academic, Finance) and SEVERITY (Low, Medium, High).

### Example 1
Ticket: The Wi-Fi in Computer Lab 2 disconnects every five minutes.
CATEGORY: Infrastructure
SEVERITY: Medium

### Example 2
Ticket: My scholarship tuition deduction is not reflected on the portal invoice.
CATEGORY: Finance
SEVERITY: High

### Example 3
Ticket: Can the instructor upload the slides for lecture 4?
CATEGORY: Academic
SEVERITY: Low

### Target Ticket
Ticket: The main power backup generator in the server room is smoking and temperatures are rising.
CATEGORY:"""

    config = types.GenerateContentConfig(
        temperature=0.0,
        max_output_tokens=50
    )

    response = client.models.generate_content(
        model=model_name,
        contents=few_shot_prompt,
        config=config
    )

    print("--- Classification Result ---")
    print("CATEGORY:" + response.text.strip())
    print("=" * 50)

except Exception as e:
    print(f"[ERROR]: Execution failed: {e}")
    sys.exit(1)
