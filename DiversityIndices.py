#Put Diversity Indices Here
#import math
import numpy as np


"""Note: doesn't connsider multiple grading schemes per class."""

#Takes as input a 1D array of the percentages (in decimal form) for each grading method. An entry of 0 indicates that this method of evaluation wasn't used.

def shanon(arrayOfPercentages):
    shanon = 0
    #Calculates the shanon index.
    for i in range(len(arrayOfPercentages)):
        if arrayOfPercentages[i] != 0:
            x = np.log(arrayOfPercentages[i])
            p = arrayOfPercentages[i]*x
            shanon += p
    return -1*shanon
    

"""
#For Testing Purposes
array = [0, 0.1, 0, 0, 0.9]
array2 = [0, 0.5, 0, 0, 0.5]
array3 = [0.2, 0.2, 0.2, 0.2, 0.2]

print(shanon(array))
print(shanon(array2))
print(shanon(array3))
"""

"""Note: doesn't connsider multiple grading schemes per class"""

#Takes as input a 1D array of the percentages (in decimal form) for each grading method. An entry of 0 indicates that this method of evaluation wasn't used.

def simpson(arrayOfPercentages):
    sumOfp = 0
    #Calculates simpson index.
    for i in range(len(arrayOfPercentages)):
        if arrayOfPercentages[i] != 0:
            p = arrayOfPercentages[i]**2
            sumOfp += p
    simpson = 1.0/sumOfp
    return simpson

"""
print(simpson(array))
print(simpson(array2))
print(simpson(array3))

"""
