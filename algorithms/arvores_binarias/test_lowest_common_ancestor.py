from .lowest_common_ancestor import TreeNode, lowest_common_ancestor


def build_tree():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    return root


def test_empty_tree():
    p = TreeNode(1)
    q = TreeNode(2)
    assert lowest_common_ancestor(None, p, q) is None


def test_same_node():
    root = TreeNode(1)
    assert lowest_common_ancestor(root, root, root) == root


def test_lca_root():
    root = build_tree()
    p = root.left  # 5
    q = root.right  # 1
    assert lowest_common_ancestor(root, p, q) == root


def test_lca_in_subtree():
    root = build_tree()
    p = root.left  # 5
    q = root.left.right.right  # 4
    assert lowest_common_ancestor(root, p, q) == p
