#!/usr/bin/python3
p = 0
f = 0
s = 0
n = float(input("Please enter test scores. To end, type '-1': "))

while(n != -1):
    if(n >= 60):
        p = p + 1
        s = s + n
    elif(n < 60):
        f = f + 1
    n = float(input())

if(n == -1 and p == 0):
    print("no passing exam scores entered")
else:
    print(s/p)

