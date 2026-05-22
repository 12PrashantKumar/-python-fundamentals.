import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_with_temperature(prompt: str, temp_value: float):
    # 1. Create the GenerateContentConfig object
    config = types.GenerateContentConfig(
        temperature=temp_value,
        max_output_tokens=200
    )
    
    # 2. Pass the config object to the API call
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config 
    )
    
    return response.text

if __name__ == "__main__":
    test_prompt = "Write a one-sentence marketing slogan for a new brand of ultra-strong coffee."
    
    print("---Temperature 0.0 (Deterministic / Strict) ---")
    print(generate_with_temperature(test_prompt, 0.0))
    
    print("\n---Temperature 0.7 (Balanced / Default) ---")
    print(generate_with_temperature(test_prompt, 0.7))
    
    print("\n--- Temperature 1.5 (Highly Random / Creative) ---")
    print(generate_with_temperature(test_prompt, 1.5))