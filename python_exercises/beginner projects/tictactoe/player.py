import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
        #we want all players to get their next move given a game
        