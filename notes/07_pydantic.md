# Step 7: Pydantic v2 Fundamentals & Validation

**Guide by Dr. Rameshwer** | *Full-Stack AI Engineer*

---

## 1. Core Concept
Python type hints are not enforced at runtime. Pydantic's `BaseModel` provides:
- Automatic type coercion and deep validation
- Value boundaries via `Field(ge=..., le=...)`
- Instant serialization (`model_dump()`, `model_dump_json()`)
- Clear `ValidationError` exceptions when dirty data enters your system

## 2. Key Code
```python
from pydantic import BaseModel, Field, ValidationError

class Student(BaseModel):
    roll_no: str = Field(min_length=4)
    gpa: float = Field(ge=0.0, le=4.0)

# Valid
s = Student(roll_no="CS101", gpa=3.8)
print(s.model_dump())

# Invalid raises ValidationError
try:
    s_bad = Student(roll_no="C", gpa=5.0)
except ValidationError as e:
    print(e)
```

## 3. How to Run
```bash
python 07_pydantic_validation.py
```

## 4. Key Takeaways
- Always inherit from `BaseModel`.
- Pydantic v2 is written in Rust (`pydantic-core`), making validation blazingly fast.

## 5. Self-Check & Interview Question
* **Q**: *What is the difference between `model_dump()` and `model_dump_json()` in Pydantic v2?*  
* **Answer**: `model_dump()` returns a native Python dictionary; `model_dump_json()` returns a serialized JSON string.
