class Kvitek:
    def __init__(self):
        self.hp = 11
        self.energy = 9
        self.defence = 1
        self.regeneration = 2

    def kvitek_attack(self, oponent):
        self.energy -= 4
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def kvitek_special(self, oponent):
        self.energy -= 7             # tady se taky domluvíme
        blow = 5 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0