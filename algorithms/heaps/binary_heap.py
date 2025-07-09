from __future__ import annotations


class BinaryHeap:
    """Min-heap binário simples."""

    def __init__(self) -> None:
        self._data: list[int] = []

    def insert(self, value: int) -> None:
        """Insere um valor na heap."""
        raise NotImplementedError("Implementar esta função")

    def extract_min(self) -> int:
        """Remove e retorna o menor valor da heap."""
        raise NotImplementedError("Implementar esta função")

    def peek(self) -> int:
        """Retorna o menor valor sem removê-lo."""
        raise NotImplementedError("Implementar esta função")

    def size(self) -> int:
        """Retorna o número de elementos na heap."""
        raise NotImplementedError("Implementar esta função")
