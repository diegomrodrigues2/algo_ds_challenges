from __future__ import annotations
from typing import Optional, List


class TreeNode:
    """N\u00f3 de uma \u00e1rvore bin\u00e1ria."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def nivel_ordem(root: Optional[TreeNode]) -> List[int]:
    """Percorre a \u00e1rvore em ordem de n\u00edvel (BFS).

    Args:
        root: raiz da \u00e1rvore bin\u00e1ria.

    Returns:
        Lista com os valores dos n\u00f3s em ordem de n\u00edvel.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
