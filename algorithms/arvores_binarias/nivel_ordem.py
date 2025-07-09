from __future__ import annotations
from typing import Optional, List


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def nivel_ordem(root: Optional[TreeNode]) -> List[int]:
    """Percorre a árvore em ordem de nível (BFS).

    Args:
        root: raiz da árvore binária.

    Returns:
        Lista com os valores dos nós em ordem de nível.
    """
    raise NotImplementedError("Implementar esta função")
