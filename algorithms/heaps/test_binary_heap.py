from .binary_heap import BinaryHeap


def test_insert_and_peek():
    heap = BinaryHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    assert heap.peek() == 3
    assert heap.size() == 3


def test_extract_min_order():
    heap = BinaryHeap()
    for value in [4, 1, 7, 2]:
        heap.insert(value)
    extracted = [heap.extract_min() for _ in range(4)]
    assert extracted == [1, 2, 4, 7]
    assert heap.size() == 0


def test_extract_empty_raises():
    heap = BinaryHeap()
    try:
        heap.extract_min()
    except IndexError:
        assert True
    else:
        assert False, "Deveria lançar IndexError"
