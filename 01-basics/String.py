print("Hello, World!")
name = "Alice"
greeting = "HEllo"+name
print(greeting)
# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
# String repetition
echo = "Echo! " * 3
print(echo)
# String indexing
word = "Python"
print(word[0]) 
# print(word[1]) = "y"
# print(word[2]) = "t"
# print(word[3]) = "h"
# print(word[4]) = "o"
# print(word[5]) = "n"

# String slicing
print(word[0:3])
# String length
print(len(word))
text = "telusko"
print(text[-6:6])

name = input("Enter your name")
age = int(input("Enter your age"))
if age < 0:
    print("Invalid input")
else:
    print(f"Hello {name.upper()}, you are (age) years old")
   


#    String Analyzer (VERY IMPORTANT)
text = input("enter a string")
total_char = len(text)
alphabet = 0
digits = 0
for ch in text:
    if ch.isalpha():
        alpahbet += 1
    elif ch.isdigit():
        digits += 1

print(f"Total characters: {total_char}")
print(f"Alphabets: {alphabet}")
print(f"Digits: {digits}")


# Email Validator (Real-world thinking)

email = input("enter uyour email")
if "@" in email and "com" in email:
    print("valid email")
else:
    print("invalid email")
