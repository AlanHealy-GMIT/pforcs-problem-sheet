# es.py
# This program reads in a text file and outputs the number of "e"s it contains.
# Author: Alan Healy
# Date Created: 13-MAR-2021
#
# Reference: https://www.gutenberg.org/files/2701/old/moby10b.txt - First result from Google of "moby-dick.txt", and renamed as such.
# Reference: https://www.w3schools.com/python/python_strings_methods.asp - count()
# Reference: https://realpython.com/python-command-line-arguments/ - argument from CLI
# Reference: https://stackabuse.com/command-line-arguments-in-python/

# import "sys" module to read from the CLI
import sys

# if user does not specify a filename when calling the program, prompt them for one
# argv[0] is always the program name e.g. "es.py", so the length of "sys.argv" is 1 if the user doesn't specify an argument
if len(sys.argv) == 1:
    filename = input("Please enter the name of the file you wish to use: ")
else:
    ## argv[0] is always the program name, so argv[1] will be the user-specified filename
    filename = sys.argv[1]  # assign argument to variable

# create function to count the letters, would allow for future expansion for user to specify the letter to be counted
def countLetters():
    try:
        with open(filename, "rt") as f:
            readFile = f.read()
            count = int(readFile.count("e"))
            return count
    except:
        # error means no file exists, so return None
        print("\"{}\" was not found. Please check the name of the file and try again.".format(
            filename))
        return None # not zero as there could be a file with zero of a particular letter

# call the function and assign the value it returns to a variable
numLetters = countLetters()

# if numLetters is "None" it means the file could not be found.
# logically, a result should not be printed in this case, as you cant get a count of nothing i.e. null (and null is not the same as "0")
# this "if" statements prevents "None" from being printed to the user
if numLetters != None:
    print(numLetters)




