from .convert_to_binary import GeneralNode, BinaryNode, convert_to_binary


def binary_to_tuple(node: BinaryNode | None):
    if not node:
        return None
    return (node.value, binary_to_tuple(node.left), binary_to_tuple(node.right))


def test_none():
    assert convert_to_binary(None) is None


def test_single_node():
    root = GeneralNode(1)
    result = convert_to_binary(root)
    assert result.value == 1
    assert result.left is None
    assert result.right is None


def test_children_conversion():
    root = GeneralNode(1, [GeneralNode(2), GeneralNode(3, [GeneralNode(4)])])
    result = convert_to_binary(root)

    expected = BinaryNode(1)
    expected.left = BinaryNode(2)
    expected.left.right = BinaryNode(3)
    expected.left.right.left = BinaryNode(4)

    assert binary_to_tuple(result) == binary_to_tuple(expected)
