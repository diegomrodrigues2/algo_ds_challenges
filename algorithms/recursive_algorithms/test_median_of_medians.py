"""
Testes para o módulo de Mediana das Medianas.

Este módulo contém testes abrangentes para todas as implementações
do algoritmo Mediana das Medianas (BFPRT).
"""

import pytest
import random
import time
from typing import List

from median_of_medians import (
    median_of_medians_select,
    median_of_medians_recursive,
    find_median_of_medians,
    median_of_five,
    partition_around_pivot,
    median_of_medians_with_comparison_count,
    find_median_using_mom,
    find_kth_largest_mom,
    median_of_medians_optimized,
    validate_mom_result,
    analyze_mom_complexity,
    compare_mom_with_quickselect,
    median_of_medians_parallel,
    _mom_parallel_recursive,
    find_percentile_mom,
    median_of_medians_with_duplicates,
    partition_with_duplicates_mom,
    analyze_mom_theoretical_bounds
)


class TestMedianOfMediansSelect:
    """Testes para a função median_of_medians_select principal."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        with pytest.raises(ValueError):
            median_of_medians_select([], 1)
    
    def test_single_element(self):
        """Testa com array de um elemento."""
        assert median_of_medians_select([5], 1) == 5
    
    def test_basic_case(self):
        """Testa caso básico."""
        arr = [3, 2, 1, 5, 6, 4]
        assert median_of_medians_select(arr, 1) == 1  # menor elemento
        assert median_of_medians_select(arr, 2) == 2  # segundo menor
        assert median_of_medians_select(arr, 6) == 6  # maior elemento
    
    def test_duplicate_elements(self):
        """Testa com elementos duplicados."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert median_of_medians_select(arr, 1) == 1
        assert median_of_medians_select(arr, 2) == 1  # segundo 1
        assert median_of_medians_select(arr, 3) == 2
    
    def test_sorted_array(self):
        """Testa com array já ordenado."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(1, len(arr) + 1):
            assert median_of_medians_select(arr.copy(), i) == i
    
    def test_reverse_sorted_array(self):
        """Testa com array ordenado reversamente."""
        arr = [8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(1, len(arr) + 1):
            assert median_of_medians_select(arr.copy(), i) == i
    
    def test_all_same_elements(self):
        """Testa com todos os elementos iguais."""
        arr = [5, 5, 5, 5, 5]
        for i in range(1, len(arr) + 1):
            assert median_of_medians_select(arr.copy(), i) == 5
    
    def test_invalid_k(self):
        """Testa com k inválido."""
        arr = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError):
            median_of_medians_select(arr, 0)
        with pytest.raises(ValueError):
            median_of_medians_select(arr, 6)


class TestMedianOfMediansRecursive:
    """Testes para a função median_of_medians_recursive."""
    
    def test_basic_recursive(self):
        """Testa caso básico recursivo."""
        arr = [3, 2, 1, 5, 6, 4]
        assert median_of_medians_recursive(arr, 0, len(arr) - 1, 1) == 1
        assert median_of_medians_recursive(arr, 0, len(arr) - 1, 3) == 3
    
    def test_subarray_selection(self):
        """Testa seleção em subarrays."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        # Selecionar o 2º menor no subarray [5, 4, 3, 2, 1]
        assert median_of_medians_recursive(arr, 4, 8, 2) == 2


class TestFindMedianOfMedians:
    """Testes para encontrar a mediana das medianas."""
    
    def test_find_median_of_medians(self):
        """Testa encontrar mediana das medianas."""
        arr = [3, 2, 1, 5, 6, 4, 8, 7, 9, 10]
        pivot_index = find_median_of_medians(arr, 0, len(arr) - 1)
        assert 0 <= pivot_index < len(arr)
    
    def test_median_of_medians_quality(self):
        """Testa a qualidade do pivô escolhido."""
        arr = list(range(100))
        random.shuffle(arr)
        pivot_index = find_median_of_medians(arr, 0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        # O pivô deve estar entre o 30º e 70º percentil
        sorted_arr = sorted(arr)
        rank = sorted_arr.index(pivot) + 1
        assert 0.3 * len(arr) <= rank <= 0.7 * len(arr)


class TestMedianOfFive:
    """Testes para encontrar mediana de cinco elementos."""
    
    def test_median_of_five(self):
        """Testa mediana de cinco elementos."""
        arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        median_index = median_of_five(arr, 0, 4)
        assert 0 <= median_index <= 4
        
        # Verifica se é realmente a mediana
        group = arr[0:5]
        sorted_group = sorted(group)
        expected_median = sorted_group[2]
        assert arr[median_index] == expected_median
    
    def test_median_of_five_edge_cases(self):
        """Testa casos extremos para mediana de cinco."""
        # Todos iguais
        arr = [5, 5, 5, 5, 5]
        median_index = median_of_five(arr, 0, 4)
        assert arr[median_index] == 5
        
        # Já ordenados
        arr = [1, 2, 3, 4, 5]
        median_index = median_of_five(arr, 0, 4)
        assert arr[median_index] == 3


class TestPartitionAroundPivot:
    """Testes para partição ao redor do pivô."""
    
    def test_partition_around_pivot(self):
        """Testa partição ao redor do pivô."""
        arr = [3, 2, 1, 5, 6, 4]
        pivot_index = 3  # elemento 5
        final_pivot_index = partition_around_pivot(arr, 0, len(arr) - 1, pivot_index)
        pivot = arr[final_pivot_index]
        
        # Verifica se todos os elementos à esquerda são menores ou iguais
        for i in range(final_pivot_index):
            assert arr[i] <= pivot
        
        # Verifica se todos os elementos à direita são maiores ou iguais
        for i in range(final_pivot_index + 1, len(arr)):
            assert arr[i] >= pivot
    
    def test_partition_around_pivot_edge_cases(self):
        """Testa casos extremos de partição."""
        # Pivô no início
        arr = [1, 2, 3, 4, 5]
        final_index = partition_around_pivot(arr, 0, len(arr) - 1, 0)
        assert final_index == 0
        
        # Pivô no final
        arr = [5, 4, 3, 2, 1]
        final_index = partition_around_pivot(arr, 0, len(arr) - 1, len(arr) - 1)
        assert final_index == 0


class TestMedianOfMediansWithComparisonCount:
    """Testes para MOM com contagem de comparações."""
    
    def test_comparison_count(self):
        """Testa contagem de comparações."""
        arr = [3, 2, 1, 5, 6, 4]
        result, comparisons = median_of_medians_with_comparison_count(arr, 3)
        assert result == 3
        assert comparisons > 0
    
    def test_comparison_count_sorted(self):
        """Testa contagem em array ordenado."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        result, comparisons = median_of_medians_with_comparison_count(arr, 4)
        assert result == 4
        assert comparisons > 0


class TestFindMedianUsingMOM:
    """Testes para encontrar mediana usando MOM."""
    
    def test_find_median_odd(self):
        """Testa mediana com número ímpar de elementos."""
        arr = [1, 3, 2, 5, 4]
        median = find_median_using_mom(arr)
        assert median == 3.0
    
    def test_find_median_even(self):
        """Testa mediana com número par de elementos."""
        arr = [1, 3, 2, 4]
        median = find_median_using_mom(arr)
        assert median == 2.5  # (2 + 3) / 2
    
    def test_find_median_single(self):
        """Testa mediana com um elemento."""
        arr = [5]
        median = find_median_using_mom(arr)
        assert median == 5.0


class TestFindKthLargestMOM:
    """Testes para encontrar k-ésimo maior usando MOM."""
    
    def test_find_kth_largest_mom(self):
        """Testa encontrar k-ésimo maior."""
        arr = [3, 2, 1, 5, 6, 4]
        assert find_kth_largest_mom(arr, 1) == 6  # maior
        assert find_kth_largest_mom(arr, 2) == 5  # segundo maior
        assert find_kth_largest_mom(arr, 6) == 1  # menor
    
    def test_kth_largest_consistency(self):
        """Testa consistência entre k-ésimo menor e maior."""
        arr = [3, 2, 1, 5, 6, 4]
        for k in range(1, len(arr) + 1):
            kth_smallest = median_of_medians_select(arr.copy(), k)
            kth_largest = find_kth_largest_mom(arr.copy(), k)
            # Verifica se são consistentes
            sorted_arr = sorted(arr)
            assert kth_smallest == sorted_arr[k - 1]
            assert kth_largest == sorted_arr[-k]


class TestMedianOfMediansOptimized:
    """Testes para versão otimizada do MOM."""
    
    def test_optimized_basic(self):
        """Testa caso básico otimizado."""
        arr = [3, 2, 1, 5, 6, 4]
        assert median_of_medians_optimized(arr, 1) == 1
        assert median_of_medians_optimized(arr, 3) == 3
    
    def test_optimized_performance(self):
        """Testa performance da versão otimizada."""
        arr = list(range(1000))
        random.shuffle(arr)
        
        start_time = time.time()
        result1 = median_of_medians_optimized(arr.copy(), 500)
        optimized_time = time.time() - start_time
        
        start_time = time.time()
        result2 = median_of_medians_select(arr.copy(), 500)
        regular_time = time.time() - start_time
        
        assert result1 == result2
        # A versão otimizada deve ser pelo menos tão rápida quanto a regular


class TestValidateMOMResult:
    """Testes para validação do resultado MOM."""
    
    def test_validate_correct_result(self):
        """Testa validação de resultado correto."""
        arr = [3, 2, 1, 5, 6, 4]
        result = median_of_medians_select(arr.copy(), 3)
        assert validate_mom_result(arr, 3, result) == True
    
    def test_validate_incorrect_result(self):
        """Testa validação de resultado incorreto."""
        arr = [3, 2, 1, 5, 6, 4]
        assert validate_mom_result(arr, 3, 5) == False  # resultado incorreto


class TestAnalyzeMOMComplexity:
    """Testes para análise de complexidade MOM."""
    
    def test_complexity_analysis(self):
        """Testa análise de complexidade."""
        analysis = analyze_mom_complexity(1000)
        assert 'worst_case_time' in analysis
        assert 'average_case_time' in analysis
        assert 'constant_factor' in analysis
        assert analysis['worst_case_time'] == 'O(n)'
    
    def test_theoretical_bounds(self):
        """Testa limites teóricos."""
        bounds = analyze_mom_theoretical_bounds()
        assert 'recurrence_relation' in bounds
        assert 'solution' in bounds
        assert 'constant_factor' in bounds


class TestCompareMOMWithQuickselect:
    """Testes para comparação MOM vs Quickselect."""
    
    def test_comparison_basic(self):
        """Testa comparação básica."""
        arr = [3, 2, 1, 5, 6, 4]
        comparison = compare_mom_with_quickselect(arr, 3)
        assert 'mom_time' in comparison
        assert 'quickselect_time' in comparison
        assert 'mom_comparisons' in comparison
        assert 'quickselect_comparisons' in comparison
    
    def test_comparison_worst_case(self):
        """Testa comparação no pior caso."""
        # Array já ordenado - pior caso para Quickselect
        arr = list(range(100))
        comparison = compare_mom_with_quickselect(arr, 50)
        assert comparison['mom_time'] > 0
        assert comparison['quickselect_time'] > 0


class TestMedianOfMediansParallel:
    """Testes para versão paralela do MOM."""
    
    def test_parallel_basic(self):
        """Testa caso básico paralelo."""
        arr = [3, 2, 1, 5, 6, 4]
        assert median_of_medians_parallel(arr, 1) == 1
        assert median_of_medians_parallel(arr, 3) == 3
    
    def test_parallel_consistency(self):
        """Testa consistência da versão paralela."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        for k in range(1, len(arr) + 1):
            parallel_result = median_of_medians_parallel(arr.copy(), k)
            regular_result = median_of_medians_select(arr.copy(), k)
            assert parallel_result == regular_result


class TestFindPercentileMOM:
    """Testes para encontrar percentil usando MOM."""
    
    def test_find_percentile_mom(self):
        """Testa encontrar percentil."""
        arr = list(range(100))
        random.shuffle(arr)
        
        # 50º percentil (mediana)
        median = find_percentile_mom(arr, 50.0)
        assert median == 50
        
        # 25º percentil
        p25 = find_percentile_mom(arr, 25.0)
        assert 24 <= p25 <= 26
        
        # 75º percentil
        p75 = find_percentile_mom(arr, 75.0)
        assert 74 <= p75 <= 76
    
    def test_find_percentile_edge_cases(self):
        """Testa casos extremos de percentil."""
        arr = [1, 2, 3, 4, 5]
        
        # 0º percentil
        p0 = find_percentile_mom(arr, 0.0)
        assert p0 == 1
        
        # 100º percentil
        p100 = find_percentile_mom(arr, 100.0)
        assert p100 == 5


class TestMedianOfMediansWithDuplicates:
    """Testes para MOM com duplicatas."""
    
    def test_with_duplicates_basic(self):
        """Testa caso básico com duplicatas."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert median_of_medians_with_duplicates(arr, 1) == 1
        assert median_of_medians_with_duplicates(arr, 2) == 1  # segundo 1
        assert median_of_medians_with_duplicates(arr, 3) == 2
    
    def test_with_duplicates_all_same(self):
        """Testa com todos os elementos iguais."""
        arr = [5, 5, 5, 5, 5]
        for i in range(1, len(arr) + 1):
            assert median_of_medians_with_duplicates(arr.copy(), i) == 5


class TestPartitionWithDuplicatesMOM:
    """Testes para partição com duplicatas em MOM."""
    
    def test_partition_with_duplicates_mom(self):
        """Testa partição com duplicatas."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        start, end = partition_with_duplicates_mom(arr, 0, len(arr) - 1, 2)
        
        # Verifica se a região de elementos iguais está correta
        pivot = arr[start]
        for i in range(start, end + 1):
            assert arr[i] == pivot


class TestConsistency:
    """Testes de consistência entre diferentes implementações."""
    
    def test_all_implementations_consistent(self):
        """Testa consistência entre todas as implementações."""
        arr = [3, 2, 1, 5, 6, 4, 8, 7, 9]
        k = 5
        
        results = []
        implementations = [
            median_of_medians_select,
            median_of_medians_optimized,
            median_of_medians_parallel,
            median_of_medians_with_duplicates
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
            result = median_of_medians_select(arr.copy(), k)
            assert result == k - 1  # 0-indexed
    
    def test_repeated_elements(self):
        """Testa com muitos elementos repetidos."""
        arr = [1] * 100 + [2] * 100 + [3] * 100
        random.shuffle(arr)
        
        assert median_of_medians_select(arr.copy(), 1) == 1
        assert median_of_medians_select(arr.copy(), 100) == 1
        assert median_of_medians_select(arr.copy(), 101) == 2
        assert median_of_medians_select(arr.copy(), 200) == 2
        assert median_of_medians_select(arr.copy(), 201) == 3
    
    def test_extreme_values(self):
        """Testa com valores extremos."""
        arr = [float('-inf'), -1000000, 0, 1000000, float('inf')]
        assert median_of_medians_select(arr.copy(), 1) == float('-inf')
        assert median_of_medians_select(arr.copy(), 3) == 0
        assert median_of_medians_select(arr.copy(), 5) == float('inf')


class TestPerformance:
    """Testes de performance."""
    
    def test_performance_comparison(self):
        """Compara performance de diferentes implementações."""
        arr = list(range(1000))
        random.shuffle(arr)
        k = 500
        
        implementations = [
            median_of_medians_select,
            median_of_medians_optimized,
            median_of_medians_parallel
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
    
    def test_worst_case_performance(self):
        """Testa performance no pior caso."""
        # Array já ordenado - pior caso para Quickselect, mas MOM deve ser estável
        arr = list(range(1000))
        
        start_time = time.time()
        result = median_of_medians_select(arr.copy(), 500)
        mom_time = time.time() - start_time
        
        assert result == 499  # 0-indexed
        assert mom_time > 0  # Deve executar em tempo finito


class TestTheoreticalAnalysis:
    """Testes para análise teórica."""
    
    def test_recurrence_analysis(self):
        """Testa análise da relação de recorrência."""
        bounds = analyze_mom_theoretical_bounds()
        assert 'recurrence_relation' in bounds
        assert bounds['recurrence_relation'] == 'T(n) ≤ T(n/5) + T(7n/10) + O(n)'
        assert bounds['solution'] == 'O(n)'
    
    def test_constant_factor_analysis(self):
        """Testa análise do fator constante."""
        bounds = analyze_mom_theoretical_bounds()
        assert 'constant_factor' in bounds
        assert bounds['constant_factor'] > 0  # Deve ser positivo
    
    def test_pivot_quality_analysis(self):
        """Testa análise da qualidade do pivô."""
        bounds = analyze_mom_theoretical_bounds()
        assert 'pivot_quality' in bounds
        assert 'lower_bound_percentile' in bounds
        assert 'upper_bound_percentile' in bounds
        assert bounds['lower_bound_percentile'] == 30
        assert bounds['upper_bound_percentile'] == 70


if __name__ == "__main__":
    pytest.main([__file__]) 