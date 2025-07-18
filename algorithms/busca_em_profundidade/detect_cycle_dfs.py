from __future__ import annotations


def has_cycle(grafo: dict[int, list[int]]) -> bool:
    """Detecta se há ciclo em um grafo direcionado usando DFS.

    Args:
        grafo: Grafo em lista de adjacência.

    Returns:
        ``True`` se o grafo contém ciclo, caso contrário ``False``.
    """
    status = {v: 'não visitado' for v in grafo.keys()}

    def detect_cycle(v):
        status[v] = 'em processamento'

        for u in grafo[v]:
            if status[u] == 'em processamento':
                return True

            if status[u] == 'não visitado':
                if detect_cycle(u):
                    return True
            
        status[v] = 'processado'
        
        return False

    for v in grafo.keys():
        if status[v] == 'não visitado':
            if detect_cycle(v):
                return True
    
    return False
