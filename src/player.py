# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curr_room='outside'):
        self.name = name
        self.curr_room = curr_room
        self.rooms_visited = [curr_room]
    inventory = ['Blue stone']
