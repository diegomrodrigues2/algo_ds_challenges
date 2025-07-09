from .simple_queue import Queue


def test_new_queue_empty():
    q = Queue()
    assert q.is_empty() is True
    assert q.size() == 0


def test_enqueue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.is_empty() is False
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty() is True


def test_dequeue_empty_raises():
    q = Queue()
    try:
        q.dequeue()
    except IndexError:
        assert True
    else:
        assert False, "Deveria lançar IndexError"
