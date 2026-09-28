# Topic 06: Structured Reasoning & Problem Decomposition

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 06*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Explain why direct answer generation fails on multi-step computational problems.
2. Structure prompts that elicit observable step-by-step reasoning.
3. Separate intermediate calculation steps from the final answer.
4. Apply structured problem decomposition to academic scheduling, mathematics, and logic puzzles.

---

## 2. Why Are We Learning This?
LLMs do not have internal scratchpads during a single token generation step. If you ask an LLM for the direct answer to a complex 5-step problem, it tries to guess the answer in one forward pass and frequently hallucinates. Forcing the model to output intermediate steps creates working memory, dramatically improving accuracy.

---

## 3. Concept in Simple Words
Don't rush the model! Instruct it to:
1. **Analyze the inputs**.
2. **Break down the problem step by step**.
3. **Show all intermediate arithmetic / logic**.
4. **State the final answer clearly**.

---

## 4. Real-World Analogy
When a math professor grades an exam, a student who writes only the final number gets 0 marks if it's wrong. A student who writes each step of the calculation can verify their work line-by-line and arrives at the correct result.

---

## 5. Technical Explanation
In autoregressive Transformers, each newly generated token is appended to the context sequence. When the model generates intermediate tokens explaining step 1 and step 2, those tokens are attended to by self-attention heads when calculating step 3. The context window effectively acts as an **external working memory register**.

---

## 6. Important Terminology
* **Chain-of-Thought (CoT)**: Generating intermediate natural language reasoning steps before outputting the final solution.
* **Observable Reasoning**: Intermediate calculations explicitly written to the output text rather than hidden internal states.
* **Decomposition**: Splitting a compound problem into modular sub-tasks.

---

## 7. Python Syntax & Concepts Encountered
* Explicit formatting directives in prompt strings.
* Section parsing using string splitting methods (`response.text.split("FINAL ANSWER:")`).

---

## 8. Smallest Working Example (`06_reasoning.py`)

```python
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

problem = """
A student is taking 4 courses:
- Data Structures: 4 credits, Grade A (4.0 points)
- Database Systems: 3 credits, Grade B (3.0 points)
- Discrete Mathematics: 3 credits, Grade A (4.0 points)
- Technical Writing: 2 credits, Grade C (2.0 points)

Calculate the student's Grade Point Average (GPA).
"""

reasoning_prompt = f"""
Solve the following academic problem carefully.
Follow this exact structure:
1. STEP-BY-STEP CALCULATION: Show all credit-point products and sums.
2. VERIFICATION: Briefly check the arithmetic.
3. FINAL ANSWER: State the numerical GPA rounded to 2 decimal places.

Problem:
{problem}
"""

config = types.GenerateContentConfig(temperature=0.0)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=reasoning_prompt,
    config=config
)

print(response.text)
```

---

## 9. Code Explanation — Line by Line
* **Lines 10-17**: Defines the multi-step student GPA calculation problem.
* **Lines 19-27**: Constructs `reasoning_prompt` enforcing a 3-part structured breakdown: calculation, verification, and final answer.
* **Line 29**: Sets `temperature=0.0` for precision arithmetic.
* **Lines 31-35**: Dispatches the generation request.
* **Line 37**: Prints the full step-by-step reasoning trace and final answer.

---

## 10. Expected Output
```text
1. STEP-BY-STEP CALCULATION:
- Total Credits: 4 + 3 + 3 + 2 = 12 credits.
- Quality Points per course:
  * Data Structures: 4 credits * 4.0 points = 16.0
  * Database Systems: 3 credits * 3.0 points = 9.0
  * Discrete Mathematics: 3 credits * 4.0 points = 12.0
  * Technical Writing: 2 credits * 2.0 points = 4.0
- Total Quality Points: 16.0 + 9.0 + 12.0 + 4.0 = 41.0
- GPA = Total Quality Points / Total Credits = 41.0 / 12 = 3.4166...

2. VERIFICATION:
- Re-checking sum: 16 + 9 = 25; 25 + 12 = 37; 37 + 4 = 41.
- Division: 41 / 12 = 3.4166... Arithmetic confirmed.

3. FINAL ANSWER:
GPA = 3.42
```

---

## 11. How to Run
```bash
python week03-generative-ai/examples/06_reasoning.py
```

---

## 12. Experiment Yourself
Change the problem to a library fine calculation or an exam schedule conflict problem:
* *"Student has 3 books overdue by 4, 7, and 12 days. The fine is $0.50/day for the first 5 days and $1.00/day thereafter. What is the total fine?"*
Observe how the model decomposes the piecewise calculation.

---

## 13. Common Mistakes
* Requesting direct output (`"Only output the number"`) on complex math problems, which leads to arithmetic errors.
* Failing to provide a clear delimiter (like `FINAL ANSWER:`) making programmatic extraction difficult.

---

## 14. Debugging Exercise
**Buggy Code**:
```python
# Student asks for instant answer on complex word problem:
prompt = "A factory makes 432 widgets/hr with 3 machines in 2 shifts... Output only the final integer."
```
**Fix**: Ask the model to output calculation steps first, followed by the final integer.

---

## 15. Student Practice Task
Write a script `ex06_step_by_step_reasoner.py` that parses a semester timetable and identifies scheduling conflicts between overlapping course lecture hours.

---

## 16. Mini Challenge
Write a Python parser that takes the response text from `06_reasoning.py` and programmatically extracts only the float value after `"FINAL ANSWER: GPA = "`.

---

## 17. Real-World Industry Use
Medical diagnosis pipelines, automated legal contract auditing, and algorithmic trading reasoning agents require verifiable step-by-step logic trails before taking high-stakes actions.

---

## 18. Viva Questions
1. *Why does generating intermediate reasoning steps reduce hallucination in arithmetic?*  
   **Answer**: It allows the model to attend to its own previously calculated intermediate tokens in subsequent attention layers, utilizing the context window as working memory.
2. *What is the purpose of the VERIFICATION step in reasoning prompts?*  
   **Answer**: It instructs the model to review and sanity-check its own arithmetic before emitting the final answer.

---

## 19. Interview Questions
1. *What is the difference between reasoning elicitation via prompting (CoT) and models natively trained with RL reasoning (like o1 / reasoning models)?*  
   **Answer**: Prompt-based CoT instructs standard models to output natural language thoughts into the standard completion stream. Natively trained reasoning models have internal reinforcement-learned reasoning paths and dynamically allocate thinking tokens before outputting user-facing responses.

---

## 20. Quick Revision
* Complex tasks require decomposition: **Calculation $\to$ Verification $\to$ Final Answer**.
* Use explicit structural headers.
* Set $T=0.0$.

---

## 21. Checklist
- [ ] Understand working memory mechanics in transformers
- [ ] Executed `06_reasoning.py`
- [ ] Tested piecewise calculation problem
- [ ] Built programmatic final-answer extractor
