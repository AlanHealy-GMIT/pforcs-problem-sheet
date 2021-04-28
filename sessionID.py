# sessionID.py
# This program:
#    1. Reads a log file into a dataframe
#    2. Sets date time to be the index
#    3. Uses regex to extract session IDs from URLs
#    4. Uses groupBy to get sum of all data downloaded by sessionID
#    5. Creates a plot
# Author: Alan Healy
# Date Created: 27-APR-2021
#
# Reference 1: https://regex101.com/r/c9Lw9y/1 # This is the SessionID regex
# Reference 2: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
# Reference 3: https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum

# import necessary modules
import pandas as pd
import regex as re
import matplotlib.pyplot as plt

# assign log file to a variable
# using cut down log file with 50 lines from each of the first 3 days, as the plot at the end was illegible with so much data
logFilename = 'threeDayAccess.log'
# logFilename = 'w07_www1_access.log' 

# column names to be added to the dataframe
colNames = ('IP', 'Dash1', 'UserID', 'Time', 'URL', 'Status Code',
            'Size of Response', 'Referrer', 'User Agent', 'Misc')

# read the file into a dataframe. seperator is " ", no header, column names are from the list above
df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

# remove [] from time
def getNewTime(x):
    newTime = re.search('[\w:/]+', x).group()
    return newTime

# uses function above to apply the regex to the 'Time' column
df['Time'] = df['Time'].apply(getNewTime)

# change 'Time' type from object to time, using the format of the time in the log file
df['Time'] = pd.to_datetime(df['Time'], format='%d/%b/%Y:%H:%M:%S')

# sets index to date column ('Time')
df = df.set_index(['Time'])

# print first row only (for testing)
# print(df.iloc[0])

# extract session IDs from URL and save to new column
# use regex to get sessionID (REF 1), create in normal function, as per lab
def applySessionIDRegex(x):
    findSessionID = re.search('(?:JSESSIONID=)(\S+)', x).group()
    sessionID = re.split('=', findSessionID)[1] # above regex wasn't working, so split on the '=' and chose the end part of the split [1]
    return sessionID

# create new column by applying function from above
df['SessionID'] = df['URL'].apply(applySessionIDRegex)

# groupby by sessionID and sum all the 'Size of Response' to get total data downloaded per sessionID
# REF 3 (double square brackets came from a comment on the second answer, keeps the object as DataFrame)
sumSessionIDData = df.groupby(['SessionID'])[['Size of Response']].sum()
print(sumSessionIDData)

# extra marks part
# sums SessionId data per every 1 day
# the sum values seem the same, as it looks like in this log, no sessionID is used across multiple days,
# therefore the sum of the data per sessionID per day will be the same as the sum of the data per sessionID
dailySessionIDData = df.groupby(['SessionID'])[['Size of Response']].resample(rule = '1d').sum()
print(dailySessionIDData)

# create plot of data
#sumSessionIDData.plot(marker='o', ls='--', color='r')
sumSessionIDData.plot(kind='bar', color='r', width=0.5)

plt.title("Week 09 Problem Sheet Task - sessionID.py", loc='center')
plt.xlabel("SessionID")
plt.ylabel("Size of Response (bytes)")
plt.legend()

plt.grid(axis = 'y')
plt.tight_layout()

plt.show()
