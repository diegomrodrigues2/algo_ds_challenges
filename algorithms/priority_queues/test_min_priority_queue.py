from .min_priority_queue import MinPriorityQueue


def test_insert_and_extract():
    pq = MinPriorityQueue()
    pq.insert(5)
    pq.insert(3)
    pq.insert(4)
    assert pq.size() == 3
    assert pq.peek_min() == 3
    assert pq.extract_min() == 3
    assert pq.extract_min() == 4
    assert pq.extract_min() == 5
    assert pq.is_empty() is True


def test_extract_empty_raises():
    pq = MinPriorityQueue()
    try:
        pq.extract_min()
    except IndexError:
        assert True
    else:
        assert False, "Deveria lançar IndexError"


def test_peek_empty_raises():
    pq = MinPriorityQueue()
    try:
        pq.peek_min()
    except IndexError:
        assert True
    else:
        assert False, "Deveria lançar IndexError"
