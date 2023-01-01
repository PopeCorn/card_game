from Code import functions as f

class Milan:
    def __init__(self):
        self.hp = 15
        self.max_hp = 15
        self.energy = 10
        self.max_energy = 10
        self.defence = 4
        self.cooldown = 0
        self.special_cooldown = 0

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def special_attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent, 2, self.cooldown, special=True)

    # Milan becomes empowered thanks to his harem
    def special(self, oponent):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            self.special_cooldown += 2
            self.energy -= 7
            self.max_energy += 1
            self.defence += 2
            f.attack(self.energy, 0, 2, oponent)