# Exercise 1 — agent loop skeleton 
conversation = []
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bye!")
        break
    conversation.append(
        {
        "role": "user",
          "content": user_input}
          )
    print(f"AI: (not implemented yet) you asked: {user_input}")
    conversation.append(
        {
        "role": "assistant", 
        "content": "placeholder"}
        )
print(f"\nTotal messages: {len(conversation)}")

# Exercise 4 — upgrade your chatbot skeleton
# Open the chatbot_skeleton.py you wrote on Day 3. Refactor it: move the "generate response"
# logic into a function called generate_response(user_message, history) that takes the user
# message and conversation history, and returns a placeholder string. The main loop should now call
# this function instead of having the logic inline
 
def generate_response(user_message, history):
    return f"(placeholder reponse to '{user_message}' with {len(history)} messages in history  )"

conversation = []
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bye!")
        break
    conversation.ap
    pend({"role": "user", "content": user_input})
    response = generate_response(user_input, conversation)
    print(f"AI: {response}")
    conversation.append({"role": "assistant", "content": response})
print(f"\nTotal messages: {len(conversation)}")