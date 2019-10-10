# Justin Greever
# CS-161
# LoHiGame
# Can you guess the random integer between 1 and 20 (inclusive) in 4 trys?
# Write a program that randomly chooses an integer between 1 and 20 inclusive and then gives the user 4 chances to guess the hidden number.  After each incorrect answer the computer should say that the guess was too high or too low.  If the user does not guess the number after 4 trys, the computer should say: "You are out of guesses, you lose!" and then tell the user what the hidden number actually was.

import random
import math

x = math.floor(20*random.random() +1)
print("x = " , x)   #comment out this line before turning in
print("Guess a number between 1 and 20: ")
guess = float(input())

if(guess == x) :
    print("You win! The number is" , x)
else :
    if(guess < x) :
        print("Your number is too low, 3 attempts remaining, try again: ")
    elif(guess > x) :
        print("Your number is too high, 3 attempts remaining, try again: ")
    guess = float(input())

    if(guess == x) :
        print("You Win! The number is" , x)
    else :
        if(guess < x) :
            print("Your number is too low, 2 attemps remaining, try again: ")
        elif(guess > x) :
            print("Your number is too high, 2 attempts remaining, try again: ")
        guess = float(input())

        if(guess == x) :
            print("You Win! The number is" , x)
        else :
            if(guess < x) :
                print("Your number is too low, 1 attempt remaining, try again: ")
            elif(guess > x) :
                print("Your number is too high, 1 attempt remaining, try again: ")
            guess = float(input())

            if(guess == x) :
                print("You Win! The number is" , x)
            else :
                if(guess < x) :
                    print("Your number is too low.")
                elif(guess > x) :
                    print("Your number is too high.")
                print("You are out of guesses, you lose! The number was", x)
print("Thank you for playing!")
