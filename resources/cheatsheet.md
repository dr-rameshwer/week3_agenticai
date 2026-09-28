# Python & Generative AI Quick Cheatsheet

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Fast-Reference Syntax for Python, Google GenAI SDK, Pydantic, and FastAPI*

---

## 1. Environment & Packages
```bash
# Virtual environment setup
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows

# Installing and saving requirements
pip install -r requirements.txt
pip freeze > requirements.txt
```

---

## 2. Google GenAI SDK (`google-genai`)
```python
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Basic Generation
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain recursion in 10 words."
)
print(response.text)

# 2. Generation with System Instruction & Temperature
config = types.GenerateContentConfig(
    system_instruction="You are a strict programming examiner.",
    temperature=0.2,
    max_output_tokens=300
)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is a segmentation fault?",
    config=config
)

# 3. Structured JSON Output with Pydantic
from pydantic import BaseModel

class StudentReport(BaseModel):
    name: str
    gpa: float
    summary: str

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Generate a profile for Alice with 3.9 GPA.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=StudentReport
    )
)
# Parse to verified Pydantic instance:
report = StudentReport.model_validate_json(response.text)
```

---

## 3. Pydantic v2 Syntax
```python
from pydantic import BaseModel, Field, ValidationError
from typing import Optional, List

class CourseEnrollment(BaseModel):
    course_code: str = Field(min_length=5, max_length=10, description="e.g. CS101")
    credits: int = Field(ge=1, le=4)
    instructor: str
    is_active: bool = True
    prerequisites: List[str] = Field(default_factory=list)

# Creation and Validation
try:
    obj = CourseEnrollment(course_code="CS101", credits=3, instructor="Dr. Rameshwer")
    print(obj.model_dump())       # Convert to Python dict
    print(obj.model_dump_json())  # Convert to JSON string
except ValidationError as e:
    print(e.errors())
```

---

## 4. FastAPI & Uvicorn Microservice Syntax
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="AI Advisory Service", version="1.0.0")

class AdvisoryRequest(BaseModel):
    student_id: str
    query: str

class AdvisoryResponse(BaseModel):
    student_id: str
    advice: str
    status: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/v1/advisory", response_model=AdvisoryResponse)
async def generate_advice(request: AdvisoryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    return AdvisoryResponse(
        student_id=request.student_id,
        advice=f"Processed query for {request.student_id}",
        status="success"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```
