from __future__ import annotations
from typing import Optional, List


class GeneralNode:
    """Nó de uma árvore geral (n-ária)."""

    def __init__(self, value: int, children: Optional[List['GeneralNode']] | None = None) -> None:
        self.value = value
        self.children = children if children is not None else []


class BinaryNode:
    """Nó de uma árvore binária usando representação filho à esquerda/irmão à direita."""

    def __init__(self, value: int, left: Optional['BinaryNode'] | None = None, right: Optional['BinaryNode'] | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def convert_to_binary(root: Optional[GeneralNode]) -> Optional[BinaryNode]:
    """Converte uma árvore geral em sua representação binária.

    A conversão deve utilizar o método filho à esquerda/irmão à direita, onde
    o primeiro filho torna-se o ponteiro ``left`` e os irmãos subsequentes são
    encadeados através do ponteiro ``right``.

    Args:
        root: raiz da árvore geral.

    Returns:
        Raiz da árvore binária convertida ou ``None`` se a entrada for ``None``.
    """
    raise NotImplementedError("Implementar esta função")
