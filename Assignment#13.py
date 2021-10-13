# LOOPS
# FOR LOOP.

# QUESTION#1:

# Create a program to print all the numbers divisible by 3 and 5 to a user defined range.
# Use f-string for output with a proper understandable message
# Example Output should be like (Suppose user entered 20)
# 0 is Divisible by 3 and 5
# 15 is Divisible by 3 and 5
# Your user defined range should be greater than 30

# SOLUTION:

user_range = int(input("Enter your Range : "))

for counter in range (user_range):
    if counter % 3 == 0 and counter % 5 == 0:
        print(f"{counter} is Divisible by 3 and 5.")


##  Enter your Range : 35
# 0 is Divisible by 3 and 5.
# 15 is Divisible by 3 and 5.
# 30 is Divisible by 3 and 5.
##  Enter your Range : 48
# 0 is Divisible by 3 and 5.
# 15 is Divisible by 3 and 5.
# 30 is Divisible by 3 and 5.
# 45 is Divisible by 3 and 5.
##  Enter your Range : 90
# 0 is Divisible by 3 and 5.
# 15 is Divisible by 3 and 5.
# 30 is Divisible by 3 and 5.
# 45 is Divisible by 3 and 5.
# 60 is Divisible by 3 and 5.
# 75 is Divisible by 3 and 5.