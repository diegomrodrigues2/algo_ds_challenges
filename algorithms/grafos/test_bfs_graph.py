from .bfs_graph import bfs_graph


def test_empty_graph():
    assert bfs_graph({}, 1) == []


def test_simple_graph():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    assert bfs_graph(graph, 1) == [1, 2, 3, 4]


def test_graph_with_cycle():
    graph = {1: [2], 2: [3], 3: [1]}
    assert bfs_graph(graph, 1) == [1, 2, 3]
