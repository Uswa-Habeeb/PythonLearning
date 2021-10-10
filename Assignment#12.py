# LOOPS
# FOR LOOP.
# QUESTION#1:
# Create a program to print any user defined multiplication table.
# Example Output should be like (Suppose user entered 7)
# Your multiplication table should be else than 7
# SOLUTION:

Muliplication_table = int(input("Enter your multiplication table : "))

for counter in range (1, 11):
    print(f"{Muliplication_table} x {counter} = {Muliplication_table * counter} ")
# Enter your multiplication table : 3
# 3 x 1 = 3 
# 3 x 2 = 6 
# 3 x 3 = 9 
# 3 x 4 = 12 
# 3 x 5 = 15 
# 3 x 6 = 18 
# 3 x 7 = 21 
# 3 x 8 = 24 
# 3 x 9 = 27 
# 3 x 10 = 30 


# QUESTION#2:
# Print the same above table in reverse order.
# SOLUTION:

Muliplication_table = int(input("Enter your multiplication table to convert in reverse order : "))

for counter in range (10, 0, -1):
    print(f"{Muliplication_table} x {counter} = {Muliplication_table * counter} ")
# Enter your multiplication table to convert in reverse order : 3
# 3 x 10 = 30 
# 3 x 9 = 27 
# 3 x 8 = 24 
# 3 x 7 = 21 
# 3 x 6 = 18 
# 3 x 5 = 15 
# 3 x 4 = 12 
# 3 x 3 = 9 
# 3 x 2 = 6 
# 3 x 1 = 3 
