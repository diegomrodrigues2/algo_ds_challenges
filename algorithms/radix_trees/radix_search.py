from __future__ import annotations
from typing import Optional, Dict


class RadixNode:
    """Nó de uma Radix Tree."""

    def __init__(self) -> None:
        self.children: Dict[str, RadixNode] = {}
        self.is_word: bool = False


def radix_search(root: Optional[RadixNode], word: str) -> bool:
    """Procura uma palavra na Radix Tree.

    Args:
        root: nó inicial da árvore.
        word: palavra a ser buscada.

    Returns:
        ``True`` se a palavra existir na árvore, caso contrário ``False``.
    """
    raise NotImplementedError("Implementar esta função")
