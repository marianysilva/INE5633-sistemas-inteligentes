from copy import deepcopy

from workspace.MOVEMENTs import MOVEMENTS, calcule_next_position
from workspace.input_output import print_error
from workspace.cost_map import COST_MAP

""" List that contains the correct sequence for the board that is the Puzzle
    solution
"""
SOLUTION = [1, 2, 3, 4, 5, 6, 7, 8, None]

"""
    Node (dict):
        number (number):
            Node number
        board (list of number):
            List that contains the sequence for the board configuration 
        path (list of Node):
            Path taken to reach the Node
        cost:
            Cost of the path taken to reach the node
"""

""" Creates a board for a node based on the parent node, the position of the
    None item on the board and the move choice made by the algorithm

    Parameters:
        parent_node (Node):
            Node that gave rise to the new node for which we are going to
            generate a new board
        none_position (number):
            current position of the None item on the board
        choice (string):
            movement chosen by the algorithm
    Returns:
        board (list of number):
            List that contains the sequence for the board configuration
"""
def create_node_board(parent_node, none_position, choice):
    board = deepcopy(parent_node.get('board'))
    position = calcule_next_position(choice, none_position)
    '''makes an switch of positions between an number and None'''
    board[none_position], board[position] = board[position], board[none_position]
    return board

""" Creates the path to a Node based on the path taken by the parent Node

    Parameters:
        parent_node (Node):
            Node that gave rise to the new node for which we are going to
            generate a new board

    Returns:
        path (list of Node):
            Path taken to reach the Node
"""
def create_node_path(parent_node):
    path = deepcopy(parent_node.get('path'))
    path.append(parent_node)
    return path

""" Checks if the newly created board exists in the list of possibilities or in
    the list of visited nodes. We just want to add nodes with boards that
    haven't been discovered or visited yet.

    Parameters:
        visited (list of Node):
            List of nodes (dictionaries) visited during the execution of the
            algorithm
        possibilities (list of Node):
            List of nodes (dictionaries) List of nodes (dictionaries) that
            were generated as possible paths/solutions
        board (list of number):
            List that contains the sequence for the board configuration

    Returns:
        is_not_known_board (boolean):
            Returns false whenever the node is found in any of the control
            lists and true when the node is not found.
"""
def is_not_known_board(visited, possibilities, board):
    for node in possibilities:
        node_board = node.get('board')
        if node_board == board:
            return False

    for node in visited:
        node_board = node.get('board')
        if node_board == board:
            return False

    return True

""" Adds all possible child nodes of a parent node, as per the parent's current
    board configuration and possible play choices

    Parameters:
        number_of_nodes (number):
            current number of the total generated nodes
        visited (list of Node):
            List of nodes (dictionaries) visited during the execution of the
            algorithm
        possibilities (list of Node):
            List of nodes (dictionaries) List of nodes (dictionaries) that
            were generated as possible paths/solutions during the execution of
            the algorithm
        parent_node (Node):
            Node that gave rise to the new nodes that we will generate
        cost_function (function) = None
            heuristic function used to know the cost of a move

    Returns:
        number_of_nodes (type):
            updated number of total generated nodes
"""
def add_children(number_of_nodes, visited, possibilities, parent_node, cost_function = None):
    none_position = parent_node.get('board').index(None)
    choices = MOVEMENTS[none_position]

    for choice in choices:
        board = create_node_board(parent_node, none_position, choice)
        if is_not_known_board(visited, possibilities, board):
            number_of_nodes = number_of_nodes + 1
            new_node = {
                'number': number_of_nodes,
                'board': board,
                'path': create_node_path(parent_node)
            }            

            if cost_function != None:
                new_node['cost'] = cost_function(board)

            possibilities.append(new_node)

    """If we have a cost heuristic function we need to keep the list of
        possibilities sorted by cost
    """
    if cost_function != None:
        possibilities = sorted(possibilities, key=lambda node: node['cost']) 

    return number_of_nodes

""" To perform a amplitude search, we always need to look at the first element
    of the list of possibilities (ordered from lowest to highest cost when
    there is a cost associated with the path)

    Parameters:
        possibilities (list of Node):
            List of nodes (dictionaries) List of nodes (dictionaries) that
            were generated as possible paths/solutions during the execution of
            the algorithm

    Returns:
        next_node (Node):
            Next node to be visited
"""
def amplitude_search(possibilities):
    ''' FIFO (FIRST IN FIRST OUT) '''
    return possibilities.pop(0)

""" To perform a depth search, we always need to look at the last element of
    the list of possibilities (ordered from lowest to highest cost when there
    is a cost associated with the path)

    Parameters:
        possibilities (list of Node):
            List of nodes (dictionaries) List of nodes (dictionaries) that
            were generated as possible paths/solutions during the execution of
            the algorithm

    Returns:
        next_node (Node):
            Next node to be visited
"""
def depth_search(possibilities):
    ''' LIFO (LAST IN FIRST OUT) '''
    return possibilities.pop()

""" Calculates cost by summing the number of items on the board out of position

    Parameters:
        board (list of number):
            List that contains the sequence for the board configuration

    Returns:
        cost (number):
            number of items on the board out of position
"""
def calculate_simple_cost(board):
    cost = 0
    for index, number in enumerate(SOLUTION):
        if board.index(number) != index:
            cost = cost + 1
    return cost

""" Calculates cost by adding up the number of steps each item needs to take to
    get into the correct position on the board

    Parameters:
        board (list of number):
            List that contains the sequence for the board configuration

    Returns:
        cost (number):
            number of items on the board out of position
"""
def calculate_complex_cost(board):
    cost = 0
    for goal_index, number in enumerate(SOLUTION):
        actual_index = board.index(number)
        cost = cost + COST_MAP.get(goal_index, {}).get(actual_index, 0)
    return cost

""" Search algorithm that, according to the parameters, creates a loop of
    repetition that, from an initial node, will create a tree of possibilities
    in search of a solution

    Parameters:
        search_function (function):
            Function that will be used to define the search strategy
            (amplitude/depth)
        initial_board (list):
            List that contains the initial configuration of the board,
            initialized according to the user's choice
        cost_function (function):
            Function that will be used to define the cost heuristic used

    Returns:
        number_of_nodes (number):
            Total number of nodes generated
        visited (list):
            List of nodes (dictionaries) visited during the execution of the
            algorithm
        possibilities (list):
            List of nodes (dictionaries) List of nodes (dictionaries) that
            were generated as possible paths/solutions
        current_node:
            End node (solution)
"""
def search(search_function, initial_board, cost_function = None):
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

        number_of_nodes = add_children(
            number_of_nodes,
            visited,
            possibilities,
            current_node,
            cost_function
        )
        
        try:
            current_node = search_function(possibilities)
        except:
            print_error(number_of_nodes, visited, possibilities, current_node)
            return number_of_nodes, visited, possibilities, current_node
    return number_of_nodes, visited, possibilities, current_node


""" Performs the switching between the implemented algorithms according to the
    user's choice

    Parameters:
        algorithm (number):
            Number of the chosen algorithm
        initial_board (list):
            List that contains the initial configuration of the board,
            initialized according to the user's choice

    Returns:
        number_of_nodes (number):
            Total number of nodes generated
        visited (list):
            List of nodes (dictionaries) visited during the execution of the
            algorithm
        possibilities (list):
            List of nodes (dictionaries) List of nodes (dictionaries) that
            were generated as possible paths/solutions
        current_node:
            End node (solution)
"""
def search_solution(algorithm, initial_board):
    if algorithm == 1:
        return search(amplitude_search, initial_board)
    if algorithm == 2:
        return search(depth_search, initial_board)
    if algorithm == 3:
        return search(depth_search, initial_board, calculate_simple_cost)
    return search(depth_search, initial_board, calculate_complex_cost)
