"""
Campus Database Tools for Agentic LLM Calling
Course Instructor: Dr. Rameshwer

These functions are bound directly to the Google GenAI client as callable tools.
"""

# Simulated University Databases
STUDENTS_DB = {
    "CS2026": {
        "roll_no": "CS2026",
        "name": "Alice Smith",
        "major": "Computer Science",
        "gpa": 3.88,
        "completed_courses": ["CS101 - Intro to Programming", "CS201 - Data Structures", "MATH101 - Calculus I"],
        "academic_standing": "Dean's List"
    },
    "CS2027": {
        "roll_no": "CS2027",
        "name": "Bob Jones",
        "major": "Data Science",
        "gpa": 2.45,
        "completed_courses": ["CS101 - Intro to Programming"],
        "academic_standing": "Academic Probation"
    }
}

COURSE_CATALOGUE = {
    "CS301": {
        "course_code": "CS301",
        "title": "Database Management Systems",
        "credits": 4,
        "prerequisites": ["CS201 - Data Structures"],
        "description": "Relational algebra, SQL, indexing, transaction processing, and normalization."
    },
    "CS401": {
        "course_code": "CS401",
        "title": "Generative AI Engineering",
        "credits": 4,
        "prerequisites": ["CS201 - Data Structures", "CS301 - Database Management Systems"],
        "description": "Transformers, prompt engineering, structured outputs, tool calling, and microservices."
    }
}

def query_student_record(roll_no: str) -> dict:
    """Queries the university registrar database for a student's academic profile.

    Args:
        roll_no: The unique student roll number string (e.g. 'CS2026').

    Returns:
        A dictionary containing student profile information, GPA, completed courses, and standing.
    """
    clean_roll = roll_no.strip().upper()
    if clean_roll in STUDENTS_DB:
        return {"found": True, "student": STUDENTS_DB[clean_roll]}
    return {"found": False, "error": f"Student with roll number '{clean_roll}' not found in registry."}

def query_course_info(course_code: str) -> dict:
    """Queries the university course catalogue for prerequisites, credits, and syllabus.

    Args:
        course_code: The course code string (e.g. 'CS301' or 'CS401').

    Returns:
        A dictionary containing course details, prerequisites, and credit hours.
    """
    clean_code = course_code.strip().upper()
    if clean_code in COURSE_CATALOGUE:
        return {"found": True, "course": COURSE_CATALOGUE[clean_code]}
    return {"found": False, "error": f"Course code '{clean_code}' not found in catalogue."}
