from Code import functions as f

class Zimik:
    def __init__(self):
        self.hp = 12
        self.max_hp = 12
        self.energy = 10
        self.max_energy = 10
        self.defence = 1
        self.regeneration = 2

    def attack(self, oponent):
        self.energy -= 4
        blow = 3 - oponent.defence
        f.attacking(oponent, blow, 3)

    def special(self, oponent):
        self.energy -= 6
        blow = 5 - oponent.defence
        f.attacking(oponent, blow, 5)

    def heal(self):
        self.energy -= 1
        f.healing(self)