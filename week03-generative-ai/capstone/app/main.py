"""
FastAPI Academic Advisor Application Entrypoint
Course Instructor: Dr. Rameshwer

Main application file assembling routes, middleware, and OpenAPI configuration.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import (
    StudentAdvisoryRequest,
    StudentAdvisoryResponse,
    StudentRecord,
    CourseInfo
)
from app.tools import query_student_record, query_course_info, STUDENTS_DB, COURSE_CATALOGUE
from app.services import advisory_service
import uvicorn

# Initialize Application with metadata
app = FastAPI(
    title=settings.app_name,
    description=(
        "**Prepared by Dr. Rameshwer**\n\n"
        "A production-grade Generative AI microservice providing intelligent academic advising "
        "via Google Gemini 2.5 Flash, Pydantic v2 schemas, and tool calling."
    ),
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# System & Health Routes
# -----------------------------------------------------------------------------
@app.get("/health", tags=["System Health"])
def get_health_status():
    """Returns system status, active model configuration, and backend readiness."""
    return {
        "status": "online",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "instructor": settings.instructor,
        "model": settings.gemini_model,
        "llm_connected": advisory_service.client is not None
    }

# -----------------------------------------------------------------------------
# Core AI Advisory Routes
# -----------------------------------------------------------------------------
@app.post(
    "/api/v1/advisory/chat",
    response_model=StudentAdvisoryResponse,
    status_code=status.HTTP_200_OK,
    tags=["AI Advisory Engine"]
)
async def get_student_advisory(request: StudentAdvisoryRequest):
    """Submits a student academic query to the AI advisor.

    The engine performs automatic tool calling against the campus student registry
    and prerequisite catalogue to generate grounded guidance.
    """
    if not request.query.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student query cannot be empty."
        )

    response = await advisory_service.generate_advice(request)
    return response

# -----------------------------------------------------------------------------
# University Registry Query Routes
# -----------------------------------------------------------------------------
@app.get("/api/v1/students/{roll_no}", response_model=StudentRecord, tags=["Campus Registry"])
def get_student_by_roll(roll_no: str):
    """Direct lookup endpoint for student academic transcripts."""
    result = query_student_record(roll_no)
    if not result.get("found"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with roll number '{roll_no}' was not found in registry."
        )
    return StudentRecord(**result["student"])

@app.get("/api/v1/courses/{course_code}", response_model=CourseInfo, tags=["Campus Registry"])
def get_course_by_code(course_code: str):
    """Direct lookup endpoint for university course syllabus and prerequisites."""
    result = query_course_info(course_code)
    if not result.get("found"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course '{course_code}' was not found in catalogue."
        )
    return CourseInfo(**result["course"])

if __name__ == "__main__":
    print("=" * 60)
    print(f"Starting {settings.app_name}")
    print(f"Course Instructor: {settings.instructor}")
    print(f"Swagger Documentation: http://{settings.app_host}:{settings.app_port}/docs")
    print("=" * 60)
    uvicorn.run(app, host=settings.app_host, port=settings.app_port)
