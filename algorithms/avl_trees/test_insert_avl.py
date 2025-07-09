from .insert_avl import TreeNode, insert_avl


def compute_height(node: TreeNode | None) -> int:
    if not node:
        return 0
    return 1 + max(compute_height(node.left), compute_height(node.right))


def is_avl(node: TreeNode | None) -> bool:
    if not node:
        return True
    left_h = compute_height(node.left)
    right_h = compute_height(node.right)
    if abs(left_h - right_h) > 1:
        return False
    if node.height != 1 + max(left_h, right_h):
        return False
    return is_avl(node.left) and is_avl(node.right)


def inorder(node: TreeNode | None) -> list[int]:
    return inorder(node.left) + [node.value] + inorder(node.right) if node else []


def build_avl(values: list[int]) -> TreeNode | None:
    root: TreeNode | None = None
    for v in values:
        root = insert_avl(root, v)
    return root


def test_insert_single():
    root = insert_avl(None, 10)
    assert root.value == 10
    assert root.left is None
    assert root.right is None
    assert root.height == 1


def test_insert_balancing():
    root = build_avl([10, 20, 30])
    assert inorder(root) == [10, 20, 30]
    assert is_avl(root)
    assert root.value == 20


def test_insert_multiple():
    values = list(range(1, 8))
    root = build_avl(values)
    assert inorder(root) == values
    assert is_avl(root)

