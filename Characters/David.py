from Code import functions as f

class David:
    def __init__(self):
        self.hp = 13
        self.max_hp = 13
        self.energy = 8
        self.max_energy = 8
        self.defence = 1
        self.regeneration = 2

    def attack(self, oponent):
        self.energy -= 3
        blow = 2 - oponent.defence
        f.attacking(oponent, blow, 2)

    def special(self, oponent):
        self.energy -= 6
        blow = 6 - oponent.defence
        f.attacking(oponent, blow, 6)

    def heal(self):
        self.energy -= 1
        f.healing(self)