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
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("Step 2: Tokens and Cost Tracking")
print("Guide: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("[NOTE]: Running in simulated mode.")
    print("Metrics Example:")
    print("  * Input Tokens:  16 ($0.075 / 1M)")
    print("  * Output Tokens: 74 ($0.30 / 1M)")
    print("  * Total Tokens:  90")
    print("  * Total Cost:    $0.00002340 USD")
    print("=" * 50)
    exit(0)

from google import genai

client = genai.Client(api_key=api_key)
prompt = "List the three laws of robotics in 3 short bullet points."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text.strip())

# Read token usage
usage = response.usage_metadata
prompt_tokens = usage.prompt_token_count if usage else 0
output_tokens = usage.candidates_token_count if usage else 0
total_tokens = usage.total_token_count if usage else 0

# Calculate price (Gemini 2.5 Flash pricing benchmark)
cost = (prompt_tokens / 1_000_000 * 0.075) + (output_tokens / 1_000_000 * 0.30)

print("\n--- Token Telemetry ---")
print(f"Input Tokens:  {prompt_tokens}")
print(f"Output Tokens: {output_tokens}")
print(f"Total Tokens:  {total_tokens}")
print(f"Total Cost:    ${cost:.8f} USD")
print("=" * 50)
