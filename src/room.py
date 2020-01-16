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
