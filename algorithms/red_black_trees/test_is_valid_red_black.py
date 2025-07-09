from .is_valid_red_black import RBNode, is_valid_red_black, RED, BLACK


def test_empty_tree_valid():
    assert is_valid_red_black(None) is True


def test_single_node_black():
    root = RBNode(10, BLACK)
    assert is_valid_red_black(root) is True


def test_root_must_be_black():
    root = RBNode(10, RED)
    assert is_valid_red_black(root) is False


def test_no_consecutive_red_nodes():
    root = RBNode(10, BLACK, left=RBNode(5, RED, left=RBNode(2, RED)))
    assert is_valid_red_black(root) is False


def test_black_height_mismatch():
    root = RBNode(
        10,
        BLACK,
        left=RBNode(5, BLACK, left=RBNode(2, BLACK)),
        right=RBNode(15, BLACK),
    )
    assert is_valid_red_black(root) is False
