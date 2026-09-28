"""
Solution 03: Temperature Experimenter
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 03.
"""

from typing import Literal

def get_generation_parameters(task_type: Literal["code_generation", "math", "classification", "creative_writing", "brainstorming"]) -> dict:
    task = task_type.lower().strip()
    if task in ["code_generation", "math", "classification"]:
        return {"temperature": 0.0, "max_output_tokens": 256}
    elif task in ["creative_writing", "brainstorming"]:
        return {"temperature": 0.9, "max_output_tokens": 512}
    else:
        return {"temperature": 0.5, "max_output_tokens": 300}

if __name__ == "__main__":
    for t in ["code_generation", "creative_writing"]:
        print(t, "->", get_generation_parameters(t))
