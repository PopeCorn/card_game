from Code import functions as f

class Marekec:
    def __init__(self):
        self.hp = 13
        self.energy = 7
        self.max_energy = 7
        self.defence = 1
        self.regeneration = 2

    def marekec_attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        f.attacking(oponent, blow)

    def marekec_special(self, oponent):
        self.energy -= 6
        blow = 5 - oponent.defence
        f.attacking(oponent, blow)