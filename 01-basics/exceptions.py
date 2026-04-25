# try:
#     with open("text2.txt")as f:
#             content = f.read()
# # except FileNotFoundError:
# except FileNotFoundError as e:
#     # print("The file was not found.  Please check the file name and try again.")
#     print(e)
# else:
#     print(content)
# finally:
#     print("This block will always execute, regardless of whether an exception occurred or not.")

# Exercise 1 — read errors on purpose  
# Intentionally cause each of these errors in a single file. For each, read the traceback and write a
# one-line comment explaining what went wrong:
# 1. NameError — use a variable that doesn't exist
# 2. TypeError — add a string to an int
# 3. KeyError — access a dict key that doesn't exist
# 4. IndexError — access my_list[100] when the list has 3 items
# 5. ZeroDivisionError — divide by zero
# 6. FileNotFoundError — open a file that doesn't exist

# 1. NameError — use a variable that doesn't exist
# print(x)  # This will raise a NameError because 'x' is not defined.

# 2. TypeError — add a string to an int
# result = "the answer is" + 42  # This will raise a TypeError because you cannot concatenate a string and an integer.
# print(result)

# 3. KeyError — access a dict key that doesn't exist
# my_dict= {"name":"Prashant", "age":21}
# print(my_dict["marks"]) # This will raise a KeyError because the key 'marks' does not exist in the dictionary.

# 4. IndexError — access my_list[100] when the list has 3 items
# my_list = [1, 2, 3]
# print(my_list[100])  # This will raise an IndexError because there is no index 100 in the list, which only has 3 items.

# 5. ZeroDivisionError — divide by zero 
# result = 10 / 0  # This will raise a ZeroDivisionError because division by zero is undefined.
# print(result)

# 6. FileNotFoundError — open a file that doesn't exist
# with open("non_existent_file.txt") as f:  # This will raise a FileNotFoundError because the file does not exist.
#     content = f.read()
# print(content)

# Exercise 2 — wrap with try/except (
# Take the 6 errors from Exercise 1. Wrap each in a try/except block so that instead of crashing, the
# program prints a friendly message like "Oops: the key 'xyz' doesn't exist, please check."
# Use specific exception types, not a bare except:. A bare except will haunt you in debugging for
# years.
# 1. NameError — use a variable that doesn't exist
'''
try:
    print(x)  # This will raise a NameError because 'x' is not defined.     
except NameError as e:  
    print(f"Oops: {e}, please check the variable name.")

# 2. TypeError — add a string to an int
try:
    result = "the answer is" + 42  # This will raise a TypeError because you cannot concatenate a string and an integer.
    print(result)
except TypeError as e:  
    print(f"Oops: {e}, please check the types of the operands.")

# 3. KeyError — access a dict key that doesn't exist
my_dict= {"name":"Prashant", "age":21}  
try:
        print(my_dict["marks"]) # This will raise a KeyError because the key 'marks' does not exist in the dictionary.      
except KeyError as e:
    print(f"Oops: {e}, please check the dictionary keys.")  

# 4. IndexError — access my_list[100] when the list has 3 items
my_list = [1, 2, 3]
try:
    print(my_list[100])  # This will raise an IndexError because there is no index 100 in the list, which only has 3 items. 
except IndexError as e: 
    print(f"Oops: {e}, please check the list indices.") 
'''


# Exercise 3 — bulletproof input 
# Write a function get_integer_input(prompt) that asks the user for a number and keeps asking
# until they give a valid integer. If they enter "abc", it says "Not a number, try again" and asks again
'''
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)  # Try to convert the input to an integer
        except ValueError:  # If a ValueError occurs, it means the input was not a valid integer
            print("Not a number, try again.")  # Print an error message and continue the loop

# Example usage:
number = get_integer_input("Please enter an integer: ")
print(f"You entered:{number}")
'''


# Exercise 4 — resilient file reader 
# Write safe_read_file(path) that tries to read a file. If file doesn't exist → returns "File not found".
# If any other error → returns "Error reading file: {error message}". If success → returns the file content.
# You'll write this exact pattern for every file operation in your RAG system
def safe_read_file(path):
    try:
        with open(path, 'r') as file:  # Try to open the file for reading
            return file.read()  # If successful, return the file content
    except FileNotFoundError:  # If a FileNotFoundError occurs, it means the file does not exist
        return "File not found."
    except Exception as e:  # Catch any other exceptions that may occur
        return f"Error reading file: {e}"  # Return a message with the error details
    
# Example usage:
file_content = safe_read_file("text.txt")
print(file_content)
