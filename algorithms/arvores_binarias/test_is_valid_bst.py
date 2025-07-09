from .is_valid_bst import TreeNode, is_valid_bst


def test_empty():
    assert is_valid_bst(None) is True


def test_simple_valid():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert is_valid_bst(root) is True


def test_invalid_subtree():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert is_valid_bst(root) is False


def test_invalid_left_greater():
    root = TreeNode(5)
    root.left = TreeNode(7)
    assert is_valid_bst(root) is False
