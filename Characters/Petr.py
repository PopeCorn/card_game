from Code import functions as f

class Petr:
    def __init__(self):
        self.hp = 11
        self.energy = 7
        self.max_energy = 7
        self.defence = 1
        self.regeneration = 2

    def petr_attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        f.attacking(oponent, blow, 3)

    def petr_special(self, oponent):
        self.energy -= 6
        blow = 5 - oponent.defence
        f.attacking(oponent, blow, 5)

    def petr_heal(self):
        self.energy -= 1
        f.healing(self)