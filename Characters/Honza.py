from Code import functions as f

class Honza:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 7
        self.max_energy = 7
        self.defence = 8
        self.cooldown = 0
        self.special_cooldown = 0

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special(self, oponent):
        if self.cooldown > 0:
            print(f'You can use this ability in {self.cooldown} rounds!')
        else:
            if self.energy < 6:
                print('You do not have enough energy!')
            else:
                self.cooldown += 2
                self.energy -= 6
                oponent.hp -= 2
                oponent.energy = 0

    def calculations(self):
        if self.cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 4:
                print('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 4
                self.max_hp += 1
                f.hp += 2