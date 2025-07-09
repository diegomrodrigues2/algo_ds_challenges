from .busca_profundidade import busca_profundidade


def test_dfs_basico():
    grafo = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    ordem = busca_profundidade(grafo, 0)
    assert ordem == [0, 1, 3, 2]


def test_dfs_vertice_isolado():
    grafo = {0: [], 1: [2], 2: [1]}
    assert busca_profundidade(grafo, 0) == [0]
    assert busca_profundidade(grafo, 1) == [1, 2]
