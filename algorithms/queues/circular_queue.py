from __future__ import annotations


class CircularQueue:
    """Fila circular de capacidade fixa."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.data: list[int | None] = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, item: int) -> None:
        """Insere item se a fila não estiver cheia."""
        raise NotImplementedError("Implementar esta função")

    def dequeue(self) -> int:
        """Remove e retorna o item da frente se não estiver vazia."""
        raise NotImplementedError("Implementar esta função")

    def is_empty(self) -> bool:
        """Retorna ``True`` se a fila estiver vazia."""
        raise NotImplementedError("Implementar esta função")

    def is_full(self) -> bool:
        """Retorna ``True`` se a fila estiver cheia."""
        raise NotImplementedError("Implementar esta função")
