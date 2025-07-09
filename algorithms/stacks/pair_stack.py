from __future__ import annotations


class PairStack:
    """Pilha que armazena pares de inteiros."""

    def __init__(self) -> None:
        self._data: list[tuple[int, int]] = []

    def push(self, pair: tuple[int, int]) -> None:
        """Insere um par no topo da pilha."""
        raise NotImplementedError("Implementar esta função")

    def pop(self) -> tuple[int, int]:
        """Remove e retorna o par do topo."""
        raise NotImplementedError("Implementar esta função")

    def top(self) -> tuple[int, int]:
        """Retorna o par do topo sem removê-lo."""
        raise NotImplementedError("Implementar esta função")

    def is_empty(self) -> bool:
        """Retorna ``True`` se a pilha estiver vazia."""
        raise NotImplementedError("Implementar esta função")
