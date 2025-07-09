from .radix_delete import RadixNode, radix_delete


def search(root: RadixNode | None, word: str) -> bool:
    node = root
    while node and word:
        for prefix, child in node.children.items():
            if word.startswith(prefix):
                word = word[len(prefix):]
                node = child
                break
        else:
            return False
    return node is not None and word == "" and node.is_word


def build_tree() -> RadixNode:
    root = RadixNode()
    root.children["car"] = RadixNode()
    root.children["car"].is_word = True
    root.children["cart"] = RadixNode()
    root.children["cart"].is_word = True
    return root


def test_delete_only_word():
    root = RadixNode()
    root.children["dog"] = RadixNode()
    root.children["dog"].is_word = True
    root = radix_delete(root, "dog")
    assert root is None or root.children == {}


def test_delete_prefix_word():
    root = build_tree()
    radix_delete(root, "car")
    assert search(root, "car") is False
    assert search(root, "cart") is True


def test_delete_nonexistent():
    root = build_tree()
    radix_delete(root, "cat")
    assert search(root, "car") is True
    assert search(root, "cart") is True
