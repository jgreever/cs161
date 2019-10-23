# Justin Greever
# CS161 FA19
# s = 0 + 1^2 - 2^2 + 3^2 - 4^2 ....+- n^2
# add odd / subtract even
# input: positive int "n" from user input
# output: the value of "s"

n = float(input("Please enter a even number: "))

# use while/else statement to create a loop asking user to enter even number when they enter an odd number
while(n % 2 != 0) :  # odd sum check: sum = (n % 2 != 0)
    print("That was an odd number. Try again.")
    n = float(input("Please enter a even number: "))

else :
    s = -(n*(n+1))//2  # we can use the formula: s = -(n(n+1))/2, since we will always end up with a negative (anything x negative = negative)
                       # use x // y for x divided by y to remove remainder (return floor value, similar to using float())
    print(s)

# Weird bug, any input that is 16 numbers and under works fine, 17 numbers and it returns a value instead of saying it's odd and try again. Probably something to do with python floating point rounding.

