# What is the probability that in a classroom of x people, at least 2 will be born on the same day of the year (ignore leap year)?
# I have given you the skeleton and some of the code... you complete it!

import math
import random

ft = []
k = 0
while(k < 365) :
    ft.append(0)
    k = k+1

print("Please type in how many people are in the class: ")
x = int(input())

success = 0

c = 0
while(c < 10000) :
    k = 0
    while(k < 365) :
        ft[k] = 0
        k = k+1

k = 0
while(k < x):
    b = math.floor(365*random.random())+1
    ft[b] = ft[b] + 1
    k = k+1

k = 0
while(k < 365):
# your code goes here  #########################
    if(ft[k] >= 2) :
        success = success + 1
k = k+1

c = c+1

print("The probability that in a class of ", end="")
print(x , end="")
print(" people, at least two have the same birthday is:  " , end="")
print(success/10000)

