'''
Created on 18/10/2012

@author: repli
'''

import random

def name_to_number(name):
    
    print 'Player chooses ' + name
    
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    
def rpsls(guess):
    player_number = name_to_number(guess)
    comp_number = random.randrange(0, 5)
    
    print 'Computer chooses ' + number_to_name(comp_number)
    
    if player_number > comp_number:
        print 'Player wins!\n'
    elif player_number < comp_number:
        print 'Computer wins!\n'
    else:
        print 'Player and computer tie!\n'
        

rpsls('paper')
rpsls('rock')
    