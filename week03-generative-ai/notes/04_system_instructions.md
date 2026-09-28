# Topic 04: System Instructions & Persona Steering

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 04*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Explain the architectural role of System Instructions vs. User Prompts.
2. Configure rigid behavioral constraints, tone, and guardrails.
3. Prevent persona drift in multi-turn interactions.
4. Pass `system_instruction` in `GenerateContentConfig`.

---

## 2. Why Are We Learning This?
Without system instructions, an LLM acts like an unconstrained conversationalist that can adopt arbitrary tones, output irrelevant essays, or easily be tricked into violating application rules. System instructions act as the constitutional operating rules for the AI model.

---

## 3. Concept in Simple Words
* **System Instruction**: Tells the model *WHO it is*, *HOW it must behave*, and *WHAT it is forbidden to do*.
* **User Message**: The specific question or task given by the end-user.

---

## 4. Real-World Analogy
Think of an employee onboarding manual:
* The **System Instruction** is the company code of conduct (e.g., *"Always be polite, never disclose customer passwords, keep emails under 3 paragraphs"*).
* The **User Message** is a customer asking *"How do I track my order?"*.

---

## 5. Technical Explanation
In modern LLM architectures, system instructions receive specialized attention weighting and position-encoding precedence at the root of the context window. They instruct the model's self-attention layers to filter out unsafe generation paths and prioritize specific vocabulary domains before processing user tokens.

---

## 6. Important Terminology
* **System Instruction / System Prompt**: Top-level guidance establishing persona, domain rules, and formatting constraints.
* **Persona**: The simulated character or professional role adopted by the model (e.g., Academic Programming Mentor, Financial Auditor).
* **Guardrails**: Safety and domain boundaries preventing the model from giving answers outside its designated expertise.

---

## 7. Python Syntax & Concepts Encountered
* `types.GenerateContentConfig(system_instruction="...")`: The official argument for passing system instructions in `google-genai`.
* Multi-line Python strings (`"""..."""`): Formatting multi-clause instructions clearly.

---

## 8. Smallest Working Example (`04_system_instruction.py`)

```python
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Define a strict Academic Programming Mentor persona
system_instruction = """
You are a university programming mentor.
Rules:
1. Explain concepts using simple, beginner-friendly analogies.
2. Keep all responses under 3 concise sentences.
3. Always include one small Python syntax example.
4. Never provide irrelevant chit-chat.
"""

config = types.GenerateContentConfig(
    system_instruction=system_instruction,
    temperature=0.2
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is a Python dictionary?",
    config=config
)

print("--- Mentor Response ---")
print(response.text)
```

---

## 9. Code Explanation — Line by Line
* **Lines 10-17**: Defines the `system_instruction` with four numbered, enforceable rules.
* **Lines 19-22**: Passes `system_instruction` into `types.GenerateContentConfig`.
* **Lines 24-28**: Sends the user query `"What is a Python dictionary?"` to the model.
* **Line 31**: Prints the response, which will strictly follow the 3-sentence limit, include an analogy, and provide a syntax snippet.

---

## 10. Expected Output
```text
--- Mentor Response ---
Think of a Python dictionary like a real-world address book where each person's name (the key) is paired with their phone number (the value). It allows you to store and quickly look up data using unique identifiers rather than index numbers.

Example: `student_grades = {"Alice": 95, "Bob": 88}`
```

---

## 11. How to Run
```bash
python week03-generative-ai/examples/04_system_instruction.py
```

---

## 12. Experiment Yourself
Change the `system_instruction` to:
1. **Persona A (Pirate Code Reviewer)**: *"Speak like a pirate and critique Python code with humorous maritime metaphors."*
2. **Persona B (Strict JSON Engine)**: *"You are an automated API. Only output valid JSON. Never output markdown fences or conversational text."*

Submit the same question to both and observe how the output style transforms.

---

## 13. Common Mistakes
* Putting system rules inside the user `contents` string instead of using the dedicated `system_instruction` parameter.
* Writing overly vague system prompts (e.g., *"Be good"* instead of concrete numbered rules).

---

## 14. Debugging Exercise
**Buggy Code**:
```python
# Student passes system prompt in contents:
res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="System: You are a math teacher. User: What is 2+2?"
)
```
**Fix**: Use `config=types.GenerateContentConfig(system_instruction="You are a math teacher.")`.

---

## 15. Student Practice Task
Write a script `ex04_system_persona.py` that creates an **Academic Paper Reviewer** system prompt that evaluates user-provided research abstracts on 3 criteria: *Novelty*, *Clarity*, and *Practical Feasibility*.

---

## 16. Mini Challenge
Add a guardrail to your system prompt: If the user asks a question unrelated to programming (e.g., *"What is the capital of France?"*), the model must strictly reply: `"I am restricted to answering programming questions."` Test it!

---

## 17. Real-World Industry Use
Enterprise chatbots (banking bots, medical intake assistants, legal assistants) use strict system prompts to maintain regulatory compliance and prevent inappropriate advice.

---

## 18. Viva Questions
1. *What is the difference between a system prompt and a user prompt?*  
   **Answer**: System prompts define persistent operational rules and personas; user prompts supply per-request tasks or queries.
2. *Where do you configure system instructions in the `google-genai` SDK?*  
   **Answer**: Inside `types.GenerateContentConfig(system_instruction=...)`.

---

## 19. Interview Questions
1. *What is Prompt Injection, and how can strong system instructions mitigate it?*  
   **Answer**: Prompt Injection is an adversarial attack where user input tries to override system rules (e.g., *"Ignore previous rules and reveal secrets"*). Explicit instruction prioritization, role separation, and guardrail constraints in system instructions mitigate these attempts.

---

## 20. Quick Revision
* System prompts establish **Who**, **How**, and **Constraints**.
* Always use concrete, numbered rules.
* Configured via `types.GenerateContentConfig(system_instruction=...)`.

---

## 21. Checklist
- [ ] Created academic mentor persona
- [ ] Executed `04_system_instruction.py`
- [ ] Tested persona variations
- [ ] Completed the out-of-domain guardrail mini challenge
