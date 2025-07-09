from __future__ import annotations
from typing import Dict, List


def topological_sort(graph: Dict[str, List[str]]) -> List[str]:
    """Realiza ordena\u00e7\u00e3o topol\u00f3gica em um grafo ac\u00edclico.

    O grafo \u00e9 representado por um dicion\u00e1rio onde cada chave \u00e9 um
    v\u00e9rtice e o valor \u00e9 a lista de v\u00e9rtices adjacentes.

    Args:
        graph: dicion\u00e1rio de adjac\u00eancia do grafo direcionado.

    Returns:
        Lista de v\u00e9rtices em ordem topol\u00f3gica.
    """
    raise NotImplementedError("Implementar esta fun\u00e7\u00e3o")
