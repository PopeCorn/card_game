from Characters import David, Matyas, Mojmir, Honza, Kvítek, Mark, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
from colorama import Fore

def special_attacks(main_character):
    while True:
        oponent = input('Who do you want to attack: ')
        if oponent in all_unplayable:
            main_character.special(transfer[oponent])
            break
        else:
            print('That character is not in the game!')
            continue


def poison_checking():
    if s.mata_poison is True:
        mata.poison(s.mata_poison_target)
        s.mata_poison = False
    else:
        pass


if __name__ == "__main__":
    available_characters = ['david', 'matyas', 'mojmir', 'honza', 'zimik', 'kvitek', 'mark', 'milan', 'nikolas', 'pavel', 'petr', 'tom']
    first_player_collection = []
    second_player_collection = []
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
    f.choose_character(first_player_collection, 1, available_characters)
    print('---------------------------------------')
    f.choose_character(second_player_collection, 2, available_characters)
    all_unplayable = (first_player_collection + second_player_collection)
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


    index = 0
    while True:
        s.count += 1
        f.cooldowns(all_playable)
        f.regeneration(all_playable)
        if s.mata_here:
            poison_checking()
        for character in all_playable[0, 4]:
            print(f'''Player 1, choose your action with {str(first_player_collection[index]).capitalize} (TYPE ITS NUMBER):
            1. Attack
            2. Special attack
            3. Special action''')
            index += 1
            while True:
                action = input('Type here: ')
                if action == '1' or action == '2':
                    target = input('Who do you want to attack: ').lower()
                    if target in all_unplayable:
                        character.attack(transfer[target])
                    else:
                        print('That character is not in the game!')
                        continue

                elif action == '3':
                    if inverted_transfer[character] == 'david' or inverted_transfer[character] == 'honza' or inverted_transfer[character] == 'mark' or inverted_transfer[character] == 'nikolas' or inverted_transfer[character] == 'mojmir':
                        character.special()

                    elif inverted_transfer[character] == 'kvitek' or inverted_transfer[character] == 'matyas' or inverted_transfer[character] == 'milan' or inverted_transfer[character] == 'pavel' or inverted_transfer[character] == 'petr' or inverted_transfer[character] == 'zimik':
                        special_attacks(character)

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
                            else:
                                print('That is not an option!')
                                continue
                            break
                break
        index = 0
        for character in all_playable[4, 7]:
            pass
        exit()
        
        