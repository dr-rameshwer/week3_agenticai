# Topic 07: Pydantic Fundamentals & Schema Validation

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 07*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Understand why Python type hints alone are insufficient for runtime validation.
2. Define data models by inheriting from Pydantic's `BaseModel`.
3. Apply field constraints and descriptions using `Field(...)`.
4. Handle optional fields, default values, and list/dict containers.
5. Catch and inspect `ValidationError` exceptions when data is corrupted.
6. Serialize models to Python dictionaries (`model_dump()`) and JSON strings (`model_dump_json()`).

---

## 2. Why Are We Learning This?
Python is a dynamically typed language. When developing production backends or integrating with AI models, incoming data is frequently dirty, missing keys, or malformed. Pydantic guarantees that data passing through your software adheres strictly to defined schemas before your business logic processes it.

---

## 3. Concept in Simple Words
Pydantic is like a **strict security guard** at the entrance of your program. When raw data arrives, Pydantic checks every field against your blueprint. If the data is valid, it lets it through as a clean Python object. If anything is wrong, it immediately blocks it and reports the exact mistake.

---

## 4. Real-World Analogy
Think of a university admissions form:
* A blank form has fields: *Name (text)*, *Age (positive integer)*, *GPA (0.0 to 4.0)*.
* If a student writes `"banana"` for Age or `5.5` for GPA, the admissions office rejects the form with an explicit error. Pydantic is that admissions office.

---

## 5. Technical Explanation
When you define a class inheriting from `pydantic.BaseModel`:
1. Pydantic creates an internal schema validator compiled in Rust (`pydantic-core`).
2. When instantiated with keyword arguments or raw JSON, Pydantic performs type coercion (e.g., converting the string `"123"` to the integer `123` if specified as `int`).
3. It evaluates all `Field` constraints (e.g., `ge=0.0`, `le=4.0`, `min_length=2`).
4. If validation succeeds, attributes are stored in `__dict__` and accessible via dot notation.
5. If validation fails, a `ValidationError` containing a list of error dictionaries is raised.

---

## 6. Important Terminology
* **BaseModel**: The core Pydantic parent class.
* **Type Annotation / Hint**: Python syntax (`x: int`) declaring expected types.
* **Field**: Function providing metadata, constraints, and descriptions for individual model attributes.
* **ValidationError**: The exception raised when validation fails.
* **Serialization**: Converting a live Pydantic object into a dictionary or JSON string.

---

## 7. Python Syntax & Concepts Encountered
* `class ModelName(BaseModel):` — Class inheritance.
* `name: str` — Type annotations.
* `age: Optional[int] = None` — Optional fields using `typing.Optional`.
* `Field(ge=0.0, le=4.0, description="...")` — Value constraints (`ge` = greater than or equal, `le` = less than or equal).
* `obj.model_dump()` & `obj.model_dump_json()` — Pydantic v2 export methods.

---

## 8. Smallest Working Example (`07_pydantic_basics.py`)

```python
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

# Step 1: Define the Pydantic schema
class StudentProfile(BaseModel):
    roll_no: str = Field(min_length=4, max_length=10, description="Unique student ID")
    name: str = Field(min_length=2, description="Full student name")
    gpa: float = Field(ge=0.0, le=4.0, description="GPA on a 4.0 scale")
    enrolled_courses: List[str] = Field(default_factory=list)
    email: Optional[str] = None

# Step 2: Instantiate with Valid Data
print("--- 1. Valid Student Profile ---")
valid_student = StudentProfile(
    roll_no="CS2026",
    name="Alice Smith",
    gpa=3.85,
    enrolled_courses=["Data Structures", "Generative AI"]
)
print(f"Student Object: {valid_student}")
print(f"Dictionary Export: {valid_student.model_dump()}")
print(f"JSON Export:       {valid_student.model_dump_json()}")

# Step 3: Test Validation Error Handling
print("\n--- 2. Testing Invalid Data ---")
try:
    invalid_student = StudentProfile(
        roll_no="CS",        # Too short! (min_length=4)
        name="Bob",
        gpa=4.95            # Out of bounds! (le=4.0)
    )
except ValidationError as e:
    print("Caught expected ValidationError:")
    for err in e.errors():
        field = err["loc"][0]
        msg = err["msg"]
        print(f"  * Field '{field}': {msg}")
```

---

## 9. Code Explanation — Line by Line
* **Line 1-2**: Imports `BaseModel`, `Field`, `ValidationError` and typing helpers.
* **Lines 5-10**: Declares `StudentProfile` inheriting from `BaseModel`. Note that no `def __init__` is written; Pydantic generates it automatically.
* **Lines 14-19**: Creates a valid instance. Pydantic verifies that `gpa=3.85` is between $0.0$ and $4.0$.
* **Lines 21-22**: `model_dump()` converts the object to a standard Python dictionary; `model_dump_json()` converts it to a clean JSON string.
* **Lines 26-34**: Attempts to create an invalid instance. `ValidationError` is caught, and `e.errors()` iterates through the exact failure reasons.

---

## 10. Expected Output
```text
--- 1. Valid Student Profile ---
Student Object: roll_no='CS2026' name='Alice Smith' gpa=3.85 enrolled_courses=['Data Structures', 'Generative AI'] email=None
Dictionary Export: {'roll_no': 'CS2026', 'name': 'Alice Smith', 'gpa': 3.85, 'enrolled_courses': ['Data Structures', 'Generative AI'], 'email': None}
JSON Export:       {"roll_no":"CS2026","name":"Alice Smith","gpa":3.85,"enrolled_courses":["Data Structures","Generative AI"],"email":null}

--- 2. Testing Invalid Data ---
Caught expected ValidationError:
  * Field 'roll_no': String should have at least 4 characters
  * Field 'gpa': Input should be less than or equal to 4
```

---

## 11. How to Run
```bash
python week03-generative-ai/examples/07_pydantic_basics.py
```

---

## 12. Experiment Yourself
1. Add a new field `is_graduated: bool = False` to `StudentProfile`.
2. Test instantiating with string `"true"` or integer `1`. Does Pydantic automatically coerce it to boolean `True`?
3. Add a regex pattern to `email`: `pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"`.

---

## 13. Common Mistakes
* Using Pydantic v1 methods like `.dict()` or `.json()` instead of Pydantic v2 `.model_dump()` and `.model_dump_json()`.
* Using mutable default arguments like `courses: List[str] = []` instead of `Field(default_factory=list)`.

---

## 14. Debugging Exercise
**Buggy Code**:
```python
class Book(BaseModel):
    title: str
    price: float = Field(gt=0)

# Why will this error?
b = Book(title="AI Handbook", price="-15.5")
```
**Fix**: `price` is negative (violating `gt=0`). Value must be a positive float.

---

## 15. Student Practice Task
Create a script `ex07_pydantic_validator.py` that defines a `CourseSyllabus` schema with:
* `course_code` (str)
* `title` (str)
* `credits` (int between 1 and 4)
* `modules` (list of strings with at least 3 module names)

---

## 16. Mini Challenge
Use Pydantic's `@field_validator` decorator to verify that `course_code` starts with uppercase letters followed by digits (e.g., `"CS101"`).

---

## 17. Real-World Industry Use
Pydantic is the validation engine powering **FastAPI**, **LangChain**, **Instructor**, and modern database ORMs across thousands of production cloud systems.

---

## 18. Viva Questions
1. *Why do we inherit from `BaseModel`?*  
   **Answer**: To gain automated data validation, type coercion, field inspection, and JSON serialization capabilities.
2. *What is the difference between `model_dump()` and `model_dump_json()` in Pydantic v2?*  
   **Answer**: `model_dump()` returns a Python dictionary; `model_dump_json()` returns a serialized JSON string.

---

## 19. Interview Questions
1. *How does Pydantic v2 achieve high performance compared to Pydantic v1?*  
   **Answer**: The core validation and serialization logic was rewritten in Rust (`pydantic-core`), avoiding Python interpreter overhead for nested data structures.

---

## 20. Quick Revision
* Inherit from `BaseModel`.
* Use `Field(ge=..., le=..., min_length=...)` for constraints.
* Export with `.model_dump()` and `.model_dump_json()`.

---

## 21. Checklist
- [ ] Understand `BaseModel` inheritance
- [ ] Executed `07_pydantic_basics.py`
- [ ] Observed `ValidationError` handling
- [ ] Tested `.model_dump()` and `.model_dump_json()`
