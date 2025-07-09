from .k_largest_elements import k_largest_elements


def test_k_zero():
    assert k_largest_elements([1, 2, 3], 0) == []


def test_k_equal_length():
    assert k_largest_elements([3, 1, 2], 3) == [3, 2, 1]


def test_basic_case():
    result = k_largest_elements([5, 2, 8, 1, 3], 2)
    assert result == [8, 5]
