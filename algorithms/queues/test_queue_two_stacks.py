from .queue_two_stacks import QueueTwoStacks


def test_basic_operations():
    q = QueueTwoStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4


def test_dequeue_empty():
    q = QueueTwoStacks()
    try:
        q.dequeue()
    except IndexError:
        assert True
    else:
        assert False, "Deveria lançar IndexError"
