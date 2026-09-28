"""
Exercise 06: Step-by-Step Problem Reasoner & Output Extractor
Course Instructor: Dr. Rameshwer

Task:
Write a parser that extracts the numeric final answer from a structured
Chain-of-Thought LLM response.
"""

def extract_final_gpa(llm_response_text: str) -> float:
    """Extracts the float GPA following 'FINAL ANSWER: GPA = ' from response text.

    TODO: Use string searching or regex to extract the float value.
    """
    marker = "FINAL ANSWER:"
    if marker not in llm_response_text:
        raise ValueError("Missing 'FINAL ANSWER:' delimiter in model response.")

    answer_section = llm_response_text.split(marker)[-1]
    
    # Extract numerical tokens
    for token in answer_section.replace("=", " ").replace("GPA", " ").split():
        try:
            return float(token)
        except ValueError:
            continue

    raise ValueError("Could not parse float value from answer section.")

if __name__ == "__main__":
    sample_llm_output = """
    1. STEP-BY-STEP CALCULATION:
    - Quality points: 16.0 + 9.0 + 12.0 + 4.0 = 41.0
    - Total credits: 12
    - Division: 41 / 12 = 3.4166
    2. VERIFICATION: Checked.
    3. FINAL ANSWER: GPA = 3.42
    """
    gpa = extract_final_gpa(sample_llm_output)
    print(f"Parsed GPA: {gpa} (Type: {type(gpa).__name__})")
