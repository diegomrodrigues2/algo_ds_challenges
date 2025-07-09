from .count_nodes import TreeNode, count_nodes


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def test_empty_tree():
    assert count_nodes(None) == 0


def test_single_node():
    node = TreeNode(7)
    assert count_nodes(node) == 1


def test_count_nodes():
    root = build_tree()
    assert count_nodes(root) == 5
