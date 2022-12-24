from Code import functions as f
import random

class Nikolas:
    def __init__(self):
        self.hp = 15
        self.max_hp = 15
        self.energy = 7
        self.max_energy = 7
        self.defence = 10
    
    def attack(self, oponent):
        f.attack(self.energy, 3, 4, oponent)

    def special(self, oponent):
        random_number = random.randrange(1, 10)
        f.attack(self.energy, 6, random_number, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)