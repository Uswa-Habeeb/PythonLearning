# Decision Making


# Problem 1
# If craving, eat chocolates

# Condition
Craving = True

if Craving:
    print(f'Craving Sugar')
    print(f'Eat Chocolates')

# Craving Sugar
# Eat Chocolates



# Problem 2
# Condition
student_1 = 79
student_2 = 20
student_3 = 60.5
student_4 = 35
# Passing marks = 60

condition = student_1 > 60 
if condition:
    print(f'student_1 PASSED')
# student_1 PASSED


condition = student_2 > 60
if condition:
    print(f'student_2 PASSED')
# Nothing 
# Because marks are lower than passing marks


condition = student_3 > 60
if condition:
    print(f'student_3 PASSED')
# student_3 PASSED


condition = student_4 > 60
if condition:
    print(f'student_4 PASSED')
# Nothing 
# Because marks are lower than passing marks



# Problem 3
student_1 = 79
student_2 = 20
student_3 = 60.5
student_4 = 35
# Passing marks = 55


# Condition
condition = student_1 < 55
if condition:
    print(f'student_1 FAIL')
# Nothing 
# Because marks are higher than passing marks


condition = student_2 < 55
if condition:
    print(f'student_2 FAIL')
# student_2 FAIL


condition = student_3 < 55
if condition:
    print(f'student_3 FAIL')
# Nothing 
# Because marks are higher than passing marks


condition = student_4 < 55
if condition:
    print(f'student_4 FAIL')
# student_4 FAIL