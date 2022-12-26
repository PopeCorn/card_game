from card_game_code import functions as f
from card_game_code import settings as s

class David:
    def __init__(self):
        self.hp = 13
        self.max_hp = 13
        self.energy = 8
        self.max_energy = 8
        self.defence = 6

    def attack(self, oponent):
        f.attack(self.energy, 3, 2, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 6, oponent)

    def reduce_damage(self):
        self.energy -= 3
        s.david_defence = True