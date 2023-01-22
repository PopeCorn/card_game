import PySimpleGUI as sg
from Code import settings as s

# Function for choosing characters from sg combo menu that is tied to the first while loop in main.py and is handling all situations that could happen
def choose_character(collection, character):
    while True:
        if len(collection) == 3:
            sg.popup('That player already has 3 characters!')
            break
        if character in s.all_available:
            if character in s.all_characters:
                sg.popup('You or someone else already have that character!')
            else:
                s.all_characters.append(character)
                collection.append(character)
                sg.popup('Character added')
        else:
            sg.popup('That character does not exist!')
        break

# Function that handles a character doing some action and using other functions such as init_attack()
def action(window2, character_name, enemy_collection):
    while True:
        event2, values2 = window2.read()
        character = s.transfer[character_name]
        layout3 = [[sg.Combo(enemy_collection, key='oponent'), sg.Button('Attack this enemy')]]
        window3 = sg.Window('Oponent', layout3, size=(300, 300))
        if event2 == sg.WIN_CLOSED:
            break
        if event2 == 'Select this':
            if values2['action'] == '':
                sg.popup('You have not selected your action yet!')
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
                s.already_played[character_name] = True
        window2.close()


# Function that checks if the input is empty or the character has already played, then passes the necessary arguments to action()
def playing(values, window2, key, enemy_collection):
    character_name = values[key]
    if character_name == '':
        sg.popup('You have not selected a character yet!')
    else:
        if s.already_played[character_name]:
            sg.popup('That character has already played this round!')
        else:
            window2.TKroot.title(character_name)
            action(window2, character_name, enemy_collection)

# Simple function for selecting an enemy (oponent) that the playing character is going to target
def init_attack(window3, action):
    while True:
        event3, values3 = window3.read()
        if event3 == sg.WIN_CLOSED:
            break
        elif event3 == 'Attack this enemy':
            if values3['oponent'] == '':
                sg.popup('You have not selected an enemy!')
                continue
            oponent = s.transfer[values3['oponent']]
            original_hp, original_defence = oponent.hp, oponent.defence
            print('oponent', values3['oponent'], 'hp', oponent.hp)
            action(oponent)
            sg.popup(f'''You attacked {values3['oponent']} with damage:
            HP: - {original_hp - oponent.hp}
            Defence: - {original_defence - oponent.defence}''')
            print('oponent', values3['oponent'], 'hp', oponent.hp)
            window3.close()
            break

# Simple function for finishing the process of converting strings to actual, playable characters (instances of classes)
def making_playables(collection, playable):
    for character in collection:
        playable.append(s.transfer[character])