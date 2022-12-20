import random

class Nikolas:
    def __init__(self):
        self.hp = 15
        self.energy = 7
        self.defence = 1
        self.regeneration = 2
    
    def nikolas_attack(oponent):
        Nikolas.energy -= 3
        blow = 4 - oponent.defence
        oponent.hp -= blow
    
    def nikolas_special(oponent):
        Nikolas.energy -= 6
        roll = random.randrange(1, 10)
        blow = roll - oponent.defence
        oponent.hp -= blow
        