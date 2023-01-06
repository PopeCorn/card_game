from Code import functions as f
from Code import settings as s

class Kvitek:
    def __init__(self):
        self.hp, self.max_hp = 11, 11
        self.energy, self.max_energy = 9, 9
        self.defence = 5
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def special_attack(self, oponent):
        f.attack(self.energy, 7, 5, oponent, 2, self.cooldown, special=True)

    # After a long preparation, Kvitek unleashes his sigma male grindset upon one unsuspecting enemy, killing them instantly
    def special(self, oponent):
        if s.count > 6 and s.kvitek_ultimate is not True:
            oponent.hp = 0
            self.energy = 0
            s.kvitek_ultimate = True
        else:
            print('You can use this ability only once and the game has to be over 24 rounds long!')

