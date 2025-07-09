from .merge_k_sorted_lists import merge_k_sorted_lists


def test_merge_basic():
    lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert merge_k_sorted_lists(lists) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_merge_with_empty():
    lists = [[1, 3], [], [2]]
    assert merge_k_sorted_lists(lists) == [1, 2, 3]


def test_all_empty():
    assert merge_k_sorted_lists([[], [], []]) == []
