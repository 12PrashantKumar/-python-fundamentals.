import os
import json
from dotenv import load_dotenv  # Load environment variables from .env file
from google import genai
from google.genai import types

load_dotenv()  # Load environment variables from .env file

client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))


# 1. Define your system prompt at the top of your file (below imports)
SYSTEM_PROMPT_TUTOR = """
You are a patient, friendly tutor for Indian government exam aspirants
preparing for SSC CGL, UPSC, and similar exams.

Your Style:
- Explain concepts in simple language a 12th-pass student understands
- Use Indian context examples (Mumbai trains, Delhi metro, Indian rupees)
- Keep answers under 100 words unless explanation needs more
- After answering, suggest one related practice question
- Encourage learning, never make them feel bad for not knowing something. Always be supportive!
"""


def generate_response(user_message, chat_history):
    """
    Takes the current manual history and the new user message,
    sends the combined payload to the API, and returns the text.
    """
    # Create a temporary array for the API call that includes the new message
    messages_for_api = chat_history + [
        types.Content(
            role = "user",
            parts=[types.Part.from_text(text=user_message)]
        )
    ]
    # 2. Update your generate_response function to use Config
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT_TUTOR
    )

    # Call the stateless endpoint using the new SDK
    response = client.models.generate_content_stream(
        model = "gemini-2.5-flash",
        contents= messages_for_api,
        config=config

    )
    full_response = ""

    for chunk in response:
        if chunk.text:
            print(chunk.text,end="",flush=True)  # Print each chunk as it arrivesh

            full_response += chunk.text

    return full_response




def main():
    chat_history = []  # This will store the entire conversation history
    print("Chatbot v4 - I remember what we talked about. Type 'quit' to exit.")
    while True:
        try:
            user_message = input("You: ").strip()

            if user_message.lower() == "quit":
                # The new SDK uses specific Python objects (types.Content) 
                # We need to convert them to standard dictionaries so json.dump can save them
                serializable_history = []
                for content in chat_history:
                    serializable_history.append({
                    "role":content.role,
                    "parts":content.parts[0].text 
                    })
                
                with open("chat_history.json","w") as f:
                    json.dump(serializable_history, f, indent= 2)
                    print("goodbye!")
                    break

            if not user_message:
                continue

            # Generate the AI response using the combined history   
            # ai_response = generate_response(user_message, chat_history)

            # print(f"AI: {ai_response }")
            print("AI: ", end="", flush=True)
            ai_response = generate_response(user_message, chat_history)
            print()  # move to next line after streami

            # Update the manual history with the new user message and AI response
            chat_history.append(types.Content(role="user",parts=[types.Part.from_text(text=user_message)]))
            chat_history.append(types.Content(role="model",parts=[types.Part.from_text(text=ai_response)]))

        except Exception as e:
            print(f"Something went wrong: {e} -- please try again.")


if __name__ == "__main__":
    main()