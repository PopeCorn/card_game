class Honimír:
    def __init__(self):
        self.hp = 11
        self.energy = 8
        self.defence = 1
        self.regeneration = 2

    def honimír_attack(self, oponent):
        self.energy -= 2
        blow = 2 - oponent.defence
        oponent.hp -= blow

    def honimír_special(self, oponent):
        self.energy -= 7             # tady se taky domluvíme
        blow = 7 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0