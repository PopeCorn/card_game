def regeneration(list):
    for character in list:
        if character.energy == character.max_energy or character.energy == character.max_energy - 1:
            character.energy = character.max_energy
        else:
            character.energy += 2


def attacking(target, attack, original_attack):
    if attack == 0:
        target.defence = 0
    elif attack < 0:
        target.defence -= original_attack
    else:
        target.hp -= attack
        target.defence = 0


def healing(character):
    if character.hp == character.max_hp or character.hp == character.max_hp - 1:
        character.hp = character.max_hp
    else:
        character.hp += 2
