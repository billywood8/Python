from __future__ import print_function
import random

def guess_winner(players):
    '''The function in this docstring is for the user to be guess the winner of the lottery
    
    The arguement in the code is players.It is a tuple.
    A tuple is a list that cannot be changed.
    '''
    winner = random.choice(players) 

    ####
    # The winner is chosee at random from the tuple.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players:
        print(p+', ', end='')

    ####
    # It checks if the users choice was right or wrong. If right, it will say you guessed in (number of tries) guesses! and if wrong it will say guess again!
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
    
def goguess():
    num = random.randint(1,20)
    guess = 21
    tries = 0
    print('I have a number between 1 and 20 inclusive.')
    while guess != num: 
        guess = int(raw_input('Guess: '))
        if guess > num:
            print(str(guess) + ' is too high.')
            tries = tries + 1
        if guess < num: 
            print(str(guess) + ' is too low.')
            tries = tries + 1
    if guess == num: 
        tries = tries + 1
        print('Right! My number is ' + str(guess) + '!' + ' You guessed in ' + str(tries) + ' guesses!')