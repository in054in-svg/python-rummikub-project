def check_and_converter_move_input(move, hand_size):
    convert_move = []
    for i, m in enumerate(move):
        if m.isdigit() and m not in move[:i] and 1 <= int(m) <= hand_size:
            convert_move.append(int(m) - 1)
        else:
            return None
        
    return convert_move