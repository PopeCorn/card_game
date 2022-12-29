from Code import functions as f
from Code import settings as s

class Kvitek:
    def __init__(self):
        self.hp = 11
        self.max_hp = 11
        self.energy = 9
        self.max_energy = 9
        self.defence = 5

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 7, 5, oponent)

    def ultimate(self, oponent):
        if s.count > 5 and s.kvitek_ultimate is not True:
            oponent.hp = 0
            self.energy = 0
            s.kvitek_ultimate = True
        else:
            print('You can use this ability only once and the game has to be over 24 rounds long!')

