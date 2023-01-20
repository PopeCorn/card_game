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

def action(window, character_name):
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Select this':
            if values['action'] == 'Normal Attack':
                pass
            if values['action'] == 'Special Attack':
                pass
            if values['action'] == 'Special Action':
                pass