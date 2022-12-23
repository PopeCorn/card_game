from Code import functions as f

class Kvitek:
    def __init__(self):
        self.hp = 11
        self.energy = 9
        self.max_energy = 9
        self.defence = 1
        self.regeneration = 2

    def kvitek_attack(self, oponent):
        self.energy -= 4
        blow = 3 - oponent.defence
        f.attacking(oponent, blow, 3)

    def kvitek_special(self, oponent):
        self.energy -= 7
        blow = 5 - oponent.defence
        f.attacking(oponent, blow, 5)