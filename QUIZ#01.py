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
    print(f"{integer_3} is the maximum number out of all integers.")

# OUTPUT:
# Integer #1: 50
# Integer #2: 80
# Integer #3: -85
# 80 is the maximum number out of all integers.
# -----------------------------------------------------

# QUESTION - 02:
# Write a program to calculate Area of Circle by taking radius as input.

# SOLUTION:
radius = int(input("Radius of Circle: "))
if Area == radius ** 2:
    print(f"Area = {Area * 3.14}㎠")

# OUTPUT:
# Radius of Circle: 9
# Area = 254.34㎠
# -----------------------------------------------------

# QUESTION - 03:
# Write a program to calculate percentage of total marks obtained in final term for a student.

# SOLUTION:
total_marks = 75
percentage = total_marks % 100
print(f"Percentage of total marks obtained = {percentage}%")

# OUTPUT:
# Percentage of total marks obtained = 75%
# -----------------------------------------------------

# QUESTION - 04:
# Write a program to print whether the user defined number is a prime number 
# or not with proper message.

# SOLUTION:
number = int(input("Enter the number: "))
if number >= 1:
    for counter in range(2, number):
        if (number % i) == 0:
            print(f"{number} is not a prime number")
            print(f"Because {i} multiply by {number/i} = {number}.")
            break
    else:
        print(number, "is a prime number")
        print(f"Because {number} is divisible only by itself and 1.")

# OUTPUT:
# 11 is a prime number
# Because 11 is divisible only by itself and 1.
# 8 is not a prime number
# Because 2 multiply by 4.0 = 8.
# -----------------------------------------------------

# QUESTION - 05:
# Write a Python program to check whether an alphabet is a vowel or consonant.

# SOLUTION:
alphabet = input("Enter the Alphabet: ")
vowels = "a" or "e" or "i" or "o" or "u"
if alphabet == vowels:
    print(f"{alphabet} is Vowel.")
else:
    print(f"{alphabet} is Consonant.")

# OUTPUT:
# a is Vowel.
# b is Consonant.
# -----------------------------------------------------

# QUESTION - 06:
# Write a Python program to sum up two user defined integers. However, if the sum is:

# Below Zero - Display "Bigger number was negative"
# Equal to ZERO - Display "Both numbers were equally distant on number line on opposite sides"
# Greater than ZERO - Display "Bigger number was positive"

# SOLUTION:
integer_1 = int(input("Integer #1: "))
integer_2 = int(input("Integer #2: "))
print(f"{integer_1} + {integer_2} = {integer_1 + integer_2 }")
if integer_1 + integer_2 < 0:
    print(f"Bigger number was negative.")
if integer_1 + integer_2 == 0:
    print(f"Both numbers were equally distant on number line on opposite sides.")
if integer_1 + integer_2 > 0:
    print(f"Bigger number was positive.")

# OUTPUT:
# Integer #1: -5
# Integer #2: 9
# -5 + 9 = 4
# Bigger number was positive.

# Integer #1: -50
# Integer #2: 8
# -50 + 8 = -42
# Bigger number was negative.
# -----------------------------------------------------

# QUESTION - 07:
# Write a Python program to check whether
# two user defined integers are additive inverse of each other.

# SOLUTION:
integer_1 = int(input("Integer #1: "))
integer_2 = int(input("Integer #2: "))
if integer_1 + integer_2 == 0:
    print(f"{integer_1} and {integer_2} are additive inverse of each other.")
else:
    print(f"{integer_1} and {integer_2} are NOT additive inverse of each other.")

# OUTPUT:
# Integer #1: 4
# Integer #2: -4
# 4 and -4 are additive inverse of each other.

# Integer #1: 9
# Integer #2: 9
# 9 and 9 are NOT additive inverse of each other.
# -----------------------------------------------------

# QUESTION - 08:
# Write a Python program to check whether 
# two user defined integers are multiplicative inverse of each other.
# SOLUTION:
integer_1 = int(input("Integer #1: "))
integer_2 = int(input("Integer #2: "))
if integer_1 * integer_2 == 1:
    print(f"{integer_1} and {integer_2} are multiplicative inverse of each other.")
else:
    print(f"{integer_1} and {integer_2} are NOT multiplicative inverse of each other.")
# -----------------------------------------------------

# QUESTION - 09:
# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# All triangles have three sides.
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

# SOLUTION:
side_1 = 50
side_2 = 55
side_3 = 50

if side_1 == side_2 and side_3:
    print(f"It is an Equilateral triangle because all three sides are equal.")
if side_1 == side_2 or side_3:
    print(f"It is an Isosceles triangle because two sides are equal.")
else:
    print(f"It is a scalene triangle because all three sides are unequal.")

# OUTPUT:
# It is an Isosceles triangle because two sides are equal.
# -----------------------------------------------------

# QUESTION - 10:
# Write a Python program to print user defined multiplication table 
# and also reverse the table.

# SOLUTION:
# user defined multiplication table:
Muliplication_table = int(input("Enter your multiplication table : "))
for counter in range (1, 11):
    print(f"{Muliplication_table} x {counter} = {Muliplication_table * counter}")

# OUTPUT:
# Enter your multiplication table : 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60

# reverse multiplication table:
for counter in range (10, 0, -1):
    print(f"{Muliplication_table} x {counter} = {Muliplication_table * counter}")

# OUTPUT:
# 6 x 10 = 60
# 6 x 9 = 54
# 6 x 8 = 48
# 6 x 7 = 42
# 6 x 6 = 36
# 6 x 5 = 30
# 6 x 4 = 24
# 6 x 3 = 18
# 6 x 2 = 12
# 6 x 1 = 6
