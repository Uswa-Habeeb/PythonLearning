# while loop
# Conditional while loop

# PROBLEM 1:
# Suppose that you are a teacher and you want to find average obtained marks of a student.
# Create a Python program to perform the following tasks:
# Ask user if he/she has entered marks against desired number of subjects 
# and wants to calculate average so far or wants to enter marks for more subjects.
# Print Number of subjects against marks were added.
# Print Average of all obtained marks.
# Example Output should be like
# Number of subjects are 7
# Average marks are 85(after calculation)

# SOLUTION:
flag = True
count = 1
total_marks = 0

while flag:
    marks = int(input(f"Enter Marks for subject {count} : "))
    total_marks += marks
    count += 1
    choice = input('Press N to exit or any other to continue :')
    if choice == 'N' or choice == 'n':
        flag = False
count -= 1
average = total_marks/count
print(f"Number of subjects are : {count} ")
print(f"Average marks are : {average} ")

# OUTPUT:
# Enter Marks for subject 1 : 20
# Press N to exit or any other to continue :p
# Enter Marks for subject 2 : 30
# Press N to exit or any other to continue :k
# Enter Marks for subject 3 : 25
# Press N to exit or any other to continue :l
# Enter Marks for subject 4 : 10
# Press N to exit or any other to continue :n
# Number of subjects are : 4 
# Average marks are : 21.25 