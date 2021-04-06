# es.py
# This program reads a log file and extracts URLs.
# Author: Alan Healy
# Date Created: 14-MAR-2021
#
# Reference: https://www.w3schools.com/python/python_regex.asp
# Reference: https://regex101.com/r/Iafoaq/1 # This may be overwritten, but this what I used to verify my first regex ( /| show)
# Reference: https://regex101.com/r/Iafoaq/2 # This is the (GET | POST ) regex

import re

#######
#regex = "( /\S+| show\S+)"
#######
# I originally went with this regex, as the part of every url began with either " /" or " show".
# See line 405 of log file to see e.g. of a part that begins with 405
# I'm not a fan of hardcoding someting like that, as it makes it hard to maintain/futureproof it.
# Also, other log files may have a different format from the characters above. It also had a whitespace at the start.
# This is why I went with what is below, using GET and POST.
# While these are also hardcoded, they are likely not to change as much as the other characters.

regex = "(?:GET |POST )(\S+)"

# filename = "./../Prog_CyberSecOps/week07-regex/smallerAccess.txt" # smaller log file for testing (to print)
filename = "./w07_www1_access.log"


extractedURLList = []

with open(filename) as inputFile:
    for line in inputFile:
        extractedURL = re.findall(regex, line)
        #extractedURLList.append(extractedURL) # append adds [] to each list item [[item1], [item2], [item3]]
        extractedURLList.extend(extractedURL)  # extend allows list to be created as per spec [item1, item 2, item 3]

# print list to verify
print(extractedURLList)

# extra marks part to go here
