import PySimpleGUI as sg
from Code import functions as f

class Petr:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.defence = 9
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(3, oponent, 'Petr')

    def special_attack(self, oponent):
        self.cooldown = f.attack(5, oponent, 'Petr', 2, self.cooldown, special=True)

    # Petr uses his unmatched speed give himself energy and attack at the same time
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            sg.popup('The following attack will decrease both of your cooldowns by 1')
            self.special_cooldown = f.attack(2, oponent, 'Petr', self.special_cooldown, special=True)