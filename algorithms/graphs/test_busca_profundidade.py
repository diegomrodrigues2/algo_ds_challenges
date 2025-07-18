from .busca_profundidade import busca_profundidade


def test_grafo_simples():
    adj = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    resultado = busca_profundidade(adj, 0)
    assert resultado[0] == 0
    assert len(resultado) == 4
    assert all(v in resultado for v in [0, 1, 2, 3])


def test_grafo_linear():
    adj = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
    resultado = busca_profundidade(adj, 0)
    assert resultado[0] == 0
    assert resultado[1] == 1
    assert resultado[2] == 2
    assert resultado[3] == 3


def test_grafo_isolado():
    adj = {0: [], 1: [2], 2: [1]}
    resultado = busca_profundidade(adj, 0)
    assert resultado == [0] 