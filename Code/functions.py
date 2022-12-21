def regeneration(list):
    for character in list:
        if character.energy == character.max_energy or character.energy == character.max_energy - 1:
            character.energy = character.max_energy
        else:
            character.energy += 2


def attacking(target, attack):
    if attack == 0:
        target.defence = 0
    elif attack < 0:
        target.defence -= attack
    else:
        target.hp -= attack
        target.defence = 0