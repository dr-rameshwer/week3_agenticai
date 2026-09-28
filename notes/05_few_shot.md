# Step 5: Few-Shot Prompt Engineering

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
- **Zero-Shot**: Giving instructions without any examples.
- **Few-Shot**: Giving 2 to 4 solved input $\to$ output examples before asking the target question.
- **Why it works**: LLMs excel at recognizing and continuing repeating patterns in-context.

## 2. Key Code
```python
prompt = """
Classify tickets:
### Example 1
Ticket: Wi-Fi disconnected in Lab 2.
CATEGORY: Infrastructure

### Example 2
Ticket: Tuition invoice error.
CATEGORY: Financial

### Target Ticket
Ticket: Server room power outage.
CATEGORY:"""
```

## 3. How to Run
```bash
python 05_few_shot_prompting.py
```

## 4. Key Takeaways
- Use consistent formatting, delimiters, and balanced category examples.
- Combine Few-Shot with $T=0.0$ for rock-solid classification.

## 5. Self-Check & Interview Question
* **Q**: *When is Few-Shot prompting preferred over fine-tuning a model?*  
* **Answer**: When you have small datasets (5-20 examples), need rapid iteration, and want to avoid the infrastructure and training cost of fine-tuning.
