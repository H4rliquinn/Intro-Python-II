import os
import textwrap

from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room('outside', "Outside Cave Entrance",
                     "North of you, the cave mouth beckons. Wind howls out from beneath the earth as you approach. You can just hear the scurrying of rats in the darkness just inside.", ['dagger']),

    'foyer':    Room('foyer', "Foyer", """Dim light filters in from the south. Dusty
passages run north and east. A large rock dominates the northwest corner"""),

    'overlook': Room('overlook', "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['Potion of Strength']),

    'narrow':   Room('narrow', "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room('treasure', "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. There appear to be some very small rocks floating in water here. The only exit is to the south.""", ['Very Small Rocks']),
}


# Link rooms together

room['outside'].n_to = 'foyer'
room['outside'].exits = 'N'

room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['foyer'].exits = 'N, S, and E'

room['overlook'].s_to = 'foyer'
room['overlook'].exits = 'S'

room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['narrow'].exits = 'N and W'

room['treasure'].s_to = 'narrow'
room['treasure'].exits = 'S'
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_one = Player('outside')
# Write a loop that:
#
# * Prints the current room name


def print_room():
    os.system('cls')
    print('='*60+'\n'+room[player_one.curr_room].name+'\n'+'='*60)
    # * Prints the current description (the textwrap module might be useful here).
    tw = textwrap.wrap(room[player_one.curr_room].description, width=60)
    for line in tw:
        print(line)
    if len(room[player_one.curr_room].items):
        print('\n')
        for item in room[player_one.curr_room].items:
            print(f'There is a {item} here')
    print('\n')
    print('Exits are: '+room[player_one.curr_room].exits+'\n')

# Print Map


def print_map():
    map_id = room[player_one.curr_room].id
    top = '\u2554'+'\u2550'*13+'\u2557\n'
    mid = '\u2551'+' '*13+'\u2551\n'
    mid_name = '\u2551'+map_id+' '*(13-len(map_id))+'\u2551\n'
    mid_player = '\u2551'+' '*6+'@'+' '*6+'\u2551\n'
    mid_comp = mid_name+mid+mid_player+mid*2
    bot = '\u255A'+'\u2550'*13+'\u255D\n'
    print(top+mid_comp+bot)


def get_item(uimp):
    if len(uimp) == 1:
        print("Not sure what to get!")
    else:
        req_item = ' '.join(uimp[1:])
        if req_item in room[player_one.curr_room].items:
            player_one.inventory.append(req_item)
            room[player_one.curr_room].items.remove(req_item)
            print_room()
        else:
            print("That doesn't exit here!")


def drop_item(uimp):
    if len(uimp) == 1:
        print("Not sure what to drop!")
    else:
        req_item = ' '.join(uimp[1:])
        if req_item in player_one.inventory:
            player_one.inventory.remove(req_item)
            room[player_one.curr_room].items.append(req_item)
            print_room()
        else:
            print("You don't have that!")


commands = ['q: Quit', 'n,s,e,w: Move North/South/East/West',
            'i: Inventory', 'Get: Pickup Item', 'Drop: Drop Item', 'Push: Push Object', '? or h: This list']

print_room()
# print_map()
while True:
    # * Waits for user input and decides what to do.
    #
    uimp = input('Enter Command===>')
    if uimp == '':
        uimp = ['']
    else:
        uimp = uimp.split()
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    if uimp[0] == 'q':
        break
    elif uimp[0] == 'n':
        if hasattr(room[player_one.curr_room], 'n_to'):
            player_one.curr_room = room[player_one.curr_room].n_to
            print_room()
        else:
            print("Can't move that way\n")
    elif uimp[0] == 's':
        if hasattr(room[player_one.curr_room], 's_to'):
            player_one.curr_room = room[player_one.curr_room].s_to
            print_room()
        else:
            print("Can't move that way\n")
    elif uimp[0] == 'w':
        if hasattr(room[player_one.curr_room], 'w_to'):
            player_one.curr_room = room[player_one.curr_room].w_to
            print_room()
        else:
            print("Can't move that way\n")
    elif uimp[0] == 'e':
        if hasattr(room[player_one.curr_room], 'e_to'):
            player_one.curr_room = room[player_one.curr_room].e_to
            print_room()
        else:
            print("Can't move that way\n")
    elif uimp[0] == 'i':
        print('You are currently carrying:')
        if len(player_one.inventory):
            for item in player_one.inventory:
                print(item)
        else:
            print('Nothing')
    elif uimp[0] == 'get':
        get_item(uimp)
    elif uimp[0] == 'drop':
        drop_item(uimp)
    elif uimp[0] == '?' or uimp[0] == 'h':
        print('Available Commands')
        for command in commands:
            print(command)
    else:
        print("Sorry, I don't understand")
