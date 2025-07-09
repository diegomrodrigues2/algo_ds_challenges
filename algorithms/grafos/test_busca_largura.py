from .busca_largura import busca_largura


def test_bfs_basico():
    grafo = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    ordem = busca_largura(grafo, 0)
    assert ordem == [0, 1, 2, 3]


def test_bfs_vertice_isolado():
    grafo = {0: [], 1: [2], 2: [1]}
    assert busca_largura(grafo, 0) == [0]
    assert busca_largura(grafo, 1) == [1, 2]
