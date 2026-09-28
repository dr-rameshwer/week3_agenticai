# Topic 08: Guaranteed Structured Output with Pydantic

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 08*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Explain why free-form natural language output fails in production backend pipelines.
2. Configure LLMs to return guaranteed JSON adhering to a Pydantic schema.
3. Use `response_schema` and `response_mime_type="application/json"` in `google-genai`.
4. Parse and validate LLM responses directly into strongly-typed Pydantic model instances.

---

## 2. Why Are We Learning This?
If your backend expects `{ "sentiment": "positive", "score": 0.95 }`, and the LLM responds with *"Sure, here is your output: The sentiment appears to be positive..."*, your JSON parser crashes (`json.decoder.JSONDecodeError`). Production software requires **guaranteed machine-readable schemas**.

---

## 3. Concept in Simple Words
Instead of asking the LLM to *"please reply in JSON"*, we give the API our Pydantic class as a blueprint. The API constrains the model's token generation so it is mathematically impossible for it to output invalid syntax or missing keys.

---

## 4. Real-World Analogy
Think of filling out a government web form:
* If you give a citizen a blank piece of paper, they might write paragraphs or draw diagrams.
* If you give them a web form with rigid dropdowns, date pickers, and required text boxes, the submitted data is guaranteed to be clean and structured for the database.

---

## 5. Technical Explanation
Modern LLM APIs employ **Constrained Decoding** (Context-Free Grammar / CFG masking):
1. The developer registers a Pydantic class. The SDK translates it into JSON Schema.
2. As the model samples tokens one by one, tokens that would violate the JSON grammar or the schema (e.g., closing a bracket prematurely or emitting an invalid key) are masked out (logits $\to -\infty$).
3. The resulting string is guaranteed to be valid JSON matching the schema.
4. The client deserializes the string using `Model.model_validate_json(response.text)`.

---

## 6. Important Terminology
* **Structured Output**: LLM generation strictly adhering to a machine-readable schema.
* **Constrained Decoding**: Restricting token logits at sampling time to conform to a formal grammar.
* **`response_schema`**: The configuration property accepting a Pydantic class or JSON Schema.
* **`response_mime_type`**: Setting indicating `"application/json"`.

---

## 7. Python Syntax & Concepts Encountered
* `types.GenerateContentConfig(response_mime_type="application/json", response_schema=YourModel)`
* `YourModel.model_validate_json(response.text)`: Deserializes JSON directly into a verified Pydantic instance.

---

## 8. Smallest Working Example (`08_structured_output.py`)

```python
import os
from typing import List
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Step 1: Define the target schema
class CourseFeedbackAnalysis(BaseModel):
    course_code: str = Field(description="University course identifier, e.g., CS301")
    sentiment: str = Field(description="Overall sentiment: Positive, Neutral, or Negative")
    sentiment_score: float = Field(ge=0.0, le=1.0, description="Confidence score from 0.0 to 1.0")
    key_topics: List[str] = Field(description="List of core topics mentioned in feedback")
    recommended_action: str = Field(description="Actionable suggestion for the instructor")

# Step 2: Sample unstructured student feedback
student_review = """
I really enjoyed CS301 this semester! The coding assignments on FastAPI and Pydantic were
extremely practical, though the server deployment lecture went a bit too fast in week 3.
Overall, one of the best courses in the department!
"""

# Step 3: Configure generation with strict schema enforcement
config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=CourseFeedbackAnalysis,
    temperature=0.0
)

# Step 4: Invoke the model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Analyze the following student course review:\n{student_review}",
    config=config
)

# Step 5: Parse into validated Pydantic object
parsed_result = CourseFeedbackAnalysis.model_validate_json(response.text)

print("--- Validated Pydantic Object ---")
print(f"Course Code:        {parsed_result.course_code}")
print(f"Sentiment:          {parsed_result.sentiment} (Score: {parsed_result.sentiment_score})")
print(f"Key Topics:         {', '.join(parsed_result.key_topics)}")
print(f"Recommended Action: {parsed_result.recommended_action}")
```

---

## 9. Code Explanation — Line by Line
* **Lines 10-16**: Defines `CourseFeedbackAnalysis` with exact typed fields and descriptions.
* **Lines 19-23**: The unstructured raw student review text.
* **Lines 26-30**: Configures `response_mime_type="application/json"` and binds `response_schema=CourseFeedbackAnalysis`.
* **Lines 33-37**: Executes generation with `gemini-2.5-flash`.
* **Line 40**: `CourseFeedbackAnalysis.model_validate_json(response.text)` parses the guaranteed JSON string into a fully typed Python object.
* **Lines 43-47**: Accesses attributes directly using dot notation (`parsed_result.sentiment`).

---

## 10. Expected Output
```text
--- Validated Pydantic Object ---
Course Code:        CS301
Sentiment:          Positive (Score: 0.95)
Key Topics:         FastAPI, Pydantic, Server Deployment
Recommended Action: Allocate more time or supplementary materials for the server deployment topic.
```

---

## 11. How to Run
```bash
python week03-generative-ai/examples/08_structured_output.py
```

---

## 12. Experiment Yourself
Pass different student reviews:
1. Review A: *"The lab hardware in EE201 was broken every single week. Extremely frustrating experience."*
2. Review B: *"Math 105 was average. Lectures were clear, but the textbook was outdated."*

Observe how the schema guarantees structured fields for every review without parsing errors.

---

## 13. Common Mistakes
* Relying on regex or manual `json.loads(response.text.replace("```json", ""))` instead of native `response_schema`.
* Forgetting to set `response_mime_type="application/json"`.

---

## 14. Debugging Exercise
**Buggy Code**:
```python
# Student writes:
config = types.GenerateContentConfig(response_schema=CourseFeedbackAnalysis)
# Missing response_mime_type="application/json"
```
**Fix**: Both `response_mime_type="application/json"` and `response_schema` should be configured together.

---

## 15. Student Practice Task
Create a script `ex08_json_extractor.py` that extracts structured resume data (`CandidateInfo`: name, years_experience, top_skills, highest_degree) from raw biography text.

---

## 16. Mini Challenge
Add an `enum` for the `sentiment` field (`Literal["Positive", "Neutral", "Negative"]`) to restrict allowed string values at the schema level.

---

## 17. Real-World Industry Use
ETL data pipelines, automated invoice processing, customer feedback analytics, and database ingestion services all rely on guaranteed structured output.

---

## 18. Viva Questions
1. *What is the benefit of `response_schema` over asking the model to write JSON in the prompt?*  
   **Answer**: `response_schema` enforces constrained grammar decoding at the sampling layer, eliminating JSON markdown formatting artifacts and ensuring 100% syntactic and schema validity.
2. *How do you convert the JSON response string into a Pydantic object?*  
   **Answer**: Using `MyModel.model_validate_json(response.text)`.

---

## 19. Interview Questions
1. *How does constrained decoding prevent JSON syntax errors during inference?*  
   **Answer**: By masking token logits during sampling: only tokens that form valid JSON and conform to the schema transition state are assigned non-zero probabilities.

---

## 20. Quick Revision
* Define schema as `BaseModel`.
* Pass `response_schema=MyModel` and `response_mime_type="application/json"`.
* Ingest with `MyModel.model_validate_json(response.text)`.

---

## 21. Checklist
- [ ] Defined Pydantic schema for feedback analysis
- [ ] Executed `08_structured_output.py`
- [ ] Verified dot-notation attribute access
- [ ] Completed the resume extractor exercise
