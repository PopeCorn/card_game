from Code import functions as f
from Code import settings as s

class Matyas:
    def __init__(self):
        self.hp, self.max_hp = 12, 12
        self.energy, self.max_energy = 7, 7
        self.defence = 3
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 3, 3, oponent)

    def special_attack(self, oponent):
        self.energy, self.special_cooldown = f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    # Matyas poisons an enemy with his arguments, which he repeats for entire 2 rounds 
    def special(self, oponent):
        if self.cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 4:
                print('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 4
                s.mata_poison = True
                s.mata_poison_target = oponent
                oponent.hp -= 2
        