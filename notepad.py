#!/usr/bin/env python3
# Personal notepad to expand my python skills
# and get ready for more programming classes
# that I will be taking very soon at school.
#
#


## imports ##
import datetime

## subroutines ##
f = open("notepad.txt", "a")
l = []

## main ##
print("Please type your notes.")
print("When finished, type")
print("      endnotes")
print("on a new line and press")
print("Enter/Return")
print("")

i = str(input())
now = datetime.datetime.now()
l.append(now.strftime("%Y-%m-%d %H:%M:%S"))

while(i != "endnotes") :
        l.append(i)
        i = str(input())

f.write(str("\n".join(l)))
f.write("\n") # used these two in order to get a blank
f.write("\n") # line for formatting reasons. will fix later.
f.close()

f = open("notepad.txt", "r")
r = f.read()
print("")
print(r)
print("")

f.close()

