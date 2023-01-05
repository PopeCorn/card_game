from Code import settings as s
import random
from colorama import Fore

# Basic function, enabling both players to choose their characters at the start of the game
def choose_character(player_list, number, available_list, all_list):
    for i in range(1, 4):
        while True:
                new_character = input(f'PLAYER {number}, select your new character (You will have 3 of them in total): ').lower()
                if (new_character in available_list):
                    if (new_character in all_list):
                        print(f'{Fore.RED}You or someone else already have that character!{Fore.RESET}')
                        continue
                    else:
                        print(f'{Fore.BLUE}{new_character.capitalize()} added! {Fore.RESET}')
                        player_list.append(new_character)
                        all_list.append(new_character)
                        break
                else:
                    print(f'{Fore.RED}That character is not available!{Fore.RESET}')
                    continue
    print(f'{Fore.BLUE}------------------------------------------------------------------------------------{Fore.RESET}')

# After action is done, values in the dictionary turn True
def initialize_dict(dictionary, list):
        for i in range(0, 6):
            dictionary[list[i]] = False

# Energy regeneration for all characters
def energy_regen(list):
    for character in list:
        character.energy = recovery_actions(character.energy, character.max_energy)

# Cooldowns reducing for all characters
def cooldowns(list):
    for character in list:
        if character.cooldown > 0:
            character.cooldown -= 1
        if character.special_cooldown > 0:
            character.special_cooldown -= 1

# Regeneration of attributes for all characters
def recovery_actions(attribute, max_attribute):
    if attribute == max_attribute or attribute == max_attribute - 1:
        attribute = max_attribute
    else:
        return attribute + 2
    return attribute


# Defence usage while defending from an attack
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

# Attack function, takes care of most crucial things before handing everything over to "attacking()"
def attack(energy, energy_taken, damage, defender, cooldown_increase=None, cooldown=None, special=False):
    if energy < energy_taken:
            print('You do not have enough energy!')
    else:
        if special:
            if cooldown > 0:
                print(f'You can use this ability in {cooldown} rounds!')
            else:
                cooldown += cooldown_increase
                energy -= energy_taken
                blow = damage - defender.defence
                attacking(defender, blow, damage)
        else:
            energy -= energy_taken
            blow = damage - defender.defence
            attacking(defender, blow, damage)


def initialize_attack(transfered, friendly_list, action):
     while True:
        oponent = input('Who do you want to attack: ')
        if oponent not in friendly_list:
            action(transfered[oponent])
            break
        else:
            print('That character is not in the game or is on your team!')
            continue

# Mojmir's double attack function, checking his every attack
def double_attack(doubled, not_doubled):
    if s.mojmir_double_damage is True:
        s.mojmir_double_damage  = False
        s.mojmir_attack = doubled
    else:
        s.mojmir_attack = not_doubled