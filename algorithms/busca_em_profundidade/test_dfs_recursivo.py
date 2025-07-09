from .dfs_recursivo import dfs_recursivo


def test_dfs_basico():
    grafo = {1: [2, 3], 2: [4], 3: [4], 4: []}
    assert dfs_recursivo(grafo, 1) == [1, 2, 4, 3]


def test_dfs_com_vertice_sem_arestas():
    grafo = {1: [], 2: [1]}
    assert dfs_recursivo(grafo, 2) == [2, 1]


def test_dfs_grafo_desconexo():
    grafo = {1: [2], 2: [], 3: []}
    assert dfs_recursivo(grafo, 3) == [3]
