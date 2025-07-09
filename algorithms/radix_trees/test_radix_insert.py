from .radix_insert import RadixNode, radix_insert


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


def test_insert_single():
    root = radix_insert(None, "car")
    assert search(root, "car") is True
    assert search(root, "ca") is False


def test_insert_multiple_words():
    root = RadixNode()
    root = radix_insert(root, "car")
    root = radix_insert(root, "cat")
    assert search(root, "car") is True
    assert search(root, "cat") is True
    assert search(root, "cart") is False


def test_insert_prefix_split():
    root = RadixNode()
    root = radix_insert(root, "car")
    root = radix_insert(root, "cart")
    assert search(root, "car") is True
    assert search(root, "cart") is True
