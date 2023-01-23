import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Zimik:
    def __init__(self):
        self.hp, self.max_hp = 12, 12
        self.energy, self.max_energy = 10, 10
        self.defence = 2
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent, 'Žimík')

    def special_attack(self, oponent):
        f.attack(self.energy, 6, 5, oponent, 'Žimík', 2, self.cooldown, special=True)

    # Zimik takes off his shirt and shows the hottest body on the planet, instantly weaking one chosen oponent
    def special(self, oponent):
        if self.energy > 5 and s.zimik_reduce_energy is not True:
            oponent.max_energy -= 2
            oponent.energy -= 2
            self.defence += 2
            s.zimik_reduce_energy = True
            s.already_played['Žimík'] = True
            sg.popup(f"You reduced {s.inv_transfer[oponent]}'s max. energy and his actual energy by 2")
        else:
            sg.popup('You can use this ability only once!')