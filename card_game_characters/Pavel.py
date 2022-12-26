from card_game_code import functions as f

class Pavel:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 8
        self.max_energy = 8
        self.defence = 8

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 7, 8, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)