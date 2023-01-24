import PySimpleGUI as sg
import random
from Code import functions as f
from Code import settings as s

class Nikolas:
    def __init__(self):
        self.hp, self.max_hp = 15, 15
        self.energy, self.max_energy = 7, 7
        self.defence, self.max_defence = 10, 10
        self.cooldown, self.special_cooldown = 0, 0
        
    def attack(self, oponent):
        f.attack(self.energy, 3, 4, oponent, 'Nikolas')

    def special_attack(self, oponent):
        random_number = random.randrange(1, 10)
        f.attack(self.energy, 6, random_number, oponent, 'Nikolas', 2, self.cooldown, special=True)

    # In the chaos of battle, Nikolas stops to have Beef Jerky and replenish his defence 
    def special(self):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            if self.energy < 4:
                sg.popup('You do not have enough energy to do that!', title='Error')
            else:
                self.special_cooldown += 1
                self.energy -= 4
                self.defence = f.recovery_actions(self.defence, self.max_defence)
                s.already_played['Nikolas'] = True
                sg.popup('You recovered 2 of your defence points')