from .tree_height import TreeNode, tree_height


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    return root


def test_empty_tree():
    assert tree_height(None) == 0


def test_single_node():
    node = TreeNode(7)
    assert tree_height(node) == 1


def test_tree_height():
    root = build_tree()
    assert tree_height(root) == 4
