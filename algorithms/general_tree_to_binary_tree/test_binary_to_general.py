from .binary_to_general import BinaryNode, GeneralNode, binary_to_general


def general_to_tuple(node: GeneralNode | None):
    if not node:
        return None
    return (node.value, [general_to_tuple(child) for child in node.children])


def test_none():
    assert binary_to_general(None) is None


def test_single_node():
    root = BinaryNode(1)
    result = binary_to_general(root)
    assert result.value == 1
    assert result.children == []


def test_conversion_with_siblings():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    root.left.right = BinaryNode(3)
    root.left.right.left = BinaryNode(4)

    result = binary_to_general(root)

    expected = GeneralNode(1, [GeneralNode(2), GeneralNode(3, [GeneralNode(4)])])
    assert general_to_tuple(result) == general_to_tuple(expected)
