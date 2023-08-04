import PySimpleGUI as sg
from Code import functions as f
from Code import settings as s

class Anus:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.defence = 8
        self.cooldown, self.special_cooldown = 2, 2

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

    # Anus calculates the situation with his superior mathematic skills and prepares for anything bad that might happen
    def special(self):
        if self.cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            self.max_hp += 1
            self.hp = f.recovery_actions(self.hp, self.max_hp)
            s.already_played['Anus'] = True
            sg.popup('You increased your max. hp by 1 and your actual hp by 2')


class BigChungus:
    def __init__(self):
        self.hp, self.max_hp = 13, 13
        self.defence = 6
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.attack(3, oponent, 'Big Chungus')

    def special_attack(self, oponent):
        self.cooldown = f.attack(6, oponent, 'Big Chungus', 2, self.cooldown, special=True)

    # Big Chungus uses his special Chungus powers to reduce damage of the next attack aimed at him
    def special(self):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            s.chungus_defence = True
            s.already_played['Big Chungus'] = True
            sg.popup('The next attack aimed at David will have its damage reduced by 3')


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


class Marekec:
    def __init__(self):
        self.hp, self.max_hp = 13, 13
        self.defence = 7
        self.cooldown, self.special_cooldown = 2, 2
        
    def attack(self, oponent):
        f.attack(3, oponent, 'Marekec')

    def special_attack(self, oponent):
        self.cooldown = f.attack(6, oponent, 'Marekec', 2, self.cooldown, special=True)

    # Marekec prepares for an upcoming attack with his dodging skills
    def special(self):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            s.marekec_dodge = True
            s.already_played['Marekec'] = True
            sg.popup('You now have a 50% chance to dodge the next attack')


class Máta:
    def __init__(self):
        self.hp, self.max_hp = 12, 12
        self.defence = 3
        self.cooldown, self.special_cooldown = 2, 2
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


class Milanus:
    def __init__(self):
        self.hp, self.max_hp = 15, 15
        self.defence = 4
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.attack(3, oponent, 'Milanus')

    def special_attack(self, oponent):
        self.cooldown = f.attack(5, oponent, 'Milanus', 2, self.cooldown, special=True)

    # Milanus becomes empowered thanks to his harem
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            self.defence += 1
            f.attack(5, oponent, 'Milanus')
            sg.popup('You increased your your defence by 1')


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


class PopeC0rn:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.defence = 8
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.attack(4, oponent, 'PopeC0rn')

    def special_attack(self, oponent):
        self.cooldown = f.attack(8, oponent, 'PopeC0rn', 2, self.cooldown, special=True)

    # PopeC0rn unleashes his powerful and logical arguments, unlike Matyas' ones
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 2
            self.attack(oponent)
            oponent.hp -= 2
            sg.popup(f'You dealt 2 points of additional damage to {s.inv_transfer[oponent]}')


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


class Zálabář:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.defence = 9
        self.cooldown, self.special_cooldown = 2, 2

    def attack(self, oponent):
        f.attack(3, oponent, 'Zálabář')

    def special_attack(self, oponent):
        self.cooldown = f.attack(6, oponent, 'Zálabář', 2, self.cooldown, special=True)

    # Zálabář uses his unmatched speed to reduce his cooldown and attack the opponent at the same time
    def special(self, oponent):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            sg.popup('The following attack will decrease both of your cooldowns by 1')
            self.special_cooldown = f.attack(2, oponent, 'Zálabář', self.special_cooldown, special=True)
            self.cooldown -= 1
            self.special_cooldown -= 1


class Žeromán:
    def __init__(self):
        self.hp, self.max_hp = 15, 15
        self.defence, self.max_defence = 10, 10
        self.cooldown, self.special_cooldown = 2, 1
        
    def attack(self, oponent):
        f.attack(2, oponent, 'Žeromán')

    def special_attack(self, oponent):
        random_number = random.randrange(1, 11)
        self.cooldown = f.attack(random_number, oponent, 'Žeromán', 2, self.cooldown, special=True)

    # In the chaos of battle, Žeromán stops to have Beef Jerky and replenish his defence 
    def special(self):
        if self.special_cooldown > 0:
            sg.popup(f'You can use this ability in {self.special_cooldown} rounds!', title='Error')
        else:
            self.special_cooldown += 1
            self.defence = f.recovery_actions(self.defence, self.max_defence)
            s.already_played['Žeromán'] = True
            sg.popup('You recovered 2 of your defence points')


class Žimík:
    def __init__(self):
        self.hp, self.max_hp = 12, 12
        self.defence, self.max_defence = 4, 4
        self.cooldown, self.special_cooldown = 2, 2

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