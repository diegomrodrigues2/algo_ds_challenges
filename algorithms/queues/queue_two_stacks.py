from __future__ import annotations


class QueueTwoStacks:
    """Fila usando duas pilhas."""

    def __init__(self) -> None:
        self._in: list[int] = []
        self._out: list[int] = []

    def enqueue(self, item: int) -> None:
        """Insere item na fila."""
        raise NotImplementedError("Implementar esta função")

    def dequeue(self) -> int:
        """Remove e retorna o primeiro item da fila."""
        raise NotImplementedError("Implementar esta função")
