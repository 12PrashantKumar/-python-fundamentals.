import os
from google import genai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


# configure genai client with API key from .env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



# Start chat session (THIS HOLDS MEMORY)

chat = client.chats.create(
    model = "gemini-2.5-flash",
    history = []
)


def main():
    print("Chatbot v3 -- type 'quit' to exit")
    while True:
        try:
            user_message = input("You: ").strip()

            # skip empty messages
            if not user_message:
                print("Please enter a message.")
                continue

            # Exit condition
            if user_message.lower() == "quit":
                print("Bye!")
                break

            # Send user message to chat session and get response

            response = chat.send_message(user_message)
            print(f"AI: {response.text}")

        except Exception as e:
            print(f"Something went wrong: {e} -- please try again.")

if __name__ == "__main__":
    main()






