"""
Exercise 10: Automated Code Review Endpoint with FastAPI
Course Instructor: Dr. Rameshwer

Task:
Build a standalone FastAPI application with a code review endpoint.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Automated Code Review API",
    description="Student Practice Endpoint | Prepared by Dr. Rameshwer",
    version="1.0.0"
)

# TODO 1: Define Request Schema
class CodeReviewRequest(BaseModel):
    language: str = Field(min_length=1, max_length=20, description="Programming language (e.g. Python)")
    code_snippet: str = Field(min_length=5, description="Code to be analyzed")

# TODO 2: Define Response Schema
class CodeReviewResponse(BaseModel):
    language: str
    quality_score: int = Field(ge=0, le=100, description="Score from 0 to 100")
    feedback: str
    is_approved: bool

# TODO 3: Implement POST Endpoint
@app.post("/api/v1/review", response_model=CodeReviewResponse)
async def review_code(request: CodeReviewRequest):
    if "eval(" in request.code_snippet or "exec(" in request.code_snippet:
        return CodeReviewResponse(
            language=request.language,
            quality_score=30,
            feedback="Security Warning: Usage of eval/exec is dangerous and violates security rules.",
            is_approved=False
        )

    return CodeReviewResponse(
        language=request.language,
        quality_score=95,
        feedback="Code structure looks clean and follows idiomatic patterns.",
        is_approved=True
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
