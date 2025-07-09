from .in_ordem import TreeNode, in_ordem


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def test_empty():
    assert in_ordem(None) == []


def test_single_node():
    root = TreeNode(7)
    assert in_ordem(root) == [7]


def test_inorder():
    root = build_tree()
    assert in_ordem(root) == [4, 2, 5, 1, 3, 6]
