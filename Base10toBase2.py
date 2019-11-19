#!/usr/bin/python3

# Convert a base 10 number to base 2 (list, list.append())
# First, divide the base 10 by 2 and record the remainder in the list
# repeat until the number reaches 0
# print the list back in reverse order
x = []
y = []
n = int(input("Please enter a positive number: "))
while(n > 0) :
	s = n % 2
	x.append(s)
	n = n // 2
s = len(x) - 1
while(s >= 0) :
	y.append(x[s])
	s = s - 1
print(*y, sep='')  # cleanup the output and show without commas or brackets.

