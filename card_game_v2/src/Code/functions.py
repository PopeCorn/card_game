import PySimpleGUI as sg
from Code import settings as s

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

def making_playables(collection, playable):
    for character in collection:
        playable.append(s.transfer[character])

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
                    pass

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
            print('oponent', values3['oponent'], 'hp', oponent.hp)
            action(oponent)
            print('oponent', values3['oponent'], 'hp', oponent.hp)
            break