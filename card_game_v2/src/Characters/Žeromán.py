import PySimpleGUI as sg
import random
from Code import functions as f
from Code import settings as s

class Žeromán:
    def __init__(self):
        self.hp, self.max_hp = 15, 15
        self.defence, self.max_defence = 10, 10
        self.cooldown, self.special_cooldown = 2, 1
        
    def attack(self, oponent):
        f.attack(2, oponent, 'Žeromán')

    def special_attack(self, oponent):
        random_number = random.randrange(1, 11)
        self.cooldown = f.attack(random_number, oponent, 'Žeromán', 2, self.cooldown, special=True)

    # In the chaos of battle, Žeromán stops to have Beef Jerky and replenish his defence 
    def special(self):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 1
            self.defence = f.recovery_actions(self.defence, self.max_defence)
            s.already_played['Žeromán'] = True
            sg.popup('You recovered 2 of your defence points')