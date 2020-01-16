# Print Map


def print_map(room, player_one):
    map_id = room[player_one.curr_room].id
    top = '\u2554'+'\u2550'*13+'\u2557\n'
    mid = '\u2551'+' '*13+'\u2551\n'
    mid_name = '\u2551'+map_id+' '*(13-len(map_id))+'\u2551\n'
    mid_player = '\u2551'+' '*6+'@'+' '*6+'\u2551\n'
    mid_comp = mid_name+mid+mid_player+mid*2
    bot = '\u255A'+'\u2550'*13+'\u255D\n'
    print(top+mid_comp+bot)
