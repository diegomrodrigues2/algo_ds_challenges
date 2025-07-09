from .equal_stacks import equal_stacks


def test_example_case():
    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]
    assert equal_stacks(h1, h2, h3) == 5


def test_already_equal():
    h1 = [2, 2]
    h2 = [4]
    h3 = [1, 3]
    assert equal_stacks(h1, h2, h3) == 4


def test_no_possible_height():
    assert equal_stacks([3], [2], [1]) == 0


def test_empty_stacks():
    assert equal_stacks([], [], []) == 0
