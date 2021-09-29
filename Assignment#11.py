# QUESTION:
# Create a program that will take all the necessary information from the user like:
# (First Name, Last Name, Age, Gender, Religion, Nationality, Polling Station City, User's residential city etc.). 
# Base on that information show that : 
# whether the user is allowed to cast the vote or not keeeping the following parameters in mind for decision making:
# User must be 18 or over.
# User must belong to the same polling station city.
# User must be Pakistani.
# SOLUTION:

FirstName = (input("Enter your First Name : "))
LastName = (input("Enter your Last Name : "))
Gender = (input("Enter your Gender : "))
Religion = (input("Enter your Religion : "))
Age = int(input("Enter your Age : " ))


if Age >= 18:
    print("YOUR AGE IS ELIGIBLE.")
    Residential_City = (input("Enter your User's Residential City : "))
    Polling_Station_City = (input("Enter your Polling Station City : "))
    if (Polling_Station_City) == (Residential_City) :
        print("Your Polling Station and Residential City is Same.")
    else:
        print("Your Polling Station and Residential City should be the SAME.")
    Nationality = (input("Enter your Nationality : "))
    if Nationality == "Pakistani" :
        print("YOU ARE ALLOWED TO CAST VOTE.")
    else:
        print("YOU ARE NOT ALLOWED TO CAST VOTE.")
else:
    print("YOU MUST BE 18 OR OVER 18 TO CAST VOTE.")


print(f"First Name : {FirstName}")
print(f"Last Name : {LastName}")
print(f"Gender : {Gender}")
print(f"Religion : {Religion}")
print(f"Age : {Age}")
print(f"Residential City : {Residential_City}")
print(f"Polling Station City : {Polling_Station_City}")
print(f"Nationality : {Nationality}")
print(f"YOU ARE ALLOWED TO CAST VOTE.")

# First Name : Uswa
# Last Name : Habeeb
# Gender : Female
# Religion : Islam
# Age : 18
# Residential City : Sahiwal
# Polling Station City : Sahiwal
# Nationality : Pakistani
# YOU ARE ALLOWED TO CAST VOTE.