import PySimpleGUI as sg
from Characters import Anus, Big_Chungus, Kvítek, Marekec, Máta, Milanus, Mojmi_chan, PopeC0rn, Tolbus, Zálabář, Žeromán, Žimík
from Code import settings as s
from Code import functions as f
sg.theme('DarkTeal10')  

layout = []
layout = f.layout(layout, choose_characters=True)
window = sg.Window('Card Game - choose characters', layout, size=(380, 150))

if __name__ == '__main__':
    # Loop for choosing characters for both players
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

    # Section for making playables
    for unused in s.all_characters:
        if unused == 'Big Chungus':
            big_chungus = Big_Chungus.BigChungus()
            s.transfer['Big Chungus'] = big_chungus
            s.all_playable.append(big_chungus)
        elif unused == 'Anus':
            anus = Anus.Anus()
            s.transfer['Anus'] = anus
            s.all_playable.append(anus)
        elif unused == 'Kvítek':
            kvitek = Kvítek.Kvítek()
            s.transfer['Kvítek'] = kvitek
            s.all_playable.append(kvitek)
        elif unused == 'Marekec':
            marekec = Marekec.Marekec()
            s.transfer['Marekec'] = marekec
            s.all_playable.append(marekec)
        elif unused == 'Máta':
            s.mata_here = True
            mata = Máta.Máta()
            s.transfer['Máta'] = mata
            s.all_playable.append(mata)
        elif unused == 'Milanus':
            milanus = Milanus.Milanus()
            s.transfer['Milanus'] = milanus
            s.all_playable.append(milanus)
        elif unused == 'Mojmi-chan':
            mojmi_chan = Mojmi_chan.Mojmi_chan()
            s.transfer['Mojmi-chan'] = mojmi_chan
            s.all_playable.append(mojmi_chan)
        elif unused == 'Žeromán':
            zeroman = Žeromán.Žeromán()
            s.transfer['Žeromán'] = zeroman
            s.all_playable.append(zeroman)
        elif unused == 'PopeC0rn':
            popec0rn = PopeC0rn.PopeC0rn()
            s.transfer['PopeC0rn'] = popec0rn
            s.all_playable.append(popec0rn)
        elif unused == 'Zálabář':
            zalabar = Zálabář.Zálabář()
            s.transfer['Zálabář'] = zalabar
            s.all_playable.append(zalabar)
        elif unused == 'Tolbus':
            tolbus = Tolbus.Tolbus()
            s.transfer['Tolbus'] = tolbus
            s.all_playable.append(tolbus)
        elif unused == 'Žimík':
            zimik = Žimík.Žimík()
            s.transfer['Žimík'] = zimik
        s.inv_transfer = {v: k for k, v in s.transfer.items()}

    f.adding_playables(s.first_collection, s.first_playable, s.second_collection, s.second_playable)
    f.already_played_false()
    layout = f.layout(layout, game=True)
    window = sg.Window('Card Game - Round 1', layout, size=(500, 500))

    # Loop for the actual game
    while True:
        event, values = window.read()
        if s.end:
            sg.popup(f'THE WINNER IS {s.winner}!')
            quit()
    
        if event == 'Exit' or event == sg.WIN_CLOSED:
            quit()

        elif event == 'NEXT ROUND!':
            res= True
            played = list(s.already_played.values())
            res = f.is_next_round(played, res)
            window = f.next_round(window, res)

        elif event == '1st player - Play with this character' or event == '2nd player - Play with this character':
            layout2 = f.layout(layout, action=True)
            window2 = sg.Window('Turn', layout2).finalize()
            if event == '1st player - Play with this character':
                f.playing(values, window2, '1stplayer_character', s.second_collection)
            elif event == '2nd player - Play with this character':
                f.playing(values, window2, '2ndplayer_character', s.first_collection)

        elif event == '1st player - Check this character':
            name = values['1stplayer_character']
            f.stat_checking(name)

        elif event == '2nd player - Check this character':
            name = values['2ndplayer_character']
            f.stat_checking(name)
            
        try:
            window2.close()
        except NameError:
            pass
    
        layout = f.checking_for_dead(layout)
        window = sg.Window('Card Game - Round 1', layout, size=(500, 500))