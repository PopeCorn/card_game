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
        f.attack(self.energy, 4, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)