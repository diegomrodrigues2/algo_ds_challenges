from .circular_queue import CircularQueue


def test_wrap_around():
    q = CircularQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.is_full() is True
    assert q.dequeue() == 1
    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.is_empty() is True


def test_overflow_underflow():
    q = CircularQueue(2)
    q.enqueue(10)
    q.enqueue(20)
    try:
        q.enqueue(30)
    except IndexError:
        pass
    else:
        assert False, "Inserção em fila cheia deve lançar IndexError"
    q.dequeue()
    q.dequeue()
    try:
        q.dequeue()
    except IndexError:
        pass
    else:
        assert False, "Remoção em fila vazia deve lançar IndexError"
