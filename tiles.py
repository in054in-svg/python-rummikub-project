from random import randint

def create_pool():
    pool = []
    tiles_types = ('R', 'B', 'K', 'O')
    for i in range(4):
        for j in range(1, 14):
            tile = (j, tiles_types[i])
            pool.append(tile)
            pool.append(tile)
    
    mix_a_pool(pool)
    return pool


def mix_a_pool(pool):
    for _ in range(1000):
        i1 = randint(0, len(pool) - 1)
        i2 = randint(0, len(pool) - 1)
        while i2 == i1:
            i2 = randint(0, len(pool) - 1)
        pool[i1], pool[i2] = pool[i2], pool[i1]
        
        
def is_valid_set(tiles):
    tiles.sort()
    group_counter = 0
    sequence_counter = 0
    if_group = True
    if_sequence = True
    for i in range(len(tiles) - 1):
        if tiles[i][0] == tiles[i+1][0] and tiles[i][1] != tiles[i+1][1] and tiles[i+1] not in tiles[:i+1]  and if_group:
            group_counter += 1
        else:
            if_group = False
        
        if tiles[i][0] + 1 == tiles[i+1][0] and tiles[i][1] == tiles[i+1][1] and if_sequence:
            sequence_counter += 1
        else:
            if_sequence = False
            
    if (group_counter >= 2 and if_group) or (sequence_counter >= 2 and if_sequence):
        return True
    
    return False


def play_set(hand, table, indexes):
    transition_list = []
    for i in indexes:
        transition_list.append(hand[i])
    for tile in transition_list:
        hand.remove(tile)
    
    table.append(transition_list)
    
    return sorted(transition_list)