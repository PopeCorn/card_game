class Milan:
    def __init__(self):
        self.hp = 15
        self.energy = 10
        self.defence = 1
        self.regeneration = 2

    def milan_attack(self, oponent):
        self.energy -= 4
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def milan_special(self, oponent):
        self.energy -= 7            # tady se taky domluvíme
        blow = 5 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0