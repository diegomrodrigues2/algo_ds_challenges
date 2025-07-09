from __future__ import annotations
from typing import Optional


class ListNode:
    """Nó de uma lista ligada simples."""

    def __init__(self, value: int, next: Optional['ListNode'] | None = None) -> None:
        self.value = value
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverte uma lista ligada simples.

    Args:
        head: primeiro nó da lista.

    Returns:
        O novo nó inicial após a reversão.
    """
    tail = None
    curr = head

    while curr is not None:
        tail = ListNode(curr.value, next=tail)
        curr = curr.next

    return tail
