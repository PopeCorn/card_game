from Code import functions as f
from Code import settings as s

class Zimik:
    def __init__(self):
        self.hp = 12
        self.max_hp = 12
        self.energy = 10
        self.max_energy = 10
        self.defence = 2
        self.cooldown = 0

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def special_attack(self, oponent):
        f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    def special(self, oponent):
        if self.energy > 5 and s.zimik_reduce_defence is not True:
            oponent.max_energy -= 2
            oponent.energy -= 2
            self.defence += 2
            s.zimik_reduce_defence = True
        else:
            print('You can use this ability only once!')