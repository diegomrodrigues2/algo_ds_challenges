from __future__ import annotations
from typing import Optional, Dict


class RadixNode:
    """Nó de uma Radix Tree."""

    def __init__(self) -> None:
        self.children: Dict[str, RadixNode] = {}
        self.is_word: bool = False


def radix_insert(root: Optional[RadixNode], word: str) -> RadixNode:
    """Insere uma palavra na Radix Tree.

    Args:
        root: nó inicial ou ``None`` para árvore vazia.
        word: palavra a ser inserida.

    Returns:
        A raiz da árvore após a inserção.
    """
    raise NotImplementedError("Implementar esta função")
