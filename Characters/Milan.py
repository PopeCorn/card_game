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

    def heal(self):
        self.energy -= 1
        f.healing(self)