from .detect_cycle_dfs import has_cycle


def test_sem_ciclo():
    grafo = {1: [2], 2: [3], 3: []}
    assert has_cycle(grafo) is False


def test_com_ciclo_simples():
    grafo = {1: [2], 2: [3], 3: [1]}
    assert has_cycle(grafo) is True


def test_ciclo_em_componente():
    grafo = {1: [2], 2: [], 3: [4], 4: [3]}
    assert has_cycle(grafo) is True


def test_grafo_vazio():
    assert has_cycle({}) is False
