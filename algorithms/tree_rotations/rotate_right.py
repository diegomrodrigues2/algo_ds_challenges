from __future__ import annotations
from typing import Optional


class TreeNode:
    """Nó de uma árvore binária."""

    def __init__(self, value: int, left: Optional['TreeNode'] | None = None, right: Optional['TreeNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def rotate_right(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Realiza uma rotação à direita em torno do ``root``.

    A operação assume que ``root`` possui filho à esquerda. Após a
    rotação, o filho esquerdo torna-se a nova raiz e ``root`` passa a ser
    filho direito desse novo nó.

    Args:
        root: nó que será rotacionado.

    Returns:
        Novo nó raiz após a rotação ou ``None`` se ``root`` for ``None``.
    """
    raise NotImplementedError("Implementar esta função")
