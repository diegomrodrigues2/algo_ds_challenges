from .rotate_right import TreeNode, rotate_right


def test_rotate_right_none():
    assert rotate_right(None) is None


def test_rotate_right_single():
    node = TreeNode(1)
    assert rotate_right(node) is node


def test_rotate_right_simple():
    root = TreeNode(2)
    root.left = TreeNode(1)
    new_root = rotate_right(root)
    assert new_root.value == 1
    assert new_root.right.value == 2
    assert new_root.right.left is None


def test_rotate_right_subtree():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    new_root = rotate_right(root)
    assert new_root.value == 1
    assert new_root.right.value == 3
    assert new_root.right.left.value == 2

