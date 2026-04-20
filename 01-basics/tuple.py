# Task 1: Student Profile System
person = ('Prashant',21,'Python Developer','India')
name,age,profession,country = person
print(name)
print(age)
print(profession)
print(country)


# Task 2: Swap Values using Tuple
a = 10
b = 20
a,b = b,a
print("a =",a)
print("b =",b)

def calc(a,b):
    total= a+b
    product = a*b
    return total,product
total,product= calc(5,3)
print("Total:",total)
print("Product:",product)
