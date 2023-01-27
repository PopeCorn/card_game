import PySimpleGUI as sg
import random
from Code import settings as s

# Function for handling a character doing some action and using other functions such as init_attack()
def action(window2, character_name, enemy_collection):
    while True:
        event2, values2 = window2.read()
        character = s.transfer[character_name]
        layout3 = [[sg.Combo(enemy_collection, key='oponent'), sg.Button('Attack this enemy')],
        [sg.Button('Exit')]]
        window3 = sg.Window('Oponent', layout3)
        if event2 == sg.WIN_CLOSED or event2 == 'Exit':
            window2.close()
            break
        if event2 == 'Select this':
            if values2['action'] == '':
                sg.popup('You have not selected your action yet!', title='Error')
            else:
                window2.close()
                if values2['action'] == 'Normal attack':
                    init_attack(window3, character.attack)
                elif values2['action'] == 'Special attack':
                    init_attack(window3, character.special_attack)
                elif values2['action'] == 'Special action':
                    if character_name == 'David' or character_name == 'Honza' or character_name == 'Mark' or character_name == 'Nikolas' or character_name == 'Mojmír':
                        character.special()
                    else:
                        init_attack(window3, character.special)

# Function for finishing the process of converting strings to actual, playable characters (instances of classes)
def adding_playables(collection, playable, collection2, playable2):
    simplifying(collection, playable)
    simplifying(collection2, playable2)

# Function for initializing s.already_played dictionary
def already_played_false():
    for character in s.all_characters:
        s.already_played[character] = False

# Function for checking if the attack is special, calculating the actual blow and passing arguments to attacking()
def attack(damage, defender, character_name, cooldown_increase=None, cooldown=None, special=False):
    if special:
        if cooldown > 0:
            sg.popup(f'You can use this ability in {cooldown} rounds!', title='Error')
        else:
            blow = damage - defender.defence
            attacking(defender, blow, damage, character_name)
            return cooldown + cooldown_increase
    else:
        blow = damage - defender.defence
        attacking(defender, blow, damage, character_name)
    return cooldown

# Function for the finishing of attack, calculating defence and special effect
def attacking(target, attack, original_attack, character_name):
    target_name = s.inv_transfer[target]
    if target_name == "David":
        if s.david_defence is True:
            s.david_defence = False
            attack -= 3
            original_attack -= 3
        else:
            pass
    elif target_name == "Mark":
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

    original_hp, original_defence = target.hp, target.defence
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
    s.already_played[character_name] = True
    sg.popup(f'''You attacked {target_name} with damage:
            HP: - {original_hp - target.hp}
            Defence: - {original_defence - target.defence}''')

# Function for calling other ones
def calling_functions(character, first_collection, second_collection, first_playable, second_playable, name_1, name_2):
    removing_characters(character, first_collection, first_playable)
    removing_characters(character, second_collection, second_playable)
    winning(first_collection, name_1)
    winning(second_collection, name_2)

# Function for choosing characters from sg combo menu that is tied to the first while loop in main.py and is handling all situations that could happen
def choose_character(collection, character):
    if len(collection) == 3:
        sg.popup('That player already has 3 characters!', title='Error')
    if character in s.all_available:
        if character in s.all_characters:
            sg.popup('You or someone else already have that character!', title='Error')
        else:
            s.all_characters.append(character)
            collection.append(character)
            sg.popup(f'{character} added', title='Addition')
    else:
        sg.popup('That character does not exist!', title='Error')

# Function for checking for the death of characters
def death_system(character, first_collection, first_playable, second_collection, second_playable):
    sg.popup(f'{s.inv_transfer[character]} is dead')
    s.all_playable.remove(character)
    calling_functions(character, first_collection, second_collection, first_playable, second_playable, 'PLAYER 1', 'PLAYER 2')

# Function for Mojmir's attack
def double_attack(doubled, not_doubled):
    if s.mojmir_double_damage is True:
        s.mojmir_double_damage  = False
        s.mojmir_attack = doubled
    else:
        s.mojmir_attack = not_doubled

# Function finishing the attacking process with new functions and handling it over to old functions, taken from v1 and slightly modified
def init_attack(window3, action):
    while True:
        event3, values3 = window3.read()
        if event3 == sg.WIN_CLOSED or event3 == 'Exit':
            window3.close()
            break
        elif event3 == 'Attack this enemy':
            if values3['oponent'] == '':
                sg.popup('You have not selected an enemy!', title='Error')
                continue
            oponent = s.transfer[values3['oponent']]
            action(oponent)
            window3.close()
            break

# Function for making layouts (PySimpleGUI)
def layout(layout, choose_characters=False, game=False, action=False):
    if choose_characters:
        layout = [[sg.Button('Proceed to the game')],
            [sg.Combo(['David', 'Honza', 'Kvítek', 'Mark', 'Matyáš', 'Milan', 'Mojmír', 'Nikolas', 'Pavel', 'Petr', 'Tom', 'Žimík'], key='first'), sg.Button('Add for 1st player')],
            [sg.Combo(['David', 'Honza', 'Kvítek', 'Mark', 'Matyáš', 'Milan', 'Mojmír', 'Nikolas', 'Pavel', 'Petr', 'Tom', 'Žimík'], key='second'), sg.Button('Add for 2nd player')],
            [sg.Text('(ONE PLAYER CAN ONLY HAVE 3 CHARACTERS)'), sg.Button('Exit')]]
    elif game:
        layout = [[sg.Text('ROUND 1', key='IN', text_color='Red')],
            [sg.Text('1st player')],
            [sg.Combo(s.first_collection, key='1stplayer_character'), sg.Button('1st player - Play with this character')],
            [sg.Text('                '), sg.Button('1st player - Check this character')],
            [sg.Text('')],
            [sg.Text('2nd player')],
            [sg.Combo(s.second_collection, key='2ndplayer_character'), sg.Button('2nd player - Play with this character')],
            [sg.Text('                '), sg.Button('2nd player - Check this character')],
            [sg.Text('')],
            [sg.Button('NEXT ROUND!'), sg.Text('(Press when all characters have played)')],
            [sg.Text('')],
            [sg.Button('Exit')]]
    elif action:
        layout = [[sg.Button('Select this'), sg.Combo(['Normal attack', 'Special attack', 'Special action'], key='action')],
            [sg.Button('Exit')]]
    return layout

# Function for handling processing to next round
def next_round(window, res):
    if res:
        for unbound in s.all_characters:
            s.already_played[unbound] = False
        for character in s.all_playable:
            character.cooldown -= 1
            character.special_cooldown -= 1
        if s.mata_here:
            poison_checking()
        s.count += 1
        sg.popup(f'Round {s.count} Begins!')
        window.TKroot.title(f'Card Game - Round {s.count}')
        window['IN'].update(f'ROUND {s.count}', text_color='Red')
    else:
        sg.popup('All characters have not played yet!')
    return window

# Function for checking if the input is empty or the character has already played, then passing the necessary arguments to action()
def playing(values, window2, key, enemy_collection):
    character_name = values[key]
    if character_name == '':
        sg.popup('You have not selected a character yet!', title='Error')
    else:
        if s.already_played[character_name]:
            sg.popup('That character has already played this round!', title='Error')
        else:
            window2.TKroot.title(character_name)
            action(window2, character_name, enemy_collection)

# Function for checking if Mata has applied his poison
def poison_checking():
    if s.mata_poison is True:
        s.mata_poison_target.hp -= 2
        s.mata_poison = False
        sg.popup(f"Matyáš's poison from the last round reduced {s.inv_transfer[s.mata_poison_target]}'s hp by 2")
    else:
        pass

# Function for regeneration of attributes for all characters
def recovery_actions(attribute, max_attribute):
    if attribute == max_attribute or attribute == max_attribute - 1:
        attribute = max_attribute
    else:
        return attribute + 2
    return attribute

# Function for removing dead characters
def removing_characters(playable, unplayable_list, playable_list):
    if playable in playable_list:
        unplayable_list.remove(s.inv_transfer[playable])
        playable_list.remove(playable)

# Function for the actual adding of playables
def simplifying(collection, playable):
    for character in collection:
        playable.append(s.transfer[character])

# Function for checking character's stats
def stat_checking(character_name):
    character = s.transfer[character_name]
    sg.popup(f'''{character_name.upper()}:
    HP - {character.hp}
    Defence - {character.defence}
    Special Attack cooldown - {character.cooldown}
    Special Action cooldown - {character.special_cooldown}''', title=f"{character_name}'s stats")

# Function for determining who won
def winning(string, list):
    if len(list) == 0:
        s.end = True
        s.winner = string