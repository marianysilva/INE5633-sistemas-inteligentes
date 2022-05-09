from copy import deepcopy

from workspace.moviments import MOVIMENTS, calcule_next_position

SOLUTION = [1, 2, 3, 4, 5, 6, 7, 8, None]


def create_node_board(current_node, none_position, choice):
    board = deepcopy(current_node.get('board'))

    position = calcule_next_position(choice, none_position)
    board.remove(None)
    board.insert(position, None)

    return board


def create_node_path(current_node):
    path = deepcopy(current_node.get('path'))
    path.append(current_node)
    return path


def is_not_know_board(visited, possibilities, board):
    for node in possibilities:
        node_board = node.get('board')
        if node_board == board:
            return False

    for node in visited:
        node_board = node.get('board')
        if node_board == board:
            return False

    return True


def add_childrens(number_of_nodes, visited, possibilities, current_node):
    none_position = current_node.get('board').index(None)
    choices = MOVIMENTS[none_position]

    for choice in choices:
        board = create_node_board(current_node, none_position, choice)

        if is_not_know_board(visited, possibilities, board):
            number_of_nodes = number_of_nodes + 1
            new_node = {
                'number': number_of_nodes,
                'board': board,
                'path': create_node_path(current_node)
            }

            possibilities.append(new_node)
    return number_of_nodes


def amplitude_search(possibilities):
    ''' FIFO (FIRST IN FIRST OUT) '''
    return possibilities.pop(0)


def depth_search(possibilities):
    ''' LIFO (LAST IN FIRST OUT) '''
    return possibilities.pop()


def calculate_cost():
    pass


def uniform_cost_search(search_function, initial_board):
    number_of_nodes = 0
    visited = []
    possibilities = []

    current_node = {
        'number': 0,
        'board': initial_board,
        'path': []
    }

    while current_node.get('board') != SOLUTION:

        visited.append(current_node)

        number_of_nodes = add_childrens(
            number_of_nodes,
            visited,
            possibilities,
            current_node
        )
        
        current_node = search_function(possibilities)

    return number_of_nodes, visited, possibilities, current_node


def simple_heuristic_search():
    pass


def complex_heuristic_search():
    pass


def search_solution(algorithm, initial_board):
    if algorithm == 1:
        return uniform_cost_search(amplitude_search, initial_board)
    if algorithm == 2:
        return uniform_cost_search(depth_search, initial_board)
    if algorithm == 3:
        return simple_heuristic_search()
    return complex_heuristic_search()
