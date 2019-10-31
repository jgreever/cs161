# row 1 to 8, column 1 to 8
# 16 pieces per player
# only using the rook in this example
# rook moves up/down/left/right till it is at the edge of the board or hits another piece
# using 2 rooks, determine the probability that they could attack each other
# use monte carlo simulation
# 100000 trials
# record successful attacks
# ignore when rooks 'spawn' on the same square

import random
import math

t = 0  # number of tries
a = 0  # attack success

while t < 100000:
    r1 = math.floor(8 * random.random()) + 1  # Rook-1 row
    c1 = math.floor(8 * random.random()) + 1  # Rook-1 column
    r2 = math.floor(8 * random.random()) + 1  # Rook-2 row
    c2 = math.floor(8 * random.random()) + 1  # Rook-2 column

    if r1 == r2 or c1 == c2:  # Same column or row, successful attack
        a = a + 1

    if r1 == r2 and c1 == c2:  # Same column and row, consider it a failure since its the same location
        a = a - 1
        t = t - 1

    t = t + 1  # add one to the trials after a successful roll/attack

print("Probability of two rooks being able to attack after being randomly placed on the board is: ", a / t)
