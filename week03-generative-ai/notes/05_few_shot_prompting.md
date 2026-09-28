# Topic 05: Few-Shot Prompt Engineering

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 05*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Distinguish between Zero-Shot, One-Shot, and Few-Shot prompting paradigms.
2. Structure high-quality demonstration exemplars (Input $\to$ Output pairs).
3. Enforce consistent formatting, categorization, and domain vocabulary.
4. Build a reliable multi-class support ticket classifier without training weights.

---

## 2. Why Are We Learning This?
Explaining complex classification logic or exact text formats purely with natural language instructions is often ambiguous. Showing the model 2 to 4 concrete examples of expected inputs and outputs anchors the model's in-context attention, yielding vastly superior consistency.

---

## 3. Concept in Simple Words
* **Zero-Shot**: You give the instructions and immediately ask the question.
* **One-Shot**: You give instructions, show **1** solved example, then ask the question.
* **Few-Shot**: You give instructions, show **2 to 5** solved examples, then ask the question.

---

## 4. Real-World Analogy
When a professor hands out a laboratory assignment:
* Giving only the assignment title is **Zero-Shot**.
* Providing a sample lab report from last year showing the expected format is **Few-Shot**. Students follow the sample format much more accurately.

---

## 5. Technical Explanation
Large language models are pre-trained on next-token prediction over massive text corpora. When an input matches a repeating structural pattern:
$$\text{Input 1} \to \text{Output 1}, \quad \text{Input 2} \to \text{Output 2}, \quad \text{Input 3} \to \text{Output 3}, \quad \text{Target Input} \to \text{???}$$
The model's self-attention heads recognize the repetitive relational pattern and complete the final output token sequence with identical syntax, delimiters, and categorization vocabulary.

---

## 6. Important Terminology
* **Zero-Shot**: Direct execution without exemplars.
* **Few-Shot Learning**: In-context demonstration using $K$ examples ($K \in [2, 8]$).
* **Exemplar**: An individual solved demonstration pair consisting of input text and gold-standard output.
* **Delimiters**: Special characters (e.g., `---`, `###`, `Input:`) that clearly separate exemplars from the target query.

---

## 7. Python Syntax & Concepts Encountered
* Python f-strings for building dynamic prompt templates: `f"Input: {text}\nOutput: "`
* Multi-line strings with structured delimiters.

---

## 8. Smallest Working Example (`05_few_shot.py`)

```python
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Construct a Few-Shot classification prompt with 3 clear exemplars
few_shot_prompt = """
You are an automated campus IT support ticket classifier.
Classify the given ticket into CATEGORY (Infrastructure, Academic, Finance) and SEVERITY (Low, Medium, High).

### Example 1
Ticket: The Wi-Fi in Computer Lab 2 disconnects every five minutes.
CATEGORY: Infrastructure
SEVERITY: Medium

### Example 2
Ticket: My scholarship tuition deduction is not showing on the portal invoice.
CATEGORY: Finance
SEVERITY: High

### Example 3
Ticket: Can the professor share the slides for lecture 4?
CATEGORY: Academic
SEVERITY: Low

### Target Ticket
Ticket: The main air conditioning unit in the server room has stopped working and temperatures are rising.
CATEGORY:"""

config = types.GenerateContentConfig(temperature=0.0, max_output_tokens=60)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=few_shot_prompt,
    config=config
)

print("CATEGORY:" + response.text.strip())
```

---

## 9. Code Explanation — Line by Line
* **Lines 10-28**: Constructs `few_shot_prompt` containing the system definition, 3 solved examples with identical formatting, and the target ticket.
* **Line 28**: Leaves `CATEGORY:` as the completion trigger, nudging the model to start generating the exact completion.
* **Line 30**: Sets `temperature=0.0` for deterministic classification.
* **Lines 32-36**: Executes the generation call.
* **Line 38**: Prints the classified result.

---

## 10. Expected Output
```text
CATEGORY: Infrastructure
SEVERITY: High
```

---

## 11. How to Run
```bash
python week03-generative-ai/examples/05_few_shot.py
```

---

## 12. Experiment Yourself
Test the classifier with these new target tickets:
1. Target A: `"I lost my library ID card and need a replacement before finals."`
2. Target B: `"The projector bulb in Hall B exploded during class."`
3. Target C: `"Where can I find the academic calendar for next semester?"`

---

## 13. Common Mistakes
1. **Inconsistent Formatting in Exemplars**: Using `CATEGORY: Academic` in Example 1 but `Category = Academic` in Example 2 confuses the model.
2. **Imbalanced Exemplars**: Providing 4 "High" severity examples and 0 "Low" severity examples biases the model towards "High".

---

## 14. Debugging Exercise
**Buggy Code**:
```python
# Student prompt missing delimiters:
prompt = "Wifi is down. Cat: Infra. Money missing. Cat: Fin. Projector broken. Cat:"
```
**Fix**: Use structured formatting with clear labels and line breaks to ensure high attention separation.

---

## 15. Student Practice Task
Create a script `ex05_few_shot_classifier.py` that classifies customer reviews of electronic gadgets into `[SENTIMENT: Positive/Negative/Neutral]` and `[KEY_FEATURE: Battery/Screen/Performance/Price]`.

---

## 16. Mini Challenge
Write a dynamic few-shot generator function `build_prompt(exemplars: list[dict], target: str) -> str` that programmatically builds the few-shot prompt string from a list of Python dictionaries.

---

## 17. Real-World Industry Use
Banks, airlines, and tech companies use few-shot prompt templates to triage hundreds of thousands of customer support inquiries and route them to appropriate departments.

---

## 18. Viva Questions
1. *What is the difference between Few-Shot prompting and Model Fine-Tuning?*  
   **Answer**: Few-Shot prompting provides examples in the temporary context window without modifying model weights. Fine-tuning permanently updates model weights via gradient descent on training datasets.
2. *How many exemplars are typically optimal for few-shot prompts?*  
   **Answer**: Typically 2 to 5 diverse, balanced examples are sufficient.

---

## 19. Interview Questions
1. *How can Retrieval-Augmented Generation (RAG) be used to implement Dynamic Few-Shot prompting?*  
   **Answer**: When a user query arrives, the system queries a vector database for the top-$K$ most semantically similar solved historical examples and dynamically injects them into the prompt as few-shot exemplars before model invocation.

---

## 20. Quick Revision
* Few-shot = Demonstrations $\to$ Pattern replication.
* Always use consistent formatting and balanced category examples.
* Combine with $T=0.0$ for deterministic classification.

---

## 21. Checklist
- [ ] Understand difference between zero-shot and few-shot
- [ ] Executed `05_few_shot.py`
- [ ] Tested unseen campus ticket classifications
- [ ] Completed the dynamic prompt builder mini challenge
