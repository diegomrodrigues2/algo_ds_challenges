from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária de busca (BST)."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def search_bst(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """Busca um valor na BST e retorna o nó correspondente.

    Args:
        root: raiz da BST.
        target: valor a ser buscado.

    Returns:
        O nó contendo ``target`` ou ``None`` se não encontrado.
    """
    raise NotImplementedError("Implementar esta função")
