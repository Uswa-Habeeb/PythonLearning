# Strings
# Indexing
# 1D-Array
# Slicing
# String Methods
# This assignment focuses on exploring python built-in methods

# PROBLEM 1:
# Write a python programe to check 
# if a user defined string ends with any user deined sub string
# SOLUTION:
string = input("Enter your string: ")
deined_substr = input("Enter your deined sub string: ")
sub_str = string.endswith(deined_substr)
print(sub_str)
# OUTPUT: 
# Enter your string: USWA HABEEB.
# Enter your deined sub string: .
# True


# PROBLEM 2:
# Find the index where the substring starts in a major string
# SOLUTION:
str = "hello, it's me."
substr = str.rfind("it's")
print(substr)
# OUTPUT: 
# 7


# PROBLEM 3:
# Check whether a user defined string consists of alphabets only or numbers only
# SOLUTION:
string = input("Enter your string: ")
check = string.isalpha() or string.isnumeric()
print(check)
# OUTPUT: 
# Enter your string: company1
# False


# PROBLEM 4:
# Check whether a user defined string consists of alpha-numerics only
# SOLUTION:
string = input("Enter your string: ")
check = string.isalnum()
print(check)
# OUTPUT: 
# Enter your string: 
# uswa123
# True