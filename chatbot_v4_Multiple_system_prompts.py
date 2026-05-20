import os
import json
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types

from Chatbot_systemCommands import count_tokens_rough

load_dotenv() 

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Define  dictionary of personalities
SYSTEM_PROMPTS = {
    "tutor": """You are a patient, friendly tutor for Indian government exam aspirants. 
                Explain simply, use Indian context examples (Rupees, Metro), and keep it under 100 words.""",
                
    "coder": """You are a senior Python engineer. Give concise, highly optimized code examples. 
                No fluff, just code and a 1-sentence explanation.""",
                
    "casual": """You are a sarcastic, funny chat companion. Be informal, crack jokes, 
                 and use emojis. Do not act like a corporate AI robot.""",
                 
    "strict": """You are a harsh code reviewer. Find every bug. Do not use flattery. 
                 Point out exactly why the user's code is terrible and how to fix it."""
}

# 2. Update the function to accept the active system prompt
def generate_response(user_message, chat_history, active_system_prompt):
    messages_for_api = chat_history + [
        types.Content(role="user", parts=[types.Part.from_text(text=user_message)])
    ]
    
    # Inject the chosen personality dynamically
    config = types.GenerateContentConfig(
        system_instruction=active_system_prompt
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages_for_api,
        config=config 
    )
    return response.text

def main():
    chat_history = [] 
    current_mode = "tutor" # Default personality
    
    
    
    while True:
        try:
           
            user_message = input("You: ").strip()

            if not user_message:
                continue

            # ==========================================
            #  CONTROL PLANE
            # ==========================================
            
            if user_message.lower() in ("/help", "/?"):
                print("\n Available Commands:")
                print("  /help        - Show this menu")
                print("  /mode [name] - Change AI personality (e.g., /mode strict)")
                print("  /modes       - List all available personalities")
                print("  /reset       - Wipe conversation memory")
                print("  /save        - Save history to file")
                print("  quit         - Exit program\n")
                continue 

            # NEW: List available modes
            if user_message.lower() == "/modes":
                print(f" Available Personas: {', '.join(SYSTEM_PROMPTS.keys())}\n")
                continue

            # NEW: Switch modes
            if user_message.lower().startswith("/mode "):
                # Extract the word typed after "/mode "
                new_mode = user_message.split()[1].lower() 
                
                if new_mode in SYSTEM_PROMPTS:
                    current_mode = new_mode
                    chat_history = []  # CRITICAL: Wipe memory to prevent persona contamination!
                    print(f"\n🔄 Switched to {new_mode.upper()} mode. Memory wiped.\n")
                else:
                    print(f"\n❌ Unknown mode. Options: {', '.join(SYSTEM_PROMPTS.keys())}\n")
                continue

            # ... (Keep your old /reset, /save, and quit commands exactly as they were here) ...
            if user_message.lower() == "/reset":
                chat_history = []
                print("\n🧠 Memory wiped clean! Fresh start.\n")
                continue

            if user_message.lower() == "quit":
                print("\nGoodbye!")
                break

            # ==========================================
            # 💬 DATA PLANE
            # ==========================================
            # 3. Pass the active system prompt string to the generator
            active_prompt_text = SYSTEM_PROMPTS[current_mode]
            
            ai_response = generate_response(user_message, chat_history, active_prompt_text)
            print(f"AI: {ai_response}\n")

            chat_history.append(
                types.Content(role="user", parts=[types.Part.from_text(text=user_message)])
            )
            chat_history.append(
                types.Content(role="model", parts=[types.Part.from_text(text=ai_response)])
            )

        except Exception as e:
            print(f"Something went wrong: {e} -- please try again.")

if __name__ == "__main__":
    main()