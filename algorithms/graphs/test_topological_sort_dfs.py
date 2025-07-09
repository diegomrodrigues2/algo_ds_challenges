from .topological_sort_dfs import topological_sort


def test_empty_graph():
    assert topological_sort({}) == []


def test_single_vertex():
    graph = {"A": []}
    assert topological_sort(graph) == ["A"]


def test_linear_graph():
    graph = {"A": ["B"], "B": ["C"], "C": ["D"], "D": []}
    assert topological_sort(graph) == ["A", "B", "C", "D"]


def test_unique_order_graph():
    graph = {"B": ["A", "C"], "A": ["C"], "C": ["D"], "D": []}
    assert topological_sort(graph) == ["B", "A", "C", "D"]
