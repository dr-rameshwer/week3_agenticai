# Step 3: Temperature & Generation Settings

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
**Temperature ($0.0 \to 1.0+$)** controls how random or creative the model's next-token selection is:
- **Low Temperature ($T = 0.0$)**: Greedy sampling. Always picks the most probable token. Use for code generation, math, and classification.
- **High Temperature ($T = 0.8\text{--}1.0$)**: Creative sampling. Flattens probabilities for variety. Use for brainstorming, marketing copy, and storytelling.

## 2. Key Code
```python
from google.genai import types

# Deterministic
config_low = types.GenerateContentConfig(temperature=0.0)

# Creative
config_high = types.GenerateContentConfig(temperature=1.0)
```

## 3. How to Run
```bash
python 03_temperature.py
```

## 4. Key Takeaways
- Setting $T = 0.0$ does NOT fix model training errors, but it maximizes reproducibility.
- Never use $T = 1.0$ for JSON schema extraction or arithmetic.

## 5. Self-Check & Interview Question
* **Q**: *What happens mathematically when temperature is set to 0.0?*  
* **Answer**: The Softmax function converges to an argmax function, assigning probability 1.0 to the highest-scoring logit.
