import PySimpleGUI as sg
from Code import settings as s
from Code import functions as f

layout = [[sg.Button('Add character for 1st player'), sg.Button('Add character for 2nd player'), sg.Button('Proceed'), sg.Button('Exit')]]

window = sg.Window('Card Game', layout)
window.BackgroundColor = 'green'

while True:
    event, values = window.read()
    if len(s.all_characters) == 6:
        s.choosing_finish = True
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'Add character for 1st player':
        f.choose_character(s.first_collection)
    elif event == 'Add character for 2nd player':
        f.choose_character(s.second_collection)
    elif event == 'Proceed':
        if s.choosing_finish:
            break
        else:
            sg.popup('All players have not chosen their characters yet!')

window.close()