from __future__ import print_function
import random

def guess_winner(players):
    '''The function in this docstring is for the user to be guess the winner of the lottery
    
    The arguement in the code is players.It is a tuple.
    A tuple is a list that cannot be changed.
    '''
    winner = random.choice(players) 

    ####
    # The winner is chosee at random for the users list of input.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players:
        print(p+', ', end='')

    ####
    # It checks if the users choice was right or wrong. If right, it will say thank you and if wrong it will say guess again!
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