"""
Step 3: Temperature & Generation Settings
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- Low Temperature (T=0.0): Strict, deterministic (best for code, math, classification)
- High Temperature (T=1.0): Creative, exploratory (best for brainstorming, stories)
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 3: Temperature Comparison")
print("Guide: Dr. Rameshwer")
print("=" * 50)

def run_step():
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            prompt = "Suggest 2 names for a student AI robotics club."
            res_low = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.0, max_output_tokens=60)
            )
            res_high = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
                contents=prompt,
                config=types.GenerateContentConfig(temperature=1.0, max_output_tokens=60)
            )
            print("--- Low Temp (T = 0.0 — Focused) ---")
            print(res_low.text.strip())
            print("\n--- High Temp (T = 1.0 — Creative) ---")
            print(res_high.text.strip())
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    print("--- Low Temp (T = 0.0 — Focused) ---")
    print("1. AI Robotics Club\n2. Autonomous Systems Society")
    print("\n--- High Temp (T = 1.0 — Creative) ---")
    print("1. CyberForge Nexus\n2. Synaptic Automata Guild")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
