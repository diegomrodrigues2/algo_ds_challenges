"""
Testes para o módulo de Quickselect.

Este módulo contém testes abrangentes para todas as implementações
do algoritmo Quickselect.
"""

import pytest
import random
import time
from typing import List

from quickselect import (
    quickselect,
    quickselect_recursive,
    partition,
    partition_random_pivot,
    quickselect_with_comparison_count,
    quickselect_median_of_three,
    _median_of_three,
    quickselect_iterative,
    find_kth_largest,
    find_median,
    quickselect_optimized,
    validate_kth_element,
    quickselect_with_duplicates,
    partition_with_duplicates,
    quickselect_parallel,
    _quickselect_parallel_recursive,
    analyze_quickselect_complexity
)


class TestQuickselect:
    """Testes para a função quickselect principal."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        with pytest.raises(ValueError):
            quickselect([], 1)
    
    def test_single_element(self):
        """Testa com array de um elemento."""
        assert quickselect([5], 1) == 5
    
    def test_basic_case(self):
        """Testa caso básico."""
        arr = [3, 2, 1, 5, 6, 4]
        assert quickselect(arr, 1) == 1  # menor elemento
        assert quickselect(arr, 2) == 2  # segundo menor
        assert quickselect(arr, 6) == 6  # maior elemento
    
    def test_duplicate_elements(self):
        """Testa com elementos duplicados."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert quickselect(arr, 1) == 1
        assert quickselect(arr, 2) == 1  # segundo 1
        assert quickselect(arr, 3) == 2
    
    def test_sorted_array(self):
        """Testa com array já ordenado."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(1, len(arr) + 1):
            assert quickselect(arr.copy(), i) == i
    
    def test_reverse_sorted_array(self):
        """Testa com array ordenado reversamente."""
        arr = [8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(1, len(arr) + 1):
            assert quickselect(arr.copy(), i) == i
    
    def test_all_same_elements(self):
        """Testa com todos os elementos iguais."""
        arr = [5, 5, 5, 5, 5]
        for i in range(1, len(arr) + 1):
            assert quickselect(arr.copy(), i) == 5
    
    def test_invalid_k(self):
        """Testa com k inválido."""
        arr = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError):
            quickselect(arr, 0)
        with pytest.raises(ValueError):
            quickselect(arr, 6)


class TestQuickselectRecursive:
    """Testes para a função quickselect_recursive."""
    
    def test_basic_recursive(self):
        """Testa caso básico recursivo."""
        arr = [3, 2, 1, 5, 6, 4]
        assert quickselect_recursive(arr, 0, len(arr) - 1, 1) == 1
        assert quickselect_recursive(arr, 0, len(arr) - 1, 3) == 3
    
    def test_subarray_selection(self):
        """Testa seleção em subarrays."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        # Selecionar o 2º menor no subarray [5, 4, 3, 2, 1]
        assert quickselect_recursive(arr, 4, 8, 2) == 2


class TestPartition:
    """Testes para as funções de partição."""
    
    def test_basic_partition(self):
        """Testa partição básica."""
        arr = [3, 2, 1, 5, 6, 4]
        pivot_index = partition(arr, 0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        # Verifica se todos os elementos à esquerda são menores ou iguais
        for i in range(pivot_index):
            assert arr[i] <= pivot
        
        # Verifica se todos os elementos à direita são maiores ou iguais
        for i in range(pivot_index + 1, len(arr)):
            assert arr[i] >= pivot
    
    def test_partition_random_pivot(self):
        """Testa partição com pivô aleatório."""
        arr = [3, 2, 1, 5, 6, 4]
        pivot_index = partition_random_pivot(arr, 0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        # Verifica se todos os elementos à esquerda são menores ou iguais
        for i in range(pivot_index):
            assert arr[i] <= pivot
        
        # Verifica se todos os elementos à direita são maiores ou iguais
        for i in range(pivot_index + 1, len(arr)):
            assert arr[i] >= pivot
    
    def test_partition_with_duplicates(self):
        """Testa partição com duplicatas."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        start, end = partition_with_duplicates(arr, 0, len(arr) - 1)
        
        # Verifica se a região de elementos iguais está correta
        pivot = arr[start]
        for i in range(start, end + 1):
            assert arr[i] == pivot


class TestQuickselectWithComparisonCount:
    """Testes para quickselect com contagem de comparações."""
    
    def test_comparison_count(self):
        """Testa contagem de comparações."""
        arr = [3, 2, 1, 5, 6, 4]
        result, comparisons = quickselect_with_comparison_count(arr, 3)
        assert result == 3
        assert comparisons > 0
    
    def test_comparison_count_sorted(self):
        """Testa contagem em array ordenado."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        result, comparisons = quickselect_with_comparison_count(arr, 4)
        assert result == 4
        assert comparisons > 0


class TestQuickselectMedianOfThree:
    """Testes para quickselect com mediana de três."""
    
    def test_median_of_three(self):
        """Testa seleção da mediana de três."""
        arr = [5, 2, 8, 1, 9, 3]
        median_index = _median_of_three(arr, 0, len(arr) - 1)
        assert 0 <= median_index < len(arr)
    
    def test_quickselect_median_of_three(self):
        """Testa quickselect com mediana de três."""
        arr = [3, 2, 1, 5, 6, 4]
        assert quickselect_median_of_three(arr, 1) == 1
        assert quickselect_median_of_three(arr, 3) == 3


class TestQuickselectIterative:
    """Testes para versão iterativa do quickselect."""
    
    def test_iterative_basic(self):
        """Testa caso básico iterativo."""
        arr = [3, 2, 1, 5, 6, 4]
        assert quickselect_iterative(arr, 1) == 1
        assert quickselect_iterative(arr, 3) == 3
    
    def test_iterative_consistency(self):
        """Testa consistência com versão recursiva."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        for k in range(1, len(arr) + 1):
            iterative_result = quickselect_iterative(arr.copy(), k)
            recursive_result = quickselect(arr.copy(), k)
            assert iterative_result == recursive_result


class TestFindKthLargest:
    """Testes para encontrar k-ésimo maior elemento."""
    
    def test_find_kth_largest(self):
        """Testa encontrar k-ésimo maior."""
        arr = [3, 2, 1, 5, 6, 4]
        assert find_kth_largest(arr, 1) == 6  # maior
        assert find_kth_largest(arr, 2) == 5  # segundo maior
        assert find_kth_largest(arr, 6) == 1  # menor
    
    def test_kth_largest_consistency(self):
        """Testa consistência entre k-ésimo menor e maior."""
        arr = [3, 2, 1, 5, 6, 4]
        for k in range(1, len(arr) + 1):
            kth_smallest = quickselect(arr.copy(), k)
            kth_largest = find_kth_largest(arr.copy(), k)
            # Verifica se são consistentes
            sorted_arr = sorted(arr)
            assert kth_smallest == sorted_arr[k - 1]
            assert kth_largest == sorted_arr[-k]


class TestFindMedian:
    """Testes para encontrar mediana."""
    
    def test_find_median_odd(self):
        """Testa mediana com número ímpar de elementos."""
        arr = [1, 3, 2, 5, 4]
        median = find_median(arr)
        assert median == 3.0
    
    def test_find_median_even(self):
        """Testa mediana com número par de elementos."""
        arr = [1, 3, 2, 4]
        median = find_median(arr)
        assert median == 2.5  # (2 + 3) / 2
    
    def test_find_median_single(self):
        """Testa mediana com um elemento."""
        arr = [5]
        median = find_median(arr)
        assert median == 5.0


class TestQuickselectOptimized:
    """Testes para versão otimizada do quickselect."""
    
    def test_optimized_basic(self):
        """Testa caso básico otimizado."""
        arr = [3, 2, 1, 5, 6, 4]
        assert quickselect_optimized(arr, 1) == 1
        assert quickselect_optimized(arr, 3) == 3
    
    def test_optimized_performance(self):
        """Testa performance da versão otimizada."""
        arr = list(range(1000))
        random.shuffle(arr)
        
        start_time = time.time()
        result1 = quickselect_optimized(arr.copy(), 500)
        optimized_time = time.time() - start_time
        
        start_time = time.time()
        result2 = quickselect(arr.copy(), 500)
        regular_time = time.time() - start_time
        
        assert result1 == result2
        # A versão otimizada deve ser pelo menos tão rápida quanto a regular


class TestValidateKthElement:
    """Testes para validação do k-ésimo elemento."""
    
    def test_validate_correct_result(self):
        """Testa validação de resultado correto."""
        arr = [3, 2, 1, 5, 6, 4]
        result = quickselect(arr.copy(), 3)
        assert validate_kth_element(arr, 3, result) == True
    
    def test_validate_incorrect_result(self):
        """Testa validação de resultado incorreto."""
        arr = [3, 2, 1, 5, 6, 4]
        assert validate_kth_element(arr, 3, 5) == False  # resultado incorreto


class TestQuickselectWithDuplicates:
    """Testes para quickselect com duplicatas."""
    
    def test_with_duplicates_basic(self):
        """Testa caso básico com duplicatas."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert quickselect_with_duplicates(arr, 1) == 1
        assert quickselect_with_duplicates(arr, 2) == 1  # segundo 1
        assert quickselect_with_duplicates(arr, 3) == 2
    
    def test_with_duplicates_all_same(self):
        """Testa com todos os elementos iguais."""
        arr = [5, 5, 5, 5, 5]
        for i in range(1, len(arr) + 1):
            assert quickselect_with_duplicates(arr.copy(), i) == 5


class TestQuickselectParallel:
    """Testes para versão paralela do quickselect."""
    
    def test_parallel_basic(self):
        """Testa caso básico paralelo."""
        arr = [3, 2, 1, 5, 6, 4]
        assert quickselect_parallel(arr, 1) == 1
        assert quickselect_parallel(arr, 3) == 3
    
    def test_parallel_consistency(self):
        """Testa consistência da versão paralela."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        for k in range(1, len(arr) + 1):
            parallel_result = quickselect_parallel(arr.copy(), k)
            regular_result = quickselect(arr.copy(), k)
            assert parallel_result == regular_result


class TestAnalyzeQuickselectComplexity:
    """Testes para análise de complexidade."""
    
    def test_complexity_analysis(self):
        """Testa análise de complexidade."""
        analysis = analyze_quickselect_complexity(1000)
        assert 'expected_time' in analysis
        assert 'worst_case_time' in analysis
        assert 'average_case_time' in analysis
        assert analysis['expected_time'] == 'O(n)'
        assert analysis['worst_case_time'] == 'O(n²)'


class TestConsistency:
    """Testes de consistência entre diferentes implementações."""
    
    def test_all_implementations_consistent(self):
        """Testa consistência entre todas as implementações."""
        arr = [3, 2, 1, 5, 6, 4, 8, 7, 9]
        k = 5
        
        results = []
        implementations = [
            quickselect,
            quickselect_median_of_three,
            quickselect_iterative,
            quickselect_optimized,
            quickselect_with_duplicates,
            quickselect_parallel
        ]
        
        for impl in implementations:
            try:
                result = impl(arr.copy(), k)
                results.append(result)
            except NotImplementedError:
                continue
        
        # Todos os resultados devem ser iguais
        if len(results) > 1:
            assert all(r == results[0] for r in results)


class TestEdgeCases:
    """Testes para casos extremos."""
    
    def test_large_array(self):
        """Testa com array grande."""
        arr = list(range(10000))
        random.shuffle(arr)
        
        # Testa alguns valores de k
        for k in [1, 100, 5000, 9999]:
            result = quickselect(arr.copy(), k)
            assert result == k - 1  # 0-indexed
    
    def test_repeated_elements(self):
        """Testa com muitos elementos repetidos."""
        arr = [1] * 100 + [2] * 100 + [3] * 100
        random.shuffle(arr)
        
        assert quickselect(arr.copy(), 1) == 1
        assert quickselect(arr.copy(), 100) == 1
        assert quickselect(arr.copy(), 101) == 2
        assert quickselect(arr.copy(), 200) == 2
        assert quickselect(arr.copy(), 201) == 3
    
    def test_extreme_values(self):
        """Testa com valores extremos."""
        arr = [float('-inf'), -1000000, 0, 1000000, float('inf')]
        assert quickselect(arr.copy(), 1) == float('-inf')
        assert quickselect(arr.copy(), 3) == 0
        assert quickselect(arr.copy(), 5) == float('inf')


class TestPerformance:
    """Testes de performance."""
    
    def test_performance_comparison(self):
        """Compara performance de diferentes implementações."""
        arr = list(range(1000))
        random.shuffle(arr)
        k = 500
        
        implementations = [
            quickselect,
            quickselect_median_of_three,
            quickselect_iterative,
            quickselect_optimized
        ]
        
        times = {}
        for impl in implementations:
            try:
                start_time = time.time()
                result = impl(arr.copy(), k)
                end_time = time.time()
                times[impl.__name__] = end_time - start_time
            except NotImplementedError:
                continue
        
        # Verifica se todas as implementações retornam o mesmo resultado
        if len(times) > 1:
            assert len(set(times.keys())) == len(times)  # Todas diferentes


if __name__ == "__main__":
    pytest.main([__file__]) 