from Code import functions as f

class Tom:
    def __init__(self):
        self.hp, self.max_hp = 10, 10
        self.energy, self.max_energy = 7, 7
        self.defence = 7
        self.cooldown, self.special_cooldown = 0, 0

    def attack(self, oponent):
        self.energy = f.attack(self.energy, 4, 4, oponent)

    def special_attack(self, oponent):
        self.energy, self.cooldown = f.attack(self.energy, 6, 5, oponent, 2, self.cooldown, special=True)

    # Tom stays behind friendly lines, ready to heal others or himself
    def special(self, member=None, not_self=False):
        if self.special_cooldown > 0:
            print(f'You can use this ability in {self.special_cooldown} rounds!')
        else:
            if self.energy < 3:
                print('You do not have enough energy!')
            else:
                self.energy -= 3
                self.special_cooldown += 1
                if not_self:
                    member.hp = f.recovery_actions(member.hp, member.max_hp)
                else:
                    self.hp = f.recovery_actions(self.hp, self.max_hp)