import os
import time
import json
from datetime import datetime
from dotenv import Load_dotenv, load_dotenv
from google import genai
from google.genai import types

load_dotenv()   

client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

# ====================================================================
# FINOPS: 2026 Gemini 2.5 FLash Pricing
# ====================================================================
INPUT_COST_PER_MILLION_TOKENS = 0.30(dollars)
OUTPUT_COST_PER_MILLION_TOKENS = 2.5(dollars)
total_session_cost = 0.0

def estimate_cost(input_tokens,output_tokens):
    input_cost = (input_tokens/1_000_000) * INPUT_COST_PER_MILLION_TOKENS
    output_cost = (output_tokens/1_000_000) * OUTPUT_COST_PER_MILLION_TOKENS
    return input_cost + output_cost


# ====================================================================
# DEFENSE : Input Edge Validation and Retry Logic
# ====================================================================
def validation_user_input(text):
    """ Returns (is_valid, error_message)"""
    if not text:
        return False, "Input cannot be empty."
    if len(text) <2:
        return False, "Input must be at least 2 characters long."
    if len(text) >5000:
        return False, "Input exceeds maximum length of 5000 characters."
    

    # Heuristic injection block
    suspicious_keywords = suspicious = ["ignore previous instructions", "system prompt", "forget all instructions"]
    text  = text.lower()
    for keyword in suspicious_keywords:
        if keyword in text:
            return False, f"Input contains suspicious keyword: '{keyword}'"
        
    return True, None



# ====================================================================
# Resilience: Exponential Backoff Retry Logic
# ====================================================================

def generate_with_retries(messages_for_api,max_retries =3):
    """Handles API execution with retries and  mathematical exponential backoff   """
    global total_session_cost
    delay = 1  # Initial delay in seconds

    for attempt in range(max_retries):
        try:
            # Make the API call
            response = client.models.generate_content(
                model = "gemini-2.5-flash",
                contents = messages_for_api
            )

            # Estimate cost for this API call
            usage = response.usage_metadata
            if usage:
                input_tokens = usage.prompt_token_count
                output_tokens = usage.completion_token_count
                cost = estimate_cost(input_tokens,output_tokens )
                total_session_cost += cost
                print(f"API Call Success: Input Tokens={input_tokens}, Output Tokens={output_tokens}, Cost=${cost:.6f}")
            
            return response.text
        except Exception as e:
            # 429 = Rate Limit | 504 = Timeout | 500/503 = Google Server Issue
            if e.code in [429, 500, 503, 504]:
                print(f"API Call Failed (Attempt {attempt +1}/{max_retries}): {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *=2 # Exponential backoff


            # 400 = Bad Request | 403 = Forbidden (Bad API Key)
            elif e.code in [400,403]:
                print(f"API Call Failed with unrecoverable error: {e}. No more retries.")
                return None
            else:
                print(f"API Call Failed with unexpected error: {e}. No more retries.")
                return None
        except Exception as e:
            print(f"  [Unexpected Local Error]: {e}")
            return None
        
    print(f"API Call Failed after {max_retries} attempts. Please try again later.")
    return None

# ====================================================================
# Main loop
# ====================================================================

def main():
    chat_history = []

    while True:
        try:
            user_message = input("You: ").strip()

            # 1. Edge Validation (Fails fast before checking commands)
            is_valid, error_message = validation_user_input(user_message)
            if not is_valid:
                print(f"Input Validation Error: {error_message}")
                continue

            # 2. Control Plane (Commands)
            if user_message.lower() in ("/help", "/?"):
                print("\n🛠️ Commands: /help, /reset, /save, quit\n")
                continue

            if user_message.lower() == "/reset":
                chat_history.clear()
                print("Chat history cleared. Starting fresh!")
                continue

            if user_message.lower() == "/save":
                if chat_history:
                    serializable = [{"role": c.role, "parts": c.parts[0].text} for c in chat_history]
                    filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    with open(filename, "w") as f:
                        json.dump(serializable, f, indent=2)
                    print(f"Chat history saved to {filename}")
                else:
                    print("No chat history to save.")
                continue
            if user_message.lower() in ("quit", "exit"):
                print("Exiting chat. Goodbye!")
                break

            # 3. Data Plane (Build array and call API)

            messages_for_api = chat_history + [
                types.Content(
                    role = "user",
                    parts = [types.Part.from_text(text = user_message)]
                )
            ]

            ai_response = generate_with_retries(messages_for_api)

            if ai_response:
                print(f"AI: {ai_response}")
                chat_history.append(types.Content(
                    role = "user",
                    parts = [types.Part.from_text(text = user_message)]
                ))
                chat_history.append(types.Content(
                    role = "assistant",
                    parts = [types.Part.from_text(text = ai_response)]
                ))

        except Exception as e:
            print(f"  [Unexpected Local Error in main loop]: {e}")

if __name__ == "__main__":
    main()







                                        
