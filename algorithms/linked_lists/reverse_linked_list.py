from __future__ import annotations
from typing import Optional


class ListNode:
    """N\xc3\xb3 de uma lista ligada simples."""

    def __init__(self, value: int, next: Optional['ListNode'] | None = None) -> None:
        self.value = value
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverte uma lista ligada simples.

    Args:
        head: primeiro n\xc3\xb3 da lista.

    Returns:
        O novo n\xc3\xb3 inicial ap\xc3\xb3s a revers\xc3\xa3o.
    """
    raise NotImplementedError("Implementar esta fun\xc3\xa7\xc3\xa3o")
