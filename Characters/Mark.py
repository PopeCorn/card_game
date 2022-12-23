from Code import functions as f


class Marekec:
    def __init__(self):
        self.hp = 13
        self.max_hp = 13
        self.energy = 7
        self.max_energy = 7
        self.defence = 1

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)
