"""
Exercise 01: Your First LLM API Call
Course Instructor: Dr. Rameshwer

Task:
Complete the TODO blocks to load the API key from environment variables,
initialize the Gemini client, send a prompt asking for 3 career opportunities
in Data Science, and print the resulting text.
"""

import os
from dotenv import load_dotenv

def run_exercise():
    # TODO 1: Load environment variables using python-dotenv
    load_dotenv()

    # TODO 2: Retrieve GEMINI_API_KEY from environment
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("[NOTICE]: No API Key found. Returning simulated student response.")
        return "1. Data Scientist\n2. Machine Learning Engineer\n3. AI Solutions Architect"

    from google import genai

    # TODO 3: Initialize the genai.Client with the api_key
    client = genai.Client(api_key=api_key)

    prompt = "List 3 exciting career paths in Data Science with a 1-sentence description each."

    # TODO 4: Call client.models.generate_content with model="gemini-2.5-flash"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # TODO 5: Return or print the text response
    return response.text.strip()

if __name__ == "__main__":
    result = run_exercise()
    print("--- Exercise 01 Output ---")
    print(result)
