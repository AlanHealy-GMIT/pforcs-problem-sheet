# errorTesting.py
# This program tries different tests and errors.
# Author: Alan Healy
# Date Created: 28-APR-2021
#
# Reference 1: https://www.geeksforgeeks.org/sum-function-python/

#import logging module
import logging
logging.basicConfig(level=logging.DEBUG)

#use the fibonacci sequence as the list for testing. Not using user inputted number
def fibonacci():
    #define variables a,b and list
    a = 0
    b = 1
    fibonacciSequence = [0]

    # iterate through until reaching 25th term
    for i in range(1, 25): # cap at 25 to keep list small. I didn't use the user inputted number here, as that should be used in the averageTo function instead
        fibonacciSequence.append(b)
        # fibonacci sequence formula
        a, b = b, a + b

    # return the fibonacci sequence as a list
    return fibonacciSequence

# create a bullet proof function called averageTo, takes in a list and an integer
def averageTo(aList, toIndex):

    sumList = 0 # default value of sum of list
    averageList = -1 # default value of average (-1 as per spec)
    
    # iterate through list until hitting user inputted number
    for i in range(toIndex):
        sumList = sumList + aList[i] # current value of list item, add it to itself
        averageList = (sumList / toIndex)

    return averageList

while True:
    try:
        # ask user for input number. will throw error is it is not of "int" type
        
        upToNumber = int(input("Enter a positive integer between 1 and 25, to chose a term from the Fibonacci sequence: "))
        
        # if upToNumber is empty, give it a value of -1. this was done to allow more exception error handling to be added, as is the purpose of the task
        # if upToNumber is False:
        #     upToNumber = -1

    except ValueError:
        # if there is an error, display an error message
        # use ValueError to catch specific error, and not mask other exception which may possibly occur
        #print("Please enter a number value only.")
        logging.debug("%s", "The value entered was not a number.")

        # continue stops the current iteration and goes on to the next
        continue
    
    # except ZeroDivisionError:
    #     # prevents the sum being divided by 0 when calculating average
    #     logging.debug("%d: %s", upToNumber, "The value entered must not be 0.")
    #     continue

    if upToNumber <= 0 or upToNumber > 25: 
        # this prevents a ZeroDivisonError when calculating average, but also stops zero being divided by zero
        #print("Please enter a value between 1 and 25.")
        logging.debug("%d: %s", upToNumber, "The value was outside the range of 1 to 25 inclusive.")
        continue

    #else:
     
    break


print("The average is: {}".format(averageTo(fibonacci(), upToNumber)))


if __name__ == '__main__':
    # tests here
    return7 = (20 / 7) # 2.857142857142857
    return11 = (143 / 11) # 13.0
    assert averageTo([0, 1, 1, 2, 3, 5, 8], 7) == return7, 'Incorrect return for 7'
    assert averageTo([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], 11) == return11, 'Incorrect return for 11'

    logging.debug("%s", "All tests passed.")
