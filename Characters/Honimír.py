from Code import functions as f

class Honimír:
    def __init__(self):
        self.hp = 11
        self.energy = 8
        self.max_energy = 8
        self.defence = 1
        self.regeneration = 2

    def honimír_attack(self, oponent):
        self.energy -= 2
        blow = 2 - oponent.defence
        f.attacking(oponent, blow, 2)

    def honimír_special(self, oponent):
        self.energy -= 7
        blow = 7 - oponent.defence
        f.attacking(oponent, blow, 7)

    def honimir_heal(self):
        self.energy -= 1
        f.healing(self)