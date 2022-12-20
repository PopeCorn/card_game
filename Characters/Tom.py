import random


class Tom:
    def __init__(self):
        self.hp = 12
        self.attack = 6
        self.defence = 2
    def tom_attack(oponent):
        blow = Tom.attack - oponent.defence
        oponent.hp -= blow
    def tom_special(oponent):
        dice = random.randrange(0, 6)
        blow = Tom.attack + dice
        oponent.hp -= blow
    def tom_heal():
        restore = random.randrange(0, 4)
        Tom.hp += restore
    def tom_heal_team(member):
        heal = random.randrange(0, 4)
        member.hp += heal


        


        


