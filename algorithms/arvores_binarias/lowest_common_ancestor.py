from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Encontra o menor ancestral comum de dois nós.

    Args:
        root: raiz da árvore binária.
        p: primeiro nó.
        q: segundo nó.

    Returns:
        O nó que representa o menor ancestral comum de ``p`` e ``q`` ou ``None`` se algum dos nós não estiver presente.
    """
    raise NotImplementedError("Implementar esta função")
