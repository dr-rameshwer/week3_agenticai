"""
Program: 01_hello_llm.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: First programmatic LLM call, API client initialization,
         environment variables, and error handling.
"""

import os
import sys
from dotenv import load_dotenv

# Step 1: Load environment variables from .env file
load_dotenv()

# Step 2: Retrieve API Key
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 01_hello_llm.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

# Step 3: Handle execution mode (Live API vs Simulated Fallback)
if not api_key:
    print("[NOTICE]: GEMINI_API_KEY not found in environment or .env file.")
    print("[SIMULATED RESPONSE]:")
    print("Artificial Intelligence is the simulation of human intelligence processes")
    print("by computer systems to perform reasoning, learning, and problem-solving.")
    print("=" * 50)
    print("To run with live API, add GEMINI_API_KEY to your .env file.")
    sys.exit(0)

try:
    from google import genai

    # Step 4: Initialize client
    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    prompt = "Explain Artificial Intelligence in one concise sentence."
    print(f"Sending prompt to Gemini model ({model_name})...")
    print(f"Prompt: {prompt}\n")

    # Step 5: Send prompt to LLM
    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    # Step 6: Display response
    print("Response from LLM:")
    print(response.text.strip())
    print("=" * 50)
    print("Execution completed successfully.")

except Exception as e:
    print(f"[ERROR]: LLM API invocation failed: {e}")
    sys.exit(1)
