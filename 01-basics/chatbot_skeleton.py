# Exercise 1 — agent loop skeleton 
conversation = []
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bye!")
        break
    conversation.append({"role": "user", "content": user_input})
    print(f"AI: (not implemented yet) you asked: {user_input}")
    conversation.append({"role": "assistant", "content": "placeholder"})
print(f"\nTotal messages: {len(conversation)}")