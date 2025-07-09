from .pre_ordem import TreeNode, pre_ordem


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def test_empty():
    assert pre_ordem(None) == []


def test_single_node():
    root = TreeNode(7)
    assert pre_ordem(root) == [7]


def test_preorder():
    root = build_tree()
    assert pre_ordem(root) == [1, 2, 4, 5, 3, 6]
