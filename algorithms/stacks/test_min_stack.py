from .min_stack import MinStack


def test_basic_operations():
    s = MinStack()
    s.push(3)
    assert s.get_min() == 3
    s.push(5)
    assert s.get_min() == 3
    s.push(2)
    assert s.get_min() == 2
    s.push(1)
    assert s.get_min() == 1
    assert s.pop() == 1
    assert s.get_min() == 2
    assert s.top() == 2
    assert s.pop() == 2
    assert s.get_min() == 3


def test_single_element():
    s = MinStack()
    s.push(10)
    assert s.top() == 10
    assert s.get_min() == 10
    assert s.pop() == 10
