from workspace.moviments import MOVIMENTS
from workspace.engine import create_node_board

def get_board(parent_node):
    none_position = parent_node.get('board').index(None)
    choices = MOVIMENTS[none_position]
    boards = []
    for choice in choices:
        boards.append(create_node_board(parent_node, none_position, choice))
    return boards

def test_0_to_choices():
    parent_node = {
        "board": [None, 1, 2, 3, 4, 5, 6, 7, 8]
    }
    boards = get_board(parent_node)
    expected_boards = [
        [3, 1, 2, None, 4, 5, 6, 7, 8],
        [1, None, 2, 3, 4, 5, 6, 7, 8]
    ]
    assert boards == expected_boards

def test_1_to_choices():
    parent_node = {
        "board": [1, None, 2, 3, 4, 5, 6, 7, 8]
    }
    boards = get_board(parent_node)
    expected_boards = [
        [None, 1, 2, 3, 4, 5, 6, 7, 8],
        [1, 4, 2, 3, None, 5, 6, 7, 8],
        [1, 2, None, 3, 4, 5, 6, 7, 8]
    ]
    assert boards == expected_boards

def test_2_to_choices():
    parent_node = {
        "board": [1, 2, None, 3, 4, 5, 6, 7, 8]
    }
    boards = get_board(parent_node)
    expected_boards = [
        [1, None, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 5, 3, 4, None, 6, 7, 8]
    ]
    assert boards == expected_boards

def test_3_to_choices():
    parent_node = {
        "board": [1, 2, 3, None, 4, 5, 6, 7, 8]
    }

    boards = get_board(parent_node)
    expected_boards = [
        [None, 2, 3, 1, 4, 5, 6, 7, 8],
        [1, 2, 3, 6, 4, 5, None, 7, 8],
        [1, 2, 3, 4, None, 5, 6, 7, 8]
    ]
    assert boards == expected_boards

def test_4_to_choices():
    parent_node = {
        "board": [1, 2, 3, 4, None, 5, 6, 7, 8]
    }

    boards = get_board(parent_node)
    expected_boards = [
        [1, 2, 3, None, 4, 5, 6, 7, 8],
        [1, None, 3, 4, 2, 5, 6, 7, 8],
        [1, 2, 3, 4, 7, 5, 6, None, 8],
        [1, 2, 3, 4, 5, None, 6, 7, 8]
    ]
    assert boards == expected_boards

def test_5_to_choices():
    parent_node = {
        "board": [1, 2, 3, 4, 5, None, 6, 7, 8]
    }

    boards = get_board(parent_node)
    expected_boards = [
        [1, 2, 3, 4, None, 5, 6, 7, 8],
        [1, 2, None, 4, 5, 3, 6, 7, 8],
        [1, 2, 3, 4, 5, 8, 6, 7, None]
    ]
    assert boards == expected_boards

def test_6_to_choices():
    parent_node = {
        "board": [1, 2, 3, 4, 5, 6, None, 7, 8]
    }

    boards = get_board(parent_node)
    expected_boards = [
        [1, 2, 3, None, 5, 6, 4, 7, 8],
        [1, 2, 3, 4, 5, 6, 7, None, 8]
    ]
    assert boards == expected_boards

def test_7_to_choices():
    parent_node = {
        "board": [1, 2, 3, 4, 5, 6, 7, None, 8]
    }

    boards = get_board(parent_node)
    expected_boards = [
        [1, 2, 3, 4, 5, 6, None, 7, 8],
        [1, 2, 3, 4, None, 6, 7, 5, 8],
        [1, 2, 3, 4, 5, 6, 7, 8, None]
    ]
    assert boards == expected_boards

def test_7_to_choices():
    parent_node = {
        "board": [1, 2, 3, 4, 5, 6, 7, 8, None]
    }

    boards = get_board(parent_node)
    expected_boards = [
        [1, 2, 3, 4, 5, 6, 7, None, 8,],
        [1, 2, 3, 4, 5, None, 7, 8, 6],
    ]
    assert boards == expected_boards