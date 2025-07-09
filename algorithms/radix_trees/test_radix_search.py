from .radix_search import RadixNode, radix_search


def build_tree() -> RadixNode:
    root = RadixNode()
    c_node = RadixNode()
    root.children["c"] = c_node
    car_node = RadixNode()
    c_node.children["ar"] = car_node
    car_node.is_word = True
    cart_node = RadixNode()
    c_node.children["art"] = cart_node
    cart_node.is_word = True
    return root


def test_search_found():
    root = build_tree()
    assert radix_search(root, "car") is True
    assert radix_search(root, "cart") is True


def test_search_missing():
    root = build_tree()
    assert radix_search(root, "cat") is False


def test_search_empty_tree():
    assert radix_search(None, "car") is False
