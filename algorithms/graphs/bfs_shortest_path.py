from __future__ import annotations
from collections import deque
from typing import Dict, List, Hashable


def bfs_shortest_path(graph: Dict[Hashable, List[Hashable]], start: Hashable, goal: Hashable) -> List[Hashable]:
    """Encontra o caminho mais curto entre ``start`` e ``goal`` em um grafo não ponderado.

    O grafo é representado por um dicionário onde cada chave é um vértice e o
    valor correspondente é uma lista de vizinhos.

    Args:
        graph: grafo no formato ``{vertice: [vizinhos]}``.
        start: vértice de origem.
        goal: vértice de destino.

    Returns:
        Lista com os vértices do caminho mais curto, incluindo ``start`` e
        ``goal``. Se não houver caminho possível, retorna uma lista vazia.
    """
    raise NotImplementedError("Implementar esta função")
