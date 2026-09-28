"""
Exercise 03: Temperature Experimenter
Course Instructor: Dr. Rameshwer

Task:
Build a utility function that selects the appropriate temperature config
based on the target engineering task type.
"""

from typing import Literal

def get_generation_parameters(task_type: Literal["code_generation", "math", "classification", "creative_writing", "brainstorming"]) -> dict:
    """Returns the recommended temperature and max_tokens for a given task.

    TODO: Implement the logic matching industry best practices:
    - code_generation, math, classification -> temperature 0.0
    - creative_writing, brainstorming -> temperature 0.9
    """
    task = task_type.lower().strip()

    if task in ["code_generation", "math", "classification"]:
        # TODO 1: Set deterministic parameters
        return {"temperature": 0.0, "max_output_tokens": 256}
    elif task in ["creative_writing", "brainstorming"]:
        # TODO 2: Set creative parameters
        return {"temperature": 0.9, "max_output_tokens": 512}
    else:
        # Default balanced setting
        return {"temperature": 0.5, "max_output_tokens": 300}

if __name__ == "__main__":
    tasks = ["code_generation", "creative_writing", "classification"]
    for t in tasks:
        params = get_generation_parameters(t)
        print(f"Task: {t:20} -> Temp: {params['temperature']}, Max Tokens: {params['max_output_tokens']}")
