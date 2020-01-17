# Print Map


class Map():
    def __init__(self, room):
        self.room = room

    def print_map(self, player_one):
        # Build Map
        map_list = [[None, None], [None, None], [None, None]]
        for rm in self.room:
            map_list[self.room[rm].coord[0]
                     ][self.room[rm].coord[1]] = self.room[rm]

        # Show Map

        for x in map_list:
            #
            level = {'mid_door': '', 'mid_blank': '',
                     'top': '', 'mid_name': '', 'mid_player': '', 'bot': ''}
            for y in x:
                if not y == None:
                    level = self.print_room(y, player_one, level)
            mid = level['mid_name']+'\n'+level['mid_door'] + \
                '\n'+level['mid_player']+'\n'+level['mid_blank']
            print(level['top']+'\n' + mid+'\n'+level['bot'])

    def print_room(self, rm, player_one, level):
        if rm.id == player_one.curr_room.id:
            icon = '\u263A'
        else:
            icon = ' '
        # Print Room

        def create_top():
            if hasattr(rm, 'n_to'):
                return '\u2554'+'\u2550'*5+'\u255D'+'\u255A'+'\u2550'*6+'\u2557'
            else:
                return '\u2554'+'\u2550'*13+'\u2557'

        def create_bot():
            if hasattr(rm, 's_to'):
                return '\u255A'+'\u2550'*5+'\u2557'+'\u2554'+'\u2550'*6+'\u255D'
            else:
                return '\u255A'+'\u2550'*13+'\u255D'

        if rm.id in player_one.rooms_visited:
            # West Door?
            if hasattr(rm, 'w_to'):
                w_upper_door = '\u255D'
                w_lower_door = '\u2557'
            else:
                w_upper_door = '\u2551'
                w_lower_door = '\u2551'
            # East Door?
            if hasattr(rm, 'e_to'):
                e_upper_door = '\u255A'
                e_lower_door = '\u2554'
            else:
                e_upper_door = '\u2551'
                e_lower_door = '\u2551'

            level['top'] += create_top()
            level['mid_name'] += '\u2551'+rm.id+' '*(13-len(rm.id))+'\u2551'
            level['mid_door'] += w_upper_door+' '*13+e_upper_door
            level['mid_blank'] += '\u2551'+' '*13+'\u2551'
            level['mid_player'] += w_lower_door+' '*6+icon+' '*6+e_lower_door
            level['bot'] += create_bot()
            return level
        else:
            level['top'] += ' '*15
            level['mid_name'] += ' '*15
            level['mid_door'] += ' '*15
            level['mid_blank'] += ' '*15
            level['mid_player'] += ' '*15
            level['bot'] += ' '*15
            return level
