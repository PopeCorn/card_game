from Code import functions as f
import random

class Nikolas:
    def __init__(self):
        self.hp, self.max_hp = 15, 15
        self.energy, self.max_energy = 7, 7
        self.defence, self.max_defence = 10, 10
        self.cooldown, self.special_cooldown = 0, 0
        
    def attack(self, oponent):
        self.energy = f.attack(self.energy, 3, 4, oponent)

    def special_attack(self, oponent):
        random_number = random.randrange(1, 10)
        self.energy, self.cooldown = f.attack(self.energy, 6, random_number, oponent, 2, self.cooldown, special=True)

    # In the chaos of battle, Nikolas stops to have Beef Jerky and replenish his defence 
    def special(self):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 4:
                print('You do not have enough energy to do that!')
            else:
                self.special_cooldown += 1
                self.energy -= 4
                self.defence = f.recovery_actions(self.defence, self.max_defence)