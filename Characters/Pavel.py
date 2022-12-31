from Code import functions as f

class Pavel:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 8
        self.max_energy = 8
        self.defence = 8
        self.cooldown = 0
        self.special_cooldown = 0

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special_attack(self, oponent):
        f.attack(self.energy, 7, 8, oponent, 2, self.cooldown, special=True)

    def special(self, oponent):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 7:
                print('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 7
                f.attack(self.energy, 0, 3, oponent)
                f.attack(self.energy, 0, 3, oponent)