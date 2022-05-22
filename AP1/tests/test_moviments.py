from workspace.moviments import MOVIMENTS, calcule_next_position

def get_positions(none_position):
    choices = MOVIMENTS[none_position]
    positions = []
    for choice in choices:
        positions.append(calcule_next_position(choice, none_position))
    return positions

def test_0_to_choices():
    positions = get_positions(0)
    expected_positions = [3, 1]
    assert positions == expected_positions

def test_1_to_choices():
    positions = get_positions(1)
    expected_positions = [0, 4, 2]
    assert positions == expected_positions

def test_2_to_choices():
    positions = get_positions(2)
    expected_positions = [1, 5]
    assert positions == expected_positions

def test_3_to_choices():
    positions = get_positions(3)
    expected_positions = [0, 6, 4]
    assert positions == expected_positions

def test_4_to_choices():
    positions = get_positions(4)
    expected_positions = [3, 1, 7, 5]
    assert positions == expected_positions

def test_5_to_choices():
    positions = get_positions(5)
    expected_positions = [4, 2, 8]
    assert  positions == expected_positions

def test_6_to_choices():
    positions = get_positions(6)
    expected_positions = [3, 7]
    assert positions == expected_positions

def test_7_to_choices():
    positions = get_positions(7)
    expected_positions = [6, 4, 8]
    assert positions == expected_positions

def test_8_to_choices():
    positions = get_positions(8)
    expected_positions = [7, 5]
    assert positions == expected_positions