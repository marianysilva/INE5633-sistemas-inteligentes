from workspace.example import double_array

# Test using function call.
def test_double_array():
    assert double_array([1, 2, 3]) == [2, 4, 6]