from validation import check_and_converter_move_input

from tiles import is_valid_set, play_set

def read_player_move(hand):

    while True:

        move = input('Choose tile positions or D to draw >')
        

        if move.strip().lower() == 'd':

            return None
        

        move = move.split(sep=' ')
        

        indexes = check_and_converter_move_input(move, len(hand))
        

        if indexes:

            if is_valid_set([hand[i] for i in indexes]):

                return indexes
            

        print('Invalid set. Try again.')
        
        

def find_computer_move(hand):
    set_hand = set(hand)
    set_hand = list(hand)

    sort_by_number = sorted(set_hand, key= lambda t: (t[0], t[1]))

    sort_by_color = sorted(set_hand, key= lambda t: (t[1], t[0]))
    
    indexes = []
    original_indexes = []
    tiles = []
    

    for i in range(len(sort_by_number) - 3):

        if is_valid_set([sort_by_number[i], sort_by_number[i+1], sort_by_number[i+2]]) and sort_by_number[i][0] == sort_by_number[i+1][0]:
            indexes = [i, i+1, i+2]

            if sort_by_number[-1] not in indexes and is_valid_set([sort_by_number[i], sort_by_number[i+1], sort_by_number[i+2], sort_by_number[i+3]]):
                indexes.append(i+3)

            break
    
    if indexes:
        for i in indexes:
            original_indexes.append(hand.index(sort_by_number[i]))
        
        return original_indexes


    for i in range(len(sort_by_color) - 3):
        if indexes and tiles[-1][0] < 13:
            if is_valid_set(tiles + [sort_by_color[i+2]]):
                tiles.append(sort_by_color[i+2])
                indexes.append(i+2)

                continue

            break
                

        elif is_valid_set([sort_by_color[i], sort_by_color[i+1], sort_by_color[i+2]]):
            tiles = [sort_by_color[i], sort_by_color[i+1], sort_by_color[i+2]]
            indexes = [i, i+1, i+2]
    
    if indexes:
        for i in indexes:
            original_indexes.append(hand.index(sort_by_color[i]))
                
    return original_indexes



def play_turn(hand, pool, table, move):
    if move:
        results = play_set(hand, table, move)
        return results
        
    elif pool:
        hand.append(pool.pop())
        return 'draw'
    
    else:
        return 'pass'