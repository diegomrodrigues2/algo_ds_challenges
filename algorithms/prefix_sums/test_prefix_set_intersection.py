from .prefix_set_intersection import prefix_set_intersection


def test_empty_lists():
    assert prefix_set_intersection([], []) == []


def test_basic_example():
    a = [1, 2, 3]
    b = [2, 3, 4]
    assert prefix_set_intersection(a, b) == [0, 1, 2]


def test_same_lists():
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    assert prefix_set_intersection(a, b) == [1, 2, 3, 4]


def test_with_duplicates():
    a = [1, 2, 2, 3]
    b = [2, 2, 3, 3]
    assert prefix_set_intersection(a, b) == [0, 1, 1, 2]
