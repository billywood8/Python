from __future__ import print_function # must be first in file 
import random


def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')

def quiz_decimal(low, high) ~\Documents\Python\Activity134