"""
Solution 01: Your First LLM API Call
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 01.
"""

import os
from dotenv import load_dotenv

def run_solution() -> str:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "1. Data Scientist\n2. Machine Learning Engineer\n3. AI Solutions Architect"

    from google import genai

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="List 3 exciting career paths in Data Science with a 1-sentence description each."
    )
    return response.text.strip()

if __name__ == "__main__":
    print("--- Solution 01 Output ---")
    print(run_solution())
