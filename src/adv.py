
from room import Room
from player import Player
from print_room import print_room
import actions
# Declare all the rooms

room = {
    'outside':  Room('outside', "Outside Cave Entrance",
                     "North of you, the cave mouth beckons. Wind howls out from beneath the earth as you approach. You can just hear the scurrying of rats in the darkness just inside.", ['Dagger']),

    'foyer':    Room('foyer', "Foyer", """Dim light filters in from the south. Dusty
passages run north and east. A large rock dominates the northwest corner""", ['Large rock']),

    'overlook': Room('overlook', "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['Potion of Strength']),

    'narrow':   Room('narrow', "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room('treasure', "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. There appear to be some very small rocks floating in water here. The only exit is to the south.""", ['Very small rocks']),
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

player_one = Player()
# Write a loop that:
#
# * Prints the current room name


commands = ['q: Quit', 'n,s,e,w: Move North/South/East/West',
            'i: Inventory', 'Get: Pickup Item', 'Drop: Drop Item', 'Push: Push Object', '? or h: This list']

print_room(room, player_one)
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
            print_room(room, player_one)
        else:
            print("Can't move that way\n")
    elif uimp[0] == 's':
        if hasattr(room[player_one.curr_room], 's_to'):
            player_one.curr_room = room[player_one.curr_room].s_to
            print_room(room, player_one)
        else:
            print("Can't move that way\n")
    elif uimp[0] == 'w':
        if hasattr(room[player_one.curr_room], 'w_to'):
            player_one.curr_room = room[player_one.curr_room].w_to
            print_room(room, player_one)
        else:
            print("Can't move that way\n")
    elif uimp[0] == 'e':
        if hasattr(room[player_one.curr_room], 'e_to'):
            player_one.curr_room = room[player_one.curr_room].e_to
            print_room(room, player_one)
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
        actions.get_item(uimp, room, player_one)
    elif uimp[0] == 'drop':
        actions.drop_item(uimp, room, player_one)
    elif uimp[0] == '?' or uimp[0] == 'h':
        print('Available Commands')
        for command in commands:
            print(command)
    else:
        print("Sorry, I don't understand")
