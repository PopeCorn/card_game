from Code import functions as f

class Milan:
    def __init__(self):
        self.hp = 15
        self.max_hp = 15
        self.energy = 10
        self.max_energy = 10
        self.defence = 4

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def tiktok(self, oponent):
        self.energy -= 7
        self.max_energy += 1
        self.defence += 2
        f.attack(self.energy, 0, 5, oponent)