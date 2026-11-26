from tiles import create_pool
from turn import read_player_move, find_computer_move, play_turn

def play_game():
    pool = create_pool()
    table = []

    player_hand = [(1, 'R')]
    computer_hand = [(1, 'R'), (2, 'R'), (3, 'R'), (4, 'R'), (5, 'R'), (6, 'R'), (7, 'R'), (8, 'R'), (9, 'R'), (10, 'R'), (11, 'R'), (12, 'R'), (13, 'R'), (14, 'R')]
    skip_counter = 0
    turn = 1


    # for i in range(9):
    #     player_hand.append(pool.pop())
    #     computer_hand.append(pool.pop())

    while skip_counter < 2:
        if table:
            print('Table:')
            for i, set_ in enumerate(table):
                print(f'[{i + 1}]', end=' ')
                for tile in set_:
                    print(tile[0],tile[1], sep='', end=' ')
                print()
        else:
            print('Table: (empty)')
        
        print(f'Computer tiles: {len(computer_hand)}')
        print('Your hand:')
        for i, tile in enumerate(player_hand):
            print(f'[{i+1}] {tile[0]}{tile[1]}', end=' ')
        print()
        
        if turn:
            indexes = read_player_move(player_hand)
            results = play_turn(player_hand, pool, table, indexes)
        
            if results == 'draw':
                print('you draw a tile!')
                skip_counter = 0
            elif results == 'pass':
                print('you skipped turn!')
                skip_counter += 1
            else:
                print('You played:')
                for i, tile in enumerate(results):
                    print(f'[{i+1}] {tile[0]}{tile[1]}', end=' ')
                print()
                skip_counter = 0
            
            if not player_hand:
                print('You win!')
                break
            
            turn = 0
        
        else:
            indexes = find_computer_move(computer_hand)
            results = play_turn(computer_hand, pool, table, indexes)
            
            if results == 'draw':
                print('The computer draw a tile!')
                skip_counter = 0
            elif results == 'pass':
                print('The computer skipped turn!')
                skip_counter += 1
            else:
                print('Computer played:')
                for i, tile in enumerate(results):
                    print(f'[{i+1}] {tile[0]}{tile[1]}', end=' ')
                print()
                skip_counter = 0
                
            if not computer_hand:
                print('The computer win!')
                break
            
            turn = 1

    if skip_counter == 2:
        if len(player_hand) > len(computer_hand):
            print('You win!')
        elif len(computer_hand) > len(player_hand):
            print('The computer win!')
        else:
            print('Its a draw!')
            
play_game()