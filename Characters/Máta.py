from Code import functions as f

class Matyas:
    def __init__(self):
        self.hp = 12
        self.energy = 7
        self.max_energy = 7
        self.defence = 1
        self.regeneration = 2

    def matyas_attack(self, oponent):
        self.energy -= 3
        blow = 4 - oponent.defence
        f.attacking(oponent, blow, 4)

    def matyas_special(self, oponent):
        self.energy -= 6
        blow = 5 - oponent.defence
        f.attacking(oponent, blow, 5)

    def matyas_heal(self):
        self.energy -= 1
        f.healing(self)