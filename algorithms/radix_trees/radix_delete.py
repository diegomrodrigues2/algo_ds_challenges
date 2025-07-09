from __future__ import annotations
from typing import Optional, Dict


class RadixNode:
    """Nó de uma Radix Tree."""

    def __init__(self) -> None:
        self.children: Dict[str, RadixNode] = {}
        self.is_word: bool = False


def radix_delete(root: Optional[RadixNode], word: str) -> Optional[RadixNode]:
    """Remove uma palavra da Radix Tree.

    Args:
        root: nó inicial da árvore.
        word: palavra a ser removida.

    Returns:
        A raiz da árvore após a remoção (pode mudar se a árvore ficar vazia).
    """
    raise NotImplementedError("Implementar esta função")
