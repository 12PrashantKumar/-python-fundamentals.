# Exercise 2 — read + write text files 
# Create a file notes.txt manually with 5 lines of text. Write a Python script that:
# 1. Reads the file and prints each line with a line number
# 2. Writes a new file notes_upper.txt with all text in uppercase
# 3. Writes a new file notes_count.txt containing only the word count
# 
# 1. Reads the file and prints each line with a line number
# with open("notes.txt", 'r') as f:
#     lines = f.readlines()
# for i, line in enumerate(lines,start=1):
#     print(f"{i} :{line.strip()}")

# 2. Writes a new file notes_upper.txt with all text in uppercase
# with open("notes_upper.txt", 'w') as f:
#     with open("notes.txt", 'r') as f_read:
#         lines = f_read.readlines()
#         for line in lines:
#             f.write(line.upper())

'''3. Writes a new file notes_count.txt containing only the word count'''
# with open("notes_count.txt", 'w') as f:
#     with open("notes.txt", 'r') as f_read:
#         text = f_read.read()
#         word_count = len(text.split())
#         f.write(f"word count:{word_count}")
       


# Exercise 3 — JSON save and load  
# Take the conversation list from Day 3 (list of dicts with role + content). Save it to chat_log.json
# using json.dump(). Then write a second script that loads the JSON back into a list using
# json.load() and prints each message.
'''import json


with open("chat_log.json", 'w') as f:
        conversation = [
            {"role": "user", "content": "Hello!"},
            {"role": "assistant", "content": "Hi there! How can I assist you today?"},
            {"role": "user", "content": "Can you tell me a joke?"},
            {"role": "assistant", "content": "Sure! Why don't scientists trust atoms? Because they make up everything!"}
        ]
        json.dump(conversation,f,indent=4)

with open("chat_log.json", 'r') as f:
    chat_log = json.load(f)


for message in chat_log:
      print(f"{message['role']}: {message['content']}")
      '''


    #   Exercise 4 — requests library first touch 
#     Install requests (already did above). Write 5 lines of code that fetch
# https://api.github.com/users/torvalds and print the response JSON
import requests
response = requests.get("https://api.github.com/users/12PrashantKumar")
print(response.json())
print(response.status_code)
print(response.headers['Content-Type'])
data = response.json()
print(data.keys())
print(data['name'])