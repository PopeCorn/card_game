from Characters import David, Mojmir, Honza, Kvítek, Mark, Máta, Milan, Nikolas, Pavel, Petr, Tom, Žimík
from Code import settings as s
from Code import functions as f
from colorama import Fore


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
    print(f'First player: {first_player_collection}')

   # tohle udělat s těmi actual moduly a ne jenom jmény: all_characters = first_player_collection + second_player_collection

    exit()
    while True:
        s.count += 1
        f.cooldowns(all_characters)
        f.regeneration(all_characters)
        if s.mata_here:
            poison_checking()
        
        # KAŽDÉ KOLO BUDOU OBA HRÁČI HRÁT SE VŠEMI SVÝMI CHARAKTERY POMOCÍ FOR LOOPU
        exit()
        
        