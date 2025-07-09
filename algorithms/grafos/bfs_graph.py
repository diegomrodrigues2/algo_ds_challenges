from __future__ import annotations
from typing import Dict, List


def bfs_graph(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Realiza a busca em largura em um grafo a partir de ``start``.

    Args:
        graph: Grafo representado por um dicionário onde as chaves são vértices
            e os valores são listas de vízinhos.
        start: Vértice inicial da busca.

    Returns:
        Lista de vértices na ordem em que foram visitados.
    """
    raise NotImplementedError("Implementar esta função")
