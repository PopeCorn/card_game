import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Marekec:
    def __init__(self):
        self.hp, self.max_hp = 13, 13
        self.energy, self.max_energy = 7, 7
        self.defence = 7
        self.cooldown, self.special_cooldown = 0, 0
    def attack(self, oponent):
        f.attack(self.energy, 3, 3, oponent, 'Mark')

    def special_attack(self, oponent):
        f.attack(self.energy, 6, 5, oponent, 'Mark', 2, self.cooldown, special=True)

    # Marekec prepares for an upcoming attack with his dodging skills
    def special(self):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 3:
                sg.popup('You do not have enough energy!')
            else:
                self.special_cooldown += 2
                self.energy -= 3
                s.marekec_dodge = True
                s.already_played['Mark'] = True
                sg.popup('You now have a 50% chance to dodge the next attack')
