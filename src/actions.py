from print_room import print_room


def get_item(uimp, player_one):
    if len(uimp) == 1:
        print("Not sure what to get!")
    else:
        req_item = ' '.join(uimp[1:])
        if req_item in player_one.curr_room.items:
            player_one.inventory.append(req_item)
            player_one.curr_room.items.remove(req_item)
            print_room(room, player_one)
        else:
            print("That doesn't exit here!")


def drop_item(uimp, room, player_one):
    if len(uimp) == 1:
        print("Not sure what to drop!")
    else:
        req_item = ' '.join(uimp[1:])
        if req_item in player_one.inventory:
            player_one.inventory.remove(req_item)
            player_one.curr_room.items.append(req_item)
            print_room(room, player_one)
        else:
            print("You don't have that!")
