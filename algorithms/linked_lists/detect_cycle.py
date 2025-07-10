from __future__ import annotations
from typing import Optional


class ListNode:
    """Nó de uma lista ligada simples."""

    def __init__(self, value: int, next: Optional['ListNode'] | None = None) -> None:
        self.value = value
        self.next = next


def detect_cycle(head: Optional[ListNode]) -> bool:
    """Detecta se a lista ligada possui ciclo.

    Args:
        head: nó inicial da lista.

    Returns:
        ``True`` se houver ciclo; caso contrário ``False``.
    """
    # [1,2,3,4,1]
    if head is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

"""
Algoritmo de Floyd (Dois Ponteiros)

A abordagem clássica para detectar ciclos em linked lists é usar dois ponteiros com velocidades diferentes:

Ponteiro lento (slow): move 1 posição por vez
Ponteiro rápido (fast): move 2 posições por vez

Lógica:
* Se não há ciclo: o ponteiro rápido chegará ao final (None) primeiro
* Se há ciclo: o ponteiro rápido eventualmente "alcançará" o ponteiro lento dentro do ciclo
"""