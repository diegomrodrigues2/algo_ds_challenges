from .validate_parentheses import is_valid_parentheses


def test_empty_string():
    assert is_valid_parentheses("") is True


def test_simple_valid():
    assert is_valid_parentheses("()") is True


def test_complex_valid():
    assert is_valid_parentheses("([]{})") is True


def test_mismatch():
    assert is_valid_parentheses("(]") is False


def test_wrong_order():
    assert is_valid_parentheses("([)]") is False
