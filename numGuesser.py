# A binary search number guesser
# Uses Python3
from math import ceil, log

lowNum = 0                            # The lowest number we guessed
highNum = 1000                        # The highest number we guessed
guessCounter = 0                      # For each guess, this will increase by one
depth = ceil(log(highNum - lowNum,2)) # Maximum number of guesses prediction
answer = 'h'                          # Answer from user if the guess is too high/low or correct
mean = highNum                        # The average between lowNum and highNum

print("Think of a number between {0} and {1} and I will try to guess it {2} guesses or less".format(lowNum, highNum, depth))
print("If I guess too high, let me know by pressing the 'h' key.")
print("If I guess too low, let me know by pressing the 'l' key.")
print("But if I guess correctly, let me know by pressing the 'y' key.")

while lowNum < highNum:
    if answer == 'y': # guess was correct
        print("Yay! I guessed it in {0} guesses!".format(guessCounter))
        break
    if answer == 'h': # guess was too high
        highNum = mean
    if answer == 'l': # guess was too low
        lowNum = mean

    mean = ceil((highNum + lowNum)/2) #definition of the mean of 2 numbers

    answer = input("Is your number {0}? ".format(mean))
    guessCounter += 1
