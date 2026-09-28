"""
Solution 06: Step-by-Step Problem Reasoner & Output Extractor
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 06.
"""

def extract_final_gpa(llm_response_text: str) -> float:
    marker = "FINAL ANSWER:"
    if marker not in llm_response_text:
        raise ValueError("Missing 'FINAL ANSWER:' delimiter in model response.")

    answer_section = llm_response_text.split(marker)[-1]
    for token in answer_section.replace("=", " ").replace("GPA", " ").split():
        try:
            return float(token)
        except ValueError:
            continue

    raise ValueError("Could not parse float value from answer section.")

if __name__ == "__main__":
    sample = "1. Steps: calc... 2. Checked. 3. FINAL ANSWER: GPA = 3.85"
    print("Parsed GPA:", extract_final_gpa(sample))
