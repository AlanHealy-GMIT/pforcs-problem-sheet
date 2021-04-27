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
# Reference: https://regex101.com/r/c9Lw9y/1 # This is the SessionID regex
# Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html


# import necessary modules
import pandas as pd
import regex as re
import matplotlib.pyplot as plt

# assign log file to a variable
#logFilename = 'w07_www1_access.log'
logFilename = '../Prog_CyberSecOps/week09-pandas/data/access.log' # smaller log file for testing

# column names to be added to the dataframe
colNames = ('IP', 'Dash1', 'UserID', 'Time', 'URL', 'Status Code',
            'Size of Response', 'Referrer', 'User Agent', 'Misc')

# read the file into a dataframe. seperator is " ", no header, column names are from the list above
df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)

# remove [] from time


def getNewTime(x):
    newTime = re.search('[\w:/]+', x).group()
    # do your stuff
    return newTime

df['Time'] = df['Time'].apply(getNewTime)


#df['Time'] = df['Time'].apply(lambda x: re.search('[\w:/]+', x).group())

# change 'Time' type from object to time, using the format of the time in the log file
df['Time'] = pd.to_datetime(df['Time'], format='%d/%b/%Y:%H:%M:%S')

# sets index to date column ('Time')
df = df.set_index(['Time'])

# print first row only (for testing)
#print(df.iloc[0])

# extract session IDs from URL and save to new column
# use regex to get sessionID (REF 1), create in normal function, as per lab

def applySessionIDRegex(x):
    findSessionID = re.search('(?:JSESSIONID=)(\S+)', x).group()
    sessionID = re.split('=', findSessionID)[1] # above regex wasn't working, so split on the '=' and chose the end part of the split [1]
    return sessionID

# new column
df['SessionID'] = df['URL'].apply(applySessionIDRegex)

print(df)
#newdf = df['2021/02/15 18:00:00':'2021/02/15 18:59:59']

#newdf = df.between_time('23:00', '23:59') # this is times every day

#print(newdf)

# downloadSamples = df['Size of Response'].resample(rule='10Min').mean()
# print(downloadSamples)

# downloadSamples.plot()

# plt.title("readFromLog.py", loc='center')
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.legend()

# plt.show()
