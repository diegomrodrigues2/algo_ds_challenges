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
    if l1 is None and l2 is not None:
        return l2
    
    if l2 is None and l1 is not None:
        return l1

    if l1 is None and l2 is None:
        return None

    if l1.value < l2.value:
        curr = ListNode(l1.value)
        ptr_l1 = l1.next
    else:
        curr = ListNode(l2.value)
        ptr_l2 = l2.next

    while ptr_l1 is not None and ptr_l2 is not None:
        if ptr_l1.value < ptr_l2.value:
            curr.next = ListNode(ptr_l1.value)
            ptr_l1 = ptr_l1.next
        else:
            curr.next = ListNode(ptr_l2.value)
            ptr_l2 = ptr_l2.next

    if ptr_l1 is None:
        while ptr_l2 is not None:
            curr.next = ListNode(ptr_l2.value)
            ptr_l2 = ptr_l2.next
    
    if ptr_l2 is None:
        while ptr_l1 is not None:
            curr.next = ListNode(ptr_l1.value)
            ptr_l1 = ptr_l1.next

    return curr