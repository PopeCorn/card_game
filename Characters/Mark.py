class Marekec:
    def __init__(self):
        self.hp = 13
        self.energy = 7
        self.defence = 1
        self.regeneration = 2

    def marekec_attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def marekec_special(self, oponent):
        self.energy -= 6             # tady se taky domluvíme
        blow = 5 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0