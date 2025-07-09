from .tree_min_max import TreeNode, tree_min, tree_max


def build_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(30)
    return root


def test_min_single_node():
    node = TreeNode(42)
    assert tree_min(node) == 42


def test_max_single_node():
    node = TreeNode(8)
    assert tree_max(node) == 8


def test_min_and_max_tree():
    root = build_tree()
    assert tree_min(root) == 2
    assert tree_max(root) == 30
