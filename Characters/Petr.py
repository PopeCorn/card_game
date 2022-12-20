class Petr:
    def __init__(self):
        self.hp = 11
        self.energy = 7
        self.defence = 1
        self.regeneration = 2

    def petr_attack(oponent):
        Petr.energy -= 3
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def petr_special(oponent):
        Petr.energy -= 6            # tady se taky domluvíme
        blow = 5 - oponent.defence
        oponent.hp -= blow

    def petr_energy_regeneration(self):
        if self.energy == 7:
            pass
        elif self.energy == 6:
            self.energy += 1
        else:
            self.energy += 2