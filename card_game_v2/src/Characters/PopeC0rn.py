import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class PopeC0rn:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.defence = 8
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.attack(4, oponent, 'PopeC0rn')

    def special_attack(self, oponent):
        self.cooldown = f.attack(8, oponent, 'PopeC0rn', 2, self.cooldown, special=True)

    # PopeC0rn unleashes his powerful and logical arguments, unlike Matyas' ones
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            self.attack(oponent)
            oponent.hp -= 2
            sg.popup(f'You dealt 2 points of additional damage to {s.inv_transfer[oponent]}')