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
        f.attack(self.energy, 3, 2, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 6, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)