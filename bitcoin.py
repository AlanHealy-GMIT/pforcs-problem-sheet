# bitcoin.py
# This program outputs the current bitcoin price in US Dollars, and other currencies
# Author: Alan Healy
# Date Created: 14-FEB-2021
#
# Reference: https://www.w3schools.com/python/python_strings_slicing.asp
# Reference: https://stackoverflow.com/questions/23306653/python-accessing-nested-json-data
# Reference: https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string

# import requests
import requests
import html  # for escaping currency symbols

# url that the json file is located at
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)

bitCoinDict = returnedData.json()

# print("1 BTC in USD is ${:.2f}".format(bitCoinDict['bpi']['USD']['rate_float']))
# print("1 BTC in GBP is £{:.2f}".format(bitCoinDict['bpi']['GBP']['rate_float']))
# print("1 BTC in EUR is €{:.2f}".format(bitCoinDict['bpi']['EUR']['rate_float']))

# above works, but want to make it better, with less hardcoded values.
# print blank space to separate above
# print("")

# the json file uses hardcoded values after "bpi" for each currency e.g. "USD", "EUR"
# this makes it difficult to programmably reach the next level of data
# this is why two for loops are needed:
# 1. to cycle through each currency in "bpi"
# 2. to go through the details nested in each currency

bpi = bitCoinDict['bpi']
timeUK = bitCoinDict['time']['updateduk']

print("The current Bitcoin prices as of {} are as follows:".format(timeUK))

for eachCurrency in bpi:
    # this allows the next for loop to go through each cuurency
    currency = bpi[eachCurrency]
    for eachCurrencyDetail in currency:
        # assign needed details to variables
        code = currency['code']
        symbol = html.unescape(currency['symbol']) # escape html code here so only need to do once (if program was to be expanded upon)
        rate_float = currency['rate_float'] # for calculations if ever used
        rate_display = currency['rate'][:-2] # for displaying with thousand separator, to two decimal places
        break  # print needs to be outside this loop to only print once per currency
    print("1 BTC in {} is {}{}".format(code, symbol, rate_display))


# also played with this which would work but would have to done for each currency
# uSD = [bitCoinDict['bpi']['USD']['code'],
#        bitCoinDict['bpi']['USD']['symbol'],
#        bitCoinDict['bpi']['USD']['rate_float']]

# print("1 BTC in {} is {}{:.2f}".format(uSD[0], uSD[1], uSD[2]))
