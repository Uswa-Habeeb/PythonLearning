# PROBLEM 1:
# Create a program that will allow people over 18 and below 30 to watch IRON MAN 3.
# SOLUTION:

age = 20

if age >= 18 and age <= 30:
    print(f"Allowed to watch IRON MAN 3.")

elif age <= 18 or age >= 30:
    print(f"Not Allowed to watch IRON MAN 3.")
# Allowed to watch IRON MAN 3.
# REASON:
# Because age = 20, 20 is greater than 18 and less than 30, both inputs are true and as we know in (AND) result is true when both inputs are true otherwise false.
# So, the results will be (Allowed to watch IRON MAN 3.)


age = 40

if age >= 18 and age <= 30:
    print(f"Allowed to watch IRON MAN 3.")

elif age <= 18 or age >= 30:
    print(f"Not Allowed to watch IRON MAN 3.")
# Not Allowed to watch IRON MAN 3.
# REASON:
# Because age = 40, 40 is greater than 30, so 1 input is true and as we know in (OR) at least 1 input should be true for the results to be true otherwise false.
# So, the results will be (Not Allowed to watch IRON MAN 3.)



# PROBLEM 2:
# Create a program that will allow people over 4 and below 25 or above 50 and below 60 to watch cartoons.
# SOLUTION:
age = 55

if age >= 4 and age <= 25 or age >= 50 and age <= 60:
    print(f"Allowed to watch cartoons.")

elif age >= 50 and age >= 60 or age <= 4 and age <= 25:
    print(f"Not Allowed to watch cartoons.")

elif age <= 50 and age <= 60 or age >= 4 and age >= 25:
    print(f"Not Allowed to watch cartoons.")
# Allowed to watch cartoons.
# REASON:
# Because age = 55, 55 is greater than 50 and less than 60, As we know in (OR) at least 1 input should be true for the results to be true otherwise false.
# Here the second input is true so the results are (Allowed to watch cartoons.)

# STATEMENT 1:
# If the age was 3 the results would be (Not Allowed to watch cartoons.)
# REASON:
# Because 3 is less than 4 and less than 25, 1 input is true so the results would be (Not Allowed to watch cartoons.)

# STATEMENT 2:
# If the age was 30 the results would be (Not Allowed to watch cartoons.)
# REASON:
# Because 30 is less than 50 and less than 60, and again, As we know in (OR) at least 1 input should be true for the results to be true otherwise false.
# Here 1 input is true so the results would be (Not Allowed to watch cartoons.)



# PROBLEM 3:
# Suppose that you are a teacher, and you have make a list of all the students who scored above 60% and below 70% marks and those who scored above 90% in the examination.
# SOLUTION:
student_1 = marks = 65

if marks >= 60 and marks <= 70:
    print(f"B+")

elif marks >= 90:
    print(f"A+")
# B+
# REASON:
# Because marks = 65, 65 is greater than 60 and less than 70, both inputs are true and as we know in (AND) result is true when both inputs are true otherwise false.
# So, the result is true.



student_2 = marks = 98

if marks >= 60 and marks <= 70:
    print(f"B+")

elif marks >= 90:
    print(f"A+")
# A+
# REASON:
# Because marks = 98, 98 is greater than 90, the input is true.
# So, the result is true.
