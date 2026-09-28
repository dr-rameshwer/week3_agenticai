"""
Step 1: Your First LLM API Call
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- Loading API key from .env safely
- Connecting to Google Gemini with google-genai
- Sending a prompt and printing the response
"""

import os
from dotenv import load_dotenv

# 1. Load .env file
load_dotenv()

# 2. Get API key
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("Step 1: Hello LLM")
print("Guide: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("[NOTE]: GEMINI_API_KEY not found in .env.")
    print("Simulated Output:")
    print("Artificial Intelligence is the simulation of human intelligence by computers.")
    print("\nTo run with real API: copy .env.example to .env and add your key.")
    exit(0)

from google import genai

# 3. Create client
client = genai.Client(api_key=api_key)

# 4. Generate content
prompt = "Explain Artificial Intelligence in one concise sentence."
print(f"Prompt: {prompt}\n")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# 5. Print output
print("Response from Gemini:")
print(response.text.strip())
print("=" * 50)
