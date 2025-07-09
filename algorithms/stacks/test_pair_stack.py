from .pair_stack import PairStack


def test_push_pop():
    s = PairStack()
    s.push((1, 2))
    s.push((3, 4))
    assert s.top() == (3, 4)
    assert s.pop() == (3, 4)
    assert s.pop() == (1, 2)
    assert s.is_empty() is True


def test_empty_pop_raises():
    s = PairStack()
    try:
        s.pop()
    except IndexError:
        assert True
    else:
        assert False, "Deveria lançar IndexError"


def test_is_empty():
    s = PairStack()
    assert s.is_empty() is True
    s.push((5, 6))
    assert s.is_empty() is False
