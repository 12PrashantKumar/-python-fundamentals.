# Remove duplicate names:
lst = ["ram", "shyam", "ram", "mohan", "shyam"]
print(set(lst))

python_students = {"Aman", "Riya", "Kunal"}
java_students = {"Riya", "Kunal", "Vikas"}
print(python_students.intersection(java_students    ))

all_numbers = {1,2,3,4,5,6,7,8,9,10}
present = {2,4,6,8,10}
print(all_numbers.difference(present))