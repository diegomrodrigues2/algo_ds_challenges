from .pos_ordem import TreeNode, pos_ordem


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def test_empty():
    assert pos_ordem(None) == []


def test_single_node():
    root = TreeNode(7)
    assert pos_ordem(root) == [7]


def test_postorder():
    root = build_tree()
    assert pos_ordem(root) == [4, 5, 2, 6, 3, 1]
