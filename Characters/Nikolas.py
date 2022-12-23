from Code import functions as f
import random

class Nikolas:
    def __init__(self):
        self.hp = 15
        self.energy = 7
        self.max_energy = 7
        self.defence = 1
        self.regeneration = 2
    
    def nikolas_attack(self, oponent):
        self.energy -= 3
        blow = 4 - oponent.defence
        f.attacking(oponent, blow, 4)
    
    def nikolas_special(self):
        random_number = random.randrange(1, 10)
        return random_number
        
    def nikolas_heal(self):
        self.energy -= 1
        f.healing(self)