from __future__ import annotations
from typing import Optional


class ListNode:
    """Nó de uma lista ligada simples."""

    def __init__(self, value: int, next: Optional['ListNode'] | None = None) -> None:
        self.value = value
        self.next = next


def merge_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Combina duas listas ligadas ordenadas em uma única lista ordenada.

    Args:
        l1: cabeça da primeira lista ordenada.
        l2: cabeça da segunda lista ordenada.

    Returns:
        Cabeça da lista resultante em ordem crescente.
    """
    raise NotImplementedError("Implementar esta função")
