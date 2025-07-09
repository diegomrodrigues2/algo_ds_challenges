from .search_bst import TreeNode, search_bst


def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def build_bst(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


def test_empty_tree():
    assert search_bst(None, 1) is None


def test_single_node_found():
    node = TreeNode(2)
    result = search_bst(node, 2)
    assert result is node


def test_single_node_not_found():
    node = TreeNode(2)
    assert search_bst(node, 3) is None


def test_search_existing():
    values = [4, 2, 6, 1, 3, 5, 7]
    root = build_bst(values)
    result = search_bst(root, 5)
    assert result is not None
    assert result.value == 5


def test_search_missing():
    values = [4, 2, 6, 1, 3, 5, 7]
    root = build_bst(values)
    assert search_bst(root, 8) is None
