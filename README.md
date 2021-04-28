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

# 03 - collatz.py
This program takes a user inputted value and performs calculations based on it. As it had a few calculations which could go wrong, I added a lot of print statements initially to show the output. As they were actually quite helpful (and also verify my code works), I decided to leave them in and let the user decide on running the program if they want the calculations displayed or not.

# 04 - squareroot.py
This program has complex (well, relatively) calculations so I again added the ability for the user to be able to display the calculations or not. This is useful to verify the code works, as when using Newton's method to derive the square root, the first answer is not very accurate - if the user only chooses 1 iteration, the answer would look wrong.

The calculations are based on Newton's Method:  Xn+1 = (X + (b/X)) / 2. This gets more accurate as the number of iterations increase, so I added an input to let the user chose the number of iterations.

# 05 - es.py
This program reads a filename from a command line argument and counts how many letter "e"s are in it. If the user doesn't specify the filename in the command line when calling the program, then they will be prompted for the file name. 

In the function, if there is an error, it will return "None". This is different to "0", as a file could have zero e's, and that is not an error.

# 06 - extract-url.py
The bulk of this work was to get the regular expression (regex) to work correctly. I had originally went with a regex that found the part of the URL that began with "/" or "show", but I didn't like using hardcoded values like that. I changed the regex to capture on the HTTP request of either GET or POST. This is still hardcoding the values, but these would be much more prevalent and consistent.

The regex used finds anything that begins with GET or POST, but the ?: means it's a non capture group. The next set of brackets after this contains the capture group, which is the request part of the URL. This is then added to a list. I used "extend" as opposed to "append", and append added [] brackets to every item in the list, whereas extend didn't, looked neater, and more importantly, looked like what was given in the spec/task.

# 07 - plottask.py
The x points are based on the array given in the spec/task, while the y points are the functions. The "f" function is just x, the "g" function is x squared, so x to the power of 2 (x ** 2), while the "h" function is x cubed, so x ** 3.

For the plots, I changed the fonts, and added a title, axis labels, legend and changed some colours. I also used some syntax to make the 2 and 3 appear as superscripts in the labels, as these are exponent values.

Finally, there is a line of code, which if uncommented, will make the plot appear in the style of an xkcd comic. Style points for sure!

# 08 - sessionID.py
For this program, I had used the original access log file, but it was approx 4 MB in size and the plot at the end was illegible. Instead, I used a cut down version, with 50 lines taken from 3 days of logs, for 150 total.

The program gives the columns new names, reads the file into a dataframe, and uses a function with regular expressions to remove [] brackets from the "Time" column.

For the regex to get the sessionID, I tested it out in a regex website and it worked, but when running the program it didn't, so I had to change it up. It's still quite similar, but splits on the "=" sign and captures the group to the right. There is a link in the references to my original regex and sample data.

For the groupby, it groups on the sessionID, and sums up the total "Size of Response" for that group. 

For the extra marks part, the results are the same as the original groupby. I set the rule to 1 day, but there were no sessionIDs that spanned across two days (that I could see when running the original 4 MB log file, but I didn't check every sessionID). This means that the size for this period is the same as te groupby above.

For the plot, I used tight_layout so that it would display all the values and plot labels correctly.

# 09 - errorTesting.py
For the error testing, as no list was specified, I used the Fibonacci Sequence from the labs (if it's not broken, why fix it?). I created a function to create this sequence, but capped it at 25 terms, just to keep things manageable. From reading the spec/task, the averageTo function was meant to stop the list based on the toIndex value, which is why I didn't use that in the fibonacci function.

For error testing, I used a while True to allow the program to loop if an incorrect value was entered. This would allow the user to enter the value in again, without having to call the program again. I included a ValueError and a ZeroDivisionError, but ended up removing the ZeroDivisionError as the same result was achieved from an If statement, which was able to set the range of values that could be used.

For each error, instead of a print statement, an error message was added to the log with details on the error. I also added a log statement for a successful execution.
