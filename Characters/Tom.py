from Code import functions as f

class Tom:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 7
        self.max_energy = 7
        self.defence = 1
        self.regeneration = 2
    
    def attack(self, oponent):
        self.energy -= 4
        blow = 4 - oponent.defence
        f.attacking(oponent, blow, 4)
    
    def special(self, oponent):
        self.energy -= 6
        blow = 5 - oponent.defence
        f.attacking(oponent, blow, 5)

    def heal(self):
        self.energy -= 1
        f.healing(self)