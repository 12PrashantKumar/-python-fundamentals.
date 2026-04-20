# Exercise 1 — string warmup
'''Write a script that takes a full name (e.g., "prashant kumar sharma"), and prints:
1. the first name only
2. the last name only
3. the initials (P.K.S.)
4. the full name in Title Case
5. the full name reversed as a strin'''

name = "prashant kumar sharma"
first_name= name.split()
print(first_name[0])
last_name = name.split()
print(last_name[-1])

words = name.split()
initials = []
for word in words:
    initials.append(word[0].upper())

print(".".join(initials) + ".")



print(name.title())
print(name[::-1])


# Exercise 2 — student dictionary
'''Create a dict representing a student with: name, age, college, and a nested dict of marks (3 subjects:
math, english, cs). Then:
1. Print the student's name and age
2. Print only the math marks
3. Add a new subject (science) with a score
4. Update the english marks
5. Loop through all subjects and print "subject: marks" for each one'''


student = {"name" :"Prashant","age":21,"college": "GLA University","marks":{"math":88,"english":92,"cs":95}}
print(student["name"],student["age"])
print(student["marks"]["math"])
student["marks"]["science"] = 90
student["marks"]["english"] = 95
print(student)

for subject,marks in student["marks"].items():
    print(f"{subject} :{marks }")

    
# Exercise 3 — conversation history pattern 
'''Create a list called conversation. Append 4 dicts to it, each with the keys "role" (either "user" or
"assistant") and "content" (the message). Then loop through the list and print each message in format:
"[role]: content"'''

conversation = [
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user", "content": "What is the largest planet in our solar system?"},
    {"role": "assistant", "content": "The largest planet in our solar system is Jupiter."}
]
for message in conversation:
    print(f"{message['role']}: {message['content']}")