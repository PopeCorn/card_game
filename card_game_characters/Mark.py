from card_game_code import functions as f
from card_game_code import settings as s

class Mark:
    def __init__(self):
        self.hp = 13
        self.max_hp = 13
        self.energy = 7
        self.max_energy = 7
        self.defence = 7

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent)

    def dodge(self):
        self.energy -= 3
        s.marekec_dodge = True
