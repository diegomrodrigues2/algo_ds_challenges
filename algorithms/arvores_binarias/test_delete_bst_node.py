from .delete_bst_node import TreeNode, delete_bst_node


def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def test_delete_from_empty():
    assert delete_bst_node(None, 5) is None


def test_delete_leaf():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    result = delete_bst_node(root, 3)
    assert inorder(result) == [5, 7]


def test_delete_single_child():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    result = delete_bst_node(root, 3)
    assert inorder(result) == [2, 5]


def test_delete_two_children():
    root = None
    for v in [5, 3, 8, 2, 4, 7, 9]:
        root = insert(root, v)
    result = delete_bst_node(root, 3)
    assert inorder(result) == [2, 4, 5, 7, 8, 9]
