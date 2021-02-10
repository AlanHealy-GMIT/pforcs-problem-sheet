# bmi.py
# This program calculates a person's BMI
# Author: Alan Healy
# Date Created: 31-JAN-2021
#
# Reference: https://www.w3schools.com/python/python_string_formatting.asp
# Reference: https://www.w3schools.com/python/python_try_except.asp
# Reference: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

# This program will rely on data the user inputs. 
# This data must be a number value only
# Raise an error if a number isn't entered

""" try: 
    # test to see if the statement runs without errors
    weight = float(input("Enter weight in kgs: "))
    height = float(input("Enter height in cms: "))
except : 
    # if there is an error, display an error message
    print("Sorry, only numbers can be entered.")
else: 
    # if there are NO errors, keep running through program
    # bmi = weight/height. height must be converted to metres, then squared.
    bmi = weight / ((height / 100) ** 2)
    # display answer to 2 decimal places
    print("Your BMI is {:.2f}.".format(bmi)) """

# code above works but exits the program if the user enters an invalid value
# the following code will run continuously until correct values are entered

# loop through the code. "while true" allows the code to loop continously as the condition is always met
while True:
    try: 
        # test to see if the statements run without errors
        weight = float(input("Enter weight in kgs: "))
        height = float(input("Enter height in cms: "))

    except ValueError:
        # if there is an error, display an error message
        # use ValueError to catch specific error, and not mask other exception which may possibly occur
        print("Please enter a number value only.")

        # continue stops the current iteration and goes on to the next
        continue
        
    if weight <= 0 or height <= 0:
        # this prevents a ZeroDivisonError when calculating bmi
        print("Please enter a value greater than zero.")
        continue

    else: 
        # if there are NO errors, keep running through program
        # bmi = weight/height. height must be converted to metres, then squared.
        bmi = weight / ((height / 100) ** 2)
        # display answer to 2 decimal places
        print("Your BMI is {:.2f}.".format(bmi))

        # break stops the loop
        break