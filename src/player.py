# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room
        self.rooms_visited = [curr_room.id]
    inventory = ['Blue stone']

    def print_room(self, map):
        self.curr_room.print_room(self, map)

    def move(self, uimp, map):
        room = map.room
        destination = getattr(self.curr_room, uimp[0]+'_to', False)
        if destination:
            self.curr_room = room[destination]
            if self.curr_room.id not in self.rooms_visited:
                self.rooms_visited.append(self.curr_room.id)
            self.print_room(map)
        else:
            print("Can't move that way, "+self.name+"\n")

    def get_inventory(self):
        print('You are currently carrying:')
        if len(self.inventory):
            for item in self.inventory:
                print(item)
        else:
            print('Nothing')

    def get_item(self, uimp, map):
        room = map.room
        if len(uimp) == 1:
            print("Not sure what to get!")
        else:
            req_item = ' '.join(uimp[1:])
            if req_item in self.curr_room.items:
                self.inventory.append(req_item)
                self.curr_room.items.remove(req_item)
                self.print_room(map)
            else:
                print("That doesn't exit here!")

    def drop_item(self, uimp, map):
        room = map.room
        if len(uimp) == 1:
            print("Not sure what to drop!")
        else:
            req_item = ' '.join(uimp[1:])
            if req_item in self.inventory:
                self.inventory.remove(req_item)
                self.curr_room.items.append(req_item)
                self.print_room(map)
            else:
                print("You don't have that!")
