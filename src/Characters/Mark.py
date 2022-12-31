from Code import functions as f
from Code import settings as s

class Marekec:
    def __init__(self):
        self.hp = 13
        self.max_hp = 13
        self.energy = 7
        self.max_energy = 7
        self.defence = 7
        self.cooldown = 0
        self.special_cooldown = 0

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special_attack(self, oponent):
        f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    def special(self):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 3:
                print('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 3
                s.marekec_dodge = True
