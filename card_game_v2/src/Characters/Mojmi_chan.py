import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Mojmi_chan:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.defence = 6
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.double_attack(4, 2)
        f.attack(s.mojmi_chan_attack, oponent, 'Mojmi-chan')

    def special_attack(self, oponent):
        f.double_attack(12, 6)
        self.cooldown = f.attack(s.mojmi_chan_attack, oponent, 'Mojmi-chan', 2, self.cooldown, special=True)

    # Mojmi-chan positions himself behind enemy lines, ready to strike twice as hard
    def special(self):
        if s.mojmi_chan_done:
            sg.popup('You can do this only once!', title='Error')
        else:
            self.cooldown += 3
            s.mojmi_chan_double_damage = True
            s.mojmi_chan_done = True
            s.already_played['Mojmi-chan'] = True
            sg.popup('Your next attack will have doubled damage')
