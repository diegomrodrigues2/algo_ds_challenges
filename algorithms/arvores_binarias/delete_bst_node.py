from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária de busca (BST)."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def delete_bst_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """Remove o nó com o valor ``key`` de uma BST.

    Args:
        root: raiz da BST.
        key: valor a ser removido.

    Returns:
        A raiz da BST após a remoção do nó.
    """
    raise NotImplementedError("Implementar esta função")
