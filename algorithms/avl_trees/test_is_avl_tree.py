from .is_avl_tree import TreeNode, is_avl_tree


def simple_tree(values):
    nodes = [TreeNode(v) for v in values]
    for i, node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]
    return nodes[0] if nodes else None


def test_empty():
    assert is_avl_tree(None) is True


def test_balanced_bst():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.height = 2
    root.left.height = 1
    root.right.height = 1
    assert is_avl_tree(root) is True


def test_unbalanced_tree():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.height = 3
    root.right.height = 2
    root.right.right.height = 1
    assert is_avl_tree(root) is False


def test_bst_property_violation():
    root = TreeNode(10)
    root.left = TreeNode(15)
    root.right = TreeNode(5)
    root.height = 2
    root.left.height = 1
    root.right.height = 1
    assert is_avl_tree(root) is False

