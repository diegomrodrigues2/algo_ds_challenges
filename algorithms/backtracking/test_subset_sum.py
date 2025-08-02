"""
Testes para o algoritmo Subset Sum usando backtracking.

Este módulo testa todas as implementações do algoritmo Subset Sum,
incluindo casos básicos, otimizações, contagem de soluções e análise
de complexidade.
"""

import pytest
import time
from typing import List, Optional

from subset_sum import (
    subset_sum_backtracking,
    subset_sum_backtracking_optimized,
    subset_sum_count_solutions,
    subset_sum_all_solutions,
    analyze_subset_sum_complexity,
    subset_sum_with_memoization
)


class TestSubsetSumBasic:
    """Testes para a implementação básica do Subset Sum."""
    
    def test_basic_subset_sum(self):
        """Testa casos básicos do Subset Sum."""
        # Caso simples com solução
        numbers = [1, 2, 3, 4, 5]
        target = 7
        result = subset_sum_backtracking(numbers, target)
        assert result is not None
        assert sum(result) == target
        
        # Caso sem solução
        numbers = [1, 2, 3, 4, 5]
        target = 20
        result = subset_sum_backtracking(numbers, target)
        assert result is None
    
    def test_empty_input(self):
        """Testa entrada vazia."""
        result = subset_sum_backtracking([], 5)
        assert result is None
        
        result = subset_sum_backtracking([1, 2, 3], -1)
        assert result is None
    
    def test_single_element(self):
        """Testa casos com um único elemento."""
        # Target igual ao elemento
        result = subset_sum_backtracking([5], 5)
        assert result == [5]
        
        # Target diferente do elemento
        result = subset_sum_backtracking([5], 3)
        assert result is None
    
    def test_target_zero(self):
        """Testa target igual a zero."""
        result = subset_sum_backtracking([1, 2, 3], 0)
        assert result == []
    
    def test_duplicate_elements(self):
        """Testa elementos duplicados."""
        numbers = [1, 1, 2, 2, 3]
        target = 4
        result = subset_sum_backtracking(numbers, target)
        assert result is not None
        assert sum(result) == target


class TestSubsetSumOptimized:
    """Testes para a versão otimizada do Subset Sum."""
    
    def test_optimized_basic(self):
        """Testa casos básicos da versão otimizada."""
        numbers = [3, 34, 4, 12, 5, 2]
        target = 9
        result = subset_sum_backtracking_optimized(numbers, target)
        assert result is not None
        assert sum(result) == target
    
    def test_optimized_no_solution(self):
        """Testa caso sem solução na versão otimizada."""
        numbers = [10, 20, 30, 40, 50]
        target = 200  # Maior que a soma total
        result = subset_sum_backtracking_optimized(numbers, target)
        assert result is None
    
    def test_optimized_target_equals_total(self):
        """Testa quando target é igual à soma total."""
        numbers = [1, 2, 3, 4, 5]
        target = 15
        result = subset_sum_backtracking_optimized(numbers, target)
        assert result == [5, 4, 3, 2, 1]  # Ordem decrescente
    
    def test_optimized_duplicates(self):
        """Testa remoção de duplicatas na versão otimizada."""
        numbers = [1, 1, 2, 2, 3, 3]
        target = 6
        result = subset_sum_backtracking_optimized(numbers, target)
        assert result is not None
        assert sum(result) == target


class TestSubsetSumCountSolutions:
    """Testes para contagem de soluções."""
    
    def test_count_basic(self):
        """Testa contagem básica de soluções."""
        numbers = [1, 2, 3, 4, 5]
        target = 7
        count = subset_sum_count_solutions(numbers, target)
        assert count > 0
        
        # Verifica se há pelo menos uma solução
        solutions = subset_sum_all_solutions(numbers, target)
        assert len(solutions) == count
    
    def test_count_no_solutions(self):
        """Testa contagem quando não há soluções."""
        numbers = [1, 2, 3, 4, 5]
        target = 20
        count = subset_sum_count_solutions(numbers, target)
        assert count == 0
    
    def test_count_multiple_solutions(self):
        """Testa casos com múltiplas soluções."""
        numbers = [1, 1, 2, 2, 3]
        target = 3
        count = subset_sum_count_solutions(numbers, target)
        assert count > 1  # Deve ter múltiplas soluções
    
    def test_count_target_zero(self):
        """Testa contagem com target zero."""
        numbers = [1, 2, 3]
        target = 0
        count = subset_sum_count_solutions(numbers, target)
        assert count == 1  # Apenas o conjunto vazio


class TestSubsetSumAllSolutions:
    """Testes para encontrar todas as soluções."""
    
    def test_all_solutions_basic(self):
        """Testa encontrar todas as soluções."""
        numbers = [1, 2, 3, 4, 5]
        target = 7
        solutions = subset_sum_all_solutions(numbers, target)
        
        assert len(solutions) > 0
        for solution in solutions:
            assert sum(solution) == target
    
    def test_all_solutions_no_solutions(self):
        """Testa quando não há soluções."""
        numbers = [1, 2, 3, 4, 5]
        target = 20
        solutions = subset_sum_all_solutions(numbers, target)
        assert len(solutions) == 0
    
    def test_all_solutions_unique(self):
        """Testa se todas as soluções são únicas."""
        numbers = [1, 1, 2, 2, 3]
        target = 3
        solutions = subset_sum_all_solutions(numbers, target)
        
        # Converte para tuplas para verificar unicidade
        solution_tuples = [tuple(sorted(sol)) for sol in solutions]
        unique_solutions = set(solution_tuples)
        assert len(unique_solutions) == len(solutions)


class TestSubsetSumMemoization:
    """Testes para a versão com memoização."""
    
    def test_memoization_basic(self):
        """Testa casos básicos da versão com memoização."""
        numbers = [3, 34, 4, 12, 5, 2]
        target = 9
        result = subset_sum_with_memoization(numbers, target)
        assert result is not None
        assert sum(result) == target
    
    def test_memoization_consistency(self):
        """Testa consistência entre versões."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 15
        
        result1 = subset_sum_backtracking(numbers, target)
        result2 = subset_sum_with_memoization(numbers, target)
        
        if result1 is not None:
            assert result2 is not None
            assert sum(result1) == sum(result2)
        else:
            assert result2 is None


class TestSubsetSumComplexityAnalysis:
    """Testes para análise de complexidade."""
    
    def test_complexity_analysis_basic(self):
        """Testa análise básica de complexidade."""
        numbers = [1, 2, 3, 4, 5]
        target = 7
        analysis = analyze_subset_sum_complexity(numbers, target)
        
        assert 'n' in analysis
        assert 'target' in analysis
        assert 'total_sum' in analysis
        assert 'max_possible_subsets' in analysis
        assert analysis['n'] == len(numbers)
        assert analysis['target'] == target
        assert analysis['total_sum'] == sum(numbers)
        assert analysis['max_possible_subsets'] == 2 ** len(numbers)
    
    def test_complexity_analysis_feasibility(self):
        """Testa análise de viabilidade."""
        numbers = [1, 2, 3, 4, 5]
        target = 15  # Viável
        analysis = analyze_subset_sum_complexity(numbers, target)
        assert analysis['is_feasible'] == True
        
        target = 20  # Não viável
        analysis = analyze_subset_sum_complexity(numbers, target)
        assert analysis['is_feasible'] == False
    
    def test_complexity_analysis_pruning(self):
        """Testa análise de oportunidades de poda."""
        numbers = [10, 20, 30, 40, 50]
        target = 25
        analysis = analyze_subset_sum_complexity(numbers, target)
        assert 'pruning_opportunities' in analysis


class TestSubsetSumEdgeCases:
    """Testes para casos extremos."""
    
    def test_large_numbers(self):
        """Testa com números grandes."""
        numbers = [1000000, 2000000, 3000000, 4000000, 5000000]
        target = 6000000
        result = subset_sum_backtracking(numbers, target)
        if result is not None:
            assert sum(result) == target
    
    def test_repeated_elements(self):
        """Testa com muitos elementos repetidos."""
        numbers = [1] * 10 + [2] * 10 + [3] * 10
        target = 15
        result = subset_sum_backtracking(numbers, target)
        if result is not None:
            assert sum(result) == target
    
    def test_extreme_values(self):
        """Testa valores extremos."""
        numbers = [1, 999999, 1000000]
        target = 1000000
        result = subset_sum_backtracking(numbers, target)
        if result is not None:
            assert sum(result) == target


class TestSubsetSumPerformance:
    """Testes de performance."""
    
    def test_performance_small_input(self):
        """Testa performance com entrada pequena."""
        numbers = list(range(1, 21))  # 1 a 20
        target = 50
        
        start_time = time.time()
        result = subset_sum_backtracking(numbers, target)
        end_time = time.time()
        
        assert end_time - start_time < 1.0  # Deve ser rápido
        if result is not None:
            assert sum(result) == target
    
    def test_performance_medium_input(self):
        """Testa performance com entrada média."""
        numbers = list(range(1, 31))  # 1 a 30
        target = 100
        
        start_time = time.time()
        result = subset_sum_backtracking_optimized(numbers, target)
        end_time = time.time()
        
        # Deve ser aceitável para entrada média
        assert end_time - start_time < 5.0
        if result is not None:
            assert sum(result) == target
    
    def test_performance_comparison(self):
        """Compara performance entre versões."""
        numbers = list(range(1, 21))
        target = 50
        
        # Versão básica
        start_time = time.time()
        result1 = subset_sum_backtracking(numbers, target)
        time1 = time.time() - start_time
        
        # Versão otimizada
        start_time = time.time()
        result2 = subset_sum_backtracking_optimized(numbers, target)
        time2 = time.time() - start_time
        
        # Ambas devem retornar o mesmo resultado
        if result1 is not None:
            assert result2 is not None
            assert sum(result1) == sum(result2)
        else:
            assert result2 is None


class TestSubsetSumCorrectness:
    """Testes de correção abrangentes."""
    
    def test_correctness_multiple_implementations(self):
        """Testa correção entre múltiplas implementações."""
        test_cases = [
            ([1, 2, 3, 4, 5], 7),
            ([3, 34, 4, 12, 5, 2], 9),
            ([1, 2, 3, 4, 5], 15),
            ([1, 1, 1, 1, 1], 3),
            ([10, 20, 30, 40, 50], 100),
            ([1, 2, 3, 4, 5], 20),  # Sem solução
        ]
        
        for numbers, target in test_cases:
            # Testa todas as implementações
            implementations = [
                subset_sum_backtracking,
                subset_sum_backtracking_optimized,
                subset_sum_with_memoization
            ]
            
            results = []
            for impl in implementations:
                result = impl(numbers, target)
                results.append(result)
            
            # Todas devem retornar o mesmo resultado
            for i in range(1, len(results)):
                if results[0] is not None:
                    assert results[i] is not None
                    assert sum(results[0]) == sum(results[i])
                else:
                    assert results[i] is None
    
    def test_correctness_special_cases(self):
        """Testa casos especiais."""
        # Conjunto vazio
        assert subset_sum_backtracking([], 5) is None
        
        # Target zero
        assert subset_sum_backtracking([1, 2, 3], 0) == []
        
        # Target negativo
        assert subset_sum_backtracking([1, 2, 3], -1) is None
        
        # Um elemento
        assert subset_sum_backtracking([5], 5) == [5]
        assert subset_sum_backtracking([5], 3) is None


if __name__ == "__main__":
    # Executa os testes
    pytest.main([__file__, "-v"]) 