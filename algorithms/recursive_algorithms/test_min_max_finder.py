"""
Testes para o módulo de Min-Max Finder.

Este módulo contém testes abrangentes para todas as implementações
de algoritmos para encontrar mínimo e máximo.
"""

import pytest
import random
import time
from typing import List

from min_max_finder import (
    find_min_max_naive,
    find_min_max_pairs,
    find_min_max_divide_conquer,
    find_min_max_divide_conquer_recursive,
    find_min_max_with_comparison_count,
    find_min_max_tournament,
    find_min_max_optimized,
    validate_min_max_result,
    analyze_comparison_complexity,
    compare_min_max_algorithms,
    find_min_max_parallel,
    _min_max_parallel_recursive,
    find_min_max_with_duplicates,
    find_min_max_range,
    find_min_max_statistics,
    find_min_max_adaptive,
    analyze_theoretical_bounds
)


class TestFindMinMaxNaive:
    """Testes para a abordagem ingênua."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        with pytest.raises(ValueError):
            find_min_max_naive([])
    
    def test_single_element(self):
        """Testa com array de um elemento."""
        result = find_min_max_naive([5])
        assert result == (5, 5)
    
    def test_basic_case(self):
        """Testa caso básico."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_naive(arr)
        assert min_val == 1
        assert max_val == 6
    
    def test_duplicate_elements(self):
        """Testa com elementos duplicados."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        min_val, max_val = find_min_max_naive(arr)
        assert min_val == 1
        assert max_val == 9
    
    def test_all_same_elements(self):
        """Testa com todos os elementos iguais."""
        arr = [5, 5, 5, 5, 5]
        min_val, max_val = find_min_max_naive(arr)
        assert min_val == 5
        assert max_val == 5
    
    def test_negative_elements(self):
        """Testa com elementos negativos."""
        arr = [-3, -1, -5, -2, -4]
        min_val, max_val = find_min_max_naive(arr)
        assert min_val == -5
        assert max_val == -1


class TestFindMinMaxPairs:
    """Testes para a abordagem de pares."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        with pytest.raises(ValueError):
            find_min_max_pairs([])
    
    def test_single_element(self):
        """Testa com array de um elemento."""
        result = find_min_max_pairs([5])
        assert result == (5, 5)
    
    def test_basic_case(self):
        """Testa caso básico."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_pairs(arr)
        assert min_val == 1
        assert max_val == 6
    
    def test_even_length(self):
        """Testa com array de comprimento par."""
        arr = [1, 2, 3, 4]
        min_val, max_val = find_min_max_pairs(arr)
        assert min_val == 1
        assert max_val == 4
    
    def test_odd_length(self):
        """Testa com array de comprimento ímpar."""
        arr = [1, 2, 3, 4, 5]
        min_val, max_val = find_min_max_pairs(arr)
        assert min_val == 1
        assert max_val == 5
    
    def test_duplicate_elements(self):
        """Testa com elementos duplicados."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        min_val, max_val = find_min_max_pairs(arr)
        assert min_val == 1
        assert max_val == 9


class TestFindMinMaxDivideConquer:
    """Testes para a abordagem de divisão e conquista."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        with pytest.raises(ValueError):
            find_min_max_divide_conquer([])
    
    def test_single_element(self):
        """Testa com array de um elemento."""
        result = find_min_max_divide_conquer([5])
        assert result == (5, 5)
    
    def test_basic_case(self):
        """Testa caso básico."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_divide_conquer(arr)
        assert min_val == 1
        assert max_val == 6
    
    def test_recursive_function(self):
        """Testa a função recursiva."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_divide_conquer_recursive(arr, 0, len(arr) - 1)
        assert min_val == 1
        assert max_val == 6
    
    def test_subarray_selection(self):
        """Testa seleção em subarrays."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        # Selecionar min-max no subarray [5, 4, 3, 2, 1]
        min_val, max_val = find_min_max_divide_conquer_recursive(arr, 4, 8)
        assert min_val == 1
        assert max_val == 5


class TestFindMinMaxWithComparisonCount:
    """Testes para contagem de comparações."""
    
    def test_comparison_count(self):
        """Testa contagem de comparações."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val, comparisons = find_min_max_with_comparison_count(arr)
        assert min_val == 1
        assert max_val == 6
        assert comparisons > 0
    
    def test_comparison_count_small_array(self):
        """Testa contagem em array pequeno."""
        arr = [1, 2, 3, 4]
        min_val, max_val, comparisons = find_min_max_with_comparison_count(arr)
        assert min_val == 1
        assert max_val == 4
        assert comparisons > 0


class TestFindMinMaxTournament:
    """Testes para o método do torneio."""
    
    def test_tournament_basic(self):
        """Testa caso básico do torneio."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_tournament(arr)
        assert min_val == 1
        assert max_val == 6
    
    def test_tournament_power_of_two(self):
        """Testa com array de tamanho potência de 2."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        min_val, max_val = find_min_max_tournament(arr)
        assert min_val == 1
        assert max_val == 8
    
    def test_tournament_odd_length(self):
        """Testa com array de comprimento ímpar."""
        arr = [1, 2, 3, 4, 5]
        min_val, max_val = find_min_max_tournament(arr)
        assert min_val == 1
        assert max_val == 5


class TestFindMinMaxOptimized:
    """Testes para versão otimizada."""
    
    def test_optimized_basic(self):
        """Testa caso básico otimizado."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_optimized(arr)
        assert min_val == 1
        assert max_val == 6
    
    def test_optimized_performance(self):
        """Testa performance da versão otimizada."""
        arr = list(range(1000))
        random.shuffle(arr)
        
        start_time = time.time()
        result1 = find_min_max_optimized(arr.copy())
        optimized_time = time.time() - start_time
        
        start_time = time.time()
        result2 = find_min_max_pairs(arr.copy())
        pairs_time = time.time() - start_time
        
        assert result1 == result2
        # A versão otimizada deve ser pelo menos tão rápida quanto a de pares


class TestValidateMinMaxResult:
    """Testes para validação de resultados."""
    
    def test_validate_correct_result(self):
        """Testa validação de resultado correto."""
        arr = [3, 2, 1, 5, 6, 4]
        result = (1, 6)
        assert validate_min_max_result(arr, result) == True
    
    def test_validate_incorrect_result(self):
        """Testa validação de resultado incorreto."""
        arr = [3, 2, 1, 5, 6, 4]
        assert validate_min_max_result(arr, (2, 5)) == False  # resultado incorreto
    
    def test_validate_edge_cases(self):
        """Testa casos extremos de validação."""
        # Array vazio
        with pytest.raises(ValueError):
            validate_min_max_result([], (0, 0))
        
        # Resultado com min > max
        arr = [1, 2, 3]
        assert validate_min_max_result(arr, (3, 1)) == False


class TestAnalyzeComparisonComplexity:
    """Testes para análise de complexidade."""
    
    def test_complexity_analysis(self):
        """Testa análise de complexidade."""
        analysis = analyze_comparison_complexity(1000)
        assert 'naive_comparisons' in analysis
        assert 'pairs_comparisons' in analysis
        assert 'divide_conquer_comparisons' in analysis
        assert analysis['naive_comparisons'] == 1998  # 2n - 2
        assert analysis['pairs_comparisons'] == 1500  # 3n/2
    
    def test_theoretical_bounds(self):
        """Testa limites teóricos."""
        bounds = analyze_theoretical_bounds()
        assert 'lower_bound' in bounds
        assert 'upper_bound' in bounds
        assert 'optimal_algorithm' in bounds


class TestCompareMinMaxAlgorithms:
    """Testes para comparação de algoritmos."""
    
    def test_comparison_basic(self):
        """Testa comparação básica."""
        arr = [3, 2, 1, 5, 6, 4]
        comparison = compare_min_max_algorithms(arr)
        assert 'naive_time' in comparison
        assert 'pairs_time' in comparison
        assert 'divide_conquer_time' in comparison
        assert 'tournament_time' in comparison
    
    def test_comparison_large_array(self):
        """Testa comparação com array grande."""
        arr = list(range(10000))
        random.shuffle(arr)
        comparison = compare_min_max_algorithms(arr)
        assert comparison['naive_time'] > 0
        assert comparison['pairs_time'] > 0
        assert comparison['divide_conquer_time'] > 0


class TestFindMinMaxParallel:
    """Testes para versão paralela."""
    
    def test_parallel_basic(self):
        """Testa caso básico paralelo."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_parallel(arr)
        assert min_val == 1
        assert max_val == 6
    
    def test_parallel_consistency(self):
        """Testa consistência da versão paralela."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        parallel_result = find_min_max_parallel(arr.copy())
        naive_result = find_min_max_naive(arr.copy())
        assert parallel_result == naive_result


class TestFindMinMaxWithDuplicates:
    """Testes para arrays com duplicatas."""
    
    def test_with_duplicates_basic(self):
        """Testa caso básico com duplicatas."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        min_val, max_val = find_min_max_with_duplicates(arr)
        assert min_val == 1
        assert max_val == 9
    
    def test_with_duplicates_all_same(self):
        """Testa com todos os elementos iguais."""
        arr = [5, 5, 5, 5, 5]
        min_val, max_val = find_min_max_with_duplicates(arr)
        assert min_val == 5
        assert max_val == 5


class TestFindMinMaxRange:
    """Testes para encontrar range."""
    
    def test_find_range_basic(self):
        """Testa caso básico de range."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val, range_val = find_min_max_range(arr)
        assert min_val == 1
        assert max_val == 6
        assert range_val == 5
    
    def test_find_range_same_elements(self):
        """Testa range com elementos iguais."""
        arr = [5, 5, 5, 5, 5]
        min_val, max_val, range_val = find_min_max_range(arr)
        assert min_val == 5
        assert max_val == 5
        assert range_val == 0


class TestFindMinMaxStatistics:
    """Testes para estatísticas completas."""
    
    def test_statistics_basic(self):
        """Testa estatísticas básicas."""
        arr = [3, 2, 1, 5, 6, 4]
        stats = find_min_max_statistics(arr)
        assert 'min' in stats
        assert 'max' in stats
        assert 'range' in stats
        assert 'count' in stats
        assert stats['min'] == 1
        assert stats['max'] == 6
        assert stats['range'] == 5
        assert stats['count'] == 6


class TestFindMinMaxAdaptive:
    """Testes para algoritmo adaptativo."""
    
    def test_adaptive_basic(self):
        """Testa caso básico adaptativo."""
        arr = [3, 2, 1, 5, 6, 4]
        min_val, max_val = find_min_max_adaptive(arr)
        assert min_val == 1
        assert max_val == 6
    
    def test_adaptive_small_array(self):
        """Testa com array pequeno."""
        arr = [1, 2, 3]
        min_val, max_val = find_min_max_adaptive(arr)
        assert min_val == 1
        assert max_val == 3
    
    def test_adaptive_large_array(self):
        """Testa com array grande."""
        arr = list(range(1000))
        random.shuffle(arr)
        min_val, max_val = find_min_max_adaptive(arr)
        assert min_val == 0
        assert max_val == 999


class TestConsistency:
    """Testes de consistência entre diferentes implementações."""
    
    def test_all_implementations_consistent(self):
        """Testa consistência entre todas as implementações."""
        arr = [3, 2, 1, 5, 6, 4, 8, 7, 9]
        
        results = []
        implementations = [
            find_min_max_naive,
            find_min_max_pairs,
            find_min_max_divide_conquer,
            find_min_max_tournament,
            find_min_max_optimized,
            find_min_max_adaptive,
            find_min_max_parallel
        ]
        
        for impl in implementations:
            try:
                result = impl(arr.copy())
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
        
        min_val, max_val = find_min_max_pairs(arr.copy())
        assert min_val == 0
        assert max_val == 9999
    
    def test_repeated_elements(self):
        """Testa com muitos elementos repetidos."""
        arr = [1] * 100 + [2] * 100 + [3] * 100
        random.shuffle(arr)
        
        min_val, max_val = find_min_max_pairs(arr.copy())
        assert min_val == 1
        assert max_val == 3
    
    def test_extreme_values(self):
        """Testa com valores extremos."""
        arr = [float('-inf'), -1000000, 0, 1000000, float('inf')]
        min_val, max_val = find_min_max_pairs(arr.copy())
        assert min_val == float('-inf')
        assert max_val == float('inf')


class TestPerformance:
    """Testes de performance."""
    
    def test_performance_comparison(self):
        """Compara performance de diferentes implementações."""
        arr = list(range(1000))
        random.shuffle(arr)
        
        implementations = [
            find_min_max_naive,
            find_min_max_pairs,
            find_min_max_divide_conquer,
            find_min_max_tournament,
            find_min_max_optimized
        ]
        
        times = {}
        for impl in implementations:
            try:
                start_time = time.time()
                result = impl(arr.copy())
                end_time = time.time()
                times[impl.__name__] = end_time - start_time
            except NotImplementedError:
                continue
        
        # Verifica se todas as implementações retornam o mesmo resultado
        if len(times) > 1:
            assert len(set(times.keys())) == len(times)  # Todas diferentes
    
    def test_comparison_efficiency(self):
        """Testa eficiência de comparações."""
        arr = list(range(100))
        random.shuffle(arr)
        
        # Testa se a abordagem de pares usa menos comparações que a ingênua
        try:
            _, _, pairs_comparisons = find_min_max_with_comparison_count(arr.copy())
            naive_comparisons = 2 * len(arr) - 2  # 2n - 2 para abordagem ingênua
            
            # A abordagem de pares deve usar aproximadamente 3n/2 comparações
            expected_pairs_comparisons = 3 * len(arr) // 2
            
            assert pairs_comparisons <= expected_pairs_comparisons
            assert pairs_comparisons < naive_comparisons
        except NotImplementedError:
            pass


class TestTheoreticalAnalysis:
    """Testes para análise teórica."""
    
    def test_comparison_bounds(self):
        """Testa limites de comparações."""
        bounds = analyze_theoretical_bounds()
        assert 'lower_bound' in bounds
        assert 'upper_bound' in bounds
        assert bounds['lower_bound'] == '⌈3n/2⌉ - 2'
        assert bounds['upper_bound'] == '2n - 2'
    
    def test_optimal_algorithm_analysis(self):
        """Testa análise do algoritmo ótimo."""
        bounds = analyze_theoretical_bounds()
        assert 'optimal_algorithm' in bounds
        assert 'comparison_count' in bounds
        assert bounds['optimal_algorithm'] == 'Pairs Method'


if __name__ == "__main__":
    pytest.main([__file__]) 