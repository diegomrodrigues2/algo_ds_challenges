from __future__ import annotations
from typing import Optional, List


class TreeNode:
    """N\u00f3 de uma \u00e1rvore bin\u00e1ria de busca (BST)."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def balance_bst(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Balanceia uma BST desbalanceada.

    A fun\u00e7\u00e3o deve receber a raiz de uma BST possivelmente desbalanceada
    e retornar uma nova \u00e1rvore contendo os mesmos elementos, por\u00e9m com
    altura m\u00e1xima minimizada.

    Args:
        root: raiz da BST original.

    Returns:
        Raiz da nova BST balanceada ou ``None`` se a \u00e1rvore for vazia.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
