from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def tree_min(root: Optional[TreeNode]) -> int:
    """Retorna o menor valor presente na árvore.

    Args:
        root: raiz da árvore binária.

    Returns:
        Menor valor encontrado.
    """
    raise NotImplementedError("Implementar esta função")


def tree_max(root: Optional[TreeNode]) -> int:
    """Retorna o maior valor presente na árvore.

    Args:
        root: raiz da árvore binária.

    Returns:
        Maior valor encontrado.
    """
    raise NotImplementedError("Implementar esta função")
