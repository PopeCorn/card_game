import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Mojmir:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.defence = 6
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.double_attack(4, 2)
        f.attack(s.mojmir_attack, oponent, 'Mojmír')

    def special_attack(self, oponent):
        f.double_attack(12, 6)
        self.cooldown = f.attack(s.mojmir_attack, oponent, 'Mojmír', 2, self.cooldown, special=True)

    # Mojmir positions himself behind enemy lines, ready to strike twice as hard
    def special(self):
        if s.mojmir_done:
            sg.popup('You can do this only once!', title='Error')
        else:
            self.cooldown += 3
            s.mojmir_double_damage = True
            s.mojmir_done = True
            s.already_played['Mojmír'] = True
            sg.popup('Your next attack will have doubled damage')
