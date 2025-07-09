from .bfs_shortest_path import bfs_shortest_path


def test_start_equals_goal():
    graph = {1: [2], 2: []}
    assert bfs_shortest_path(graph, 1, 1) == [1]


def test_simple_path():
    graph = {1: [2], 2: [3], 3: []}
    assert bfs_shortest_path(graph, 1, 3) == [1, 2, 3]


def test_multiple_paths():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    result = bfs_shortest_path(graph, 1, 4)
    assert result in ([1, 2, 4], [1, 3, 4])
    assert len(result) == 3


def test_no_path():
    graph = {1: [2], 2: [], 3: []}
    assert bfs_shortest_path(graph, 1, 3) == []
