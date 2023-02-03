import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Tolbus:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.defence = 7
        self.cooldown, self.special_cooldown = 2, 1

    def attack(self, oponent):
        f.attack(4, oponent, 'Tolbus')

    def special_attack(self, oponent):
        self.cooldown = f.attack(5, oponent, 'Tolbus', 2, self.cooldown, special=True)

    # Tolbus stays behind friendly lines, ready to heal others or himself
    def special(self, member=None, not_self=False):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 1
            if not_self:
                member.hp = f.recovery_actions(member.hp, member.max_hp)
                sg.popup(f'You healed {s.inv_transfer[member]} by 2 hp')
            else:
                self.hp = f.recovery_actions(self.hp, self.max_hp)
                sg.popup('You healed yourself by 2 hp')
            s.already_played['Tolbus'] = True