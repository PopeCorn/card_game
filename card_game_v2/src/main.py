import PySimpleGUI as sg
from Characters import David, Honza, Kvítek, Mark, Matyas, Milan, Mojmir, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f

layout = [[sg.Text('Add character for 1st player'), sg.Text('Add character for 2nd player'), sg.Button('Proceed'), sg.Button('Exit')]]

window = sg.Window('Card Game - choose characters', layout, background_color='#617713', size=(500, 500))
window.add_row([sg.Button('Add David to 1st player'), sg.Button('Add David to 2nd player')], 
[sg.Button('Add David to 1st player'), sg.Button('Add David to 2nd player')], 
[sg.Button('Add Honza to 1st player'), sg.Button('Add Honza to 2nd player')], 
[sg.Button('Add Kvítek to 1st player'), sg.Button('Add Kvítek to 2nd player')], 
[sg.Button('Add Mark to 1st player'), sg.Button('Add Mark to 2nd player')], 
[sg.Button('Add Matyáš to 1st player'), sg.Button('Add Matyáš to 2nd player')], 
[sg.Button('Add Milan to 1st player'), sg.Button('Add Milan to 2nd player')], 
[sg.Button('Add Mojmír to 1st player'), sg.Button('Add Mojmír to 2nd player')], 
[sg.Button('Add Nikolas to 1st player'), sg.Button('Add Nikolas to 2nd player')], 
[sg.Button('Add Pavel to 1st player'), sg.Button('Add Pavel to 2nd player')], 
[sg.Button('Add Petr to 1st player'), sg.Button('Add Petr to 2nd player')], 
[sg.Button('Add Tom to 1st player'), sg.Button('Add Tom to 2nd player')],
[sg.Button('Add Žimík to 1st player'), sg.Button('Add Žimík to 2nd player')])

if __name__ == '__main__':
    while True:
        event, values = window.read()
        if len(s.all_characters) == 6:
            s.choosing_finish = True
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        # funkce na checkování jaké button bylo stisknuto(event)
        elif event == 'Proceed':
            if s.choosing_finish:
                break
            else:
                sg.popup('All players have not chosen their characters yet!')

    window.close()

    for unused in s.all_characters:
        if unused == 'david':
            david = David.David()
            s.transfer['david'] = david
            s.all_playable.append(david)
        elif unused == 'honza':
            honza = Honza.Honza()
            s.transfer['honza'] = honza
            s.all_playable.append(honza)
        elif unused == 'kvitek':
            kvitek = Kvítek.Kvitek()
            s.transfer['kvitek'] = kvitek
            s.all_playable.append(kvitek)
        elif unused == 'mark':
            mark = Mark.Marekec()
            s.transfer['mark'] = mark
            s.all_playable.append(mark)
        elif unused == 'matyas':
            s.mata_here = True
            matyas = Matyas.Matyas()
            s.transfer['matyas'] = matyas
            s.all_playable.append(matyas)
        elif unused == 'milan':
            milan = Milan.Milan()
            s.transfer['milan'] = milan
            s.all_playable.append(milan)
        elif unused == 'mojmir':
            mojmir = Mojmir.Mojmir()
            s.transfer['mojmir'] = mojmir
            s.all_playable.append(mojmir)
        elif unused == 'nikolas':
            nikolas = Nikolas.Nikolas()
            s.transfer['nikolas'] = nikolas
            s.all_playable.append(nikolas)
        elif unused == 'pavel':
            pavel = Pavel.Pavel()
            s.transfer['pavel'] = pavel
            s.all_playable.append(pavel)
        elif unused == 'petr':
            petr = Petr.Petr()
            s.transfer['petr'] = petr
            s.all_playable.append(petr)
        elif unused == 'tom':
            tom = Tom.Tom()
            s.transfer['tom'] = tom
            s.all_playable.append(tom)
        elif unused == 'zimik':
            zimik = Žimík.Zimik()
            s.transfer['zimik'] = zimik
            s.all_playable.append(zimik)
        s.inv_transfer = {v: k for k, v in s.transfer.items()}

    layout = [[sg.Button('Play'), sg.Button('Exit')]]
    window = sg.Window('Card Game - game', layout, background_color='#000000', size=(500, 50))
    while True:
        event, values = window.read()