from Code import functions as f

class Honimír:
    def __init__(self):
        self.hp = 11
        self.max_hp = 11
        self.energy = 8
        self.max_energy = 8
        self.defence = 1
        self.regeneration = 2

    def attack(self, oponent):
        f.attack(self.energy, 2, 2, oponent)

    def special(self, oponent):
        f.attack(self.energy, 7, 7, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)