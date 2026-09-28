# Step 8: Guaranteed Structured Output with Pydantic

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
Never use regex or markdown string replacement to parse JSON from an LLM.
Using `response_schema=YourPydanticModel` activates **Constrained Decoding** at the API sampling layer, guaranteeing 100% valid JSON matching your schema.

## 2. Key Code
```python
from pydantic import BaseModel
from google.genai import types

class CourseReview(BaseModel):
    course_code: str
    sentiment: str
    key_topics: list[str]

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=CourseReview,
    temperature=0.0
)

res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Analyze: 'CS301 was amazing! Loved FastAPI.'",
    config=config
)

# Ingest directly:
obj = CourseReview.model_validate_json(res.text)
print(obj.sentiment)  # 'Positive'
```

## 3. How to Run
```bash
python 08_structured_output.py
```

## 4. Key Takeaways
- Constrained decoding eliminates JSON syntax errors and missing keys entirely.
- Ingest into typed Python objects using `Model.model_validate_json()`.

## 5. Self-Check & Interview Question
* **Q**: *How does the API enforce structured JSON output during token generation?*  
* **Answer**: Through context-free grammar masking: at each token generation step, logits for tokens that would violate the JSON grammar or Pydantic schema are set to $-\infty$.
