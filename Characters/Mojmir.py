from Code import functions as f
from Code import settings as s

class Mojmir:
    def __init__(self):
        self.hp = 11
        self.max_hp = 11
        self.energy = 8
        self.max_energy = 8
        self.defence = 6

    def attack(self, oponent):
        f.double_attack(4, 2)
        f.attack(self.energy, 2, s.mojmir_attack, oponent)

    def special(self, oponent):
        f.double_attack(12, 6)
        f.attack(self.energy, 7, s.mojmir_attack, oponent)

    def double_damage(self):
        if self.energy < 6:
            print('You do not have enough energy to do that!')
        else:
            self.energy -= 6
            s.mojmir_double_damage = True
