class Tom:
    def __init__(self):
        self.hp = 10
        self.energy = 7
        self.defence = 1
        self.regeneration = 2
    
    def tom_attack(oponent):
        Tom.energy -= 4
        blow = 4 - oponent.defence
        oponent.hp -= blow
    
    def tom_special(oponent):
        Tom.energy -= 6
        blow = 5 - oponent.defence
        oponent.hp -= blow
    def tom_energy_regeneration(self):
        if self.energy == 7:
            pass
        elif self.energy == 6:
            self.energy += 1
        else:
            self.energy += 2