"""
Step 5: Few-Shot Prompt Engineering
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- Giving 2-3 solved examples (Few-Shot) to teach formatting and classification
- Achieving 100% reliable structure without fine-tuning
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 5: Few-Shot Classification")
print("Guide: Dr. Rameshwer")
print("=" * 50)

def run_step():
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            prompt = """
Classify campus IT support tickets into CATEGORY (Infrastructure/Academic/Finance) and SEVERITY (Low/Medium/High).

### Example 1
Ticket: The Wi-Fi in Lab 2 disconnects every five minutes.
CATEGORY: Infrastructure
SEVERITY: Medium

### Example 2
Ticket: My tuition scholarship deduction is missing from the portal.
CATEGORY: Finance
SEVERITY: High

### Target Ticket
Ticket: The server room power generator is overheating and alarms are sounding.
CATEGORY:"""
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.0, max_output_tokens=50)
            )
            print("CATEGORY:" + response.text.strip())
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    print("CATEGORY: Infrastructure\nSEVERITY: High")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
