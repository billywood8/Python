from __future__ import print_function
import random

def guess_winner(players):
    '''Summarize the function in this docstring.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # Summarize the following section of code here
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players:
        print(p+', ', end='')

    ####
    # Summarize the following section of code here
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    

def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')