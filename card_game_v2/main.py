import PySimpleGUI as sg
from Code import settings as s




def choose_character(collection):
    while True:
        if len(collection) == 3:
            sg.popup('That player already has 3 characters!')
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


layout = [[sg.Button('Add character for 1st player'), sg.Button('Add character for 2nd player'), sg.Button('Proceed'), sg.Button('Exit')]]

window = sg.Window('Card Game', layout)
window.BackgroundColor = 'green'

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'Add character for 1st player':
        choose_character(s.first_collection)
    elif event == 'Add character for 2nd player':
        choose_character(s.second_collection)

window.close()