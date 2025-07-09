from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def count_nodes(root: Optional[TreeNode]) -> int:
    """Conta o número de nós da árvore.

    Args:
        root: raiz da árvore binária.

    Returns:
        Quantidade de nós na árvore.
    """
    raise NotImplementedError("Implementar esta função")
