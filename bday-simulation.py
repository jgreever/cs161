#!/usr/bin/env python3

import math
import random

ft = []
k = 0
while(k < 365) :
	ft.append(0)
	k = k + 1

print("Please type in how many people are in the class: ")
x = int(input())

success = 0

c = 0
while(c < 10000) :
	k = 0
	while(k < 365) :
		ft[k] = 0
		k = k + 1

	k = 0
	while(k < x):
		b = math.floor(364*random.random()) + 1
		ft[b] = ft[b] + 1
		k = k + 1

	k = 0
	f = 0
	while(k < 365):
		if(ft[k] >= 2) :
			f = 1
		k = k + 1
	if(f == 1) :
		success = success + 1
	c = c + 1

print("The probability that in a class of ", end="")
print(x , end="")
print(" people, at least two have the same birthday is:  " , end="")
print(success/10000)
