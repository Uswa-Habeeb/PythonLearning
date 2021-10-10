# LOOPS
# FOR LOOP.
# QUESTION#1:
# Create a program to print any user defined multiplication table.
# Example Output should be like (Suppose user entered 7)
# Your multiplication table should be else than 7
# SOLUTION:

Muliplication_table = (input("Enter your multiplication table : "))

for Muliplication_table in range (1, 11):
    print(f"5 x {Muliplication_table} = {Muliplication_table * 5} ")

# Enter your multiplication table : 5
# 5 x 1 = 5 
# 5 x 2 = 10 
# 5 x 3 = 15 
# 5 x 4 = 20 
# 5 x 5 = 25 
# 5 x 6 = 30 
# 5 x 7 = 35 
# 5 x 8 = 40 
# 5 x 9 = 45 
# 5 x 10 = 50

# QUESTION#2:
# Print the same above table in reverse order.
# SOLUTION:

Muliplication_table = (input("Enter your multiplication table to convert in reverse order : "))

for Muliplication_table in range (10, 0, -1):
    print(f"5 x {Muliplication_table} = {Muliplication_table * 5} ")

# Enter your multiplication table : 5
# 5 x 10 = 50 
# 5 x 9 = 45 
# 5 x 8 = 40 
# 5 x 7 = 35 
# 5 x 6 = 30 
# 5 x 5 = 25 
# 5 x 4 = 20 
# 5 x 3 = 15 
# 5 x 2 = 10 
# 5 x 1 = 5 