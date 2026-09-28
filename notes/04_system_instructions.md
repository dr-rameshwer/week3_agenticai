# Step 4: System Instructions & Persona Steering

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
- **System Instruction**: Tells the LLM *WHO* it is, *HOW* to respond, and what rules it *MUST* follow across the session.
- **User Prompt**: The immediate question or input payload.

## 2. Key Code
```python
system_instruction = """
You are a senior code reviewer.
Rules:
1. Identify potential bugs in 2 bullet points.
2. Suggest 1 optimization.
3. Keep response under 100 words.
"""

config = types.GenerateContentConfig(
    system_instruction=system_instruction,
    temperature=0.2
)
```

## 3. How to Run
```bash
python 04_system_instructions.py
```

## 4. Key Takeaways
- Use clear, numbered, unambiguous rules.
- System instructions help prevent prompt injection and keep model responses concise.

## 5. Self-Check & Interview Question
* **Q**: *Why pass system instructions in `GenerateContentConfig` instead of the user prompt?*  
* **Answer**: Dedicated system instructions receive architectural attention priority in modern models, ensuring guardrails remain intact across multi-turn interactions.
