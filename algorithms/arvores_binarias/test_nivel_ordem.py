from .nivel_ordem import TreeNode, nivel_ordem


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def test_empty():
    assert nivel_ordem(None) == []


def test_single_node():
    root = TreeNode(7)
    assert nivel_ordem(root) == [7]


def test_level_order():
    root = build_tree()
    assert nivel_ordem(root) == [1, 2, 3, 4, 5, 6]
