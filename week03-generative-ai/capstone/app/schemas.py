"""
Data Schemas and Request/Response Models
Course Instructor: Dr. Rameshwer

Pydantic v2 schemas for API validation and structured outputs.
"""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class StudentRecord(BaseModel):
    roll_no: str = Field(description="Unique student roll number, e.g. 'CS2026'")
    name: str = Field(description="Full name of student")
    major: str = Field(description="Degree major")
    gpa: float = Field(ge=0.0, le=4.0, description="Cumulative Grade Point Average")
    completed_courses: List[str] = Field(default_factory=list, description="List of passed courses")
    academic_standing: Literal["Good Standing", "Academic Probation", "Dean's List"] = "Good Standing"

class CourseInfo(BaseModel):
    course_code: str = Field(description="Course identifier, e.g. 'CS301'")
    title: str = Field(description="Full course title")
    credits: int = Field(ge=1, le=4)
    prerequisites: List[str] = Field(default_factory=list)
    description: str

class StudentAdvisoryRequest(BaseModel):
    roll_no: str = Field(min_length=4, max_length=12, description="Student roll number, e.g. 'CS2026'")
    query: str = Field(min_length=5, max_length=500, description="Academic inquiry or guidance request")

class StudentAdvisoryResponse(BaseModel):
    roll_no: str
    student_name: Optional[str] = None
    query: str
    advisory_recommendation: str
    sources_used: List[str] = Field(default_factory=list, description="Tools or databases queried")
    status: str = "success"
