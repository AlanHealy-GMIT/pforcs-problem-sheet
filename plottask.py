# plottask.py
# This program plots three functions on one axes:
# f(x)=x, g(x)=x^2 and h(x)=x^3, in the range [0,4]
# Author: Alan Healy
# Date Created: 11-APR-2021
#
# Reference 1: https://www.mathsisfun.com/sets/function.html
# Reference 2: https://www.w3schools.com/python/matplotlib_plotting.asp
# Reference 3: https://matplotlib.org/stable/tutorials/text/mathtext.html
# Reference 4: https://www.w3schools.com/python/matplotlib_labels.asp
# Reference 5: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xkcd.html

# import necessary modules
import numpy as np
import matplotlib.pyplot as plt

# set the x axis to the array given in the problem [0, 4]
xpoints = np.array(range(0, 4))

# the Y axis is taken from the functions listed above. so for "f", it will be the same as x, for "g", it's x^2 (x squared), and for "h" it's x^3 (x cubed)
fx_ypoints = xpoints
gx_ypoints = xpoints ** 2 # this is x squared
hx_ypoints = xpoints ** 3 # this is x cubed

# uncomment the next line to make the plot appear as a xkcd comic! Ref 5
# plt.xkcd(scale=1, length=200, randomness=1)

# create the plot with the x and y points from above. add colours and labels to each individual function here
plt.plot(xpoints, fx_ypoints, color = 'green', label = 'f(x) = x')
plt.plot(xpoints, gx_ypoints, color = 'orange', label = r'g(x) = x$^2$') # this syntax is from mathtext, found at Ref 3 above. it writes the 2 as a superscript
plt.plot(xpoints, hx_ypoints, color = 'red', label = r'h(x) = x$^3$') # this syntax is from mathtext, found at Ref 3 above. it writes the 3 as a superscript

# set fonts to make plot look nice, Ref 4
font1 = {'family': 'Arial', 'color': 'blue', 'size': 20}
font2 = {'family': 'Times New Roman', 'color': 'brown', 'size': 15}

# add other details to the plot such as title, axis labels, legend
plt.title("Week 08 Problem Sheet Task - plottask.py", loc = 'center', fontdict = font1)
plt.xlabel("X Axis", fontdict = font2)
plt.ylabel("Y Axis", fontdict = font2)
plt.legend()

# output the plot for viewing
plt.show()
