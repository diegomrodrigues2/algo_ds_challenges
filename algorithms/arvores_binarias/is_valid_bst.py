from __future__ import annotations
from typing import Optional


class TreeNode:
    """N\u00f3 de uma \u00e1rvore bin\u00e1ria."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Verifica se a \u00e1rvore \u00e9 uma BST v\u00e1lida.

    Args:
        root: raiz da \u00e1rvore.

    Returns:
        ``True`` se a \u00e1rvore obedecer as propriedades de uma BST, caso contr\u00e1rio ``False``.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
