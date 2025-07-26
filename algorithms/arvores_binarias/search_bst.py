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
    
    Esta função aproveita a propriedade fundamental da BST:
    - Todos os valores na subárvore esquerda são MENORES que a raiz
    - Todos os valores na subárvore direita são MAIORES que a raiz
    
    Isso permite eliminar metade da árvore a cada comparação,
    resultando em complexidade O(log n) no caso médio.

    Args:
        root: raiz da BST.
        target: valor a ser buscado.

    Returns:
        O nó contendo ``target`` ou ``None`` se não encontrado.
        
    Exemplo:
        # Árvore:    8
        #           / \
        #          3   10
        #         / \    \
        #        1   6    14
        #           / \
        #          4   7
        
        search_bst(root, 6)  # Retorna nó com valor 6
        search_bst(root, 5)  # Retorna None (não encontrado)
    """
    raise NotImplementedError("Implementar esta função")
