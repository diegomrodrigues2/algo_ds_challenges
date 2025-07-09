from __future__ import annotations
from typing import Optional


RED = "red"
BLACK = "black"


class RBNode:
    """Nó de uma árvore Rubro-Negra."""

    def __init__(self, value: int, color: str = RED,
                 left: Optional['RBNode'] | None = None,
                 right: Optional['RBNode'] | None = None,
                 parent: Optional['RBNode'] | None = None) -> None:
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


def insert(root: Optional[RBNode], value: int) -> RBNode:
    """Insere um valor em uma árvore Rubro-Negra.

    A função deve retornar a nova raiz da árvore após a inserção e
    rebalanceamento conforme as regras Rubro-Negras.

    Args:
        root: raiz atual da árvore ou ``None`` se vazia.
        value: valor a ser inserido.

    Returns:
        Nova raiz da árvore contendo ``value``.
    """
    raise NotImplementedError("Implementar esta função")
