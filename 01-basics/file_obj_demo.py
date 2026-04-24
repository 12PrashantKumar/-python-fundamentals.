#file object
# with open("text.txt", 'r') as f:
    # print(f) # <_io.TextIOWrapper name='text.txt' mode='r' encoding='UTF-8'>, a file object
    # print(f.read()) # read the whole file as a string
    # print(f.readline()) # read one line at a time, returns a string with a newline character at the end

    # print(f.readline(), end= '') # read the next line
    # print(f.readline(),end= '') # read the next line, returns empty string if end of file is reached

    # for line in f:
    #     print(line, end= '') # read line by line, end='' to avoid adding extra newline character


# import os
# print(os.getcwd()) # get current working directory

# with open("test2.txt",'w') as f:
#     f.write("This is a test file.\n")
#     f.write("This file is created using Python.\n")
#     f.seek(0) # move the file pointer to the beginning of the file
#     f.write("This file is created using Python.\n")

import json
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science"],
    "is_graduated": False
}
# with open("student.json",'w') as f:
#     json.dump(student,f,indent = 4) # write the student dictionary to a json file
with open("student.json",'r') as f:
    data  = json.load(f) # read the json file and convert it to a dictionary
print(data)
print(data['name']) # access the name key in the dictionary
print(data['courses'][0]) # access the first course in the courses list


import math
print(math.sqrt(81))


