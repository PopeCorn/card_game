from Code import functions as f

class Tom:
    def __init__(self):
        self.hp = 10
        self.energy = 7
        self.max_energy = 7
        self.defence = 1
        self.regeneration = 2
    
    def tom_attack(self, oponent):
        self.energy -= 4
        blow = 4 - oponent.defence
        f.attacking(oponent, blow)
    
    def tom_special(self, oponent):
        self.energy -= 6
        blow = 5 - oponent.defence
        f.attacking(oponent, blow)