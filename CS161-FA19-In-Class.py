"""
s = 1
k = 1

while(k <= 5) :
    s = s * k
    k = k + 1
print("s = ", s)
"""

# Problem 1
# input: n, where n is a positive integer (any whole number above 0)
# output: 1/(n) + 2/(n-1) + 3/(n-2) + 4/(n-3) + 5/(n-4) + ... + (n-1)/2 + (n)/1
"""
n = float(input("Please enter a positive, whole number: "))
s = 0
t = 1
b = n

while(t <= n) :
    s = s + (t/b)
    t = t + 1
    b = b - 1

print("Your answer = ", s)
"""

"""
n = float(input("Please enter a positive number: "))
s = 0
k = 1
while(k <= n) :
    s = s + k/(n - k + 1)
    k = k + 1
print("Your answer = ", s)
"""

# Problem 2
# import math
# code: math.sqrt(n)
# Vietes Formula: 2/pi = sqrt(2)/2 * sqrt(2 + sqrt(2))/2 * sqrt(2 + sqrt(2 + sqrt(sqrt(2)))/2
# use a factor of 10 should give us a close approximation of pi
# input: n, number of factors
"""
import math

n = int(input("Please enter a positive number to factor pi: "))
sq = math.sqrt(2)
s = (sq / 2)
t = 0

while(t <= n) :
    sq = math.sqrt(2 + sq)
    s = (s * (sq / 2))
    t = (t + 1)

print("Pi is about: ", (2 / s))
"""

