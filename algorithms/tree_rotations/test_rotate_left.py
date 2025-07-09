from .rotate_left import TreeNode, rotate_left


def test_rotate_left_none():
    assert rotate_left(None) is None


def test_rotate_left_single():
    node = TreeNode(1)
    assert rotate_left(node) is node


def test_rotate_left_simple():
    root = TreeNode(1)
    root.right = TreeNode(2)
    new_root = rotate_left(root)
    assert new_root.value == 2
    assert new_root.left.value == 1
    assert new_root.left.right is None


def test_rotate_left_subtree():
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    new_root = rotate_left(root)
    assert new_root.value == 3
    assert new_root.left.value == 1
    assert new_root.left.right.value == 2
