from .detect_cycle import ListNode, detect_cycle


def build_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def create_cycle(values, pos):
    head = build_list(values)
    if pos < 0:
        return head
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    nodes[-1].next = nodes[pos]
    return head


def test_none_list():
    assert detect_cycle(None) is False


def test_no_cycle():
    head = build_list([1, 2, 3])
    assert detect_cycle(head) is False


def test_with_cycle():
    head = create_cycle([1, 2, 3, 4], 1)
    assert detect_cycle(head) is True
