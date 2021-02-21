# collatz.py
# This program takes any positive integer and outputs successive values of a calculation
# Calculation is:
# -  if the number is even, divide by 2.
# -  if the number is odd, multiply by 3, then add 1
# -  repeat the calculations above until the number equals 1
# Author: Alan Healy
# Date Created: 20-FEB-2021
#
# Reference 1: http://www.math.com/school/subject1/lessons/S1U1L10GL.html#
# Reference: Week 04 tutorial/labs

# read user input, will loop until correct values are entered.
while True:
    try:
        # ask user for input number. will throw error is it is not of "int" type
        number = int(input("Enter a positive integer: "))

        # if user enters a negative number or 0, the program will loop until a correct value is entered
        while number <= 0:
            number = int(input("Please enter a positive integer only: "))

    # use ValueError to catch specific error, and not mask other exception which may possibly occur
    except ValueError:
        # if there is an error, display an error message
        print("Please enter a number value only.")

        # continue stops the current iteration and goes on to the next
        continue

    else:  # if there are no errors
        break # stops the while True loop and continues the program

# my initial version had a lot of print statements to display the working of the code.
# the code can be reduced a good bit without those, and the output displayed on one line
# decided to leave them in and add an if statement to let the user decide if they want to see them or not

while True:
    displayCalculations = input("Would you like view the calculations? Y/N: ")
    displayCalculations = displayCalculations.upper() # convert user input to uppercase to help with IF statements

    if displayCalculations in ('Y','YES'): # will display calculations

        # program will loop continuously until "number" = 1)
        while number > 1: 
            
            # if statements to check whether number is even or not
            # this block runs if the number is even
            if (number % 2) == 0: 
                print ("{} is even.".format(number)) # display current value of "number" variable
                previousValue = number # store "number" before calculation
                number = (number // 2) # perform calculation. // is for integer division
                print ("{} / 2 = {}".format(previousValue, number)) # verbose output of calculation

            # this block runs if the number is odd (logically, the number can only be odd or even, so no more if/elif statements needed)
            else :
                # display current value of "number" variable
                print("{} is odd.".format(number))
                previousValue = number  # store "number" before calculation
                number = ((number * 3) + 1)  # perform calculation.
                print ("({} * 3) + 1 = {}".format(previousValue, number)) # output calculation

        # print final number, which will be 1
        print("{} has been reached. The program will now end.".format(number))

    elif displayCalculations in ('N','NO'): # will NOT display calculations

        # program will loop continuously until "number" = 1)
        while number > 1:
            
            # this block runs if the number is even
            if (number % 2) == 0:
                print(number, end=", ")
                number = (number // 2)

            # this block runs if the number is odd 
            else :
                print(number, end=", ")
                number = ((number * 3) + 1)

        # print final number, which will be 1
        print(number)

    else: # displayCalculations not in ("y", "n"):
        print("Please only enter 'y' or 'n'.")
        continue

    break
