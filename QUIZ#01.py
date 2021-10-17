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
    for i in range(2, number):
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

# QUESTION - 04:
# Write a Python program to sum up two user defined integers. However, if the sum is:

# Below Zero - Display "Bigger number was negative"
# Equal to ZERO - Display "Both numbers were equally distant on number line on opposite sides"
# Greater than ZERO - Display "Bigger number was positive"

# SOLUTION:
integer_1 = input("Integer #1: ")
integer_2 = input("Integer #2: ")