import os
import textwrap
# from print_map import print_map
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """Class to define rooms in the game"""

    def __init__(self, id, name, description, items=[]):
        self.id = id
        self.name = name
        self.description = description
        self.items = items

    def get_exits(self):
        exitstring = ''
        for attr in vars(self):
            if attr[-2:] == 'to':
                exitstring += attr[0].upper()+', '
        return exitstring

    def print_room(self, player_one, map):
        os.system('cls')
        print('='*60+'\n'+self.name+'\n'+'='*60)
        # * Prints the description and items
        desc_string = self.description
        # if len(self.items):
        item_list = []
        for item in self.items:
            desc_string += item.description
            item_list.append(item.id)
        if len(item_list):
            desc_string += 'Items: ['+']['.join(item_list)+']'

        tw = textwrap.wrap(desc_string, width=60)
        for line in tw:
            print(line)

        print('\n')
        print('Exits are: '+self.get_exits()[:-2]+'\n')
        map.print_map(player_one)
