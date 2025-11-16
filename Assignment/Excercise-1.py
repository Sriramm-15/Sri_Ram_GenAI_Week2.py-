#Exercise 1: Age Calculator

#importing date time modules for calculations
from datetime import datetime
dob = input("Enter your DOB (mm/dd/yyyy): ")
try:
    # Convert input string to date object
    bday = datetime.strptime(dob, "%m/%d/%Y")
    today = datetime.now()
    # Calculate the age
    age = today.year - bday.year
    if (today.month, today.day) < (bday.month, bday.day):
        age=age-1
    # Print present age anf birthdate in european format
    print("Your preesent age is:", age)
    print("Birthdate in European format:", bday.strftime("%d/%m/%Y"))
except:
    print("Enter the date in the correct format (mm/dd/yyyy)")
