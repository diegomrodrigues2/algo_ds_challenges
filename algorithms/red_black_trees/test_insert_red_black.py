from .insert_red_black import RBNode, insert, RED, BLACK


def inorder(node: RBNode | None) -> list[int]:
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def _check(node: RBNode | None) -> int:
    if node is None:
        return 1
    left = _check(node.left)
    right = _check(node.right)
    assert left == right, "black height mismatch"
    if node.color == RED:
        if (node.left and node.left.color == RED) or (
            node.right and node.right.color == RED
        ):
            raise AssertionError("consecutive red nodes")
    return left + (1 if node.color == BLACK else 0)


def is_rb_tree(root: RBNode | None) -> bool:
    if root is None:
        return True
    if root.color != BLACK:
        return False
    try:
        _check(root)
        return True
    except AssertionError:
        return False


def test_insert_root_black():
    root = None
    root = insert(root, 10)
    assert root.value == 10
    assert root.color == BLACK
    assert inorder(root) == [10]
    assert is_rb_tree(root)


def test_insert_multiple_values():
    root = None
    values = [10, 5, 20, 15, 25]
    for v in values:
        root = insert(root, v)
        assert is_rb_tree(root)
    assert inorder(root) == sorted(values)
