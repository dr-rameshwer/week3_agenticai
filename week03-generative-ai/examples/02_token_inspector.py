"""
Program: 02_token_inspector.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: Token metrics, usage metadata inspection (prompt tokens,
         candidates tokens, total tokens), and latency estimation.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 02_token_inspector.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("[NOTICE]: Running in educational fallback mode (No API Key).")
    print("Simulated Token Metrics:")
    print("  * Prompt Tokens (Input):     16")
    print("  * Candidates Tokens (Output): 74")
    print("  * Total Tokens:              90")
    print("  * Estimated Cost (USD):      $0.000023")
    print("=" * 50)
    sys.exit(0)

try:
    from google import genai

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    prompt = "List the three primary laws of robotics formulated by Isaac Asimov."
    print(f"Prompt: {prompt}\n")

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    print("--- Generated Response ---")
    print(response.text.strip())

    # Inspect usage metadata
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count if usage else 0
    candidate_tokens = usage.candidates_token_count if usage else 0
    total_tokens = usage.total_token_count if usage else 0

    print("\n--- Token Usage Telemetry ---")
    print(f"Prompt Tokens (Input):     {prompt_tokens}")
    print(f"Candidates Tokens (Output): {candidate_tokens}")
    print(f"Total Tokens:              {total_tokens}")

    # Cost calculation (Gemini 2.5 Flash pricing benchmark)
    cost_in = (prompt_tokens / 1_000_000) * 0.075
    cost_out = (candidate_tokens / 1_000_000) * 0.30
    total_cost = cost_in + cost_out

    print(f"Estimated Cost:            ${total_cost:.8f} USD")
    print("=" * 50)

except Exception as e:
    print(f"[ERROR]: Execution failed: {e}")
    sys.exit(1)
