# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # standard short name
import random
def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    # a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()
def roll_hundred_pair():
    p = []
    for dice in range(100):
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)
        k = dice_one + dice_two 
        p += [k]
    plt.hist(p)
    plt.show
    
def dice(n):
    m = 0
    for roll in range(n):
        rolls = random.randint(1,6)
        m = rolls + m 
    return('Roll was ' + str(m))
    
def matches(ticket, winners):
    food = 0
    for pterodactyl in ticket:
        if pterodactyl in winners:
            food = food + 1 
    return food 
    
