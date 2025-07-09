from __future__ import annotations
from typing import Optional, List


class TreeNode:
    """Nó de uma árvore binária de busca (BST)."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def balance_bst(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Balanceia uma BST desbalanceada.

    A função deve receber a raiz de uma BST possivelmente desbalanceada
    e retornar uma nova árvore contendo os mesmos elementos, porém com
    altura máxima minimizada.

    Args:
        root: raiz da BST original.

    Returns:
        Raiz da nova BST balanceada ou ``None`` se a árvore for vazia.
    """
    raise NotImplementedError("Implementar esta função")
