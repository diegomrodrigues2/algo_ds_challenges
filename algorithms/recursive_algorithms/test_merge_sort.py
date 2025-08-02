"""
Testes para o módulo de Merge Sort.

Este módulo contém testes abrangentes para todas as implementações
do algoritmo Mergesort.
"""

import pytest
import random
import time
from typing import List

from merge_sort import (
    merge_sort,
    _merge_sort_recursive,
    _merge,
    merge_sort_inplace,
    merge_sort_iterative,
    merge_sort_with_comparison_count,
    merge_sort_optimized,
    natural_merge_sort,
    _find_runs,
    merge_sort_parallel,
    _merge_sort_parallel_recursive,
    validate_sorted_array,
    count_inversions_merge_sort,
    _merge_with_inversion_count
)


class TestMergeSort:
    """Testes para a função merge_sort principal."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        assert merge_sort([]) == []
    
    def test_single_element(self):
        """Testa com array de um elemento."""
        assert merge_sort([5]) == [5]
    
    def test_two_elements_sorted(self):
        """Testa com dois elementos já ordenados."""
        assert merge_sort([1, 2]) == [1, 2]
    
    def test_two_elements_unsorted(self):
        """Testa com dois elementos desordenados."""
        assert merge_sort([2, 1]) == [1, 2]
    
    def test_multiple_elements(self):
        """Testa com múltiplos elementos."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert merge_sort(arr) == expected
    
    def test_already_sorted(self):
        """Testa com array já ordenado."""
        arr = [1, 2, 3, 4, 5]
        assert merge_sort(arr) == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted(self):
        """Testa com array ordenado em ordem decrescente."""
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        assert merge_sort(arr) == expected
    
    def test_duplicate_elements(self):
        """Testa com elementos duplicados."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        assert merge_sort(arr) == expected
    
    def test_negative_numbers(self):
        """Testa com números negativos."""
        arr = [-5, 3, -1, 0, -10, 7]
        expected = [-10, -5, -1, 0, 3, 7]
        assert merge_sort(arr) == expected
    
    def test_large_array(self):
        """Testa com array grande."""
        arr = list(range(1000, 0, -1))
        expected = list(range(1, 1001))
        assert merge_sort(arr) == expected


class TestMergeSortRecursive:
    """Testes para a função _merge_sort_recursive."""
    
    def test_basic_recursive(self):
        """Testa a função recursiva básica."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        _merge_sort_recursive(arr, 0, len(arr))
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert arr == expected
    
    def test_partial_sort(self):
        """Testa ordenação parcial."""
        arr = [5, 4, 3, 2, 1, 0]
        _merge_sort_recursive(arr, 1, 4)  # Ordena apenas [4, 3, 2]
        expected = [5, 2, 3, 4, 1, 0]
        assert arr == expected


class TestMerge:
    """Testes para a função _merge."""
    
    def test_merge_two_sorted_halves(self):
        """Testa mesclagem de duas metades ordenadas."""
        arr = [1, 3, 5, 2, 4, 6]
        _merge(arr, 0, 3, 6)
        expected = [1, 2, 3, 4, 5, 6]
        assert arr == expected
    
    def test_merge_with_duplicates(self):
        """Testa mesclagem com elementos duplicados."""
        arr = [1, 2, 2, 3, 1, 2, 3]
        _merge(arr, 0, 4, 7)
        expected = [1, 1, 2, 2, 2, 3, 3]
        assert arr == expected
    
    def test_merge_different_sizes(self):
        """Testa mesclagem de sub-listas de tamanhos diferentes."""
        arr = [1, 3, 5, 7, 2, 4]
        _merge(arr, 0, 4, 6)
        expected = [1, 2, 3, 4, 5, 7]
        assert arr == expected


class TestMergeSortInplace:
    """Testes para a função merge_sort_inplace."""
    
    def test_inplace_sorting(self):
        """Testa ordenação in-place."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        merge_sort_inplace(arr)
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert arr == expected
    
    def test_inplace_empty(self):
        """Testa array vazio in-place."""
        arr = []
        merge_sort_inplace(arr)
        assert arr == []
    
    def test_inplace_single_element(self):
        """Testa array de um elemento in-place."""
        arr = [5]
        merge_sort_inplace(arr)
        assert arr == [5]


class TestMergeSortIterative:
    """Testes para a função merge_sort_iterative."""
    
    def test_iterative_sorting(self):
        """Testa ordenação iterativa."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = merge_sort_iterative(arr)
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert result == expected
    
    def test_iterative_empty(self):
        """Testa array vazio iterativo."""
        assert merge_sort_iterative([]) == []
    
    def test_iterative_consistency(self):
        """Testa consistência com versão recursiva."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        iterative_result = merge_sort_iterative(arr.copy())
        recursive_result = merge_sort(arr)
        assert iterative_result == recursive_result


class TestMergeSortWithComparisonCount:
    """Testes para a função merge_sort_with_comparison_count."""
    
    def test_comparison_count_basic(self):
        """Testa contagem de comparações básica."""
        arr = [3, 1, 4, 1, 5]
        sorted_arr, comparisons = merge_sort_with_comparison_count(arr)
        expected = [1, 1, 3, 4, 5]
        assert sorted_arr == expected
        assert comparisons > 0
    
    def test_comparison_count_already_sorted(self):
        """Testa contagem com array já ordenado."""
        arr = [1, 2, 3, 4, 5]
        sorted_arr, comparisons = merge_sort_with_comparison_count(arr)
        assert sorted_arr == [1, 2, 3, 4, 5]
        assert comparisons > 0
    
    def test_comparison_count_reverse_sorted(self):
        """Testa contagem com array em ordem reversa."""
        arr = [5, 4, 3, 2, 1]
        sorted_arr, comparisons = merge_sort_with_comparison_count(arr)
        assert sorted_arr == [1, 2, 3, 4, 5]
        assert comparisons > 0


class TestMergeSortOptimized:
    """Testes para a função merge_sort_optimized."""
    
    def test_optimized_sorting(self):
        """Testa ordenação otimizada."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = merge_sort_optimized(arr)
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert result == expected
    
    def test_optimized_already_sorted(self):
        """Testa otimização com array já ordenado."""
        arr = [1, 2, 3, 4, 5]
        result = merge_sort_optimized(arr)
        assert result == [1, 2, 3, 4, 5]
    
    def test_optimized_small_array(self):
        """Testa otimização com array pequeno."""
        arr = [3, 1, 2]
        result = merge_sort_optimized(arr)
        assert result == [1, 2, 3]


class TestNaturalMergeSort:
    """Testes para a função natural_merge_sort."""
    
    def test_natural_merge_sort(self):
        """Testa natural merge sort."""
        arr = [1, 2, 3, 5, 4, 6, 7, 9, 8]
        result = natural_merge_sort(arr)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected
    
    def test_natural_merge_sort_already_sorted(self):
        """Testa com array já ordenado."""
        arr = [1, 2, 3, 4, 5]
        result = natural_merge_sort(arr)
        assert result == [1, 2, 3, 4, 5]
    
    def test_natural_merge_sort_reverse(self):
        """Testa com array em ordem reversa."""
        arr = [5, 4, 3, 2, 1]
        result = natural_merge_sort(arr)
        assert result == [1, 2, 3, 4, 5]


class TestFindRuns:
    """Testes para a função _find_runs."""
    
    def test_find_runs_basic(self):
        """Testa descoberta de runs básica."""
        arr = [1, 2, 3, 5, 4, 6, 7, 9, 8]
        runs = _find_runs(arr)
        # Esperamos runs: [1,2,3], [5], [4], [6,7], [9], [8]
        assert len(runs) > 0
        for start, end in runs:
            assert start < end
            assert end <= len(arr)
    
    def test_find_runs_already_sorted(self):
        """Testa com array já ordenado."""
        arr = [1, 2, 3, 4, 5]
        runs = _find_runs(arr)
        assert len(runs) == 1
        assert runs[0] == (0, 5)
    
    def test_find_runs_reverse_sorted(self):
        """Testa com array em ordem reversa."""
        arr = [5, 4, 3, 2, 1]
        runs = _find_runs(arr)
        assert len(runs) == 5  # Cada elemento é uma run


class TestMergeSortParallel:
    """Testes para a função merge_sort_parallel."""
    
    def test_parallel_sorting(self):
        """Testa ordenação paralela."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = merge_sort_parallel(arr, num_threads=2)
        expected = [11, 12, 22, 25, 34, 64, 90]
        assert result == expected
    
    def test_parallel_consistency(self):
        """Testa consistência da versão paralela."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        parallel_result = merge_sort_parallel(arr, num_threads=4)
        sequential_result = merge_sort(arr)
        assert parallel_result == sequential_result
    
    def test_parallel_different_threads(self):
        """Testa com diferentes números de threads."""
        arr = list(range(100, 0, -1))
        result1 = merge_sort_parallel(arr, num_threads=2)
        result2 = merge_sort_parallel(arr, num_threads=4)
        expected = list(range(1, 101))
        assert result1 == expected
        assert result2 == expected


class TestValidateSortedArray:
    """Testes para a função validate_sorted_array."""
    
    def test_validate_sorted(self):
        """Testa validação de array ordenado."""
        arr = [1, 2, 3, 4, 5]
        assert validate_sorted_array(arr) == True
    
    def test_validate_unsorted(self):
        """Testa validação de array desordenado."""
        arr = [3, 1, 4, 2, 5]
        assert validate_sorted_array(arr) == False
    
    def test_validate_empty(self):
        """Testa validação de array vazio."""
        assert validate_sorted_array([]) == True
    
    def test_validate_single_element(self):
        """Testa validação de array com um elemento."""
        assert validate_sorted_array([5]) == True
    
    def test_validate_duplicates(self):
        """Testa validação com elementos duplicados."""
        arr = [1, 2, 2, 3, 4]
        assert validate_sorted_array(arr) == True


class TestCountInversionsMergeSort:
    """Testes para a função count_inversions_merge_sort."""
    
    def test_count_inversions_basic(self):
        """Testa contagem de inversões básica."""
        arr = [3, 1, 4, 1, 5]
        inversions = count_inversions_merge_sort(arr)
        # Inversões: (3,1), (3,1), (4,1), (4,1), (5,1), (5,1)
        assert inversions == 6
    
    def test_count_inversions_sorted(self):
        """Testa contagem com array ordenado."""
        arr = [1, 2, 3, 4, 5]
        inversions = count_inversions_merge_sort(arr)
        assert inversions == 0
    
    def test_count_inversions_reverse(self):
        """Testa contagem com array em ordem reversa."""
        arr = [5, 4, 3, 2, 1]
        inversions = count_inversions_merge_sort(arr)
        # n*(n-1)/2 = 5*4/2 = 10 inversões
        assert inversions == 10
    
    def test_count_inversions_duplicates(self):
        """Testa contagem com elementos duplicados."""
        arr = [2, 2, 2]
        inversions = count_inversions_merge_sort(arr)
        assert inversions == 0


class TestMergeWithInversionCount:
    """Testes para a função _merge_with_inversion_count."""
    
    def test_merge_with_inversion_count(self):
        """Testa mesclagem com contagem de inversões."""
        arr = [1, 3, 5, 2, 4, 6]
        inversions = _merge_with_inversion_count(arr, 0, 3, 6)
        # Inversões: (3,2), (5,2), (5,4)
        assert inversions == 3
    
    def test_merge_no_inversions(self):
        """Testa mesclagem sem inversões."""
        arr = [1, 2, 3, 4, 5, 6]
        inversions = _merge_with_inversion_count(arr, 0, 3, 6)
        assert inversions == 0


class TestConsistency:
    """Testes de consistência entre diferentes implementações."""
    
    def test_all_implementations_consistent(self):
        """Testa que todas as implementações produzem o mesmo resultado."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        
        assert merge_sort(arr.copy()) == expected
        assert merge_sort_iterative(arr.copy()) == expected
        assert merge_sort_optimized(arr.copy()) == expected
        assert natural_merge_sort(arr.copy()) == expected
        
        # Testa in-place
        arr_copy = arr.copy()
        merge_sort_inplace(arr_copy)
        assert arr_copy == expected


class TestEdgeCases:
    """Testes para casos extremos."""
    
    def test_large_random_array(self):
        """Testa com array grande e aleatório."""
        arr = [random.randint(-1000, 1000) for _ in range(1000)]
        result = merge_sort(arr.copy())
        assert validate_sorted_array(result)
    
    def test_all_same_elements(self):
        """Testa com todos os elementos iguais."""
        arr = [5] * 100
        result = merge_sort(arr.copy())
        assert result == [5] * 100
    
    def test_alternating_pattern(self):
        """Testa com padrão alternado."""
        arr = [1, -1, 1, -1, 1, -1]
        result = merge_sort(arr.copy())
        expected = [-1, -1, -1, 1, 1, 1]
        assert result == expected
    
    def test_extreme_values(self):
        """Testa com valores extremos."""
        arr = [float('inf'), float('-inf'), 0, 1, -1]
        result = merge_sort(arr.copy())
        expected = [float('-inf'), -1, 0, 1, float('inf')]
        assert result == expected


class TestPerformance:
    """Testes de performance."""
    
    def test_performance_large_array(self):
        """Testa performance com array grande."""
        arr = list(range(10000, 0, -1))
        start_time = time.time()
        result = merge_sort(arr.copy())
        end_time = time.time()
        
        assert result == list(range(1, 10001))
        assert end_time - start_time < 1.0  # Deve completar em menos de 1 segundo
    
    def test_performance_already_sorted(self):
        """Testa performance com array já ordenado."""
        arr = list(range(10000))
        start_time = time.time()
        result = merge_sort(arr.copy())
        end_time = time.time()
        
        assert result == list(range(10000))
        assert end_time - start_time < 1.0
    
    def test_parallel_performance(self):
        """Testa performance da versão paralela."""
        arr = list(range(10000, 0, -1))
        start_time = time.time()
        result = merge_sort_parallel(arr.copy(), num_threads=4)
        end_time = time.time()
        
        assert result == list(range(1, 10001))
        assert end_time - start_time < 1.0


if __name__ == "__main__":
    pytest.main([__file__]) 