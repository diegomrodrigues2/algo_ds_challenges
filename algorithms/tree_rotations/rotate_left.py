from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def rotate_left(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Realiza uma rotação à esquerda em torno do ``root``.
    
    Esta é uma **operação atômica fundamental** que permite reestruturar
    uma árvore binária preservando a propriedade BST. A rotação à esquerda
    reduz a altura da subárvore direita.
    
    A operação assume que ``root`` possui filho à direita. Após a
    rotação, o filho direito torna-se a nova raiz e ``root`` passa a ser
    filho esquerdo desse novo nó.

    Args:
        root: nó que será rotacionado.

    Returns:
        Novo nó raiz após a rotação ou ``None`` se ``root`` for ``None``.
        
    Exemplo:
        # Antes:     Y           Depois:    X
        #           / \                    / \
        #          X   C                  A   Y
        #         / \                        / \
        #        A   B                      B   C
        
        # A propriedade BST é preservada:
        # Antes: A < X < B < Y < C
        # Depois: A < X < B < Y < C
    """
    raise NotImplementedError("Implementar esta função")
