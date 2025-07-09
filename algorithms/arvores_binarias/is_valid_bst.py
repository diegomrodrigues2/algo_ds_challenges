from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Verifica se a árvore é uma BST válida.

    Args:
        root: raiz da árvore.

    Returns:
        ``True`` se a árvore obedecer as propriedades de uma BST, caso contrário ``False``.
    """
    raise NotImplementedError("Implementar esta função")
