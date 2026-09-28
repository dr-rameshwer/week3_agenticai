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

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 1: Hello LLM")
print("Guide: Dr. Rameshwer")
print("=" * 50)

def run_step():
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            prompt = "Explain Artificial Intelligence in one concise sentence."
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents=prompt
            )
            print("Response from Gemini:")
            print(response.text.strip())
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    print("Response from Gemini:")
    print("Artificial Intelligence is the simulation of human intelligence by computer systems.")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
