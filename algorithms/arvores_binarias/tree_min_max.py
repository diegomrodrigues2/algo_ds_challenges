from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def tree_min(root: Optional[TreeNode]) -> int:
    """Retorna o menor valor presente na árvore.
    
    Em uma BST, o menor valor está sempre no nó mais à esquerda
    da árvore. Esta função segue o caminho esquerdo até encontrar
    um nó sem filho esquerdo.

    Args:
        root: raiz da árvore binária.

    Returns:
        Menor valor encontrado.
        
    Raises:
        ValueError: Se a árvore estiver vazia.
        
    Exemplo:
        # Árvore:    8
        #           / \
        #          3   10
        #         / \    \
        #        1   6    14
        #           / \
        #          4   7
        
        tree_min(root)  # Retorna 1 (nó mais à esquerda)
    """
    raise NotImplementedError("Implementar esta função")


def tree_max(root: Optional[TreeNode]) -> int:
    """Retorna o maior valor presente na árvore.
    
    Em uma BST, o maior valor está sempre no nó mais à direita
    da árvore. Esta função segue o caminho direito até encontrar
    um nó sem filho direito.

    Args:
        root: raiz da árvore binária.

    Returns:
        Maior valor encontrado.
        
    Raises:
        ValueError: Se a árvore estiver vazia.
        
    Exemplo:
        # Árvore:    8
        #           / \
        #          3   10
        #         / \    \
        #        1   6    14
        #           / \
        #          4   7
        
        tree_max(root)  # Retorna 14 (nó mais à direita)
    """
    raise NotImplementedError("Implementar esta função")
