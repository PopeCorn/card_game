from Code import functions as f
from Code import settings as s

class David:
    def __init__(self):
        self.hp = 13
        self.max_hp = 13
        self.energy = 8
        self.max_energy = 8
        self.defence = 6

    def attack(self, oponent):
        f.attack(self.energy, 3, 2, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 6, oponent)

    def reduce_damage(self):
        if self.energy < 4:
            print('You do not have enough energy!')
        else:
            self.energy -= 4
            s.david_defence = True