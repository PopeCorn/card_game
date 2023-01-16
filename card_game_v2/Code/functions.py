import PySimpleGUI as sg
import settings as s

def choose_character(collection):
    while True:
        if len(collection) == 3:
            sg.popup('That player already has 3 characters!')
        else:
            character = sg.popup_get_text('Add a new character (write "exit" to quit)').lower()
            if character == 'exit':
                    break
            elif character in s.all_available:
                if character in s.all_characters:
                    sg.popup('You or someone else already have that character!')
                else:
                    s.all_characters.append(character)
                    collection.append(character)
                    break