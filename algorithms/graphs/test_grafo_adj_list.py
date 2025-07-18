from .grafo_adj_list import Grafo


def test_adiciona_e_vizinhos():
    g = Grafo(3)
    g.adiciona_aresta(0, 1)
    g.adiciona_aresta(1, 2)
    assert sorted(g.vizinhos(1)) == [0, 2]
    assert g.vizinhos(0) == [1]
    g.adiciona_aresta(0, 2)
    assert sorted(g.vizinhos(0)) == [1, 2] 