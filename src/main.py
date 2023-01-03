from Characters import David, Matyas, Mojmir, Honza, Kvítek, Mark, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
from colorama import Fore

def poison_checking():
    if s.mata_poison is True:
        mata.poison(s.mata_poison_target)
        s.mata_poison = False
    else:
        pass

def both_players(range_start, range_end, player_collection, player_number, wanted_index):
    for character in all_playable[range_start:range_end]:
        wanted_index += 1
        character_name = player_collection[wanted_index]
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
                f.initialize_attack(transfer, player_collection, character.attack)

            elif action == '2':
                f.initialize_attack(transfer, player_collection, character.special_attack)

            elif action == '3':
                if inverted_transfer[character] == 'david' or inverted_transfer[character] == 'honza' or inverted_transfer[character] == 'mark' or inverted_transfer[character] == 'nikolas' or inverted_transfer[character] == 'mojmir':
                    character.special()
                elif inverted_transfer[character] == 'kvitek' or inverted_transfer[character] == 'matyas' or inverted_transfer[character] == 'milan' or inverted_transfer[character] == 'pavel' or inverted_transfer[character] == 'petr' or inverted_transfer[character] == 'zimik':
                    f.initialize_attack(transfer, player_collection, character.special)

                elif inverted_transfer[character] == 'tom':
                    while True:
                        healing = input('Do you want to heal yourself [1] or someone other[2] (Type the number): ')
                        if healing == '1':
                            character.special()
                            break
                        elif healing == '2':
                            while True:
                                member = input('Who do you want to heal: ')
                                if member in first_player_collection:
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
            break
    wanted_index = -1


tom = Tom.Tom()
tom.hp -= 5; print(tom.hp, "- tomovo hp po ubrání v main.py")
tom.special()
print(tom.hp, "- tomovo hp po healu v main.py")

exit()
available_characters = ['david', 'matyas', 'mojmir', 'honza', 'zimik', 'kvitek', 'mark', 'milan', 'nikolas', 'pavel', 'petr', 'tom']
first_player_collection = []
second_player_collection = []
all_unplayable = []

if __name__ == "__main__":
    index_of_character = -1
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
    f.choose_character(first_player_collection, 1, available_characters, all_unplayable)
    f.choose_character(second_player_collection, 2, available_characters, all_unplayable)
    transfer = {}
    all_playable = []
    for unused in all_unplayable:
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
    action_finish = {}
    f.initialize_dict(action_finish, all_playable)

    while True:
        s.count += 1
        f.cooldowns(all_playable)
        f.regeneration(all_playable)
        if s.mata_here:
            poison_checking()
        print(f'                             {Fore.RED}ROUND {s.count}!{Fore.RESET}')
        both_players(0, 3, first_player_collection, '1', index_of_character)
        print('--------------2ND PLAYER----------------')
        index_of_character = -1
        both_players(3, 6, second_player_collection, '2', index_of_character)
        print('FINISHED')
        exit()
        
        