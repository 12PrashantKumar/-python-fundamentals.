import os
import json
from datetime import datetime  # Added for the /save timestamp feature
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv() 

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(user_message, chat_history):
    messages_for_api = chat_history + [
        types.Content(role="user", parts=[types.Part.from_text(text=user_message)])
    ]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages_for_api
    )
    return response.text

def count_tokens_rough(history):
    """Quick heuristic: 1 token ~= 4 characters in English."""
    if not history:
        return 0
    total = " ".join([content.parts[0].text for content in history])
    return len(total) // 4

def main():
    chat_history = [] 
    print("Chatbot v4 (With System Commands) - Type '/help' to see options.\n")
    
    while True:
        try:
            # Show token tracking at the start of every turn
            print(f"[debug] Memory tokens: {count_tokens_rough(chat_history)}")
            user_message = input("You: ").strip()

            if not user_message:
                continue

            # ==========================================
            # 🎛️ CONTROL PLANE: INTERCEPT COMMANDS HERE
            # ==========================================
            
            # Command 1: Help Menu
            if user_message.lower() in ("/help", "/?"):
                print("\n Available Commands:")
                print("  /help   - Show this command list")
                print("  /reset  - Wipe conversation memory (Amnesia)")
                print("  /save   - Save conversation history to a file without exiting")
                print("  quit    - Save history and exit program\n")
                continue  # Skip talking to the AI, ask for input again

            # Command 2: Reset Memory
            if user_message.lower() == "/reset":
                chat_history = []
                print("\n Memory wiped clean! Fresh start.\n")
                continue

            # Command 3: Snapshot Save
            if user_message.lower() == "/save":
                if not chat_history:
                    print("\n History is empty. Nothing to save yet.\n")
                    continue
                
                # Convert the objects so they can be JSON serialized
                serializable_history = [
                    {"role": c.role, "parts": c.parts[0].text} for c in chat_history
                ]
                
                # Generate a unique name using a 2026 timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"chat_snapshot_{timestamp}.json"
                
                with open(filename, "w") as f:
                    json.dump(serializable_history, f, indent=2)
                print(f"\n Snapshot saved successfully to '{filename}'!\n")
                continue

            # Command 4: Quit
            if user_message.lower() == "quit":
                if chat_history:
                    serializable_history = [
                        {"role": c.role, "parts": c.parts[0].text} for c in chat_history
                    ]
                    with open("chat_history2.json", "w") as f:
                        json.dump(serializable_history, f, indent=2)
                    print("\nBye! Final conversation saved to chat_history.json")
                else:
                    print("\nBye!")
                break

            # ==========================================
            # 💬 DATA PLANE: PASS TO LLM INFERENCE
            # ==========================================
            ai_response = generate_response(user_message, chat_history)
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