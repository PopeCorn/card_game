from card_game_code import functions as f

class Petr:
    def __init__(self):
        self.hp = 11
        self.max_hp = 11
        self.energy = 7
        self.max_energy = 7
        self.defence = 9

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)