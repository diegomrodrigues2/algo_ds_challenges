from __future__ import annotations
from typing import Optional, Dict


class RadixNode:
    """N\u00f3 de uma Radix Tree."""

    def __init__(self) -> None:
        self.children: Dict[str, RadixNode] = {}
        self.is_word: bool = False


def radix_delete(root: Optional[RadixNode], word: str) -> Optional[RadixNode]:
    """Remove uma palavra da Radix Tree.

    Args:
        root: n\u00f3 inicial da \u00e1rvore.
        word: palavra a ser removida.

    Returns:
        A raiz da \u00e1rvore ap\u00f3s a remo\u00e7\u00e3o (pode mudar se a \u00e1rvore ficar vazia).
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
