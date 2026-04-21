# Exercise 1 — grade classifier 
# Write a function (you'll learn the def syntax tomorrow — for now just use a variable) that takes a marks
# value (0–100) and prints:
# A+ (≥90), A (80–89), B (70–79), C (60–69), D (50–59), Fail (<50).
# Handle invalid input: if marks < 0 or > 100, print "Invalid input"

marks = int(input("Enter marks (0-100): "))
if marks < 0 or marks >100:
    print("Invalid input")
elif marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")


# Exercise 2 — router logic (30 min)
# Imagine you're building an agent that routes queries. Take a user question as a string. If it contains the
# word "math" or "calculate", print "Route: calculator tool". If it contains "search" or "latest", print "Route:
# web search tool". If it contains "explain" or "what is", print "Route: LLM direct". Otherwise print "Route:
# default".
# This is the exact pattern inside every agent router.



query = input("Enter your query: ").lower()

if "math" in query or "calculate" in query:
    print("Route: calculator tool")
elif "search" in query or "latest" in query:
    print("Route: web search tool")
elif "explain" in query or "what is" in query:
    print("Route: LLM direct")
else:
    print("Route: default")


# Exercise 3 — input validation (15 min)
# Ask the user to enter an age using input(). If they enter a non-number, print "Please enter a
# number". If age is negative or > 150, print "Unrealistic age". Otherwise print age category (child / teen /
# adult / senior). Hint: use .isdigit() to check if a string is a number.

age_input = input("Enter your age: ")
if not age_input.isdigit():
    print("Please enter a number")
else:
    age = int(age_input)
    if age < 0 or age > 150:
        print("Unrealistic age")
    elif age < 13:
        print("Child")
    elif age < 20:
        print("Teen")
    elif age < 65:
        print("Adult")
    else:
        print("Senior")