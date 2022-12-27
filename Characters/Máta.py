from Code import functions as f
from Code import settings as s

class Matyas:
    def __init__(self):
        self.hp = 12
        self.max_hp = 12
        self.energy = 7
        self.max_energy = 7
        self.defence = 3

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent)

    def poison(self, oponent):
        self.energy -= 2
        s.mata_poison = True
        oponent.hp -= 2
        