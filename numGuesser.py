from math import ceil, log

lowNum = 0
highNum = 10000000000000
guessCounter = 0
depth = ceil(log(highNum - lowNum,2))
answer = 'h'
guess = highNum

print("Think of a number between {0} and {1} and I will try to guess it {2} guesses or less".format(lowNum, highNum, depth))
print("If I guess too high, let me know by pressing the 'h' key.")
print("If I guess too low, let me know by pressing the 'l' key.")
print("But if I guess correctly, let me know by pressing the 'y' key.")

while guessCounter <= depth:
    if answer == 'y':
        print("Yay! I guessed it in {0} guesses!".format(guessCounter))
        break
    if answer == 'h':
        highNum = guess
    if answer == 'l':
        lowNum = guess

    guess = ceil((highNum + lowNum)/2)

    answer = input("Is your number {0}? ".format(guess))
    guessCounter += 1
