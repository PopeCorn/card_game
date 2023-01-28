from Code import functions as f
from Code import settings as s

class Marekec:
    def __init__(self):
        self.hp, self.max_hp = 13, 13
        self.energy, self.max_energy = 7, 7
        self.defence = 7
        self.cooldown, self.special_cooldown = 0, 0
        
    def attack(self, oponent):
        self.energy = f.attack(self.energy, 3, 3, oponent)

    def special_attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    # Marekec prepares for an upcoming attack with his dodging skills
    def special(self):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 3:
                print('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 3
                s.marekec_dodge = True
