from Code import functions as f

class Zimik:
    def __init__(self):
        self.hp = 12
        self.max_hp = 12
        self.energy = 10
        self.max_energy = 10
        self.defence = 2

    def attack(self, oponent):
        f.attack(self.energy, 4, 3, oponent)

    def special(self, oponent):
        f.attack(self.energy, 6, 5, oponent)

    def heal(self):
        self.energy -= 1
        f.healing(self)
        # předělat heal na to, že tato postava může permanentně snížit něčí max. energy o 2 a obnovit si 2 defence.