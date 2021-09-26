# Problem 1:
# Create a program that will allow people over 18 and below 30 to watch IRON MAN 3.
# Solution:
age = 20

if age >= 18 and age <= 30:
    print(f"Allowed to watch IRON MAN 3")
# Allowed to watch IRON MAN 3

age = 18

if age >= 18 and age <= 30:
    print(f"Allowed to watch IRON MAN 3")
# Allowed to watch IRON MAN 3


# Problem 2:
# Create a program that will allow people over 4 and below 25 or above 50 and below 60 to watch cartoons.
# Solution:
age = 7

if age >= 4 and age <= 25:
    print(f"Allowed to watch cartoons")
# Allowed to watch cartoons


age = 53

if age >= 50 and age <= 60:
    print(f"Allowed to watch cartoons")
# Allowed to watch cartoons


# Problem 3:
# Suppose that you are a teacher, and you have make a list of all the students who scored above 60% and below 70% marks and those who scored above 90% in the examination.
# Solution:
student_1 = marks = 75

if marks >= 60 and marks <= 70:
    print(f"B+")

elif marks >= 90:
    print(f"A+")
# B+


student_2 = marks = 90

if marks >= 60 and marks <= 70:
    print(f"B+")


elif marks >= 90:
    print(f"A+")
# A+