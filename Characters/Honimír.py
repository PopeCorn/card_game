class Honimír:
    def __init__(self):
        self.hp = 11
        self.energy = 8
        self.defence = 1
        self.regeneration = 2

    def honimír_attack(oponent):
        Honimír.energy -= 2
        blow = 2 - oponent.defence
        oponent.hp -= blow

    def honimír_special(oponent):
        Honimír.energy -= 7
        blow = 7 - oponent.defence
        oponent.hp -= blow

    def honimír_energy_regeneration(self):
        if self.energy == 8:
            pass
        elif self.energy == 7:
            self.energy += 1
        else:
            self.energy += 2