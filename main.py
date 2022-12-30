from Characters import David, Mojmir, Honza, Kvítek, Mark, Máta, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
from colorama import Fore

def cooldowns():
    for character in all_characters:
        if character.cooldown > 0:
            character.cooldown -= 1
        if character.special_cooldown > 0:
            character.special_cooldown -= 1


def poison_checking():
    if s.mata_poison is True:
        mata.poison(s.mata_poison_target)
        s.mata_poison = False
    else:
        pass

def choose_character(player_list, number):
    for i in range(1, 4):
        while True:
                new_character = input(f'PLAYER {number}, select your new character (You will have 3 of them in total): ').lower()
                if (new_character in available_characters):
                    if new_character == 'mata':
                        s.mata_here = True
                    if (new_character in player_list):
                        print(f'{Fore.RED}You already have that character!{Fore.RESET}')
                        continue
                    else:
                        print(f'{Fore.BLUE}{new_character.capitalize()} added! {Fore.RESET}')
                        player_list.append(new_character)
                        break
                else:
                    print(f'{Fore.RED}That character is not available!{Fore.RESET}')
                    continue

david = David.David()
s.count = 1
print(david.cooldown)

exit()
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
    choose_character(first_player_collection, 1)
    print('---------------------------------------')
    choose_character(second_player_collection, 2)
    print(f'First player: {first_player_collection}')
    print(f'Second player: {second_player_collection}')
    print('TESTING NOW//////////////////////')
    all_characters = first_player_collection + second_player_collection

    while True:
        s.count += 1
        cooldowns()
        f.regeneration(all_characters)
        if s.mata_here:
            poison_checking
        
        # KAŽDÉ KOLO BUDOU OBA HRÁČI HRÁT SE VŠEMI SVÝMI CHARAKTERY POMOCÍ FOR LOOPU
        exit()
        
        