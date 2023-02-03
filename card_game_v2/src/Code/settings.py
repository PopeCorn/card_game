# In this file, all global variables used throughout the project are defined, so different files can use them
# That prevents the case of a need to pass a variable defined in main.py to function in functions.py - function can acess it because it is in settings.py and that file is imported
all_available = ['Anus', 'Big Chungus', 'Kvítek', 'Marekec', 'Máta', 'Milanus', 'Mojmi-chan', 'PopeC0rn', 'Tolbus', 'Zálabář', 'Žeromán', 'Žimík']
first_collection, second_collection, first_playable, second_playable = [], [], [], []
all_characters, all_playable = [], []
transfer, inv_transfer = {}, {}
already_played = {}
choosing_finish = False
chungus_defence = False
mata_here = False
mata_poison = False
mojmi_chan_attack = ''
mojmi_chan_double_damage = False
mojmi_chan_done = False
mata_poison_target = ''
marekec_dodge = False
kvitek_ultimate = False
zimik_increase_cooldown = False
end, winner = False, ''
count = 1