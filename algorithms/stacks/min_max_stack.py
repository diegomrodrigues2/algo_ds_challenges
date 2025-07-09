from __future__ import annotations


class MinMaxStack:
    """Pilha que retorna o valor mínimo e máximo em O(1)."""

    def __init__(self) -> None:
        self._stack: list[int] = []
        self._mins: list[int] = []
        self._maxs: list[int] = []

    def push(self, value: int) -> None:
        """Insere um valor no topo da pilha."""
        raise NotImplementedError("Implementar esta função")

    def pop(self) -> int:
        """Remove e retorna o topo da pilha."""
        raise NotImplementedError("Implementar esta função")

    def top(self) -> int:
        """Retorna o valor do topo sem removê-lo."""
        raise NotImplementedError("Implementar esta função")

    def get_min(self) -> int:
        """Retorna o menor valor presente na pilha."""
        raise NotImplementedError("Implementar esta função")

    def get_max(self) -> int:
        """Retorna o maior valor presente na pilha."""
        raise NotImplementedError("Implementar esta função")
