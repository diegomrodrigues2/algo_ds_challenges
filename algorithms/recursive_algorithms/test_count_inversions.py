"""
Testes para o módulo Contagem de Inversões.

Este módulo testa todas as funcionalidades implementadas,
incluindo diferentes algoritmos e casos de teste.
"""

import pytest
from .count_inversions import (
    count_inversions_brute_force,
    count_inversions_merge_sort,
    _merge_sort_with_inversions,
    _merge_with_inversions,
    find_inversion_pairs,
    count_inversions_fenwick_tree,
    _compress_array,
    FenwickTree,
    _get_lsb,
    validate_inversion_count
)


class TestCountInversionsBruteForce:
    """Testes para a função de força bruta."""
    
    def test_empty_array(self):
        """Testa array vazio."""
        assert count_inversions_brute_force([]) == 0
    
    def test_single_element(self):
        """Testa array com um elemento."""
        assert count_inversions_brute_force([5]) == 0
    
    def test_two_elements_no_inversion(self):
        """Testa dois elementos sem inversão."""
        assert count_inversions_brute_force([1, 2]) == 0
    
    def test_two_elements_with_inversion(self):
        """Testa dois elementos com inversão."""
        assert count_inversions_brute_force([2, 1]) == 1
    
    def test_three_elements(self):
        """Testa três elementos."""
        assert count_inversions_brute_force([3, 1, 2]) == 2
    
    def test_four_elements(self):
        """Testa quatro elementos."""
        assert count_inversions_brute_force([8, 4, 2, 1]) == 6
    
    def test_sorted_array(self):
        """Testa array ordenado."""
        assert count_inversions_brute_force([1, 2, 3, 4, 5]) == 0
    
    def test_reverse_sorted_array(self):
        """Testa array ordenado reversamente."""
        assert count_inversions_brute_force([5, 4, 3, 2, 1]) == 10
    
    def test_duplicate_elements(self):
        """Testa array com elementos duplicados."""
        assert count_inversions_brute_force([2, 2, 1, 1]) == 4


class TestCountInversionsMergeSort:
    """Testes para a função usando Mergesort."""
    
    def test_empty_array(self):
        """Testa array vazio."""
        assert count_inversions_merge_sort([]) == 0
    
    def test_single_element(self):
        """Testa array com um elemento."""
        assert count_inversions_merge_sort([5]) == 0
    
    def test_two_elements_no_inversion(self):
        """Testa dois elementos sem inversão."""
        assert count_inversions_merge_sort([1, 2]) == 0
    
    def test_two_elements_with_inversion(self):
        """Testa dois elementos com inversão."""
        assert count_inversions_merge_sort([2, 1]) == 1
    
    def test_three_elements(self):
        """Testa três elementos."""
        assert count_inversions_merge_sort([3, 1, 2]) == 2
    
    def test_four_elements(self):
        """Testa quatro elementos."""
        assert count_inversions_merge_sort([8, 4, 2, 1]) == 6
    
    def test_sorted_array(self):
        """Testa array ordenado."""
        assert count_inversions_merge_sort([1, 2, 3, 4, 5]) == 0
    
    def test_reverse_sorted_array(self):
        """Testa array ordenado reversamente."""
        assert count_inversions_merge_sort([5, 4, 3, 2, 1]) == 10
    
    def test_duplicate_elements(self):
        """Testa array com elementos duplicados."""
        assert count_inversions_merge_sort([2, 2, 1, 1]) == 4
    
    def test_large_array(self):
        """Testa array grande."""
        arr = list(range(100, 0, -1))
        expected = 99 * 50  # Soma de 1 até 99
        assert count_inversions_merge_sort(arr) == expected


class TestMergeSortWithInversions:
    """Testes para a função auxiliar _merge_sort_with_inversions."""
    
    def test_single_element(self):
        """Testa um elemento."""
        arr = [5]
        assert _merge_sort_with_inversions(arr, 0, 0) == 0
    
    def test_two_elements_no_inversion(self):
        """Testa dois elementos sem inversão."""
        arr = [1, 2]
        assert _merge_sort_with_inversions(arr, 0, 1) == 0
        assert arr == [1, 2]  # Deve estar ordenado
    
    def test_two_elements_with_inversion(self):
        """Testa dois elementos com inversão."""
        arr = [2, 1]
        assert _merge_sort_with_inversions(arr, 0, 1) == 1
        assert arr == [1, 2]  # Deve estar ordenado
    
    def test_three_elements(self):
        """Testa três elementos."""
        arr = [3, 1, 2]
        assert _merge_sort_with_inversions(arr, 0, 2) == 2
        assert arr == [1, 2, 3]  # Deve estar ordenado


class TestMergeWithInversions:
    """Testes para a função _merge_with_inversions."""
    
    def test_merge_no_inversions(self):
        """Testa mesclagem sem inversões."""
        arr = [1, 3, 2, 4]  # [1,3] e [2,4] são ordenados
        inversions = _merge_with_inversions(arr, 0, 1, 3)
        assert inversions == 0
        assert arr == [1, 2, 3, 4]
    
    def test_merge_with_inversions(self):
        """Testa mesclagem com inversões."""
        arr = [2, 4, 1, 3]  # [2,4] e [1,3] são ordenados
        inversions = _merge_with_inversions(arr, 0, 1, 3)
        assert inversions == 2  # 1 forma inversões com 2 e 4
        assert arr == [1, 2, 3, 4]
    
    def test_merge_all_inversions(self):
        """Testa mesclagem com muitas inversões."""
        arr = [5, 6, 1, 2, 3]  # [5,6] e [1,2,3] são ordenados
        inversions = _merge_with_inversions(arr, 0, 1, 4)
        assert inversions == 4  # 1,2,3 formam inversões com 5,6
        assert arr == [1, 2, 3, 5, 6]


class TestFindInversionPairs:
    """Testes para a função find_inversion_pairs."""
    
    def test_empty_array(self):
        """Testa array vazio."""
        assert find_inversion_pairs([]) == []
    
    def test_single_element(self):
        """Testa array com um elemento."""
        assert find_inversion_pairs([5]) == []
    
    def test_two_elements_no_inversion(self):
        """Testa dois elementos sem inversão."""
        assert find_inversion_pairs([1, 2]) == []
    
    def test_two_elements_with_inversion(self):
        """Testa dois elementos com inversão."""
        assert find_inversion_pairs([2, 1]) == [(0, 1)]
    
    def test_three_elements(self):
        """Testa três elementos."""
        pairs = find_inversion_pairs([3, 1, 2])
        assert len(pairs) == 2
        assert (0, 1) in pairs
        assert (0, 2) in pairs
    
    def test_four_elements(self):
        """Testa quatro elementos."""
        pairs = find_inversion_pairs([8, 4, 2, 1])
        expected = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        assert len(pairs) == 6
        for pair in expected:
            assert pair in pairs


class TestCountInversionsFenwickTree:
    """Testes para a função usando Fenwick Tree."""
    
    def test_empty_array(self):
        """Testa array vazio."""
        assert count_inversions_fenwick_tree([]) == 0
    
    def test_single_element(self):
        """Testa array com um elemento."""
        assert count_inversions_fenwick_tree([5]) == 0
    
    def test_two_elements_no_inversion(self):
        """Testa dois elementos sem inversão."""
        assert count_inversions_fenwick_tree([1, 2]) == 0
    
    def test_two_elements_with_inversion(self):
        """Testa dois elementos com inversão."""
        assert count_inversions_fenwick_tree([2, 1]) == 1
    
    def test_three_elements(self):
        """Testa três elementos."""
        assert count_inversions_fenwick_tree([3, 1, 2]) == 2
    
    def test_four_elements(self):
        """Testa quatro elementos."""
        assert count_inversions_fenwick_tree([8, 4, 2, 1]) == 6
    
    def test_sorted_array(self):
        """Testa array ordenado."""
        assert count_inversions_fenwick_tree([1, 2, 3, 4, 5]) == 0
    
    def test_reverse_sorted_array(self):
        """Testa array ordenado reversamente."""
        assert count_inversions_fenwick_tree([5, 4, 3, 2, 1]) == 10


class TestCompressArray:
    """Testes para a função _compress_array."""
    
    def test_empty_array(self):
        """Testa array vazio."""
        assert _compress_array([]) == []
    
    def test_single_element(self):
        """Testa array com um elemento."""
        assert _compress_array([5]) == [0]
    
    def test_sorted_array(self):
        """Testa array ordenado."""
        assert _compress_array([1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
    
    def test_reverse_sorted_array(self):
        """Testa array ordenado reversamente."""
        assert _compress_array([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
    
    def test_duplicate_elements(self):
        """Testa array com elementos duplicados."""
        assert _compress_array([2, 2, 1, 1]) == [1, 1, 0, 0]
    
    def test_example_from_docstring(self):
        """Testa o exemplo da docstring."""
        assert _compress_array([8, 4, 2, 1]) == [3, 2, 1, 0]


class TestFenwickTree:
    """Testes para a classe FenwickTree."""
    
    def test_init(self):
        """Testa inicialização."""
        tree = FenwickTree(5)
        assert tree.size == 5
        assert len(tree.tree) == 6  # 1-indexed
    
    def test_update_and_query_single(self):
        """Testa atualização e consulta de um elemento."""
        tree = FenwickTree(5)
        tree.update(1, 5)
        assert tree.query(1) == 5
    
    def test_update_and_query_multiple(self):
        """Testa múltiplas atualizações e consultas."""
        tree = FenwickTree(5)
        tree.update(1, 3)
        tree.update(2, 4)
        tree.update(3, 2)
        assert tree.query(1) == 3
        assert tree.query(2) == 7
        assert tree.query(3) == 9
    
    def test_update_and_query_range(self):
        """Testa consultas de intervalo."""
        tree = FenwickTree(5)
        for i in range(1, 6):
            tree.update(i, i)
        assert tree.query(5) == 15  # 1+2+3+4+5
        assert tree.query(3) == 6   # 1+2+3


class TestGetLSB:
    """Testes para a função _get_lsb."""
    
    def test_power_of_two(self):
        """Testa potências de 2."""
        assert _get_lsb(1) == 1
        assert _get_lsb(2) == 2
        assert _get_lsb(4) == 4
        assert _get_lsb(8) == 8
    
    def test_odd_numbers(self):
        """Testa números ímpares."""
        assert _get_lsb(3) == 1
        assert _get_lsb(5) == 1
        assert _get_lsb(7) == 1
    
    def test_even_numbers(self):
        """Testa números pares."""
        assert _get_lsb(6) == 2   # 6 = 110, LSB = 10 = 2
        assert _get_lsb(12) == 4  # 12 = 1100, LSB = 100 = 4
        assert _get_lsb(10) == 2  # 10 = 1010, LSB = 10 = 2
    
    def test_example_from_docstring(self):
        """Testa o exemplo da docstring."""
        assert _get_lsb(12) == 4  # 12 = 1100, LSB = 100 = 4


class TestValidateInversionCount:
    """Testes para a função validate_inversion_count."""
    
    def test_valid_count(self):
        """Testa contagem válida."""
        arr = [3, 1, 2]
        assert validate_inversion_count(arr, 2) == True
    
    def test_invalid_count(self):
        """Testa contagem inválida."""
        arr = [3, 1, 2]
        assert validate_inversion_count(arr, 1) == False
    
    def test_empty_array(self):
        """Testa array vazio."""
        assert validate_inversion_count([], 0) == True
    
    def test_sorted_array(self):
        """Testa array ordenado."""
        arr = [1, 2, 3, 4, 5]
        assert validate_inversion_count(arr, 0) == True


class TestConsistency:
    """Testes de consistência entre diferentes algoritmos."""
    
    def test_brute_force_vs_merge_sort(self):
        """Testa consistência entre força bruta e mergesort."""
        test_cases = [
            [],
            [1],
            [1, 2],
            [2, 1],
            [3, 1, 2],
            [8, 4, 2, 1],
            [5, 4, 3, 2, 1],
            [2, 2, 1, 1]
        ]
        
        for arr in test_cases:
            brute_force = count_inversions_brute_force(arr)
            merge_sort = count_inversions_merge_sort(arr)
            assert brute_force == merge_sort
    
    def test_merge_sort_vs_fenwick_tree(self):
        """Testa consistência entre mergesort e fenwick tree."""
        test_cases = [
            [],
            [1],
            [1, 2],
            [2, 1],
            [3, 1, 2],
            [8, 4, 2, 1],
            [5, 4, 3, 2, 1]
        ]
        
        for arr in test_cases:
            merge_sort = count_inversions_merge_sort(arr)
            fenwick_tree = count_inversions_fenwick_tree(arr)
            assert merge_sort == fenwick_tree


class TestEdgeCases:
    """Testes para casos extremos."""
    
    def test_large_array(self):
        """Testa array grande."""
        arr = list(range(1000, 0, -1))
        expected = 999 * 500  # Soma de 1 até 999
        assert count_inversions_merge_sort(arr) == expected
    
    def test_negative_numbers(self):
        """Testa números negativos."""
        arr = [3, -1, 2, -5]
        # Nota: Fenwick Tree pode não funcionar com números negativos
        assert count_inversions_brute_force(arr) == 4
        assert count_inversions_merge_sort(arr) == 4
    
    def test_duplicate_elements(self):
        """Testa elementos duplicados."""
        arr = [2, 2, 1, 1]
        assert count_inversions_brute_force(arr) == 4
        assert count_inversions_merge_sort(arr) == 4
    
    def test_all_same_elements(self):
        """Testa todos os elementos iguais."""
        arr = [1, 1, 1, 1]
        assert count_inversions_brute_force(arr) == 0
        assert count_inversions_merge_sort(arr) == 0


class TestPerformance:
    """Testes de performance."""
    
    def test_brute_force_performance(self):
        """Testa performance da força bruta."""
        arr = list(range(100, 0, -1))
        # Deve ser lento mas correto
        result = count_inversions_brute_force(arr)
        expected = 99 * 50  # Soma de 1 até 99
        assert result == expected
    
    def test_merge_sort_performance(self):
        """Testa performance do mergesort."""
        arr = list(range(1000, 0, -1))
        # Deve ser rápido
        result = count_inversions_merge_sort(arr)
        expected = 999 * 500  # Soma de 1 até 999
        assert result == expected
    
    def test_fenwick_tree_performance(self):
        """Testa performance da fenwick tree."""
        arr = list(range(1000, 0, -1))
        # Deve ser rápido
        result = count_inversions_fenwick_tree(arr)
        expected = 999 * 500  # Soma de 1 até 999
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__]) 