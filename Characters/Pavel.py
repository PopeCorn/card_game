class Pavel:
    def __init__(self):
        self.hp = 10
        self.energy = 8
        self.defence = 1
        self.regeneration = 2

    def pavel_attack(oponent):
        Pavel.energy -= 3
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def pavel_special(oponent):
        Pavel.energy -= 7
        blow = 8 - oponent.defence
        oponent.hp -= blow

    def pavel_energy_regeneration(self):
        if self.energy == 8:
            pass
        elif self.energy == 7:
            self.energy += 1
        else:
            self.energy += 2