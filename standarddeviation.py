# Standard Deviation Skeleton

# This program should compute the standard deviation of a sequence of non-negative numbers, terminated by a -1.
# Standard deviation is:  A measure of how spread-out data is.
# NOTE:  You are not allowed to use a built-in standard deviation function from the libraries.

import math

list1 = []
userinput = int(input("Please enter a sequence of non-negative numbers, terminated by a -1:\n"))

while (userinput >= 0):
    list1.append(userinput)
    userinput = int(input())

# 1)  Find the arithmetic mean (average)
xlen = len(list1) - 1
counter = 0
xplace = 0
mavg = 0
while (counter <= xlen):
    mavg = mavg + list1[xplace]
    xplace = xplace + 1
    counter = counter + 1
meanaverage = mavg / len(list1)

#  2)  Find the difference between each data point and the mean
list2 = []
counter2 = 0
xlen2 = len(list1) - 1
xplace2 = 0
sumsq = 0
while (counter2 <= xlen2):
    dpmean = abs(list1[xplace2] - meanaverage)
    #  3)  Square the differences
    sqdiff = math.sqrt(dpmean)
    #  4)  Sum the squares of the differences
    sumsq = sumsq + sqdiff
    #  5)  Divide the sum by the number of data points
    list2len = len(list1)
    meanavgsq = sumsq / list2len
    #  6)  Now square root it.
    list2.append(dpmean)
    counter2 = counter2 + 1
    xplace2 = xplace2 + 1
print("Standard Deviation: ", math.sqrt(meanavgsq))
