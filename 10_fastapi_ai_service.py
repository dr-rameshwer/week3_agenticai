"""
Step 10: Complete FastAPI AI Microservice
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- Building an asynchronous REST API with FastAPI
- Validating request and response bodies with Pydantic
- Automatic Swagger interactive documentation at /docs
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

# 1. Initialize FastAPI
app = FastAPI(
    title="Academic AI Advisory Microservice",
    description="Prepared by Dr. Rameshwer (Full-Stack AI Engineer)",
    version="1.0.0"
)

# 2. Schemas
class AdvisoryRequest(BaseModel):
    subject: str = Field(min_length=2, max_length=50, description="e.g. Algorithms")
    question: str = Field(min_length=5, max_length=300, description="Inquiry text")

class AdvisoryResponse(BaseModel):
    subject: str
    advice: str
    status: str = "success"

# 3. Health check endpoint
@app.get("/health", tags=["System"])
def health():
    return {"status": "online", "llm_connected": bool(api_key.startswith("AIzaSy"))}

# 4. Asynchronous AI endpoint
@app.post("/api/v1/advisory", response_model=AdvisoryResponse, tags=["AI Service"])
async def get_advisory(request: AdvisoryRequest):
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            prompt = f"Subject: {request.subject}\nQuestion: {request.question}\nGive 2 concise practical recommendations."
            res = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
                contents=prompt
            )
            return AdvisoryResponse(
                subject=request.subject,
                advice=res.text.strip(),
                status="success"
            )
        except Exception:
            pass

    return AdvisoryResponse(
        subject=request.subject,
        advice=f"[Simulated Advisor]: For {request.subject} ('{request.question}'), practice coding daily and review course notes.",
        status="simulated"
    )

if __name__ == "__main__":
    print("=" * 60)
    print("FastAPI Microservice Running!")
    print("Open in your browser: http://127.0.0.1:8000/docs")
    print("=" * 60)
    uvicorn.run(app, host="127.0.0.1", port=8000)
