from .kth_smallest import kth_smallest


def test_basic_cases():
    nums = [7, 10, 4, 3, 20, 15]
    assert kth_smallest(nums, 3) == 7
    assert kth_smallest(nums, 1) == 3


def test_single_element():
    assert kth_smallest([5], 1) == 5


def test_with_duplicates():
    nums = [3, 1, 2, 2, 4]
    assert kth_smallest(nums, 3) == 2
