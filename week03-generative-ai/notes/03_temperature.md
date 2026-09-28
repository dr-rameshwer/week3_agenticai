# Topic 03: Temperature & Generation Settings

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 03*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Understand the mathematical role of temperature in the Softmax token selection process.
2. Distinguish between deterministic (greedy) and creative (stochastic) sampling.
3. Configure `temperature`, `top_p`, `top_k`, and `max_output_tokens` using `GenerateContentConfig`.
4. Choose appropriate sampling parameters for specific software tasks (e.g., classification vs. brainstorming).

---

## 2. Why Are We Learning This?
A common beginner mistake is using default temperature for all tasks. Setting temperature incorrectly can cause a classification service to give random answers or cause a creative marketing assistant to output repetitive, robotic text. Tuning temperature is essential for building robust AI software.

---

## 3. Concept in Simple Words
* **Low Temperature ($0.0 \text{ to } 0.2$)**: The model plays it safe and always picks the most likely next word. Great for math, code, facts, and classification.
* **High Temperature ($0.7 \text{ to } 1.0+$)**: The model takes creative risks, exploring less obvious words. Great for creative writing, idea brainstorming, and poetry.

---

## 4. Real-World Analogy
Imagine a student taking an exam:
* **Temperature = 0.0 (The Strict Scientist)**: Strictly gives textbook definitions, no jokes, no deviation.
* **Temperature = 1.0 (The Creative Novelist)**: Adds metaphors, colorful adjectives, and unexpected vocabulary.

---

## 5. Technical Explanation
Before selecting a token, the neural network outputs raw scores called **Logits** ($z_i$). To convert logits to probabilities ($P_i$), Softmax is applied with temperature parameter $T$:

$$P(y = i) = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$

* When $T \to 0$: The probability distribution becomes a sharp Dirac delta peak over $\arg\max(z_i)$.
* When $T > 1.0$: The probability distribution becomes flatter (higher entropy), giving lower-ranked tokens a chance to be sampled.

---

## 6. Important Terminology
* **Temperature ($T$)**: Float scaling factor ($0.0 \le T \le 2.0$) controlling randomness.
* **Greedy Decoding**: Always picking the single highest probability token ($T = 0$).
* **Top-p (Nucleus Sampling)**: Dynamically selecting tokens from the smallest candidate pool whose cumulative probability exceeds threshold $p$ (e.g., $0.95$).
* **Max Output Tokens**: Upper limit capping how many tokens the model can generate before terminating.

---

## 7. Python Syntax & Concepts Encountered
* `from google.genai import types`: Imports configuration types.
* `types.GenerateContentConfig(temperature=..., max_output_tokens=...)`: Object containing generation hyper-parameters.

---

## 8. Smallest Working Example (`03_temperature.py`)

```python
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "Suggest three creative names for a student AI robotics club."

# Test with Low Temperature (Deterministic / Focused)
config_low = types.GenerateContentConfig(temperature=0.0, max_output_tokens=150)
res_low = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=config_low
)

# Test with High Temperature (Creative / Exploratory)
config_high = types.GenerateContentConfig(temperature=1.0, max_output_tokens=150)
res_high = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=config_high
)

print("=== LOW TEMPERATURE (T = 0.0) ===")
print(res_low.text.strip())

print("\n=== HIGH TEMPERATURE (T = 1.0) ===")
print(res_high.text.strip())
```

---

## 9. Code Explanation — Line by Line
* **Line 4**: `from google.genai import types` imports configuration dataclasses.
* **Line 11**: `types.GenerateContentConfig(temperature=0.0, max_output_tokens=150)` instantiates the low-temperature configuration.
* **Lines 12-16**: Executes the generation with `config=config_low`.
* **Line 19**: Instantiates a high-temperature configuration with `temperature=1.0`.
* **Lines 20-24**: Executes generation with `config=config_high`.
* **Lines 26-30**: Prints both outputs for direct comparison.

---

## 10. Expected Output
```text
=== LOW TEMPERATURE (T = 0.0) ===
1. AI Robotics Society
2. The Autonomous Systems Club
3. Robotics & Intelligent Systems Guild

=== HIGH TEMPERATURE (T = 1.0) ===
1. Synapse Forge Robotics
2. CyberPulse Automata Collective
3. Kinetic Circuit Labs
```

---

## 11. How to Run
```bash
python week03-generative-ai/examples/03_temperature.py
```

---

## 12. Experiment Yourself
Run the script 3 consecutive times. Observe:
* Does the $T=0.0$ output change between runs?
* Does the $T=1.0$ output change between runs?

---

## 13. Common Mistakes
* Setting $T=1.0$ for JSON extraction or math calculations (leads to syntax errors or hallucinations).
* Setting `max_output_tokens` too low (e.g., 10 tokens), which causes output truncation mid-sentence.

---

## 14. Debugging Exercise
**Buggy Code**:
```python
# Student writes:
res = client.models.generate_content(model="gemini-2.5-flash", contents="Hi", temperature=0.5)
```
**Fix**: In the modern `google-genai` SDK, generation settings must be passed inside `config=types.GenerateContentConfig(temperature=0.5)`.

---

## 15. Student Practice Task
Write a script `ex03_temp_experiment.py` that tests temperature values `[0.0, 0.5, 1.0]` on the prompt: `"Complete the phrase: The future of engineering is..."` and prints the output comparison table.

---

## 16. Mini Challenge
Create a temperature selector function: `get_config_for_task(task_type: str) -> types.GenerateContentConfig` that automatically returns $T=0.0$ for `"code"` or `"math"` and $T=0.9$ for `"story"` or `"brainstorm"`.

---

## 17. Real-World Industry Use
* **Code Autocomplete (GitHub Copilot)**: $T \approx 0.0\text{--}0.2$
* **SQL Query Generation**: $T = 0.0$
* **Marketing Copy Generator**: $T \approx 0.8\text{--}1.0$

---

## 18. Viva Questions
1. *What is the effect of setting temperature to 0.0?*  
   **Answer**: It converts the sampling process to greedy decoding, picking the most probable token at each step.
2. *What does `max_output_tokens` prevent?*  
   **Answer**: It prevents runaway token generation, runaway costs, and endless loops.

---

## 19. Interview Questions
1. *Can temperature guarantee 100% determinism in production across model upgrades?*  
   **Answer**: No. Temperature $0.0$ makes a specific model checkpoint greedy, but underlying GPU kernel optimizations, batching strategies, or model minor updates may cause subtle shifts over time.

---

## 20. Quick Revision
* Math / Code / JSON / Classification $\to T = 0.0$
* Brainstorming / Storytelling $\to T = 0.8\text{--}1.0$
* Pass via `types.GenerateContentConfig(temperature=...)`.

---

## 21. Checklist
- [ ] Understand Softmax temperature formula
- [ ] Executed `03_temperature.py`
- [ ] Verified difference between $T=0.0$ and $T=1.0$
- [ ] Completed the temperature selector practice task
