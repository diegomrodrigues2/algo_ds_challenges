from __future__ import annotations


class Queue:
    """Fila simples implementada com lista."""

    def __init__(self) -> None:
        self.items: list[int] = []

    def enqueue(self, item: int) -> None:
        """Insere um item ao final da fila."""
        raise NotImplementedError("Implementar esta função")

    def dequeue(self) -> int:
        """Remove e retorna o primeiro item da fila."""
        raise NotImplementedError("Implementar esta função")

    def is_empty(self) -> bool:
        """Retorna ``True`` se a fila estiver vazia."""
        raise NotImplementedError("Implementar esta função")

    def size(self) -> int:
        """Retorna o número de itens na fila."""
        raise NotImplementedError("Implementar esta função")
