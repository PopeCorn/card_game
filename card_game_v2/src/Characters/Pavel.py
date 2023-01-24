import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s
class Pavel:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.defence = 8
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(3, oponent, 'Pavel')

    def special_attack(self, oponent):
        self.cooldown = f.attack(8, oponent, 'Pavel', 2, self.cooldown, special=True)

    # Pavel unleashes his powerful and logical arguments, unlike Matyas' ones
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            f.attack(4, oponent, 'Pavel')
            oponent.hp -= 2
            sg.popup(f'You dealt 2 points of additional damage to {s.inv_transfer[oponent]}')