from .cumulative_sum import cumulative_sum


def test_empty():
    assert cumulative_sum([]) == []


def test_single_element():
    assert cumulative_sum([5]) == [5]


def test_positive_numbers():
    assert cumulative_sum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_mixed_numbers():
    assert cumulative_sum([-2, 3, -1, 4]) == [-2, 1, 0, 4]
