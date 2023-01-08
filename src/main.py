from Characters import David, Matyas, Mojmir, Honza, Kvítek, Mark, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
from colorama import Fore

if __name__ == "__main__":
    print('''Available characters:
        David
        Matyas
        Mojmir
        Honza
        Zimik
        Kvitek
        Mark
        Milan
        Nikolas
        Pavel
        Petr
        Tom''')
    f.choose_character(s.first_player_collection, 1)
    f.choose_character(s.second_player_collection, 2)
    for unused in s.all_unplayable:
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

    s.inverted_transfer = {v: k for k, v in s.transfer.items()}
    f.making_playables(s.first_player_collection, s.first_player_playable, s.transfer)
    f.making_playables(s.second_player_collection, s.second_player_playable, s.transfer)

    while True:
        s.all_unplayable = s.first_player_collection + s.second_player_collection
        s.count += 1
        f.cooldowns()
        for character in s.all_playable:
            character.energy = f.recovery_actions(character.energy, character.max_energy)
        if s.mata_here:
            f.poison_checking(matyas)
        print(f'''                        
                             {Fore.RED}ROUND {s.count}!{Fore.RESET}''')
        index_of_character = -1
        f.both_players(s.first_player_playable, s.first_player_collection, '1', index_of_character, s.second_player_collection)
        print(f''' 
              {Fore.CYAN}--------------2ND PLAYER----------------{Fore.RESET}''')
        f.both_players(s.second_player_playable, s.second_player_collection, '2', index_of_character, s.first_player_collection)