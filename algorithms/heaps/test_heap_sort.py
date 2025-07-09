from .heap_sort import heap_sort


def test_empty_list():
    assert heap_sort([]) == []


def test_single_element():
    assert heap_sort([1]) == [1]


def test_already_sorted():
    assert heap_sort([1, 2, 3]) == [1, 2, 3]


def test_unsorted_list():
    assert heap_sort([4, 1, 3, 2]) == [1, 2, 3, 4]


def test_with_duplicates():
    assert heap_sort([3, 1, 2, 1]) == [1, 1, 2, 3]
