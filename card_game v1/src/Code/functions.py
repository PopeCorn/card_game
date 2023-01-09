from Code import settings as s
import random


def both_players(player_playable, player_collection, player_number, wanted_index, enemy_collection):
    for character in player_playable:
        wanted_index += 1
        character_name = s.inverted_transfer[character]
        print(f'''
                                {character_name.upper()} turn
            
        ------------------------------------------------------------------------------------''')
        print(f'''  Player {player_number}, choose your action (TYPE ITS NUMBER):
        1. Attack
        2. Special attack
        3. Special action''')
        while True:
            action = input('Type here: ')
            if action == '1':
                initialize_attack(s.transfer, enemy_collection, character.attack)

            elif action == '2':
                initialize_attack(s.transfer, enemy_collection, character.special_attack)

            elif action == '3':
                inv = s.inverted_transfer[character]
                if inv == 'david' or inv == 'honza' or inv == 'mark' or inv == 'nikolas' or inv == 'mojmir':
                    character.special()
                elif inv == 'kvitek' or inv == 'matyas' or inv == 'milan' or inv == 'pavel' or inv == 'petr' or inv == 'zimik':
                    initialize_attack(s.transfer, enemy_collection, character.special)

                elif inv == 'tom':
                    while True:
                        healing = input('Do you want to heal yourself [1] or someone other[2] (Type the number): ')
                        if healing == '1':
                            character.special()
                            break
                        elif healing == '2':
                            while True:
                                member = input('Who do you want to heal: ')
                                if member in player_collection:
                                    character.special(s.transfer[member], not_self=True)
                                else:
                                    print('That player either does not exist or is not on your team!')
                                    continue
                                break
                            break
                        else:
                            print('That is not an option!')
                            continue
            else:
                print('That is not an option!')
                continue
            death_system(s.first_player_collection, s.first_player_playable, s.second_player_collection, s.second_player_playable)
            if s.end is True:
                print(f'The game has ended and the winner is {s.winner}!')
                exit()
            break
    wanted_index = -1


# Basic function, enabling both players to choose their characters at the start of the game
def choose_character(player_list, number):
    for i in range(1, 4):
        while True:
            new_character = input(f'PLAYER {number}, select your new character (You will have 3 of them in total): ').lower()
            if (new_character in s.available_characters):
                if (new_character in s.all_unplayable):
                    print('You or someone else already have that character!')
                    continue
                else:
                    print(f'{new_character.capitalize()} added!')
                    player_list.append(new_character)
                    s.all_unplayable.append(new_character)
                    break
            else:
                print(f'That character is not available!')
                continue
    print(f'------------------------------------------------------------------------------------')

# After action is done, values in the dictionary turn True
def initialize_dict(dictionary, list):
        for i in range(0, 6):
            dictionary[list[i]] = False

# Cooldowns reducing for all characters
def cooldowns():
    for character in s.all_playable:
        if character.cooldown > 0:
            character.cooldown -= 1
        if character.special_cooldown > 0:
            character.special_cooldown -= 1

# A short function for calling other ones
def calling_functions(inverted, character, first_player, second_player, first_playable, second_playable, name_1, name_2):
    removing_characters(inverted, character, first_player, first_playable)
    removing_characters(inverted, character, second_player, second_playable)
    winning(first_player, name_1)
    winning(second_player, name_2)

# A short function to determine who won
def winning(string, list):
    if len(list) == 0:
        s.end = True
        s.winner = string

# A function for removing dead characters
def removing_characters(unplayable, playable, unplayable_list, playable_list):
    if unplayable in unplayable_list:
        unplayable_list.remove(unplayable)
        playable_list.remove(playable)

# System checking for the death of characters
def death_system(first_player, first_playable, second_player, second_playable):
    for character in s.all_playable:
        inverted = s.inverted_transfer[character]
        if character.hp == 0:
            s.all_playable.remove(character)
            calling_functions(inverted, character, first_player, second_player, first_playable, second_playable, 'PLAYER 1', 'PLAYER 2')
        else:
            pass

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


def initialize_attack(transfered, enemy_list, action):
     while True:
        oponent = input('Who do you want to attack: ')
        if oponent in enemy_list:
            action(transfered[oponent])
            break
        else:
            print('That character is not in the game or is on your team!')
            continue

def making_playables(collection, playable, transfered):
    for not_transfered in collection:
        playable.append(transfered[not_transfered])

        
# Mojmir's double attack function, checking his every attack
def double_attack(doubled, not_doubled):
    if s.mojmir_double_damage is True:
        s.mojmir_double_damage  = False
        s.mojmir_attack = doubled
    else:
        s.mojmir_attack = not_doubled

# Checking if Matyas threw his poison at anybody during the last round
def poison_checking(name):
    if s.mata_poison is True:
        name.poison(s.mata_poison_target)
        s.mata_poison = False
    else:
        pass