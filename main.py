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
    all_playable = []
    for unused in (first_player_collection + second_player_collection):
        if unused == 'david':
            david = David.David()
            all_playable.append(david)
        elif unused == 'honza':
            honza = Honza.Honza()
            all_playable.append(honza)
        elif unused == 'kvitek':
            kvitek = Kvítek.Kvitek()
            all_playable.append(kvitek)
        elif unused == 'mark':
            mark = Mark.Marekec()
            all_playable.append(mark)
        elif unused == 'matyas':
            s.mata_here = True
            matyas = Matyas.Matyas()
            all_playable.append(matyas)
        elif unused == 'milan':
            milan = Milan.Milan()
            all_playable.append(milan)
        elif unused == 'mojmir':
            mojmir = Mojmir.Mojmir()
            all_playable.append(mojmir)
        elif unused == 'nikolas':
            nikolas = Nikolas.Nikolas()
            all_playable.append(nikolas)
        elif unused == 'pavel':
            pavel = Pavel.Pavel()
            all_playable.append(pavel)
        elif unused == 'petr':
            petr = Petr.Petr()
            all_playable.append(petr)
        elif unused == 'tom':
            tom = Tom.Tom()
            all_playable.append(tom)
        elif unused == 'zimik':
            zimik = Žimík.Zimik()
            all_playable.append(zimik)

    action_finish = {}
    f.initialize_dict(action_finish, all_playable)
    exit()
    while True:
        s.count += 1
        f.cooldowns(all_playable)
        f.regeneration(all_playable)
        if s.mata_here:
            poison_checking()
        
        # KAŽDÉ KOLO BUDOU OBA HRÁČI HRÁT SE VŠEMI SVÝMI CHARAKTERY POMOCÍ FOR LOOPU
        exit()
        
        