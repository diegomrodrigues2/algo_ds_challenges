from __future__ import annotations
from typing import Optional, List


class GeneralNode:
    """Nó de uma árvore geral (n-ária)."""

    def __init__(self, value: int, children: Optional[List['GeneralNode']] | None = None) -> None:
        self.value = value
        self.children = children if children is not None else []


class BinaryNode:
    """Nó de uma árvore binária em representação filho à esquerda/irmão à direita."""

    def __init__(self, value: int, left: Optional['BinaryNode'] | None = None, right: Optional['BinaryNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def binary_to_general(root: Optional[BinaryNode]) -> Optional[GeneralNode]:
    """Converte uma árvore binária na forma filho à esquerda/irmão à direita em uma árvore geral.

    Args:
        root: raiz da árvore binária.

    Returns:
        Raiz da árvore geral resultante ou ``None`` se a entrada for ``None``.
    """
    raise NotImplementedError("Implementar esta função")
