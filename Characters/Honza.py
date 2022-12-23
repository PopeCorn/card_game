from Code import functions as f

class Honza:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 7
        self.max_energy = 7
        self.defence = 1
        self.regeneration = 2

    def attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        f.attacking(oponent, blow, 3)

    def special(self, oponent):
        self.energy -= 6
        oponent.hp -= 2
        oponent.energy = 0

    def heal(self):
        self.energy -= 1
        f.healing(self)