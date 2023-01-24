import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class David:
    def __init__(self):
        self.hp, self.max_hp = 13, 13
        self.defence = 6
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(2, oponent, 'David')

    def special_attack(self, oponent):
        self.cooldown = f.attack(6, oponent, 'David', 2, self.cooldown, special=True)

    # David uses his special Big Chungus powers to reduce damage of the next attack aimed at him
    def special(self):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            s.david_defence = True
            s.already_played['David'] = True
            sg.popup('The next attack aimed at David will have its damage reduced by 3')