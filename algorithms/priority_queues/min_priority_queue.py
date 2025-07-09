from __future__ import annotations


class MinPriorityQueue:
    """Fila de prioridade mínima implementada com heap binário."""

    def __init__(self) -> None:
        self._data: list[int] = []

    def insert(self, item: int) -> None:
        """Insere ``item`` na fila."""
        raise NotImplementedError("Implementar esta função")

    def extract_min(self) -> int:
        """Remove e retorna o menor elemento."""
        raise NotImplementedError("Implementar esta função")

    def peek_min(self) -> int:
        """Retorna o menor elemento sem removê-lo."""
        raise NotImplementedError("Implementar esta função")

    def is_empty(self) -> bool:
        """Retorna ``True`` se a fila estiver vazia."""
        raise NotImplementedError("Implementar esta função")

    def size(self) -> int:
        """Retorna o número de elementos na fila."""
        raise NotImplementedError("Implementar esta função")
