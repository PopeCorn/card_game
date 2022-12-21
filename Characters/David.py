class David:
    def __init__(self):
        self.hp = 13
        self.energy = 8
        self.max_energy = 8
        self.defence = 1
        self.regeneration = 2

    def david_attack(self, oponent):
        self.energy -= 3
        blow = 2 - oponent.defence
        oponent.hp -= blow

    def david_special(self, oponent):
        self.energy -= 6             # tady se taky domluvíme
        blow = 6 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0