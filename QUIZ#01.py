# QUESTION - 01:
# Write a program that will take three integers as user defined inputs
# and prints the maximum number out of them.

# SOLUTION:
integer_1 = input("Integer #1: ")
integer_2 = input("Integer #2: ")
integer_3 = input("Integer #3: ")

if integer_1 > integer_2 and integer_3:
    print(f"Integer #1 = {integer_1} is the maximum number out of all integers.")
if integer_2 > integer_1 and integer_3:
    print(f"Integer #2 = {integer_2} is the maximum number out of all integers.")
if integer_3 > integer_2 and integer_1:
    print(f"Integer #3 = {integer_3} is the maximum number out of all integers.")

# OUTPUT:
# Integer #1: 50
# Integer #2: 80
# Integer #3: -85
# Integer #2 = 80 is the maximum number out of all integers.

# -----------------------------------------------------

# QUESTION - 02:
# Write a program to calculate Area of Circle by taking radius as input.

# SOLUTION:
# A= πr²
radius = int(input("Radius of Circle: "))
Area = radius ** 2
if Area == radius ** 2:
    print(f"Area = {Area * 3.14}㎠")

# OUTPUT:
# Radius of Circle: 9
# Area = 254.34㎠

# -----------------------------------------------------

# QUESTION - 03:
# Write a program to calculate percentage of total marks obtained in final term for a student.

# SOLUTION:
