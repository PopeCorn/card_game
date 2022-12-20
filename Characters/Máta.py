class Matyas:
    def __init__(self):
        self.hp = 12
        self.energy = 7
        self.defence = 1
        self.regeneration = 2

    def matyas_attack(oponent):
        Matyas.energy -= 3
        blow = 4 - oponent.defence
        oponent.hp -= blow

    def matyas_special(oponent):
        Matyas.energy -= 6             # Tady se taky domluvíme
        blow = 5 - oponent.defence
        oponent.hp -= blow

    def matyas_energy_regeneration(self):
        if self.energy == 7:
            pass
        elif self.energy == 6:
            self.energy += 1
        else:
            self.energy += 2