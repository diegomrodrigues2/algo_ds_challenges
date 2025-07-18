from __future__ import annotations
from typing import List


class Grafo:
    """Grafo não direcionado usando lista de adjacência."""

    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.adj: list[list[int]] = [[] for _ in range(num_vertices)]

    def adiciona_aresta(self, u: int, v: int) -> None:
        """Adiciona uma aresta entre ``u`` e ``v``."""
        raise NotImplementedError("Implementar esta função")

    def vizinhos(self, u: int) -> List[int]:
        """Retorna a lista de vértices adjacentes a ``u``."""
        raise NotImplementedError("Implementar esta função") 