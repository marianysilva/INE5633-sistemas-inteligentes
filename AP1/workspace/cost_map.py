"""
    COST_MAP (dict):
        dictionary that maps the cost for a board item to arrive at the correct
        position from any position on the board
"""
COST_MAP = {
    # goal_index == 0
    0: {
        # actual_index == ?: cost to 0
        0: 0, 1: 1, 2: 2, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 4
    },
    # goal_index == 1
    1: {
        # actual_index == ?: cost to 1
        0: 1, 1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 4
    },
    # goal_index == 2
    2: {
        # actual_index == ?: cost to 2
        0: 2, 1: 1, 2: 0, 3: 3, 4: 2, 5: 1, 6: 4, 7: 3, 8: 2
    },
    # goal_index == 3
    3: {
        # actual_index == ?: cost to 3
        0: 1 , 1: 2, 2: 3, 3: 0, 4: 1, 5: 2, 6: 1, 7: 2, 8: 3
    },
    # goal_index == 4
    4: {
        # actual_index == ?: cost to 4
        0: 2, 1: 1, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 1, 8: 2
    },
    # goal_index == 5
    5: {
        # actual_index == ?: cost to 5
        0: 3, 1: 2, 2: 1, 3: 2, 4: 1, 5: 0, 6: 3, 7: 2, 8: 1
    },
    # goal_index == 6
    6: {
        # actual_index == ?: cost to 6
        0: 2, 1: 3, 2: 4, 3: 1, 4: 2, 5: 3, 6: 0, 7: 1, 8: 2
    },
    # goal_index == 7
    7: {
        # actual_index == ?: cost to 7
        0: 3, 1: 2, 2: 3, 3: 2, 4: 1, 5: 2, 6: 1, 7: 0, 8: 1
    },
    # goal_index == 8
    8: {
        # actual_index == ?: cost to 8
        0: 4, 1: 3, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 0
    }
}