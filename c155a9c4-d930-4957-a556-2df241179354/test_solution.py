import pytest
from solution import ww

"""
REMEMBER:
- Your tests should be comprehensive. They should test 
  - edge cases 
  - large inputs 
  - as many scenarios as possible.
- Minimum 5 tests. Maximum 10 tests.
- More tests, higher-quality tests === higher payouts.
"""


def test_one():
    """
    # Example assertion:
    assert ww(
        arg1=value1,
        arg2=value2
    ) == expected_result
    
    Rename this function to test_{description of the test}, e.g. test_basic_graph_traversal
    """
    assert ww(# args) == # expected result

def test_two():
    """
    # Example assertion:
    assert ww(
        arg1=value1,
        arg2=value2
    ) == expected_result
    
    Rename this function to test_{description of the test}, e.g. test_graph_traversal_with_multiple_paths
    """
    assert ww(# args) == # expected result

def test_three():
    """
    # Example assertion:
    assert ww(
        arg1=value1,
        arg2=value2
    ) == expected_result
    
    Rename this function to test_{description of the test}, e.g. test_invalid_graph_input
    """
    assert ww(# edge case args) == # expected result

def test_four():
    """
    # Example assertion:
    assert ww(
        arg1=value1,
        arg2=value2
    ) == expected_result
    
    Rename this function to test_{description of the test}, e.g. test_massive_graph
    """
    assert ww(# large input) == # expected result

def test_five():
    """
    # Example assertion:
    with pytest.raises(ValueError):
        ww(invalid_args)
    
    Rename this function to test_{description of the test}, e.g. test_proper_memoization
    """
    try:
        ww(# invalid args)
        assert False, "Expected error was not raised"
    except ValueError as e:
        assert str(e) == "Expected error message"

    assert ww(# args) == # expected result 