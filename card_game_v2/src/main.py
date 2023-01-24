import PySimpleGUI as sg
from Characters import David, Honza, Kvítek, Mark, Matyas, Milan, Mojmir, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
sg.theme('DarkTeal10')

layout = [[sg.Button('Proceed to the game')],
[sg.Combo(['David', 'Honza', 'Kvítek', 'Mark', 'Matyáš', 'Milan', 'Mojmír', 'Nikolas', 'Pavel', 'Petr', 'Tom', 'Žimík'], key='first'), sg.Button('Add for 1st player')],
[sg.Combo(['David', 'Honza', 'Kvítek', 'Mark', 'Matyáš', 'Milan', 'Mojmír', 'Nikolas', 'Pavel', 'Petr', 'Tom', 'Žimík'], key='second'), sg.Button('Add for 2nd player')],
[sg.Text('(ONE PLAYER CAN ONLY HAVE 3 CHARACTERS)'), sg.Button('Exit')]]

window = sg.Window('Card Game - choose characters', layout, size=(380, 150))

if __name__ == '__main__':
    while True:
        event, values = window.read()
        if len(s.all_characters) == 6:
            s.choosing_finish = True
        if event == 'Exit' or event == sg.WIN_CLOSED:
            quit()
        elif event == 'Proceed to the game':
            if s.choosing_finish:
                break
            else:
                sg.popup('All players have not chosen their characters yet!', title='Error')
        elif event == 'Add for 1st player':
            f.choose_character(s.first_collection, values['first'])
        elif event == 'Add for 2nd player':
            f.choose_character(s.second_collection, values['second'])
    window.close()

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

    f.making_playables(s.first_collection, s.first_playable)
    f.making_playables(s.second_collection, s.second_playable)

    for unbound in s.all_characters:
            s.already_played[unbound] = False

    layout = [[sg.Text('ROUND 1', key='IN', text_color='Red')],
        [sg.Text('1st player')],
        [sg.Combo(s.first_collection, key='1stplayer_character'), sg.Button('1st player - Play with this character')],
        [sg.Text('                '), sg.Button('1st player - Check this character')],
        [sg.Text('')],
        [sg.Text('2nd player')],
        [sg.Combo(s.second_collection, key='2ndplayer_character'), sg.Button('2nd player - Play with this character')],
        [sg.Text('                '), sg.Button('2nd player - Check this character')],
        [sg.Text('')],
        [sg.Button('NEXT ROUND!'), sg.Text('(Press when all characters have played)')],
        [sg.Text('')],
        [sg.Button('Exit')]]
    window = sg.Window('Card Game - Round 1', layout, size=(500, 500))

    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            quit()
        if s.end:
            sg.popup(f'THE WINNER IS {s.winner}!')
            quit()
        else:
            f.death_system(s.first_collection, s.first_playable, s.second_collection, s.second_playable, window)
        if event == 'NEXT ROUND!':
            res = True
            played = list(s.already_played.values())
            for bound in played:
                if bound is False:
                    res = False
                    break
            if res is True:
                for unbound in s.all_characters:
                    s.already_played[unbound] = False
                for character in s.all_playable:
                    character.cooldown -= 1
                    character.special_cooldown -= 1
                if s.mata_here:
                    f.poison_checking()
                s.count += 1
                sg.popup(f'Round {s.count} Begins!')
                window.TKroot.title(f'Card Game - Round {s.count}')
                window['IN'].update(f'ROUND {s.count}', text_color='r')
            else:
                sg.popup('All characters have not played yet!')
        if event == '1st player - Play with this character' or event == '2nd player - Play with this character':
            layout2 = [[sg.Button('Select this'), sg.Combo(['Normal attack', 'Special attack', 'Special action'], key='action')],
            [sg.Button('Exit')]]
            window2 = sg.Window('Turn', layout2).finalize()
            if event == '1st player - Play with this character':
                f.playing(values, window2, '1stplayer_character', s.second_collection)
            elif event == '2nd player - Play with this character':
                f.playing(values, window2, '2ndplayer_character', s.first_collection)

        if event == '1st player - Check this character' or event == '2nd player - Check this character':
            if event == '1st player - Check this character':
                name = values['1stplayer_character']
                f.stat_checking(name)
            elif event == '2nd player - Check this character':
                name = values['2ndplayer_character']
                f.stat_checking(name)
        try:
            window2.close()
        except NameError:
            pass