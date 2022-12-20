class David:
    def __init__(self):
        self.hp = 13
        self.energy = 8
        self.defence = 1
        self.regeneration = 2

    def david_attack(oponent):
        David.energy -= 3
        blow = 2 - oponent.defence
        oponent.hp -= blow

    def david_special(oponent):
        David.energy -= 6
        blow = 6 - oponent.defence
        oponent.hp -= blow

    def david_energy_regeneration(self):
        if self.energy == 8:
            pass
        elif self.energy == 7:
            self.energy += 1
        else:
            self.energy += 2