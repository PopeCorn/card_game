from Code import functions as f

class Tom:
    def __init__(self):
        self.hp = 10
        self.max_hp = 10
        self.energy = 7
        self.max_energy = 7
        self.defence = 7
        self.cooldown = 0
        self.special_cooldown = 0
    
    def attack(self, oponent):
        f.attack(self.energy, 4, 4, oponent)

    def special_attack(self, oponent):
        f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    # Tom stays behind friendly lines, ready to heal others or himself
    def special(self, member=None, not_self=False):
        f.recovery_actions(self.hp, self.max_hp)
        #if self.special_cooldown > 0:
         #   print(f'You can use this ability in {self.special_cooldown} rounds!')
        #else:
         #   if self.energy < 3:
          #      print('You do not have enough energy!')
           # else:
            #    self.energy -= 3
             #   self.special_cooldown += 1
              #  if not_self:
               #     f.healing(member)
                #else:
                 #   f.healing(self)