import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Žimík:
    def __init__(self):
        self.hp, self.max_hp = 12, 12
        self.defence, self.max_defence = 2
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(3, oponent, 'Žimík')

    def special_attack(self, oponent):
        self.cooldown = f.attack(5, oponent, 'Žimík', 2, self.cooldown, special=True)

    # Žimík takes off his shirt and shows the hottest body on the planet, instantly weaking one chosen oponent
    def special(self, oponent):
        if s.zimik_increase_cooldown is not True:
            oponent.cooldown += 2
            oponent.special_cooldown += 2
            self.defence = f.recovery_actions(self.defence, self.max_defence)
            s.zimik_increase_cooldown = True
            s.already_played['Žimík'] = True
            sg.popup(f"You increased both of {s.inv_transfer[oponent]}'s cooldowns by 1 and recovered 2 points of defence")
        else:
            sg.popup('You can use this ability only once!', title='Error')