import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Anus:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.defence = 8
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(3, oponent, 'Anus')

    def special_attack(self, oponent):
        if self.cooldown > 0:
            sg.popup(f'You can use this ability in {self.cooldown} rounds!', title='Error')
        else:
            self.cooldown += 2
            oponent.hp -= 2
            oponent.cooldown += 2
            oponent.special_cooldown += 1
            s.already_played['Anus'] = True
            sg.popup(f"You increased {s.inv_transfer[oponent]}'s Special Attack cooldown by 2 and Special Action cooldown by 1 while reducing his hp by 2")

    # Honza calculates the situation with his superior mathematic skills and prepares for anything bad that might happen
    def special(self):
        if self.cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            self.max_hp += 1
            self.hp += 2
            s.already_played['Anus'] = True
            sg.popup('You increased your max. hp by 1 and your actual hp by 2')