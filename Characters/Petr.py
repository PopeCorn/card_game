class Petr:
    def __init__(self):
        self.hp = 11
        self.energy = 7
        self.defence = 1
        self.regeneration = 2

    def petr_attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def petr_special(self, oponent):
        self.energy -= 6             # tady se taky domluvíme
        blow = 5 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0