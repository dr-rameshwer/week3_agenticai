"""
Program: 10_fastapi_ai.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: Building an asynchronous REST API microservice with FastAPI,
         Pydantic request/response schemas, and Swagger UI documentation.
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize LLM client if API key is present
client = None
if api_key:
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
    except Exception:
        client = None

# Step 1: Initialize FastAPI App
app = FastAPI(
    title="Academic AI Advisory Microservice",
    description="Prepared by Dr. Rameshwer | Student Learning Resource",
    version="1.0.0"
)

# Step 2: Define Pydantic Request & Response Models
class AdvisoryRequest(BaseModel):
    subject: str = Field(min_length=2, max_length=50, description="Academic subject area")
    question: str = Field(min_length=5, max_length=300, description="Specific student inquiry")

class AdvisoryResponse(BaseModel):
    subject: str
    advice: str
    status: str = "success"

# Step 3: Health Check Route
@app.get("/health", tags=["System"])
def health_check():
    """Returns the operational health and readiness of the microservice."""
    return {
        "status": "healthy",
        "service": "academic-ai-advisor",
        "llm_connected": client is not None
    }

# Step 4: Asynchronous Advisory Endpoint
@app.post("/api/v1/advisory", response_model=AdvisoryResponse, tags=["Advisory Service"])
async def get_academic_advisory(request: AdvisoryRequest):
    """Processes a student academic inquiry and returns tailored mentor advice."""
    if not client:
        # Graceful simulation fallback if no API key is configured
        simulated_advice = (
            f"Regarding {request.subject}: For '{request.question}', ensure you review the core "
            "theoretical principles, complete laboratory exercises, and consult course notes."
        )
        return AdvisoryResponse(
            subject=request.subject,
            advice=simulated_advice,
            status="simulated"
        )

    try:
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        prompt = (
            f"Subject: {request.subject}\n"
            f"Student Question: {request.question}\n"
            "Provide 2 concise, practical study recommendations as an academic mentor."
        )

        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )

        return AdvisoryResponse(
            subject=request.subject,
            advice=response.text.strip(),
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")

# Step 5: Direct Execution Block
if __name__ == "__main__":
    print("=" * 50)
    print("STARTING FASTAPI MICROSERVICE")
    print("Course Instructor: Dr. Rameshwer")
    print("Interactive Documentation: http://127.0.0.1:8000/docs")
    print("=" * 50)
    uvicorn.run(app, host="127.0.0.1", port=8000)
