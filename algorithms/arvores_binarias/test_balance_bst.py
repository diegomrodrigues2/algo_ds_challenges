from .balance_bst import TreeNode, balance_bst


def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(node):
    result = []
    stack = []
    current = node
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def build_skewed(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


def test_empty_tree():
    assert balance_bst(None) is None


def test_single_node():
    node = TreeNode(1)
    result = balance_bst(node)
    assert result.value == 1
    assert result.left is None
    assert result.right is None


def test_balance_height_and_order():
    values = list(range(1, 8))
    root = build_skewed(values)
    balanced = balance_bst(root)
    assert inorder(balanced) == values
    assert height(balanced) <= 3
