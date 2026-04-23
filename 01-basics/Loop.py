# Exercise 1 — agent loop skeleton 
# conversation = []
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "quit":
#         print("Bye!")
#         break
#     conversation.append({"role": "user", "content": user_input})
#     print(f"AI: (not implemented yet) you asked: {user_input}")
#     conversation.append({"role": "assistant", "content": "placeholder"})
# print(f"\nTotal messages: {len(conversation)}")

# Exercise 2 — for loop with enumerate
# Given a list: questions = ["what is python", "what is ML", "what is RAG"]
# Use enumerate() to print each question as:
# Q1: what is python
# Q2: what is ML
# Q3: what is RAG
questions = ["what is python", "what is ML", "what is RAG"]
for index,question in enumerate(questions,start=1):
    print(f"Q{index}:{question}")

# Exercise 3 — nested loop, list of dicts 
# Create a list of 3 student dicts (each with name, marks_dict). Write a loop that prints each student's
# name, then a nested loop that prints each subject and mark indented beneath it. This is the exact
# pattern for displaying search results in a RAG system.
students = [
    {"name": "Alice", "marks_dict": {"math": 90, "english": 85}},
    {"name": "Bob", "marks_dict": {"math": 75, "english": 80}},
    {"name": "Charlie", "marks_dict": {"math": 60, "english": 70}}
]
for student in students:
    print(student["name"])
    for subject, mark in student["marks_dict"].items():
        print(f"  {subject}: {mark}")

