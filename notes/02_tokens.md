# Step 2: Tokens, Context Windows & Cost Tracking

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
LLMs do not process raw words or characters directly; they process **Tokens** (~4 characters or 0.75 words).
- **Prompt Tokens**: Words you send (Input).
- **Candidate Tokens**: Words the model generates (Output).
- **Cost**: You are billed per 1 million tokens.

## 2. Key Code
```python
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="List 3 laws of robotics."
)

usage = response.usage_metadata
print(f"Input Tokens:  {usage.prompt_token_count}")
print(f"Output Tokens: {usage.candidates_token_count}")
print(f"Total Tokens:  {usage.total_token_count}")
```

## 3. How to Run
```bash
python 02_tokens_and_cost.py
```

## 4. Key Takeaways
- Output tokens are more expensive than input tokens because they are generated sequentially (one by one).
- Monitoring tokens is essential for keeping production API costs within budget.

## 5. Self-Check & Interview Question
* **Q**: *What is a Context Window?*  
* **Answer**: The maximum number of tokens (input prompt + generated output) an LLM can hold in active memory during a single request.
