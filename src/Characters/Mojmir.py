from Code import functions as f
from Code import settings as s

class Mojmir:
    def __init__(self):
        self.hp = 11
        self.max_hp = 11
        self.energy = 8
        self.max_energy = 8
        self.defence = 6
        self.cooldown = 0
        self.special_cooldown = 0

    def attack(self, oponent):
        f.double_attack(4, 2)
        f.attack(self.energy, 2, s.mojmir_attack, oponent)

    def special_attack(self, oponent):
        f.double_attack(12, 6)
        f.attack(self.energy, 7, s.mojmir_attack, oponent, 2, self.cooldown, special=True)

    def special(self):
        if self.energy < 6 and s.mojmir_done is True:
            print('You do not have enough energy and you can do this only once!')
        else:
            self.cooldown += 3
            self.energy -= 6
            s.mojmir_double_damage = True
            s.mojmir_done = True