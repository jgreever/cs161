# David Ely - CS 161 Fall 2019
# Write a program that prompts the user for their age.  The program ouptuts the following depending on the age the user supplies:
# if age is less than 18:  "You are not old enough to vote."
# if age is between 18 and 24 inclusive:  "You are in the prime of your life."
# if age is over 24:  "You are starting to shows signs of age."
# At the end the program should print" "Goodbye"

# Below are multiple solutions (do all of them work?)


# Solution 1:

print ("Please type in your age in years: ")
age = float(input())

if(age < 18) :
  print("You are not old enough to vote.")
if(age >= 18) :
  if(age <= 24) :
    print("You are in the prime of your life.")
if(age > 24) :
  print("You are starting to shows signs of age.")
print("goodbye")


# Solution 2:
"""
print ("Please type in your age in years: ")
age = float(input())

if(age < 18) :
  print("You are not old enough to vote.")
if(age >= 18 and age <= 24) :
  print("You are in the prime of your life.")
if(age > 24) :
  print("You are starting to shows signs of age.")
"""

# Solution 3:
"""
print ("Please type in your age in years: ")
age = float(input())

if(age < 18) :
  print("You are not old enough to vote.")
if(age >= 18) :
  if(age <= 24) :
    print("You are in the prime of your life.")
  else :
    print("You are starting to shows signs of age.")
"""

# Solution 4:
"""
print ("Please type in your age in years: ")
age = float(input())

if(age < 18) :
  print("You are not old enough to vote.")
elif(age <= 24) :
  print("You are in the prime of your life.")
else :
  print("You are starting to shows signs of age.")
"""


# Solution 5 (This is an ERRONEOUS solution, why?):
"""
print ("Please type in your age in years: ")
age = float(input())

if(age < 18) :
  print("You are not old enough to vote.")
if(age <= 24) :
  print("You are in the prime of your life.")
else :
  print("You are starting to shows signs of age.")
"""

# Solution 6 (This is an ERRONEOUS solution, why?):
"""
print ("Please type in your age in years: ")
age = float(input())

if(age < 18) :
  print("You are not old enough to vote.")
else : (age <= 24) 
  print("You are in the prime of your life.")
else :
  print("You are starting to shows signs of age.")
"""
"""
# Solution 7 (This solution works in Python, but is unlikely to work in many progamming languages, why?):

print ("Please type in your age in years: ")
age = float(input())

if(age < 18) :
  print("You are not old enough to vote.")
if(24 >= age >= 18) : # Imagine your age is 20, Python evaluates this "if" statement as true but other languages may evaluate the statement as false!  Why?
  print("You are in the prime of your life.")
if(age > 24) :
  print("You are starting to shows signs of age.")
"""


