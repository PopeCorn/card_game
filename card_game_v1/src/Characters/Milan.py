from Code import functions as f

class Milan:
    def __init__(self):
        self.hp, self.max_hp = 15, 15
        self.energy, self.max_energy = 10, 10
        self.defence = 4
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 4, 3, oponent)

    def special_attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 4, 3, oponent, 2, self.cooldown, special=True)

    # Milan becomes empowered thanks to his harem
    def special(self, oponent):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            self.special_cooldown += 2
            self.energy -= 7
            self.max_energy += 1
            self.defence += 2
            self.energy = f.attack(self.energy, 0, 2, oponent)