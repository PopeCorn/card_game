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

def using(collection, new_collection):
        for unused in collection:
            if unused == 'david':
                david = David.David()
                new_collection.append(david)
            elif unused == 'honza':
                honza = Honza.Honza()
                new_collection.append(honza)
            elif unused == 'kvitek':
                kvitek = Kvítek.Kvitek()
                new_collection.append(kvitek)
            elif unused == 'mark':
                mark = Mark.Marekec()
                new_collection.append(mark)
            elif unused == 'matyas':
                s.mata_here = True
                matyas = Matyas.Matyas()
                new_collection.append(matyas)
            elif unused == 'milan':
                milan = Milan.Milan()
                new_collection.append(milan)
            elif unused == 'mojmir':
                mojmir = Mojmir.Mojmir()
                new_collection.append(mojmir)
            elif unused == 'nikolas':
                nikolas = Nikolas.Nikolas()
                new_collection.append(nikolas)
            elif unused == 'pavel':
                pavel = Pavel.Pavel()
                new_collection.append(pavel)
            elif unused == 'petr':
                petr = Petr.Petr()
                new_collection.append(petr)
            elif unused == 'tom':
                tom = Tom.Tom()
                new_collection.append(tom)
            elif unused == 'zimik':
                zimik = Žimík.Zimik()
                new_collection.append(zimik)


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
    all_unplayable = first_player_collection + second_player_collection
    transfer = {}
    first_player_playable = []
    second_player_playable = []
    all_playable = first_player_playable + second_player_playable
    for i in range(0, 7):
        transfer[all_unplayable[i]] = all_playable[i]
    inverted_transfer = {v: k for k, v in transfer.items()}
    using(first_player_collection, first_player_playable)
    using(second_player_collection, second_player_playable)

    action_finish = {}
    f.initialize_dict(action_finish, all_playable)
    index = 0
    while True:
        s.count += 1
        f.cooldowns(all_playable)
        f.regeneration(all_playable)
        if s.mata_here:
            poison_checking()
        for character in first_player_playable:
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
                    if inverted_transfer[character] == 'david':
                        character.special()

                    elif inverted_transfer[character] == 'honza':
                        character.special()

                    elif inverted_transfer[character] == 'kvitek':
                        while True:
                            oponent = input('Who do you want to attack: ')
                            if oponent in all_unplayable:
                                character.special(transfer[oponent])
                                break
                            else:
                                print('That character is not in the game!')
                                continue

                    elif inverted_transfer[character] == 'mark':
                        character.special()
                    elif inverted_transfer[character] == 'matyas':
                        while True:
                            oponent = input('Who do you want to attack: ')
                            if oponent in all_unplayable:
                                character.special(transfer[oponent])
                                break
                            else:
                                print('That character is not in the game!')
                                continue

                    elif inverted_transfer[character] == 'milan':
                        while True:
                            oponent = input('Who do you want to attack: ')
                            if oponent in all_unplayable:
                                character.special(transfer[oponent])
                                break
                            else:
                                print('That character is not in the game!')
                                continue

                    elif inverted_transfer[character] == 'mojmir':
                        character.special()

                    elif inverted_transfer[character] == 'nikolas':
                        character.special()

                    elif inverted_transfer[character] == 'pavel':
                        while True:
                            oponent = input('Who do you want to attack: ')
                            if oponent in all_unplayable:
                                character.special(transfer[oponent])
                                break
                            else:
                                print('That character is not in the game!')
                                continue

                    elif inverted_transfer[character] == 'petr':
                        while True:
                            oponent = input('Who do you want to attack: ')
                            if oponent in all_unplayable:
                                character.special(transfer[oponent])
                                break
                            else:
                                print('That character is not in the game!')
                                continue

                    elif inverted_transfer[character] == 'tom':
                        healing = input('Do you want to heal yourself [1] or someone other[2] (Type the number): ')
                        if healing == '1':
                            character.special()
                        elif healing == '2':
                            member = input('Who do you want to heal: ')
                            if member in all_unplayable:
                                character.special(transfer[member], not_self=True)

                    elif inverted_transfer[character] == 'zimik':
                         while True:
                            oponent = input('Who do you want to attack: ')
                            if oponent in all_unplayable:
                                character.special(transfer[oponent])
                                break
                            else:
                                print('That character is not in the game!')
                                continue

        # KAŽDÉ KOLO BUDOU OBA HRÁČI HRÁT SE VŠEMI SVÝMI CHARAKTERY POMOCÍ FOR LOOPU
        exit()
        
        