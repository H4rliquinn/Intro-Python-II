import os
import textwrap
from print_map import print_map


def print_room(room, player_one):
    os.system('cls')
    print('='*60+'\n'+player_one.curr_room.name+'\n'+'='*60)
    # * Prints the current description (the textwrap module might be useful here).
    tw = textwrap.wrap(player_one.curr_room.description, width=60)
    for line in tw:
        print(line)
    if len(player_one.curr_room.items):
        print('\n')
        for item in player_one.curr_room.items:
            print(f'There is a {item} here')
    print('\n')
    print('Exits are: '+player_one.curr_room.get_exits()[:-2]+'\n')
    print_map(room, player_one)
