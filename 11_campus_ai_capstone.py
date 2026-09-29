#!/usr/bin/env python3
# ==============================================================================
# WEEK 3 CAPSTONE: LLM-POWERED FASTAPI APPLICATION
# File: 11_campus_ai_capstone.py
#
# Prepared by Dr. Rameshwer | Full-Stack AI Engineer
#
# CONCEPTS COMBINED (WEEK 3 SYLLABUS):
#   1. Gemini LLM Fundamentals & Inference
#   2. System Prompt & Prompt Engineering (Campus Advisor Persona)
#   3. Function Calling / Tools (Connecting LLM to Campus Database)
#   4. Structured Input/Output (Pydantic BaseModel)
#   5. REST API Microservice (FastAPI + Swagger UI at /docs)
#
# HOW TO RUN:
#   uvicorn 11_campus_ai_capstone:app --reload --port 8000
#   (Then open in your browser: http://127.0.0.1:8000/docs)
# ==============================================================================

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

# ------------------------------------------------------------------------------
# STEP 1: LOAD ENVIRONMENT VARIABLES & API CONFIGURATION
# ------------------------------------------------------------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

SYSTEM_PROMPT = (
    "You are the Campus AI Academic Advisor. "
    "Be brief, helpful, and polite (2 sentences max). "
    "When asked about student exam eligibility or attendance, "
    "always call the get_student_record tool."
)

# ------------------------------------------------------------------------------
# STEP 2: SIMULATED PRIVATE DATABASE & PYTHON TOOL
# ------------------------------------------------------------------------------
STUDENTS_DB = {
    "AI-2026-001": {"name": "Aarav Sharma", "attendance": 88.5, "eligible": True},
    "AI-2026-002": {"name": "Priya Patel", "attendance": 64.0, "eligible": False}
}

def get_student_record(roll_no: str) -> dict:
    """Look up a student's official attendance percentage and exam eligibility.

    Args:
        roll_no: The student roll number, e.g. 'AI-2026-001' or 'AI-2026-002'.
    """
    clean_roll = roll_no.strip().upper()
    if clean_roll in STUDENTS_DB:
        return {"status": "SUCCESS", "record": STUDENTS_DB[clean_roll]}
    return {"status": "NOT_FOUND", "error": f"Student {clean_roll} was not found."}

# ------------------------------------------------------------------------------
# STEP 3: PYDANTIC DATA MODELS (STRUCTURED CONTRACTS)
# ------------------------------------------------------------------------------
class ChatQuery(BaseModel):
    message: str  # The student's question sent to the API

class ChatResponse(BaseModel):
    reply: str    # The final plain-text answer returned to the student

# ------------------------------------------------------------------------------
# STEP 4: FASTAPI WEB APPLICATION SETUP
# ------------------------------------------------------------------------------
app = FastAPI(
    title="Campus AI Advisor API",
    description="Week 3 Final Capstone: LLM-Powered FastAPI Application | Prepared by Dr. Rameshwer",
    version="1.0.0"
)

@app.get("/")
def home():
    """Health Check route to verify the server is active."""
    return {"status": "ONLINE", "docs_url": "http://127.0.0.1:8000/docs"}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_advisor(query: ChatQuery):
    """Main conversational endpoint that accepts questions and generates AI answers."""
    # Check if a valid Gemini API key is configured
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            try:
                from google import genai
                from google.genai import types
                client = genai.Client(api_key=api_key)
                model_name = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

                config = types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    tools=[get_student_record],
                    temperature=0.1
                )
                response = client.models.generate_content(
                    model=model_name,
                    contents=query.message,
                    config=config
                )
                return ChatResponse(reply=response.text.strip())
            except Exception:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(
                    model_name=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
                    system_instruction=SYSTEM_PROMPT,
                    tools=[get_student_record]
                )
                chat_session = model.start_chat(enable_automatic_function_calling=True)
                response = chat_session.send_message(query.message)
                return ChatResponse(reply=response.text.strip())
        except Exception:
            pass

    # Offline Simulation Mode (Ensures students can test without API keys or internet)
    msg = query.message.upper()
    if "AI-2026-001" in msg:
        reply_text = "Student Aarav Sharma (AI-2026-001) has 88.5% attendance and is ELIGIBLE for exams."
    elif "AI-2026-002" in msg:
        reply_text = "Student Priya Patel (AI-2026-002) has 64.0% attendance and is NOT ELIGIBLE for exams."
    else:
        reply_text = "Hello! I am your Campus AI Academic Advisor. Ask me about student attendance or exam eligibility."

    return ChatResponse(reply=reply_text)

# ------------------------------------------------------------------------------
# STEP 5: SERVER ENTRYPOINT
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Campus AI Advisor API...")
    print("📖 Interactive Swagger Documentation: http://127.0.0.1:8000/docs\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)
