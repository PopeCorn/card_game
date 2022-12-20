class Kvitek:
    def __init__(self):
        self.hp = 11
        self.energy = 9
        self.defence = 1
        self.regeneration = 2

    def kvitek_attack(self, oponent):
        self.energy -= 4
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def kvitek_special(self, oponent):
        self.energy -= 7          # Pak se domluvíme jak to uděláme
        blow = 5 - oponent.defence
        oponent.hp -= blow

    def kvitek_energy_regeneration(self):
        if self.energy == 9:
            pass
        elif self.energy == 8:
            self.energy += 1
        else:
            self.energy += 2