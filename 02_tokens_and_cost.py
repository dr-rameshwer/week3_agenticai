"""
Step 2: Token Economics & Cost Calculation
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- How LLMs read text in tokens (~4 chars = 1 token)
- Reading prompt tokens, output tokens, and total tokens
- Calculating estimated API cost in USD
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 2: Tokens and Cost Tracking")
print("Guide: Dr. Rameshwer")
print("=" * 50)

def run_step():
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            prompt = "List the three laws of robotics in 3 short bullet points."
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
                contents=prompt
            )
            print(response.text.strip())
            usage = response.usage_metadata
            p_tokens = usage.prompt_token_count if usage else 16
            o_tokens = usage.candidates_token_count if usage else 74
            t_tokens = usage.total_token_count if usage else 90
            cost = (p_tokens / 1_000_000 * 0.075) + (o_tokens / 1_000_000 * 0.30)
            print("\n--- Token Telemetry ---")
            print(f"Input Tokens:  {p_tokens}")
            print(f"Output Tokens: {o_tokens}")
            print(f"Total Tokens:  {t_tokens}")
            print(f"Total Cost:    ${cost:.8f} USD")
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    print("1. A robot may not injure a human being.")
    print("2. A robot must obey orders given by humans.")
    print("3. A robot must protect its own existence.")
    print("\n--- Token Telemetry ---")
    print("Input Tokens:  16")
    print("Output Tokens: 74")
    print("Total Tokens:  90")
    print("Total Cost:    $0.00002340 USD")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
