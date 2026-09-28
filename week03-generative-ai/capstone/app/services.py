"""
AI Advisory Orchestration Service
Course Instructor: Dr. Rameshwer

Manages LLM client communication, tool registration, prompt assembly,
and fallback logic for the Smart Student Advisory Microservice.
"""

from typing import Optional
from app.config import settings
from app.schemas import StudentAdvisoryRequest, StudentAdvisoryResponse
from app.tools import query_student_record, query_course_info

class AdvisoryService:
    def __init__(self):
        self.api_key = settings.gemini_api_key
        self.model_name = settings.gemini_model
        self.client = None

        if self.api_key:
            try:
                from google import genai
                self.client = genai.Client(api_key=self.api_key)
            except Exception as e:
                print(f"[WARNING]: Could not initialize Gemini Client: {e}")
                self.client = None

    async def generate_advice(self, request: StudentAdvisoryRequest) -> StudentAdvisoryResponse:
        """Orchestrates student inquiry processing with tool calling."""
        clean_roll = request.roll_no.strip().upper()

        # Step 1: If client is not available, execute smart local advisory logic
        if not self.client:
            return self._simulate_advisory(request)

        # Step 2: Live LLM Call with Tool Integration
        try:
            from google.genai import types

            system_instruction = """
            You are an expert University Academic Advisor assisting students.
            Rules:
            1. Always query the student database using query_student_record to check the student's background.
            2. If course prerequisites are mentioned, verify them using query_course_info.
            3. Provide tailored, encouraging, and actionable academic advice.
            4. If the student is on Academic Probation, advise them on GPA improvement strategies.
            5. Keep the total recommendation concise (3-5 sentences).
            """

            config = types.GenerateContentConfig(
                system_instruction=system_instruction,
                tools=[query_student_record, query_course_info],
                temperature=0.1
            )

            prompt = f"Student Roll Number: {clean_roll}\nInquiry: {request.query}"

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=config
            )

            # Check student name from DB if available
            student_data = query_student_record(clean_roll)
            student_name = student_data.get("student", {}).get("name") if student_data.get("found") else None

            return StudentAdvisoryResponse(
                roll_no=clean_roll,
                student_name=student_name,
                query=request.query,
                advisory_recommendation=response.text.strip(),
                sources_used=["Google Gemini 2.5 Flash", "University Registrar DB"],
                status="success"
            )

        except Exception as e:
            # Fallback to local deterministic advisory if network or quota issue occurs
            print(f"[FALLBACK TRIGGERED]: {e}")
            return self._simulate_advisory(request)

    def _simulate_advisory(self, request: StudentAdvisoryRequest) -> StudentAdvisoryResponse:
        """Deterministic rule-based advisory for offline / test environments."""
        clean_roll = request.roll_no.strip().upper()
        record_res = query_student_record(clean_roll)

        if not record_res.get("found"):
            return StudentAdvisoryResponse(
                roll_no=clean_roll,
                student_name="Unknown Student",
                query=request.query,
                advisory_recommendation=(
                    f"Roll number '{clean_roll}' was not found in the academic registry. "
                    "Please visit the university admissions office to verify your registration status."
                ),
                sources_used=["University Registrar DB (Fallback)"],
                status="not_found"
            )

        student = record_res["student"]
        advice_parts = [
            f"Hello {student['name']} ({student['major']}).",
            f"Your current academic standing is '{student['academic_standing']}' with a GPA of {student['gpa']}."
        ]

        if student['gpa'] < 3.0:
            advice_parts.append(
                "You are currently on academic probation. We strongly recommend meeting with your "
                "course tutor and prioritizing prerequisite subjects to raise your GPA."
            )
        else:
            advice_parts.append(
                "You are maintaining excellent academic progress! You meet all standard prerequisites "
                "for advanced elective registrations."
            )

        return StudentAdvisoryResponse(
            roll_no=clean_roll,
            student_name=student["name"],
            query=request.query,
            advisory_recommendation=" ".join(advice_parts),
            sources_used=["University Registrar DB (Local Simulation)"],
            status="simulated"
        )

advisory_service = AdvisoryService()
