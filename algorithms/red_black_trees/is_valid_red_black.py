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


def is_valid_red_black(root: Optional[RBNode]) -> bool:
    """Verifica se a árvore satisfaz as propriedades Rubro-Negras.

    Args:
        root: raiz da árvore.

    Returns:
        ``True`` se a árvore for válida; caso contrário ``False``.
    """
    raise NotImplementedError("Implementar esta função")
