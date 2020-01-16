# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, curr_room='outside'):
        self.curr_room = curr_room
        self.rooms_visited = [curr_room]
    game_map = [['outside', None], [None, None, None]]
    inventory = ['Blue stone']
