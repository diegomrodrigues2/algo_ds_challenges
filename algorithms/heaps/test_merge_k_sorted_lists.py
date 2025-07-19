import pytest
from .merge_k_sorted_lists import merge_k_sorted_lists


class TestMergeKSortedLists:
    """Testes para a função merge_k_sorted_lists."""
    
    def test_empty_lists(self):
        """Testa com lista vazia de listas."""
        assert merge_k_sorted_lists([]) == []
    
    def test_single_empty_list(self):
        """Testa com uma única lista vazia."""
        assert merge_k_sorted_lists([[]]) == []
    
    def test_multiple_empty_lists(self):
        """Testa com múltiplas listas vazias."""
        assert merge_k_sorted_lists([[], [], []]) == []
    
    def test_single_list(self):
        """Testa com uma única lista."""
        assert merge_k_sorted_lists([[1, 2, 3]]) == [1, 2, 3]
    
    def test_two_lists(self):
        """Testa com duas listas."""
        lists = [[1, 4, 5], [1, 3, 4]]
        assert merge_k_sorted_lists(lists) == [1, 1, 3, 4, 4, 5]
    
    def test_three_lists(self):
        """Testa com três listas."""
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        assert merge_k_sorted_lists(lists) == [1, 1, 2, 3, 4, 4, 5, 6]
    
    def test_lists_with_duplicates(self):
        """Testa com listas que contêm elementos duplicados."""
        lists = [[1, 1, 2], [1, 2, 2], [1, 3]]
        assert merge_k_sorted_lists(lists) == [1, 1, 1, 1, 2, 2, 2, 3]
    
    def test_lists_different_lengths(self):
        """Testa com listas de tamanhos diferentes."""
        lists = [[1, 3, 5, 7], [2, 4], [6, 8, 9]]
        assert merge_k_sorted_lists(lists) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_negative_numbers(self):
        """Testa com números negativos."""
        lists = [[-3, -1, 1], [-2, 0, 2], [-4, 4]]
        assert merge_k_sorted_lists(lists) == [-4, -3, -2, -1, 0, 1, 2, 4]
    
    def test_mixed_empty_and_non_empty(self):
        """Testa com mistura de listas vazias e não vazias."""
        lists = [[], [1, 2, 3], [], [4, 5], []]
        assert merge_k_sorted_lists(lists) == [1, 2, 3, 4, 5]
    
    def test_single_element_lists(self):
        """Testa com listas contendo apenas um elemento cada."""
        lists = [[1], [2], [3], [4]]
        assert merge_k_sorted_lists(lists) == [1, 2, 3, 4]
    
    def test_large_numbers(self):
        """Testa com números grandes."""
        lists = [[1000, 2000], [1500, 2500], [1200, 1800]]
        assert merge_k_sorted_lists(lists) == [1000, 1200, 1500, 1800, 2000, 2500] 