# What it does:
# 1. Loops forever asking the user a question
# 2. If user types quit → save conversation to chat_log.json and exit
# 3. Otherwise, calls generate_response(user_msg, history) which returns "(placeholder) you
# asked: {user_msg}"
# 4. Appends both user msg and response to a conversation list (list of dicts with role + content)
# 5. If anything errors at any point → catches it, prints "Something went wrong: {error}", continues the
# loop instead of crashing
# 6. On exit, also prints total message count

import json


def generate_response(user_message,history):
    return f"(placeholder responds to {user_message} with {len(history)} message in history )"

def save_conversation(conversation, filename="chat_log.json"):
    with open(filename, "w") as f:
        json.dump(conversation, f,indent=4)

def main():
    conversation = []
    print("Chatbot v1 --type 'quit' to exit")
    while True:
        try:
            user_message = input("You: ")
            if user_message.lower() == "quit":
                # print("Bye!")
                save_conversation(conversation)
                break
            conversation.append({"role": "user", "content": user_message})
            response = generate_response(user_message, conversation)
            conversation.append({"role": "assistant", "content": response})
            print(f"AI: {response}")
        except Exception as e:
            print(f"Something went wrong: {e} -- please try again.")
    # print(f"\nTotal messages: {len(conversation)}")



if __name__ == "__main__":

    main()