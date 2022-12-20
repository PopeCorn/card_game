class Zimik:
    def __init__(self):
        self.hp = 12
        self.energy = 10
        self.defence = 1
        self.regeneration = 2

    def zimik_attack(self, oponent):
        self.energy -= 4
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def zimik_special(self, oponent):
        self.energy -= 6             # tady se taky domluvíme
        blow = 5 - oponent.defence
        oponent.hp -= blow

    def zimik_energy_regeneration(self):
        if self.energy == 10:
            pass
        elif self.energy == 9:
            self.energy += 1
        else:
            self.energy += 2