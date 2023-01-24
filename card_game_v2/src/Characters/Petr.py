import PySimpleGUI as sg
from Code import functions as f

class Petr:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.energy, self.max_energy = 7, 7
        self.defence = 9
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent, 'Petr')

    def special_attack(self, oponent):
        f.attack(self.energy, 6, 5, oponent, 'Petr', 2, self.cooldown, special=True)

    # Petr uses his unmatched speed give himself energy and attack at the same time
    def special(self, oponent):
        sg.popup('The following attack will not cost you any energy')
        f.attack(self.energy, 0, 2, oponent, 'Petr', self.special_cooldown, special=True)