import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# =====================================================================
# METHOD 1: FEW-SHOT PROMPTING (Standardizing Ticket Categorization)
# =====================================================================
FEW_SHOT_PROMPT = """
You are a backend database classifier. Categorize the difficulty of the input question into exactly one of three strings: [EASY, MEDIUM, HARD]. Do not return any prose, markdown formatting, or sentences.

Examples:
Q: What is 2+2?
Difficulty: EASY

Q: Solve for x: x^2 - 4 = 0
Difficulty: MEDIUM

Q: Derive the mathematical proof for the Pythagorean theorem.
Difficulty: HARD

Now classify this target:
Q: Calculate the derivative of f(x) = 3x^2 + 5x - 2
Difficulty:"""

def classify_ticket():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=FEW_SHOT_PROMPT
    )
    print("--- Few-Shot Structural Output ---")
    print(f"Classification Result: {response.text.strip()}\n")


# =====================================================================
# METHOD 2: CHAIN-OF-THOUGHT (Complex Train Physics Problem)
# =====================================================================
COT_PROMPT = """
Two trains, A and B, are 420 km apart. Train A leaves Mumbai at 3:00 PM travelling east at 60 km/h. 
Train B leaves Delhi at 5:00 PM travelling west towards Mumbai at 80 km/h. 
At what exact time will the two trains pass each other?

Let's think step by step:
1. Establish the state of the system at 5:00 PM (when both trains are finally moving).
2. Calculate the remaining distance between them at 5:00 PM.
3. Determine their relative closing speed.
4. Solve for time elapsed after 5:00 PM and calculate the final clock time.
"""

def solve_complex_problem():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=COT_PROMPT
    )
    print("--- Chain-of-Thought Reasoning Output ---")
    print(response.text)


if __name__ == "__main__":
    classify_ticket()
    print("=" * 60 + "\n")
    solve_complex_problem()