from .min_max_stack import MinMaxStack


def test_basic_operations():
    s = MinMaxStack()
    s.push(3)
    assert s.get_min() == 3
    assert s.get_max() == 3
    s.push(5)
    assert s.get_min() == 3
    assert s.get_max() == 5
    s.push(2)
    assert s.get_min() == 2
    assert s.get_max() == 5
    s.push(7)
    assert s.get_min() == 2
    assert s.get_max() == 7
    assert s.pop() == 7
    assert s.get_max() == 5
    assert s.top() == 2
    assert s.pop() == 2
    assert s.get_min() == 3
    assert s.get_max() == 5


def test_single_element():
    s = MinMaxStack()
    s.push(4)
    assert s.get_min() == 4
    assert s.get_max() == 4
    assert s.pop() == 4
