# squareroot.py
# This program uses functions and Newton's method of estimating square roots
# Author: Alan Healy
# Date Created: 28-FEB-2021

# Reference: https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
# Reference: http://www.sosmath.com/calculus/diff/der07/der07.html
# Reference: https://stackoverflow.com/questions/22402548/default-values-on-empty-user-input



# Newton's Method:
# to find a sqrt of "b", 

#          1 (       b )
#  Xn+1 =  - ( Xn +  - )
#          2 (       Xn )

#  Xn+1 = (X + (b/X)) / 2

# 'b' is the number you are trying to find the sqrt of
# 'x' is a "reasonable guess", close to what the answer should be
# for the first iteration, take 'x' as 'b'
# for the next iteration, the answer from the first iteration will be x, giving an more accurate answer

# define a function called "sqrtFunction", which takes 3 arguments
# the first arg is mandatory, but the other args have default values so the user doesn't have to enter values
def sqrtFunction(findSqrtOf, numberOfIterations = 1, displayCalculations = 'N'):

    while True:
        try:
            # ask user for input number. will throw error is it is not of "int" type
            numberOfIterations = int(input("Please enter the number of iterations for accuracy: ") or "1")

            # if user enters a negative number or 0, the program will loop until a correct value is entered
            while numberOfIterations <= 0:
                numberOfIterations = int(input("Please enter a number greater than 0: "))

        # use ValueError to catch specific error, and not mask other exception which may possibly occur
        except ValueError:
            # if there is an error, display an error message
            print("Please enter a number value only.")

            # continue stops the current iteration and goes on to the next
            continue

        else:  # if there are no errors
            break  # stops the while True loop and continues the program

    # this is the Xn+1 from the equation, which set to 0 initially
    newX = float(0)

    while True:
        # lets the user see the calculations or not, as the first few iterations are not very accurate and seem incorrect
        displayCalculations = input("Would you like view the calculations? Y/N: " or "N") #if left blank, will default to "N"
        displayCalculations = displayCalculations.upper() # convert user input to uppercase to help with IF statements


        # "for" loop to keep going through the equation for the number of iterations the user specified
        for iteration in range(1, (numberOfIterations + 1)):

            # Xn for the next iteration = Xn+1 from the previous iteration
            currentX = newX

            if displayCalculations in ('Y', 'YES'):  # will display calculations
                # prints the iteration
                print("")
                print("Iteration: {}".format(iteration))

                # only true for very first iteration
                if newX == 0:
                    print("Initial Xn({}) value: {}".format(iteration,findSqrtOf))
                    newX = (findSqrtOf + 1) / 2 # as Xn = 1 for the first iteration, b / Xn is just = b
                    print("Initial Xn+1({}) value: {}".format((iteration+1),newX))
                else:
                    print("Xn({}) is: {}".format(iteration,currentX))
                    # Xn+1 = (X + (b/X)) / 2
                    newX = ((currentX + (findSqrtOf / currentX)) / 2)
                    print("Xn+1({}) is now: {}".format((iteration+1),newX))
            else: # same as above but without print statements
                if newX == 0:
                    newX = (findSqrtOf + 1) / 2 
                else:
                    newX=((currentX + (findSqrtOf / currentX)) / 2)
            # keep count of the iterations
            iteration += 1
        
        break

    print("")
    # this is the final Xn+1 value
    return newX


while True:
    try:
        # ask user for input number. will throw error is it is not of "float" type
        # this variable will contain the number to find the square root of
        findSqrtOf = float(input("Please enter a positive number: "))

        # if user enters a negative number or 0, the program will loop until a correct value is entered
        while findSqrtOf <= 0:
            findSqrtOf = float(input("Please enter a number greater than 0: "))

    # use ValueError to catch specific error, and not mask other exception which may possibly occur
    except ValueError:
        # if there is an error, display an error message
        print("Please enter a number value only.")

        # continue stops the current iteration and goes on to the next
        continue

    else:  # if there are no errors
        break  # stops the while True loop and continues the program

# sqrt variable is assigned the return value of the sqrtFunction function, for the number findSqrtOf
sqrt = sqrtFunction(findSqrtOf)

#print answer
print("The square root of {} is approx. {:.1f}.".format(findSqrtOf, sqrt))
print("")

