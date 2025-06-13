from matching_sums import find_matching_sums
import random

### Type Checking Tests ###
def test_find_matching_sums_with_different_input_types():
    # None
    try:
        find_matching_sums(None)
        assert False, "Function completed successfully with none input"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"
    
    # String
    try:
        find_matching_sums("test")
        assert False, "Function completed successfully with string input"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"

    # Float
    try:
        find_matching_sums([1.0, 2.0, 3.0])
        assert False, "Function completed successfully with float input"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"

    # Set
    try:
        find_matching_sums({1, 2, 3})
        assert False, "Function completed successfully with set input"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"

    # Composite Input Types
    # With float
    try:
        find_matching_sums([1, 2, 3.0])
        assert False, "Function completed successfully with composite input (float)"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"  
    
    # With string
    try:
        find_matching_sums([1, 2, '3'])
        assert False, "Function completed successfully with composite input (str)"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"
    
    # Empty list
    result = find_matching_sums([])
    assert result == {}

### Functional Tests ###
def test_find_matching_sums_with_insufficient_elements():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)

    # Single element
    result = find_matching_sums([x])
    assert result == {}

    # Two elements
    result = find_matching_sums([x, y])
    assert result == {}

    # Three elements
    result = find_matching_sums([x, y, z])
    assert result == {}


def test_find_matching_sums_with_zero():
    result = find_matching_sums([1, 2, 3, 0])
    assert result == {
        '3': [(1, 2), (3, 0)],
    }

def test_find_matching_sums_with_negative():
    result = find_matching_sums([1, 2, 3, -1, -2, -3])
    assert result == {
        '-1': [(1, -2), (2, -3)],
        '0': [(1, -1), (2, -2), (3, -3)],
        '1': [(2, -1), (3, -2)],
    }

def test_find_matching_sums_with_reverse_simple_input():
    arr = [1, 2, 3, 3, 2, 1]
    result = find_matching_sums(arr)
    assert result == {
        '4': [(1, 3), (2, 2)],
    }

def test_find_matching_sums_with_duplicate_input():
    arr = [1, 2, 3, 1, 2, 3]
    result = find_matching_sums(arr)
    assert result == {
        '4': [(1, 3), (2, 2)],
    }

def test_find_matching_sums_with_larger_duplicate_input():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_matching_sums(arr)
    assert result == {
        '4': [(1, 3), (2, 2)],
        '5': [(1, 4), (2, 3)],
        '6': [(1, 5), (2, 4), (3, 3)],
        '7': [(1, 6), (2, 5), (3, 4)],
        '8': [(1, 7), (2, 6), (3, 5), (4, 4)],
        '9': [(1, 8), (2, 7), (3, 6), (4, 5)],
        '10': [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)],
        '11': [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)],
        '12': [(2, 10), (3, 9), (4, 8), (5, 7), (6, 6)],
        '13': [(3, 10), (4, 9), (5, 8), (6, 7)],
        '14': [(4, 10), (5, 9), (6, 8), (7, 7)],
        '15': [(5, 10), (6, 9), (7, 8)],
        '16': [(6, 10), (7, 9), (8, 8)],
        '17': [(7, 10), (8, 9)],
        '18': [(8, 10), (9, 9)],
    }

def test_find_matching_sums_with_range_input():
    arr = list(range(1, 11))
    result = find_matching_sums(arr)
    assert result == {
        '5': [(1, 4), (2, 3)],
        '6': [(1, 5), (2, 4)],
        '7': [(1, 6), (2, 5), (3, 4)],
        '8': [(1, 7), (2, 6), (3, 5)],
        '9': [(1, 8), (2, 7), (3, 6), (4, 5)],
        '10': [(1, 9), (2, 8), (3, 7), (4, 6)],
        '11': [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)],
        '12': [(2, 10), (3, 9), (4, 8), (5, 7)],
        '13': [(3, 10), (4, 9), (5, 8), (6, 7)],
        '14': [(4, 10), (5, 9), (6, 8)],
        '15': [(5, 10), (6, 9), (7, 8)],
        '16': [(6, 10), (7, 9)],
        '17': [(7, 10), (8, 9)],
    }

def test_find_matching_sums_with_all_identical_input():
    arr = [2, 2, 2, 2]
    result = find_matching_sums(arr)
    assert result == {}

def test_find_matching_sums_with_first_example():
    result = find_matching_sums([6, 4, 12, 10, 22, 54, 32, 42, 21, 11])
    assert result == {
        '16': [(4, 12), (6, 10)],
        '32': [(10, 22), (21, 11)],
        '33': [(12, 21), (22, 11)],
        '43': [(22, 21), (32, 11)],
        '53': [(32, 21), (42, 11)],
        '54': [(12, 42), (22, 32)],
        '64': [(10, 54), (22, 42)],
    }

def test_find_matching_sums_with_first_example_tuple():
    result = find_matching_sums((6, 4, 12, 10, 22, 54, 32, 42, 21, 11))
    assert result == {
        '16': [(4, 12), (6, 10)],
        '32': [(10, 22), (21, 11)],
        '33': [(12, 21), (22, 11)],
        '43': [(22, 21), (32, 11)],
        '53': [(32, 21), (42, 11)],
        '54': [(12, 42), (22, 32)],
        '64': [(10, 54), (22, 42)],
    }

def test_find_matching_sums_with_first_example_set():
    try:
        find_matching_sums({6, 4, 12, 10, 22, 54, 32, 42, 21, 11})
        assert False, "Function completed successfully with set input"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"

def test_find_matching_sums_with_second_example():
    result = find_matching_sums([4, 23, 65, 67, 24, 12, 86])
    assert result == {
        '90': [(4, 86), (23, 67)],
    }   

def test_find_matching_sums_with_second_example_tuple():
    result = find_matching_sums((4, 23, 65, 67, 24, 12, 86))
    assert result == {
        '90': [(4, 86), (23, 67)],
    }  

def test_find_matching_sums_with_second_example_set():
    try:
        find_matching_sums({4, 23, 65, 67, 24, 12, 86})
        assert False, "Function completed successfully with set input"
    except ValueError as e:
        assert str(e) == "Input must be a list or set of integers"

def test_find_matching_sums_with_duplicate_second_example():
    result = find_matching_sums([4, 23, 65, 67, 24, 12, 86, 4, 23, 65, 67, 24, 12, 86])
    assert result == {
        '90': [(4, 86), (23, 67)],
    }

def test_find_matching_sums_with_large_input():
    arr = list(range(1, 1001))
    result = find_matching_sums(arr)
    assert len(result) > 0
    assert len(result) < len(arr) * (len(arr) - 1) // 2
    
    sample_sums = ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1000']
    assert all([sum in result for sum in sample_sums])

    sample_pairs = [(1, 499), (2, 498), (3, 497), (4, 496), (5, 495), (6, 494), (7, 493), (8, 492), (9, 491), (10, 490)]
    assert all([pair in result['500'] for pair in sample_pairs])
