class Tom:
    def __init__(self):
        self.hp = 10
        self.energy = 7
        self.defence = 1
        self.regeneration = 2
    
    def tom_attack(self, oponent):
        self.energy -= 4
        blow = 4 - oponent.defence
        oponent.hp -= blow
    
    def tom_special(self, oponent):
        self.energy -= 6             # tady se taky domluvíme
        blow = 5 - oponent.defence
        if blow == 0:
            oponent.defence = 0
        elif blow > 0:
            oponent.defence -= blow
        else:
            oponent.hp -= blow
            oponent.defence = 0