from __future__ import annotations
from typing import Optional


class ListNode:
    """N\xc3\xb3 de uma lista ligada simples."""

    def __init__(self, value: int, next: Optional['ListNode'] | None = None) -> None:
        self.value = value
        self.next = next


def detect_cycle(head: Optional[ListNode]) -> bool:
    """Detecta se a lista ligada possui ciclo.

    Args:
        head: n\xc3\xb3 inicial da lista.

    Returns:
        ``True`` se houver ciclo; caso contr\xc3\xa1rio ``False``.
    """
    raise NotImplementedError("Implementar esta fun\xc3\xa7\xc3\xa3o")
