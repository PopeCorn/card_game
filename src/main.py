from Characters import David, Matyas, Mojmir, Honza, Kvítek, Mark, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
from colorama import Fore

def both_players(player_playable, player_collection, player_number, wanted_index, enemy_collection):
    for character in player_playable:
        wanted_index += 1
        character_name = inverted_transfer[character]
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
                f.initialize_attack(transfer, enemy_collection, character.attack)

            elif action == '2':
                f.initialize_attack(transfer, enemy_collection, character.special_attack)

            elif action == '3':
                if inverted_transfer[character] == 'david' or inverted_transfer[character] == 'honza' or inverted_transfer[character] == 'mark' or inverted_transfer[character] == 'nikolas' or inverted_transfer[character] == 'mojmir':
                    character.special()
                elif inverted_transfer[character] == 'kvitek' or inverted_transfer[character] == 'matyas' or inverted_transfer[character] == 'milan' or inverted_transfer[character] == 'pavel' or inverted_transfer[character] == 'petr' or inverted_transfer[character] == 'zimik':
                    f.initialize_attack(transfer, player_collection, character.special, enemy_collection)

                elif inverted_transfer[character] == 'tom':
                    while True:
                        healing = input('Do you want to heal yourself [1] or someone other[2] (Type the number): ')
                        if healing == '1':
                            character.special()
                            break
                        elif healing == '2':
                            while True:
                                member = input('Who do you want to heal: ')
                                if member in s.first_player_collection:
                                    character.special(transfer[member], not_self=True)
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
            f.death_system(all_playable, inverted_transfer, s.first_player_collection, first_player_playable, s.second_player_collection, second_player_playable)
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
    transfer = {}
    all_playable = []
    for unused in s.all_unplayable:
            if unused == 'david':
                david = David.David()
                transfer['david'] = david
                all_playable.append(david)
            elif unused == 'honza':
                honza = Honza.Honza()
                transfer['honza'] = honza
                all_playable.append(honza)
            elif unused == 'kvitek':
                kvitek = Kvítek.Kvitek()
                transfer['kvitek'] = kvitek
                all_playable.append(kvitek)
            elif unused == 'mark':
                mark = Mark.Marekec()
                transfer['mark'] = mark
                all_playable.append(mark)
            elif unused == 'matyas':
                s.mata_here = True
                matyas = Matyas.Matyas()
                transfer['matyas'] = matyas
                all_playable.append(matyas)
            elif unused == 'milan':
                milan = Milan.Milan()
                transfer['milan'] = milan
                all_playable.append(milan)
            elif unused == 'mojmir':
                mojmir = Mojmir.Mojmir()
                transfer['mojmir'] = mojmir
                all_playable.append(mojmir)
            elif unused == 'nikolas':
                nikolas = Nikolas.Nikolas()
                transfer['nikolas'] = nikolas
                all_playable.append(nikolas)
            elif unused == 'pavel':
                pavel = Pavel.Pavel()
                transfer['pavel'] = pavel
                all_playable.append(pavel)
            elif unused == 'petr':
                petr = Petr.Petr()
                transfer['petr'] = petr
                all_playable.append(petr)
            elif unused == 'tom':
                tom = Tom.Tom()
                transfer['tom'] = tom
                all_playable.append(tom)
            elif unused == 'zimik':
                zimik = Žimík.Zimik()
                transfer['zimik'] = zimik
                all_playable.append(zimik)

    inverted_transfer = {v: k for k, v in transfer.items()}
    first_player_playable = []
    second_player_playable = []
    f.making_playables(s.first_player_collection, first_player_playable, transfer)
    f.making_playables(s.second_player_collection, second_player_playable, transfer)

    while True:
        all_unplayable = s.first_player_collection + s.second_player_collection
        s.count += 1
        f.cooldowns(all_playable)
        for character in all_playable:
            character.energy = f.recovery_actions(character.energy, character.max_energy)
        if s.mata_here:
            f.poison_checking(matyas)
        print('')
        print(f'                             {Fore.RED}ROUND {s.count}!{Fore.RESET}')
        index_of_character = -1
        both_players(first_player_playable, s.first_player_collection, '1', index_of_character, s.second_player_collection)
        print(f''' 
              {Fore.CYAN}--------------2ND PLAYER----------------{Fore.GREEN}''')
        both_players(second_player_playable, s.second_player_collection, '2', index_of_character, s.first_player_collection)
        
        