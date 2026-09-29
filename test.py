#!/usr/bin/env python3
# ==============================================================================
# WEEK 3 CAPSTONE: LLM-POWERED FASTAPI APPLICATION
# File: 11_campus_ai_capstone.py
#
# CONCEPTS COMBINED (WEEK 3 SYLLABUS):
#   1. Gemini LLM Fundamentals & Inference (gemini-3.6-flash)
#   2. System Prompt & Prompt Engineering (Campus Advisor Persona)
#   3. Function Calling / Tools (Connecting LLM to Campus Database)
#   4. Structured Input/Output (Pydantic BaseModel)
#   5. REST API Microservice (FastAPI + Swagger UI at /docs)
#
# HOW TO RUN:
#   uvicorn 11_campus_ai_capstone:app --reload --port 8000
#   (Then open in your browser: http://127.0.0.1:8000/docs)
# ==============================================================================

# Line 1: Import os to read environment variables from the operating system
import os

# Line 2: Import load_dotenv to load keys from the local .env file
from dotenv import load_dotenv

# Line 3: Import FastAPI to create the web server and REST API endpoints
from fastapi import FastAPI

# Line 4: Import BaseModel to create structured data models with type checking
from pydantic import BaseModel

# ------------------------------------------------------------------------------
# STEP 1: LOAD ENVIRONMENT VARIABLES & API CONFIGURATION
# ------------------------------------------------------------------------------
# Line 5: Load key-value pairs from .env into os.environ
load_dotenv()

# Line 6: Retrieve the Gemini API key from environment memory safely
api_key = os.getenv("GEMINI_API_KEY")

# Line 7: Define the System Prompt to give the AI its identity and behavioral rules
SYSTEM_PROMPT = (
    "You are the Campus AI Academic Advisor. "
    "Be brief, helpful, and polite (2 sentences max). "
    "When asked about student exam eligibility or attendance, "
    "always call the get_student_record tool."
)

# ------------------------------------------------------------------------------
# STEP 2: SIMULATED PRIVATE DATABASE & PYTHON TOOL
# ------------------------------------------------------------------------------
# Line 8: Private student records that the LLM cannot see directly
STUDENTS_DB = {
    "AI-2026-001": {"name": "Aarav Sharma", "attendance": 88.5, "eligible": True},
    "AI-2026-002": {"name": "Priya Patel", "attendance": 64.0, "eligible": False},
    "AI-2026-003": {"name": "Ram", "attendance": 87.0, "eligible": True}

}

# Line 9: Define the Python Tool function (Gemini reads the docstring to understand what it does!)
def get_student_record(roll_no: str) -> dict:
    """
    Look up a student's official attendance percentage and exam eligibility.
    
    Args:
        roll_no: The student roll number, e.g. 'AI-2026-001' or 'AI-2026-002'.
    """
    # Line 10: Clean the input roll number by removing extra spaces and converting to uppercase
    clean_roll = roll_no.strip().upper()
    
    # Line 11: Check if the roll number exists in our private database
    if clean_roll in STUDENTS_DB:
        # Line 12: Return the matching record as a Python dictionary
        return {"status": "SUCCESS", "record": STUDENTS_DB[clean_roll]}
    
    # Line 13: Return an error message if the student was not found
    return {"status": "NOT_FOUND", "error": f"Student {clean_roll} was not found."}

# ------------------------------------------------------------------------------
# STEP 3: PYDANTIC DATA MODELS (STRUCTURED CONTRACTS)
# ------------------------------------------------------------------------------
# Line 14: Define the input schema (FastAPI automatically validates incoming JSON)
class ChatQuery(BaseModel):
    message: str  # The student's question sent to the API

# Line 15: Define the output schema (Guarantees the API returns clean structured JSON)
class ChatResponse(BaseModel):
    reply: str    # The final plain-text answer returned to the student

# ------------------------------------------------------------------------------
# STEP 4: FASTAPI WEB APPLICATION SETUP
# ------------------------------------------------------------------------------
# Line 16: Initialize the FastAPI application instance
app = FastAPI(
    title="Campus AI Advisor API",
    description="Week 3 Weekly Project: LLM-Powered FastAPI Application",
    version="1.0.0"
)

# Line 17: Health Check route to verify the server is active
@app.get("/")
def home():
    # Line 18: Returns a simple discovery JSON with the Swagger UI documentation link
    return {"status": "ONLINE", "docs_url": "http://127.0.0.1:8000/docs"}

# Line 19: Main conversational endpoint that accepts questions and generates AI answers
@app.post("/chat", response_model=ChatResponse)
async def chat_with_advisor(query: ChatQuery):
    # Line 20: Check if a valid Gemini API key is configured
    if api_key and api_key != "your_gemini_api_key_here":
        try:
            # Line 21: Lazy-import Google Generative AI SDK
            import google.generativeai as genai
            
            # Line 22: Configure the SDK globally with the secret key
            genai.configure(api_key=api_key)
            
            # Line 23: Initialize Gemini model with System Persona and our Python Tool
            model = genai.GenerativeModel(
                model_name=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
                system_instruction=SYSTEM_PROMPT,
                tools=[get_student_record]
            )
            
            # Line 24: Start a chat session with automatic function calling enabled
            chat_session = model.start_chat(enable_automatic_function_calling=True)
            
            # Line 25: Send the user's message to Gemini (Gemini calls the tool if needed!)
            response = chat_session.send_message(query.message)
            
            # Line 26: Return the generated response wrapped in our Pydantic model
            return ChatResponse(reply=response.text.strip())
        except Exception:
            # Line 27: Pass on error to fall back to simulation mode
            pass

    # Line 28: Offline Simulation Mode (Ensures students can test without API keys or internet)
    msg = query.message.upper()
    if "AI-2026-001" in msg:
        reply_text = "Student Aarav Sharma (AI-2026-001) has 88.5% attendance and is ELIGIBLE for exams."
    elif "AI-2026-002" in msg:
        reply_text = "Student Priya Patel (AI-2026-002) has 64.0% attendance and is NOT ELIGIBLE for exams."
    else:
        reply_text = "Hello! I am your Campus AI Academic Advisor. Ask me about student attendance or exam eligibility."
    
    # Line 29: Return the simulated answer wrapped in our Pydantic model
    return ChatResponse(reply=reply_text)

# ------------------------------------------------------------------------------
# STEP 5: SERVER ENTRYPOINT
# ------------------------------------------------------------------------------
# Line 30: Check if the file is executed directly with python3
if __name__ == "__main__":
    # Line 31: Import uvicorn to run the ASGI web server
    import uvicorn
    
    # Line 32: Print helpful startup instructions to the terminal
    print("Starting Campus AI Advisor API...")
    print("Interactive Swagger Documentation: http://127.0.0.1:8000/docs\n")
    
    # Line 33: Start the server on host 127.0.0.1 and port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)