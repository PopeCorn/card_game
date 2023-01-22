import PySimpleGUI as sg
from Code import functions as f

class Pavel:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.energy, self.max_energy = 8, 8
        self.defence = 8
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special_attack(self, oponent):
        f.attack(self.energy, 7, 8, oponent, 2, self.cooldown, special=True)

    # Pavel unleashes his powerful and logical arguments, unlike Matyas' ones
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 7:
                sg.popup('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 7
                f.attack(self.energy, 0, 3, oponent)
                oponent.hp -= 2