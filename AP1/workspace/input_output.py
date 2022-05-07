def convert_choice(choice):
    try:
        if choice.lower() == "none":
            return None
        return int(choice)
    except:
        return -1

def print_board(board):
    print(' '.join(map(str, board[0:3])))
    print(' '.join(map(str, board[3:6])))
    print(' '.join(map(str, board[6:9])))

def algorithm_input():
    choices = [1, 2, 3]
    choice = 0
    while convert_choice(choice) not in choices:
        choice = input("ENTER THE NUMBER OF THE ALGORITHM: ")
        if convert_choice(choice) not in choices:
            print("[ERROR] CHOOSE ONE OF THE OPTIONS")
    return int(choice)

def board_input():
    choices = [1, 2, 3, 4, 5, 6, 7, 8, None]
    board = []

    choice = -1
    while len(choices) > 0:
        choice = input(f"ENTER {len(board) + 1}º NUMBER OR NONE: ")
        choice = convert_choice(choice)
        if choice not in choices:
            print("[ERROR] CHOOSE ONE OF THE OPTIONS")
            print('    ', ' '.join(map(str, choices)))
            choice = -1
        else:
            board.append(choice)
            choices.remove(choice)
            choice = -1
    return board

def get_user_inputs():
    print('''
    HELLO USER
    
    LET'S START OUR 8 PUZZLE GAME

    FIRST CHOOSE THE ALGORITHM STRATEGY:

        1 - Uniform Cost    2 - Simple Heuristic    3 - Complex Heuristic

    THEN INPUT THE INITIAL STATE OF YOUR BOARD, OPTIONS:

        1 2 3 4 5 6 7 8 None
    ''')

    algorithm = algorithm_input()
    initial_state = board_input()

    print('\nTHE INITIAL STATE IS:')
    print_board(initial_state)

    return algorithm, initial_state