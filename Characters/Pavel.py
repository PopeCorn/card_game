class Pavel:
    def __init__(self):
        self.hp = 10
        self.energy = 8
        self.defence = 1
        self.regeneration = 2

    def pavel_attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def pavel_special(self, oponent):
        self.energy -= 7            # tady se taky domluvíme
        blow = 8 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0