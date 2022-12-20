class Honza:
    def __init__(self):
        self.hp = 10
        self.energy = 7
        self.defence = 1
        self.regeneration = 2

    def honza_attack(self, oponent):
        self.energy -= 3
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def honza_special(self, oponent):
        self.energy -= 6
        oponent.hp -= 1
        oponent.energy = 0

    def honza_energy_regeneration(self):
        if self.energy == 7:
            pass
        elif self.energy == 6:
            self.energy += 1
        else:
            self.energy += 2