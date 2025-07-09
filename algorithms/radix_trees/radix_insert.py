from __future__ import annotations
from typing import Optional, Dict


class RadixNode:
    """N\u00f3 de uma Radix Tree."""

    def __init__(self) -> None:
        self.children: Dict[str, RadixNode] = {}
        self.is_word: bool = False


def radix_insert(root: Optional[RadixNode], word: str) -> RadixNode:
    """Insere uma palavra na Radix Tree.

    Args:
        root: n\u00f3 inicial ou ``None`` para \u00e1rvore vazia.
        word: palavra a ser inserida.

    Returns:
        A raiz da \u00e1rvore ap\u00f3s a inser\u00e7\u00e3o.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
