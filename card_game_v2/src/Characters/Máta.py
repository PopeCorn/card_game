import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Máta:
    def __init__(self):
        self.hp, self.max_hp = 12, 12
        self.defence = 3
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(3, oponent, 'Máta')

    def special_attack(self, oponent):
        self.cooldown = f.attack(4, oponent, 'Máta', 2, self.cooldown, special=True)

    # Máta poisons an enemy with his arguments, which he repeats for entire 2 rounds 
    def special(self, oponent):
        if self.cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            s.mata_poison = True
            s.mata_poison_target = oponent
            oponent.hp -= 2
            s.already_played['Máta'] = True
            sg.popup(f'You deal damage to {s.inv_transfer[oponent]} now and next round because you poisoned him')
        