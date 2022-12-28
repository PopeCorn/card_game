from Code import functions as f

class Tom:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 7
        self.max_energy = 7
        self.defence = 7
    
    def attack(self, oponent):
        f.attack(self.energy, 4, 4, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent)

    def heal(self, member=None, not_self=False):
        if self.energy < 2:
            print('You do not have enough energy!')
        else:
            self.energy -= 2
            if not_self:
                f.healing(member)
            else:
                f.healing(self)