# PROBLEM 1

# Create a program that will take all the necessary information from the user like 
# (First Name, Last Name, Age, Gender, Religion, Nationality, Polling Station City, User's residential city etc.). 
# Base on that information show that whether the user is allowed to cast the vote or not keeeping the following parameters in mind for decision making:
# User must be 18 or over.

# SOLUTION:
# User's Information:
FirstName = "Uswa"
LastName = "Habeeb"
Gender = "Female"
Religion = "Islam"
Nationality = "Pakistani"
Polling_Station_City = "Sahiwal" 
Residential_City = "Sahiwal"
# Age = 17
Age = int(input("Enter your Age : " ))

if Age >= 18:
    print(f"{FirstName} {LastName}, Age {Age}, Gender {Gender}, Religion {Religion}, Nationality {Nationality}, Polling Station City {Polling_Station_City}, Residential City {Residential_City} is ALLOWED TO CAST THE VOTE.")

else:
    print(f"{FirstName}, {LastName}, Age {Age}, Gender {Gender}, Religion {Religion}, Nationality {Nationality}, Polling Station City {Polling_Station_City}, Residential City {Residential_City} is NOT ALLOWED TO CAST THE VOTE.")

# Uswa, Habeeb, Age 17, Gender Female, Religion Islam, Nationality Pakistani, Polling Station City Sahiwal, Residential City Sahiwal is NOT ALLOWED TO CAST THE VOTE.

