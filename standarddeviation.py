#Standard Deviation Skeleton

# This program should compute the standard deviation of a sequence of non-negative numbers, terminated by a -1.
# Standard deviation is:  A measure of how spread-out data is.
# NOTE:  You are not allowed to use a built-in standard deviation function from the libraries.
""" How to compute:
1)  Find the airthmetic mean (average)
2)  Find the difference between each data point and the mean
3)  Square the differences
4)  Sum the squares of the differences
5)  Divide the sum by the number of data points
6)  Now square root it. 
    (import math library , to square root x: 
    x = math.sqrt(x) )
"""
import math

x = []
n = int(input("Please enter a sequence of non-negative numbers, terminated by a -1:\n"))
while(n >= 0) :
	x.append(n)
	n = int(input())

b = len(x) - 1
m = 0
c = 0
while(b >= 0) :
	m = x[b] + m
	b = b - 1
	c = c + 1
a = m/c

y = []
b = len(x)
d = 0
t = 0
r = 0
while(b > 0) :
	if(a > b) :
		d = a - b
	else :
		d = b - a
	t = math.sqrt(d)
	r = r + t
	b = b - 1
o = len(x) -1
l = r/o
print(math.sqrt(l))

