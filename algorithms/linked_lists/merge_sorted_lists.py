from __future__ import annotations
from typing import Optional


class ListNode:
    """N\xc3\xb3 de uma lista ligada simples."""

    def __init__(self, value: int, next: Optional['ListNode'] | None = None) -> None:
        self.value = value
        self.next = next


def merge_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Combina duas listas ligadas ordenadas em uma \xc3\xba nica lista ordenada.

    Args:
        l1: cabe\xc3\xa7a da primeira lista ordenada.
        l2: cabe\xc3\xa7a da segunda lista ordenada.

    Returns:
        Cabe\xc3\xa7a da lista resultante em ordem crescente.
    """
    raise NotImplementedError("Implementar esta fun\xc3\xa7\xc3\xa3o")
