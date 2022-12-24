from Code import functions as f

class Kvitek:
    def __init__(self):
        self.hp = 11
        self.max_hp = 11
        self.energy = 9
        self.max_energy = 9
        self.defence = 5

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 7, 5, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)