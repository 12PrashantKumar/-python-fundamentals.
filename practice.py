
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")

print("User: Hello, who are you?")
response = chat.send_message("Hello, who are you?")
print("Bot:", response.text.strip())
print("-" * 20)