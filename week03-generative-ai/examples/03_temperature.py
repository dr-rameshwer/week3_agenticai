"""
Program: 03_temperature.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: Temperature, sampling randomness, determinism (T=0.0)
         vs creative exploration (T=1.0) using GenerateContentConfig.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 03_temperature.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

if not api_key:
    print("[NOTICE]: Running in educational simulation mode (No API Key).")
    print("=== LOW TEMPERATURE (T = 0.0) ===")
    print("1. AI Robotics Club\n2. Autonomous Systems Society\n3. Robotics Engineering Guild")
    print("\n=== HIGH TEMPERATURE (T = 1.0) ===")
    print("1. Synapse Forge Automata\n2. Kinetic Nexus Club\n3. CyberPulse Robotics")
    print("=" * 50)
    sys.exit(0)

try:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    prompt = "Suggest three creative names for a student AI robotics club."

    # 1. Deterministic Sampling (T = 0.0)
    config_low = types.GenerateContentConfig(temperature=0.0, max_output_tokens=150)
    res_low = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=config_low
    )

    # 2. Creative Sampling (T = 1.0)
    config_high = types.GenerateContentConfig(temperature=1.0, max_output_tokens=150)
    res_high = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=config_high
    )

    print(f"Prompt: '{prompt}'\n")
    print("=== LOW TEMPERATURE (T = 0.0 — Deterministic) ===")
    print(res_low.text.strip())

    print("\n=== HIGH TEMPERATURE (T = 1.0 — Creative) ===")
    print(res_high.text.strip())
    print("=" * 50)

except Exception as e:
    print(f"[ERROR]: Execution failed: {e}")
    sys.exit(1)
