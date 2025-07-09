from .merge_sorted_lists import ListNode, merge_sorted_lists


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


def test_both_none():
    assert merge_sorted_lists(None, None) is None


def test_one_empty():
    l2 = build_list([1, 2, 3])
    merged = merge_sorted_lists(None, l2)
    assert to_list(merged) == [1, 2, 3]


def test_merge_basic():
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    merged = merge_sorted_lists(l1, l2)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]
