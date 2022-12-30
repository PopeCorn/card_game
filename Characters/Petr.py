from Code import functions as f

class Petr:
    def __init__(self):
        self.hp = 11
        self.max_hp = 11
        self.energy = 7
        self.max_energy = 7
        self.defence = 9
        self.cooldown = 0
        self.special_cooldown = 0

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    def touching(self, oponent):
        self.energy += 3
        f.attack(self.energy, 4, 2, oponent, 1, self.special_cooldown, special=True)