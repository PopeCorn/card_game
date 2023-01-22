import PySimpleGUI as sg
from Code import functions as f

class Honza:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.energy, self.max_energy = 7, 7
        self.defence = 8
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent)

    def special_attack(self, oponent):
        if self.cooldown > 0:
            sg.popup(f'You can use this ability in {self.cooldown} rounds!')
        else:
            if self.energy < 6:
                sg.popup('You do not have enough energy!')
            else:
                self.cooldown += 2
                self.energy -= 6
                oponent.hp -= 2
                oponent.energy = 0

    # Honza calculates the situation with his superior mathematic skills and prepares for anything bad that might happen
    def special(self):
        if self.cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 4:
                sg.popup('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 4
                self.max_hp += 1
                self.hp += 2