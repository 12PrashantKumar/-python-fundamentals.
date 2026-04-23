# def square(n):
#     return n*n

# x = square(5)
# print(x)

# def is_even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
# x= is_even(67)
# print(x)



# def fullName(first, last):
#     return (first+ " " + last).title()
# x= fullName("Prashant" , "Kumar")
# print(x)

# Exercise 1 — your first reusable function 
# Write a function ask_question(question_text). It takes a string, prints Q: {question_text},
# and returns the string "A: (placeholder answer)". Call it 3 times with different questions. Print
# each return value.
# def ask_Question(question_text):
#     print(f"Q:{question_text}")
#     return "A: (placeholder answer)"
# questions = ["What is Python?", "What is ML?", "What is RAG?"]
# for question in questions:
#     answer = ask_Question(question)
#     print(answer)

#     Exercise 2 — multiple parameters + defaults (
# Write format_message(role, content, tag="[INFO]") that returns a formatted string like
# "[INFO] user: hello". Call it with all 3 args, then with just 2 args (let tag use the default). Verify
# both work
# def format_message(role, content, tag="[INFO]"):
#     return f"{tag} {role}: {content}"
# message = format_message("user","ask question","[chat]")
# message = format_message("user","ask question",)
# print(message)

# Exercise 3 — functions calling functions 
# Build these 3 functions that call each other:
# 1. validate_input(text) — returns True if text is not empty and longer than 2 chars, else returns
# False.
# 2. process_question(text) — calls validate_input(). If invalid, returns "Error: question too short".
# Else returns "Processing: {text}".
# 3. main() — calls process_question() with 3 different inputs (one invalid, two valid) and prints each
# result
# def validate_input(text):
#     return len(text) > 2

# def process_question(text):
#     if not validate_input(text):
#         return "Error:question too short"
#     else:
#         return f"Processing: {text}"
    

# def main():
#     inputs = ["Hi", "what is python?", "What is ML?"]
#     for text in inputs:
#         result  = process_question(text)
#         print(result)
# main()


