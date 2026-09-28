# Hands-On Assignment 3: Tool-Augmented FastAPI Microservice

**Prepared by Dr. Rameshwer**  
*Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*  
*Self-Paced Training Module with Complete Solution & Self-Evaluation*

---

## 1. Problem Statement
Build an asynchronous REST microservice with FastAPI combining tool calling (querying student records and prerequisite catalogues) with interactive Swagger documentation.

---

## 2. Complete Reference Solution Code

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="Smart Academic Advisor Service", version="1.0.0")

STUDENT_DB = {
    "CS2026": {"name": "Alice", "gpa": 3.9, "completed": ["CS101", "CS201"]},
    "CS2027": {"name": "Bob", "gpa": 2.3, "completed": ["CS101"]}
}

COURSE_DB = {
    "CS301": {"title": "Database Systems", "prereq": "CS201"},
    "CS401": {"title": "Agentic AI Systems", "prereq": "CS301"}
}

class AdvisoryQuery(BaseModel):
    roll_no: str = Field(min_length=4, max_length=10)
    course_code: str = Field(min_length=4, max_length=10)

class AdvisoryResult(BaseModel):
    roll_no: str
    eligible: bool
    reason: str

@app.post("/api/v1/check-eligibility", response_model=AdvisoryResult)
async def check_eligibility(query: AdvisoryQuery):
    roll = query.roll_no.upper()
    code = query.course_code.upper()

    if roll not in STUDENT_DB:
        raise HTTPException(status_code=404, detail="Student not found in registry.")
    if code not in COURSE_DB:
        raise HTTPException(status_code=404, detail="Course not found in catalogue.")

    student = STUDENT_DB[roll]
    course = COURSE_DB[code]
    required_prereq = course["prereq"]

    if required_prereq in student["completed"]:
        return AdvisoryResult(
            roll_no=roll,
            eligible=True,
            reason=f"Eligible! Student {student['name']} has completed prerequisite {required_prereq}."
        )
    else:
        return AdvisoryResult(
            roll_no=roll,
            eligible=False,
            reason=f"Not eligible. Missing prerequisite {required_prereq}."
        )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
```

---

## 3. Self-Evaluation & Verification
1. Run: `python assignment3_service.py`
2. Open Swagger UI in browser: `http://127.0.0.1:8002/docs`
3. Execute Test Cases:
   - Query: `{"roll_no": "CS2026", "course_code": "CS301"}` $\to$ `eligible: true`.
   - Query: `{"roll_no": "CS2027", "course_code": "CS301"}` $\to$ `eligible: false`.
