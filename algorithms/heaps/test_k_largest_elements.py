from .k_largest_elements import k_largest_elements


def test_k_zero():
    assert k_largest_elements([1, 2, 3], 0) == []


def test_k_equal_length():
    assert k_largest_elements([3, 1, 2], 3) == [3, 2, 1]


def test_basic_case():
    result = k_largest_elements([5, 2, 8, 1, 3], 2)
    assert result == [8, 5]


def test_k_greater_than_length():
    result = k_largest_elements([1, 2, 3], 5)
    assert result == [3, 2, 1]


def test_duplicate_elements():
    result = k_largest_elements([3, 1, 4, 1, 5, 9, 2, 6], 3)
    assert result == [9, 6, 5]


def test_negative_numbers():
    result = k_largest_elements([-5, -2, -8, -1, -3], 2)
    assert result == [-1, -2]


def test_single_element():
    result = k_largest_elements([42], 1)
    assert result == [42]


def test_empty_array():
    result = k_largest_elements([], 3)
    assert result == []
