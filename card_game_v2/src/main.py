import PySimpleGUI as sg
from Characters import David, Honza, Kvítek, Mark, Matyas, Milan, Mojmir, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
sg.theme('DarkTeal10')
layout = [[sg.Text('Add for 1st player'), sg.Button('Proceed'), sg.Button('Exit')],
[sg.Combo(['David', 'Honza', 'Kvítek', 'Mark', 'Matyáš', 'Milan', 'Mojmír', 'Nikolas', 'Pavel', 'Petr', 'Tom', 'Žimík'], key='first'), sg.Button('Add for 1st player')],
[sg.Text('Add for 2nd player')],
[sg.Combo(['David', 'Honza', 'Kvítek', 'Mark', 'Matyáš', 'Milan', 'Mojmír', 'Nikolas', 'Pavel', 'Petr', 'Tom', 'Žimík'], key='second'), sg.Button('Add for 2nd player')]]

window = sg.Window('Card Game - choose characters', layout, size=(500, 500))

if __name__ == '__main__':
    while True:
        event, values = window.read()
        if len(s.all_characters) == 6:
            s.choosing_finish = True
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        elif event == 'Proceed':
            if s.choosing_finish:
                break
            else:
                sg.popup('All players have not chosen their characters yet!')
        elif event == 'Add for 1st player':
            f.choose_character(s.first_collection, values['first'])
        elif event == 'Add for 2nd player':
            f.choose_character(s.second_collection, values['second'])
    print('first collection:', s.first_collection, '   second collection:', s.second_collection)

    for unused in s.all_characters:
        if unused == 'David':
            david = David.David()
            s.transfer['David'] = david
            s.all_playable.append(david)
        elif unused == 'Honza':
            honza = Honza.Honza()
            s.transfer['Honza'] = honza
            s.all_playable.append(honza)
        elif unused == 'Kvítek':
            kvitek = Kvítek.Kvitek()
            s.transfer['Kvítek'] = kvitek
            s.all_playable.append(kvitek)
        elif unused == 'Mark':
            mark = Mark.Marekec()
            s.transfer['Mark'] = mark
            s.all_playable.append(mark)
        elif unused == 'Matyáš':
            s.mata_here = True
            matyas = Matyas.Matyas()
            s.transfer['Matyáš'] = matyas
            s.all_playable.append(matyas)
        elif unused == 'Milan':
            milan = Milan.Milan()
            s.transfer['Milan'] = milan
            s.all_playable.append(milan)
        elif unused == 'Mojmír':
            mojmir = Mojmir.Mojmir()
            s.transfer['Mojmír'] = mojmir
            s.all_playable.append(mojmir)
        elif unused == 'Nikolas':
            nikolas = Nikolas.Nikolas()
            s.transfer['Nikolas'] = nikolas
            s.all_playable.append(nikolas)
        elif unused == 'Pavel':
            pavel = Pavel.Pavel()
            s.transfer['Pavel'] = pavel
            s.all_playable.append(pavel)
        elif unused == 'Petr':
            petr = Petr.Petr()
            s.transfer['Petr'] = petr
            s.all_playable.append(petr)
        elif unused == 'Tom':
            tom = Tom.Tom()
            s.transfer['Tom'] = tom
            s.all_playable.append(tom)
        elif unused == 'Žimík':
            zimik = Žimík.Zimik()
            s.transfer['Žimík'] = zimik
            s.all_playable.append(zimik)
        s.inv_transfer = {v: k for k, v in s.transfer.items()}

    exit()
    layout = [[sg.Button('Play'), sg.Button('Exit')]]
    window = sg.Window('Card Game - game', layout, background_color='#000000', size=(500, 50))
    while True:
        event, values = window.read()