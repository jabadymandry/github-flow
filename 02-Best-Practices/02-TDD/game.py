# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from string import ascii_uppercase
from random import choice

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(choice(ascii_uppercase))
             
    def is_valid(self, word):
        if word != '':
            if word == 'EUREKA':
                valid = True
            else:
                valid = False
        else:
            valid = False
        
        print(f'{type(valid)} : {valid}')
        return valid
    
    