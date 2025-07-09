from __future__ import annotations
from typing import Optional


class TreeNode:
    """N\u00f3 de uma \u00e1rvore bin\u00e1ria de busca (BST)."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def delete_bst_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """Remove o n\u00f3 com o valor ``key`` de uma BST.

    Args:
        root: raiz da BST.
        key: valor a ser removido.

    Returns:
        A raiz da BST ap\u00f3s a remo\u00e7\u00e3o do n\u00f3.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
