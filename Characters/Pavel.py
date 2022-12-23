from Code import functions as f

class Pavel:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 8
        self.max_energy = 8
        self.defence = 1
        self.regeneration = 2

    def attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        f.attacking(oponent, blow, 3)

    def special(self, oponent):
        self.energy -= 7
        blow = 8 - oponent.defence
        f.attacking(oponent, blow, 8)

    def heal(self):
        self.energy -= 1
        f.healing(self)