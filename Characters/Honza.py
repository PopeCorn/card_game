from Code import functions as f

class Honza:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 7
        self.max_energy = 7
        self.defence = 8

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        self.energy -= 6
        oponent.hp -= 2
        oponent.energy = 0

    def calculations(self):
        self.energy -= 4
        self.max_hp += 2
        self.hp += 2