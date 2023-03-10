import PySimpleGUI as sg
from Code import functions as f

class Milanus:
    def __init__(self):
        self.hp, self.max_hp = 15, 15
        self.defence = 4
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.attack(3, oponent, 'Milanus')

    def special_attack(self, oponent):
        self.cooldown = f.attack(5, oponent, 'Milanus', 2, self.cooldown, special=True)

    # Milanus becomes empowered thanks to his harem
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            self.defence += 1
            f.attack(5, oponent, 'Milanus')
            sg.popup('You increased your your defence by 1')