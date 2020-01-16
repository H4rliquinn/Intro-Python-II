from room import Room
from player import Player
from print_map import Map

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
room['outside'].coord = (2, 0)
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['foyer'].coord = (1, 0)
room['overlook'].s_to = 'foyer'
room['overlook'].coord = (0, 0)
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['narrow'].coord = (1, 1)
room['treasure'].s_to = 'narrow'
room['treasure'].coord = (0, 1)

map = Map(room)
#
# Main
#
# Make a new player object that is currently in the 'outside' room.

player_one = Player('Bob', room['outside'])
# Write a loop that:
#
# * Prints the current room name


moves = ['n', 's', 'w', 'e']
commands = ['q: Quit', 'n,s,e,w: Move North/South/East/West',
            'i: Inventory', 'Get: Pickup Item', 'Drop: Drop Item', 'Push: Push Object', '? or h: This list']

player_one.print_room(map)
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
    elif uimp[0] in moves:
        player_one.move(uimp, map)
    elif uimp[0] == 'i':
        player_one.get_inventory()
    elif uimp[0] == 'get':
        player_one.get_item(uimp, map)
    elif uimp[0] == 'drop':
        player_one.drop_item(uimp, map)
    elif uimp[0] == '?' or uimp[0] == 'h':
        print('Available Commands')
        for command in commands:
            print(command)
    else:
        print("Sorry, I don't understand")
