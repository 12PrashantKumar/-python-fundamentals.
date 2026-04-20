


student = {'name': 'Prashant', 'age': 21, 'course': 'python', 'marks': 88}
print(student)

student['marks'] = 95
print(student)

username = input("Enter your username: ")
password = input("Enter your password: ")
user_info = {"username": username, "password": password}
# user_info = {'username': username, 'password': password}
users = {
   "username": "1234",
   "password": "pass123"
}
if user_info['username'] == users['username'] and user_info['password'] == users['password']:
    print("Login successful!")
else:
    print("Invalid username or password.") 


products = {
   "laptop": 50000,
   "mouse": 500,
   "keyboard": 1200
}
print(products)
print(max(products,key=products.get))
print(len(products))


for key,values in student.items():
    print(f"{key} :{values}")