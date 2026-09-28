"""
Exercise 04: Academic Persona & Guardrail Configurator
Course Instructor: Dr. Rameshwer

Task:
Construct a specialized system instruction string that enforces:
1. Persona: University Exam Invigilator & Rules Advisor
2. Guardrail: Must reject non-academic queries with a standard disclaimer.
"""

def build_academic_system_prompt() -> str:
    """Returns the formatted system instruction string.

    TODO: Fill in the multi-line prompt string.
    """
    system_instruction = """
    You are an official University Academic Integrity and Examination Rules Advisor.
    Rules:
    1. Answer queries strictly based on university examination guidelines.
    2. Maintain a professional, neutral, and authoritative academic tone.
    3. If a student asks questions unrelated to academics or exams, respond strictly with:
       'I am restricted to answering questions regarding academic policies and examinations.'
    4. Keep answers concise (under 4 sentences).
    """
    return system_instruction.strip()

if __name__ == "__main__":
    prompt = build_academic_system_prompt()
    print("--- Configured System Instruction ---")
    print(prompt)
