import os
from dotenv import load_dotenv  # Load environment variables from .env file
from google import genai

load_dotenv()  # Load environment variables from .env file

client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model = "gemini-2.5-flash",
)

print("Chatbot v3 - I remember what we talked about. Type 'quit' to exit.")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    if not user_input:
        print("Please enter a message.")
        continue

    try:
        response = chat.send_message(user_input)        
        print(f"AI: {response.text}")
    except Exception as e:
        print(f"Something went wrong: {e} -- please try again.")

print(f"\nTotal exchanges: {len(chat.get_history()) // 2}")


