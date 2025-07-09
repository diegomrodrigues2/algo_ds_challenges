from __future__ import annotations
from typing import Optional, Dict


class RadixNode:
    """N\u00f3 de uma Radix Tree."""

    def __init__(self) -> None:
        self.children: Dict[str, RadixNode] = {}
        self.is_word: bool = False


def radix_search(root: Optional[RadixNode], word: str) -> bool:
    """Procura uma palavra na Radix Tree.

    Args:
        root: n\u00f3 inicial da \u00e1rvore.
        word: palavra a ser buscada.

    Returns:
        ``True`` se a palavra existir na \u00e1rvore, caso contr\u00e1rio ``False``.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
