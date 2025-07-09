from __future__ import annotations
from typing import Dict, List


def topological_sort(graph: Dict[str, List[str]]) -> List[str]:
    """Realiza ordenação topológica em um grafo acíclico.

    O grafo é representado por um dicionário onde cada chave é um
    vértice e o valor é a lista de vértices adjacentes.

    Args:
        graph: dicionário de adjacência do grafo direcionado.

    Returns:
        Lista de vértices em ordem topológica.
    """
    raise NotImplementedError("Implementar esta função")
