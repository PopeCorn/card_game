import PySimpleGUI as sg
import random
from Code import settings as s

# Function for handling a character doing some action and using other functions such as init_attack()
def action(window2, character_name, enemy_collection):
    while True:
        event2, values2 = window2.read()
        # The name passed to the function is used as a key to access the playable version
        character = s.transfer[character_name]

        # Layout and window creation for selecting an opponent
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
                # The player has selected an action, so window2 (which is for selecting an action) can be closed
                window2.close()

                # Checking which action has been selected and calling other functions according to it
                if values2['action'] == 'Normal attack':
                    init_attack(window3, character.attack)
                elif values2['action'] == 'Special attack':
                    init_attack(window3, character.special_attack)
                elif values2['action'] == 'Special action':
                    if character_name == 'Big Chungus' or character_name == 'Anus' or character_name == 'Marekec' or character_name == 'Žeromán' or character_name == 'Mojmi-chan':
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
    # Getting the name of the target using the s.inv_transfer dictionary for calculating if any special effects affect the attack
    target_name = s.inv_transfer[target]
    if target_name == "Big Chungus":
        if s.chungus_defence is True:
            s.chungus_defence = False
            attack -= 3
            original_attack -= 3
        else:
            pass
    elif target_name == "Marekec":
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
    
    # Saving original attributes before the attack changes them, so they can be used in the results window
    original_hp, original_defence = target.hp, target.defence

    # Calculating the damage to the target and after that, making the character unplayable for the rest of the current round
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
    
    # The results window, showing what damage was dealt
    sg.popup(f'''You attacked {target_name} with damage:
            HP: - {original_hp - target.hp}
            Defence: - {original_defence - target.defence}''')

# Function for calling other ones
def calling_functions(character, first_collection, second_collection, first_playable, second_playable, name_1, name_2):
    removing_characters(character, first_collection, first_playable)
    removing_characters(character, second_collection, second_playable)
    winning(first_collection, name_2)
    winning(second_collection, name_1)

# Function for checking if any character has died and updating the layout if yes
def checking_for_dead(layout):
    for character in s.all_playable:
        if character.hp <= 0:
            death_system(character, s.first_collection, s.first_playable, s.second_collection, s.second_playable)
            layout = layout(layout, game=True)

# Function for choosing characters from sg combo menu that is tied to the first while loop in main.py and is handling all situations that could happen
def choose_character(collection, character):
    # Making sure a player can't have more than 3 characters on their team
    if len(collection) == 3:
        sg.popup('That player already has 3 characters!', title='Error')
    else:
        # Handling the actual adding of characters to the team
        if character in s.all_available:
            if character in s.all_characters:
                sg.popup('You or someone else already have that character!', title='Error')
            else:
                s.all_characters.append(character)
                collection.append(character)
                sg.popup(f'{character} added', title='Addition')
        else:
            sg.popup('That character does not exist!', title='Error')

# Function for showing who died and passing the right attributes to calling_functions(), so the character gets deleted
def death_system(character, first_collection, first_playable, second_collection, second_playable):
    sg.popup(f'{s.inv_transfer[character]} is dead')
    s.all_playable.remove(character)
    calling_functions(character, first_collection, second_collection, first_playable, second_playable, 'PLAYER 1', 'PLAYER 2')

# Function for checking if Mojmi-chan's attack is doubled by his Special Action
def double_attack(doubled, not_doubled):
    if s.mojmi_chan_double_damage is True:
        s.mojmi_chan_double_damage  = False
        s.mojmi_chan_attack = doubled
    else:
        s.mojmi_chan_attack = not_doubled

# Function finishing the attacking process with new functions and handling it over to old functions, taken from v1 and slightly modified
def init_attack(window3, action):
    while True:
        event3, values3 = window3.read()
        if event3 == sg.WIN_CLOSED or event3 == 'Exit':
            window3.close()
            break

        # Selecting a target
        elif event3 == 'Attack this enemy':
            if values3['oponent'] == '':
                sg.popup('You have not selected an enemy!', title='Error')
                continue

            # Using the opponent's name to access its playable version, then passing that version to the actual function of one of the characters in Characters/
            oponent = s.transfer[values3['oponent']]
            action(oponent)

            # Closing the window as the opponent has been selected
            window3.close()
            break
    
# Function for checking if all characters have played and returning "res" which determines if next round starts or not in the main.py
def is_next_round(played, res):
    for playable in played:
        if playable is False:
            res = False
            break
    return res

# Function for making layouts (PySimpleGUI)
def layout(layout, choose_characters=False, game=False, action=False):

    # Layout for choosing characters in the first phase of the game
    if choose_characters:
        layout = [[sg.Button('Proceed to the game')],
            [sg.Combo(s.all_available, key='first'), sg.Button('Add for 1st player')],
            [sg.Combo(s.all_available, key='second'), sg.Button('Add for 2nd player')],
            [sg.Text('(ONE PLAYER CAN ONLY HAVE 3 CHARACTERS)'), sg.Button('Exit')]]

    # Layout which is used for the rest of the game after the choose_charactesr one, showing what round it is and giving players the option to play with whatever character they chose in the first phase
    elif game:
        layout = [[sg.Text(f'ROUND {s.count}', key='IN', text_color='Red')],
            [sg.Text('1st player')],
            [sg.Combo(s.first_collection, key='1stplayer_character'), sg.Button('1st player - Play with this character')],
            [sg.Button('1st player - Check this character')],
            [sg.Text('')],
            [sg.Text('2nd player')],
            [sg.Combo(s.second_collection, key='2ndplayer_character'), sg.Button('2nd player - Play with this character')],
            [sg.Button('2nd player - Check this character')],
            [sg.Text('')],
            [sg.Button('NEXT ROUND!'), sg.Text('(Press when all characters have played)')],
            [sg.Text('')],
            [sg.Button('Exit')]]

    # Simple layout for selecting a target for an attack
    elif action:
        layout = [[sg.Button('Select this'), sg.Combo(['Normal attack', 'Special attack', 'Special action'], key='action')],
            [sg.Button('Exit')]]
    return layout

# Function for handling processing to next round, taking the "res" variable that has been changed in is_next_round() according to the situation
def next_round(window, res):
    if res:
        # Allowing all characters to play once again, reducing their cooldowns
        for unbound in s.all_characters:
            s.already_played[unbound] = False
        for character in s.all_playable:
            character.cooldown -= 1
            character.special_cooldown -= 1
        
        # Checking if Máta threw his poison at someone the last round
        if s.mata_here:
            poison_checking()

        # Updating the actual round count in settings.py, changing the round name in the main loop
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
        window2.close()
    else:
        if s.already_played[character_name]:
            sg.popup('That character has already played this round!', title='Error')
            window2.close()
        else:
            # Settings the character's name as the title of his action selection window
            window2.TKroot.title(character_name)
            action(window2, character_name, enemy_collection)

# Function for checking if Máta has applied his poison
def poison_checking():
    if s.mata_poison is True:
        s.mata_poison_target.hp -= 2
        s.mata_poison = False
        sg.popup(f"Matyáš's poison from the last round reduced {s.inv_transfer[s.mata_poison_target]}'s hp by 2")
    else:
        pass

# Function for the regeneration of hp and defence
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

# Function for determining who won, checking if 
def winning(list, string):
    if len(list) == 0:
        s.end = True
        s.winner = string