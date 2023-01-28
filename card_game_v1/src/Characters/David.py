from Code import functions as f
from Code import settings as s

class David:
    def __init__(self):
        self.hp, self.max_hp = 13, 13
        self.energy, self.max_energy = 8, 8
        self.defence = 6
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 3, 2, oponent)

    def special_attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 6, 6, oponent, 2, self.cooldown, special=True)

    # David uses his special Big Chungus powers to reduce damage of the next attack aimed at him
    def special(self):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 4:
                print('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 4
                s.david_defence = True