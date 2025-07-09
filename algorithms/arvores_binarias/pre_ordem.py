from __future__ import annotations
from typing import Optional, List


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def pre_ordem(root: Optional[TreeNode]) -> List[int]:
    """Percorre a árvore em pré-ordem (DFS pre-order).

    Args:
        root: raiz da árvore binária.

    Returns:
        Lista com os valores visitados no percurso pre-order.
    """
    raise NotImplementedError("Implementar esta função")
