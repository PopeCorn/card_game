from Characters import David, Matyas, Mojmir, Honza, Kvítek, Mark, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
from colorama import Fore

def both_players(player_playable, player_collection, player_number, wanted_index, enemy_collection):
    for character in player_playable:
        wanted_index += 1
        character_name = s.inverted_transfer[character]
        print(f'''
                            {Fore.GREEN}{character_name.upper()} turn{Fore.RESET}
            
{Fore.BLUE}------------------------------------------------------------------------------------{Fore.RESET}''')
        print(f'''  Player {player_number}, choose your action (TYPE ITS NUMBER):
        1. Attack
        2. Special attack
        3. Special action''')
        while True:
            action = input('Type here: ')
            if action == '1':
                f.initialize_attack(s.transfer, enemy_collection, character.attack)

            elif action == '2':
                f.initialize_attack(s.transfer, enemy_collection, character.special_attack)

            elif action == '3':
                inv = s.inverted_transfer[character]
                if inv == 'david' or inv == 'honza' or inv == 'mark' or inv == 'nikolas' or inv == 'mojmir':
                    character.special()
                elif inv == 'kvitek' or inv == 'matyas' or inv == 'milan' or inv == 'pavel' or inv == 'petr' or inv == 'zimik':
                    f.initialize_attack(s.transfer, player_collection, character.special, enemy_collection)

                elif inv == 'tom':
                    while True:
                        healing = input('Do you want to heal yourself [1] or someone other[2] (Type the number): ')
                        if healing == '1':
                            character.special()
                            break
                        elif healing == '2':
                            while True:
                                member = input('Who do you want to heal: ')
                                if member in s.first_player_collection:
                                    character.special(s.transfer[member], not_self=True)
                                else:
                                    print('That player either does not exist or is not on your team!')
                                    continue
                                break
                            break
                        else:
                            print('That is not an option!')
                            continue
            else:
                print('That is not an option!')
                continue
            f.death_system(s.all_playable, s.inverted_transfer, s.first_player_collection, s.first_player_playable, s.second_player_collection, s.second_player_playable)
            if s.end is True:
                print(f'{Fore.RED}The game has ended and the winner is {s.winner}!')
                exit()
            break
    wanted_index = -1

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
    f.choose_character(s.first_player_collection, 1, s.available_characters, s.all_unplayable)
    f.choose_character(s.second_player_collection, 2, s.available_characters, s.all_unplayable)
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

    f.making_playables(s.first_player_collection, s.first_player_playable, s.transfer)
    f.making_playables(s.second_player_collection, s.second_player_playable, s.transfer)

    while True:
        all_unplayable = s.first_player_collection + s.second_player_collection
        s.count += 1
        f.cooldowns(s.all_playable)
        for character in s.all_playable:
            character.energy = f.recovery_actions(character.energy, character.max_energy)
        if s.mata_here:
            f.poison_checking(matyas)
        print('')
        print(f'                             {Fore.RED}ROUND {s.count}!{Fore.RESET}')
        index_of_character = -1
        both_players(s.first_player_playable, s.first_player_collection, '1', index_of_character, s.second_player_collection)
        print(f''' 
              {Fore.CYAN}--------------2ND PLAYER----------------{Fore.GREEN}''')
        both_players(s.second_player_playable, s.second_player_collection, '2', index_of_character, s.first_player_collection)