from Code import functions as f

class Petr:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.energy, self.max_energy = 7, 7
        self.defence = 9
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        self.energy = f.attack(self.energy, 3, 3, oponent)

    def special_attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    # Petr uses his unmatched speed give himself energy and attack at the same time
    def special(self, oponent):
        self.energy += 3
        self.energy = f.attack(self.energy, 4, 2, oponent, 1, self.special_cooldown, special=True)