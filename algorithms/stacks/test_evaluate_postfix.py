from .evaluate_postfix import evaluate_postfix


def test_simple_addition():
    assert evaluate_postfix("2 3 +") == 5


def test_complex_expression():
    expr = "5 1 2 + 4 * + 3 -"
    assert evaluate_postfix(expr) == 14


def test_mixed_operations():
    assert evaluate_postfix("2 1 + 3 *") == 9
    assert evaluate_postfix("4 13 5 / +") == 6
