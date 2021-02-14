# pforcs-problem-sheet

# 01 - bmi.py
This program relies on user inputs, so a number of ways to handle errors were needed. These inputs needed to be number values only, and not be zero. A "try and except" was used to catch a "ValueError" where a string might be inputted instead of a number. An "if" statement was used to prevent zero values.

If there were no errors, the BMI would be calculated and displayed. This was all done inside a "while" loop, so that if an error occurred, the program would run from the top allowing the user to input the values correctly.

I made the conscious decision to NOT include if statements to categorise the result e.g. "Underweight", "Normal" etc. as this was not asked for in the spec. I would regard this as "scope creep" whereas while error handling wasn't asked for either, it is necessary to ensure the program runs correctly.

# 02 - bitcoin.py
This program reads data from a JSON file. It gets the data after requesting it from a specific URL, then converts it to a Python "Dict" type.

To parse through the data, two "for" loops are needed. This is due to the structure of the JSON file. It has a level "bpi", which has three currencies listed in it. Each currency is a level itself containing its own specific details. As each level has a hard-coded value like "USD", a loop was needed to first cycle through "bpi", and then cycle through each currency in the next loop, allowing details to be assigned for each specific currency during each iteration. 

The details assigned were "code", "symbol" and two rate values. "rate_float" would be used if ever any calculations were needed as it is a "number" type, while "rate_display" is only used when outputting to the user, as the data includes a thousand separator. This wouldn't be used if calculations affecting the value where needed, as it is a "string" type.

Using the above "for" loops allows only one "print" line to be needed to display the currency details. The JSON data includes the update time, and this is outputted initially when the user runs the program. 
