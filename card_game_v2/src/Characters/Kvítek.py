import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Kvítek:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.defence = 5
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.attack(2, oponent, 'Kvítek')

    def special_attack(self, oponent):
        self.cooldown = f.attack(4, oponent, 'Kvítek', 2, self.cooldown, special=True)

    # After a long preparation, Kvitek unleashes his sigma male grindset upon one unsuspecting enemy, killing them instantly
    def special(self, oponent):
        if s.count > 4 and s.kvitek_ultimate is not True:
            oponent.hp = 0
            self.energy = 0
            s.kvitek_ultimate = True
            s.already_played['Kvítek'] = True
            sg.popup(f'You annihilated {s.inv_transfer[oponent]}, killing him')
        else:
            sg.popup('You can use this ability only once and the game has to be over 8 rounds long!', title='Error')

