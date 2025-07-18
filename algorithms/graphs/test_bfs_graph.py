from .bfs_graph import bfs_graph


def test_grafo_simples():
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    resultado = bfs_graph(graph, 0)
    assert resultado[0] == 0
    assert 1 in resultado[1:3]
    assert 2 in resultado[1:3]


def test_grafo_linear():
    graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
    resultado = bfs_graph(graph, 0)
    assert resultado == [0, 1, 2, 3]


def test_grafo_isolado():
    graph = {0: [], 1: [2], 2: [1]}
    resultado = bfs_graph(graph, 0)
    assert resultado == [0] 