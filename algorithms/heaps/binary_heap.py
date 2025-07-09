from __future__ import annotations


class BinaryHeap:
    """Min-heap bin\xc3\xa1rio simples."""

    def __init__(self) -> None:
        self._data: list[int] = []

    def insert(self, value: int) -> None:
        """Insere um valor na heap."""
        raise NotImplementedError("Implementar esta fun\xc3\xa7\xc3\xa3o")

    def extract_min(self) -> int:
        """Remove e retorna o menor valor da heap."""
        raise NotImplementedError("Implementar esta fun\xc3\xa7\xc3\xa3o")

    def peek(self) -> int:
        """Retorna o menor valor sem remov\xc3\xaa-lo."""
        raise NotImplementedError("Implementar esta fun\xc3\xa7\xc3\xa3o")

    def size(self) -> int:
        """Retorna o n\xc3\xbamero de elementos na heap."""
        raise NotImplementedError("Implementar esta fun\xc3\xa7\xc3\xa3o")
