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

def action(window, character_name, enemy_collection):
    while True:
        character = s.transfer[character_name]
        event, values = window.read()
        layout3 = [[sg.Combo(enemy_collection, key='oponent'), sg.Button('Attack this enemy')]]
        window3 = sg.Window('Oponent', layout3, size=(300, 300))
        if event == sg.WIN_CLOSED:
            break
        if event == 'Select this':
            if values['action'] == 'Normal attack':
                while True:
                    event2, values2 = window3.read()
                    if event2 == sg.WIN_CLOSED:
                        break
                    elif event2 == 'Attack this':
                        oponent = s.transfer[values2['oponent']]
                        character.attack(oponent)
            if values['action'] == 'Special attack':
                pass
            if values['action'] == 'Special action':
                pass