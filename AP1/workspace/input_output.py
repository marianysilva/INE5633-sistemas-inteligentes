"""
    input_output.py:
        file with data entry functions to be used in the algorithm and also
        functions used to show the results of the search for the best solution
        for the user
"""
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
    choices = [1, 2, 3, 4]
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


def print_node_counts(number_of_nodes, visited, possibilities):
    print(f'NODES: {number_of_nodes}')
    print(f'VISITED: {len(visited)}')
    print(f'OPEN POSSIBILITIES: {len(possibilities)} \n\n')


def print_node(node):
    print('NODE NUMBER: ', node.get('number'))
    print('HEURISTIC COST: ', node.get('cost'))
    print('BOARD:')
    print_board(node.get('board'))


def print_nodes(nodes):
    cost = 0
    for node in nodes:
        cost = cost + node.get('cost', 0)
        print_node(node)
        print('\n')
    return cost


def print_result(number_of_nodes, visited, possibilities, final_node):

    print_node_counts(number_of_nodes, visited, possibilities)

    nodes = final_node.get('path')
    heuristic_cost = print_nodes(nodes)

    print_node(final_node)
    print('\n')

    print('HEURISTIC COST: ', heuristic_cost)
    print('COST: ', len(nodes))

def print_error(number_of_nodes, visited, possibilities, final_node):
    print("[ERRO] O algoritmo chegou em um impasse!")

    print("\n[VISITED NODES]:")
    print_nodes(visited)
    print("========================================")
    print("\n[POSSIBILITIES NODES]:")
    print_nodes(possibilities)
    print("========================================")

    print_result(number_of_nodes, visited, possibilities, final_node)
