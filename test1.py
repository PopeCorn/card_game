import random


class Tom:
    def __init__(self):
        self.hp = 12
        self.attack = 4
        self.defence = 2
    def tom_attack(oponent):
        blow = Tom.attack - oponent.defence
        oponent.hp -= blow
    def tom_special(oponent):
        dice = random.randrange(0, 4)
        blow = Tom.attack + dice
        oponent.hp -= blow
    


        


        


