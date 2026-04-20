# Student Marks System
Marks = [85, 90, 78, 92, 88]
total_Marks = sum(Marks)
avg_marks = total_Marks /len(Marks)
highest_Marks = max(Marks)
Lowest_Marks = min(Marks)
print(f"Total Marks: {total_Marks} Average Marks: {avg_marks} Highest Marks: {highest_Marks} Lowest Marks: {Lowest_Marks}")


# Even-Odd Separator
lst = [1, 2, 3, 4, 5]
even_numbers = []
odd_numbers = []
for i in lst:
    if i %2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(f"Even numbers: {even_numbers} Odd numbers:{odd_numbers }")

# Reverse a list WITHOUT using .reverse()
lst = [1, 2, 3, 4, 5]
reversed_lst = lst[::-1]
print(reversed_lst)    