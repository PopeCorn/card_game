class marekec:
    def __init__(self):
        self.hp = 13
        self.energy = 7
        self.defence = 1
        self.regeneration = 2

    def marekec_attack(oponent):
        marekec.energy -= 3
        blow = 3 - oponent.defence
        oponent.hp -= blow

    def marekec_special(oponent):
        marekec.energy -= 6            # tady se pak taky domluvíme
        blow = 5 - oponent.defence
        oponent.hp -= blow

    def marekec_energy_regeneration(self):
        if self.energy == 9:
            pass
        elif self.energy == 8:
            self.energy += 1
        else:
            self.energy += 2