from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def tree_height(root: Optional[TreeNode]) -> int:
    """Calcula a altura da árvore.

    Args:
        root: raiz da árvore binária.

    Returns:
        Altura da árvore, onde uma árvore vazia tem altura 0.
    """
    raise NotImplementedError("Implementar esta função")
