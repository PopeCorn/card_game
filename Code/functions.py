import settings as s
import random

def regeneration(list):
    for character in list:
        if character.energy == character.max_energy or character.energy == character.max_energy - 1:
            character.energy = character.max_energy
        else:
            character.energy += 2


def attacking(target, attack, original_attack):
    if target == "david":
        if s.david_defence is True:
            s.david_defence = False
            attack -= 3
            original_attack -= 3
        else:
            pass
    elif target == "marekec":
        if s.marekec_dodge is True:
            s.marekec_dodge = False
            number = random.randrange(1, 3)
            if number == 1:
                original_attack = 0
                attack = -1
            else:
                pass
        else:
            pass
    if attack == 0:
        target.defence = 0
    elif attack < 0:
        if original_attack == 0 or original_attack < 0:
            pass
        else:
            target.defence -= original_attack
    else:
        target.hp -= attack
        target.defence = 0


def attack(energy, energy_taken, damage, defender):
    if energy < energy_taken:
            print('You do not have enough energy!')
    else:
        energy -= energy_taken
        blow = damage - defender.defence
        attacking(defender, blow, damage)

def healing(character):
    if character.hp == character.max_hp or character.hp == character.max_hp - 1:
        character.hp = character.max_hp
    else:
        character.hp += 2

def double_attack(doubled, not_doubled):
    if s.mojmir_double_damage is True:
        s.mojmir_double_damage  = False
        s.mojmir_attack = doubled
    else:
        s.mojmir_attack = not_doubled
