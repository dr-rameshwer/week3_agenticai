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
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("Step 3: Temperature Comparison")
print("Guide: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("Simulated Output:")
    print("Low Temp (0.0):  1. AI Robotics Club  2. Autonomous Systems Society")
    print("High Temp (1.0): 1. CyberForge Nexus   2. Synaptic Automata Guild")
    exit(0)

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)
prompt = "Suggest 2 names for a student AI robotics club."

# 1. Deterministic (T = 0.0)
res_low = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(temperature=0.0, max_output_tokens=60)
)

# 2. Creative (T = 1.0)
res_high = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(temperature=1.0, max_output_tokens=60)
)

print("--- Low Temp (T = 0.0 — Focused) ---")
print(res_low.text.strip())

print("\n--- High Temp (T = 1.0 — Creative) ---")
print(res_high.text.strip())
print("=" * 50)
