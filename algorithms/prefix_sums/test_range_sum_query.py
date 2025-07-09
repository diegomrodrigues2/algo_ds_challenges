from .range_sum_query import range_sum


def test_empty_queries():
    assert range_sum([1, 2, 3], []) == []


def test_single_interval():
    nums = [1, 2, 3, 4, 5]
    assert range_sum(nums, [(1, 3)]) == [9]


def test_multiple_intervals():
    nums = [3, 8, 1, -2, 6]
    queries = [(0, 2), (2, 4), (1, 3)]
    assert range_sum(nums, queries) == [12, 5, 7]
