# Zatím jenom základní funkce regenerace, později main.py doděláme
def regeneration(list):
    for character in list:
        if character.energy == character.max_energy or character.energy == character.max_energy - 1:
            character.energy = character.max_energy
        else:
            character.energy += 2