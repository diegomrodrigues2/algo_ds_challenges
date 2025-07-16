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
    if root is None:
        return None

    # Obter lista ordenada dos valores
    from .in_ordem import in_ordem
    values = in_ordem(root)
    
    # Função auxiliar para construir árvore balanceada
    def build_balanced_tree(arr, start, end):
        if start > end:
            return None
            
        # Usar o elemento do meio como raiz
        mid = (start + end) // 2
        node = TreeNode(arr[mid])
        
        # Construir recursivamente as subárvores
        node.left = build_balanced_tree(arr, start, mid - 1)
        node.right = build_balanced_tree(arr, mid + 1, end)
        
        return node
    
    # Construir árvore balanceada a partir dos valores ordenados
    return build_balanced_tree(values, 0, len(values) - 1)
