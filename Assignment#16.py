# while loop
# Conditional while loop
# Strings
# Indexing
# 1D-Array
# Slicing
# String Methods

# PROBLEM 1:
# Reverse the string to make it readable
# ?elbadaer ti ekam uoy naC
# SOLUTION:
string = '?elbadaer ti ekam uoy naC'
print(string[::-1])
# OUTPUT:
# Can you make it readable?

# PROBLEM 2:
# Assign each word in the given string to a different variable using slicing
# Slice me if you can.
# SOLUTION:
string = 'Slice me if you can.'
str_1 = print(string[0:5])
str_2 = print(string[6:8])
str_3 = print(string[9:11])
str_4 = print(string[12:15])
str_5 = print(string[16:20])
# OUTPUT:
# Slice
# me
# if
# you
# can.

# PROBLEM 3:
# Find number of characters in the given string
# Can you tell me how many characters are there using python?
# SOLUTION:
print(len(string))
# OUTPUT:
20
# PROBLEM 4:
# Find middle character of the given string
# Hey! You can use a built-in python method to find the middle element. 
# Test your logics using python. Best of Luck!.
# SOLUTION:
string = 'Slice me if you can.'
length = len(string)
middle = length// 2
print(string[middle]) 
# OUTPUT:
# f
