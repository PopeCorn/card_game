import PySimpleGUI as sg
from Code import settings as s

def choose_character(collection, character):
    while True:
        if len(collection) == 3:
            sg.popup('That player already has 3 characters!')
            break
        if character in s.all_available:
            if character in s.all_characters:
                sg.popup('You or someone else already have that character!')
            else:
                s.all_characters.append(character)
                collection.append(character)
                sg.popup('Character added')
        else:
            sg.popup('That character does not exist!')
        break

def both_players(player_playable, player_number, wanted_index):
    for character in player_playable:
        wanted_index += 1
        character_name = s.inv_transfer[character]
        print(f'''
                                {character_name.upper()} turn
            
        ------------------------------------------------------------------------------------''')
        print(f'''  Player {player_number}, choose your action (TYPE ITS NUMBER):
        1. Attack
        2. Special attack
        3. Special action''')


def making_playables(collection, playable):
    for character in collection:
        playable.append(s.transfer[character])