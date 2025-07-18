from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária de busca (BST)."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def find_min(node: TreeNode) -> TreeNode:
    """Encontra o nó com valor mínimo em uma subárvore."""
    while node.left is not None:
        node = node.left
    return node


def delete_bst_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """Remove o nó com o valor ``key`` de uma BST.

    Args:
        root: raiz da BST.
        key: valor a ser removido.

    Returns:
        A raiz da BST após a remoção do nó.
    """
    # Caso base: árvore vazia
    if root is None:
        return root
    
    # Se a chave é menor que a raiz, está na subárvore esquerda
    if key < root.value:
        root.left = delete_bst_node(root.left, key)
    
    # Se a chave é maior que a raiz, está na subárvore direita
    elif key > root.value:
        root.right = delete_bst_node(root.right, key)
    
    # Se a chave é igual à raiz, este é o nó a ser deletado
    else:
        # Caso 1: Nó sem filhos (folha)
        if root.left is None and root.right is None:
            return None
        
        # Caso 2: Nó com apenas um filho
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Caso 3: Nó com dois filhos
        else:
            # Encontra o sucessor inorder (menor valor na subárvore direita)
            successor = find_min(root.right)
            
            # Substitui o valor do nó atual pelo valor do sucessor
            root.value = successor.value
            
            # Remove o sucessor da subárvore direita
            root.right = delete_bst_node(root.right, successor.value)
    
    return root
