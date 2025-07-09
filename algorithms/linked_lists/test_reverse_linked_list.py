from .reverse_linked_list import ListNode, reverse_linked_list


def build_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result


def test_reverse_empty():
    assert reverse_linked_list(None) is None


def test_reverse_single():
    node = ListNode(1)
    result = reverse_linked_list(node)
    assert result.value == 1
    assert result.next is None


def test_reverse_multiple():
    head = build_list([1, 2, 3, 4])
    reversed_head = reverse_linked_list(head)
    assert to_list(reversed_head) == [4, 3, 2, 1]
