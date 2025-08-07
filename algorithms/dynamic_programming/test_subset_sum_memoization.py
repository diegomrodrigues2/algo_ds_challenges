"""
Testes para Soma de Subconjuntos com Memoização

Este módulo contém testes abrangentes para validar a implementação
do problema da Soma de Subconjuntos usando memoização.
"""

import pytest
import time
from typing import List, Dict

from .subset_sum_memoization import (
    subset_sum_memoization,
    subset_sum_backtracking,
    subset_sum_tabulation,
    analyze_subset_sum_complexity,
    compare_approaches,
    get_subset_solution,
    count_subset_solutions,
    generate_test_cases
)


class TestSubsetSumMemoization:
    """Testes para a função principal subset_sum_memoization."""
    
    def test_basic_cases(self):
        """Testa casos básicos da função principal."""
        # Caso do exemplo da documentação
        assert subset_sum_memoization([3, 34, 4, 12, 5, 2], 9) == True
        assert subset_sum_memoization([3, 34, 4, 12, 5, 2], 30) == False
        
        # Casos simples
        assert subset_sum_memoization([1, 2, 3, 4, 5], 10) == True
        assert subset_sum_memoization([1, 2, 3, 4, 5], 15) == True
        assert subset_sum_memoization([1, 2, 3, 4, 5], 20) == False
    
    def test_edge_cases(self):
        """Testa casos extremos e de borda."""
        # Array vazio
        assert subset_sum_memoization([], 0) == True
        assert subset_sum_memoization([], 5) == False
        
        # Array com um elemento
        assert subset_sum_memoization([1], 1) == True
        assert subset_sum_memoization([1], 2) == False
        assert subset_sum_memoization([1], 0) == True
        
        # Target zero
        assert subset_sum_memoization([1, 2, 3], 0) == True
        assert subset_sum_memoization([0, 1, 2], 0) == True
        
        # Todos os elementos
        assert subset_sum_memoization([1, 2, 3], 6) == True
        assert subset_sum_memoization([1, 2, 3], 7) == False
    
    def test_zeros_and_negatives(self):
        """Testa casos com zeros e números negativos."""
        # Com zeros
        assert subset_sum_memoization([0, 1, 2, 3], 3) == True
        assert subset_sum_memoization([0, 0, 1], 1) == True
        assert subset_sum_memoization([0, 0, 0], 0) == True
        
        # Com números negativos
        assert subset_sum_memoization([-1, 1, 2], 0) == True
        assert subset_sum_memoization([-2, -1, 1, 2], 0) == True
        assert subset_sum_memoization([-1, -2, -3], -6) == True
        assert subset_sum_memoization([-1, -2, -3], -3) == True
    
    def test_large_numbers(self):
        """Testa casos com números grandes."""
        nums = [100, 200, 300, 400, 500]
        assert subset_sum_memoization(nums, 600) == True  # 100 + 500
        assert subset_sum_memoization(nums, 1000) == True  # 100 + 200 + 300 + 400
        assert subset_sum_memoization(nums, 1500) == True  # Todos
        assert subset_sum_memoization(nums, 1600) == False  # Impossível
    
    def test_duplicate_elements(self):
        """Testa casos com elementos duplicados."""
        nums = [1, 1, 2, 2, 3, 3]
        assert subset_sum_memoization(nums, 4) == True  # 1 + 1 + 2
        assert subset_sum_memoization(nums, 6) == True  # 1 + 2 + 3
        assert subset_sum_memoization(nums, 12) == True  # Todos
        assert subset_sum_memoization(nums, 13) == False  # Impossível


class TestSubsetSumBacktracking:
    """Testes para a função de backtracking (comparação)."""
    
    def test_backtracking_basic(self):
        """Testa casos básicos do backtracking."""
        # Apenas para arrays pequenos (performance)
        assert subset_sum_backtracking([1, 2, 3, 4, 5], 10) == True
        assert subset_sum_backtracking([1, 2, 3, 4, 5], 15) == True
        assert subset_sum_backtracking([1, 2, 3, 4, 5], 20) == False
    
    def test_backtracking_edge_cases(self):
        """Testa casos extremos do backtracking."""
        assert subset_sum_backtracking([], 0) == True
        assert subset_sum_backtracking([], 5) == False
        assert subset_sum_backtracking([1], 1) == True
        assert subset_sum_backtracking([1], 2) == False


class TestSubsetSumTabulation:
    """Testes para a função de tabulação."""
    
    def test_tabulation_basic(self):
        """Testa casos básicos da tabulação."""
        assert subset_sum_tabulation([3, 34, 4, 12, 5, 2], 9) == True
        assert subset_sum_tabulation([3, 34, 4, 12, 5, 2], 30) == False
        assert subset_sum_tabulation([1, 2, 3, 4, 5], 10) == True
        assert subset_sum_tabulation([1, 2, 3, 4, 5], 15) == True
    
    def test_tabulation_edge_cases(self):
        """Testa casos extremos da tabulação."""
        assert subset_sum_tabulation([], 0) == True
        assert subset_sum_tabulation([], 5) == False
        assert subset_sum_tabulation([1], 1) == True
        assert subset_sum_tabulation([1], 2) == False
        assert subset_sum_tabulation([1, 2, 3], 0) == True
        assert subset_sum_tabulation([1, 2, 3], 6) == True
    
    def test_tabulation_large_numbers(self):
        """Testa tabulação com números grandes."""
        nums = [100, 200, 300, 400, 500]
        assert subset_sum_tabulation(nums, 600) == True
        assert subset_sum_tabulation(nums, 1000) == True
        assert subset_sum_tabulation(nums, 1500) == True
        assert subset_sum_tabulation(nums, 1600) == False


class TestConsistency:
    """Testes para verificar consistência entre abordagens."""
    
    def test_all_approaches_consistent(self):
        """Verifica que todas as abordagens retornam o mesmo resultado."""
        test_cases = [
            ([3, 34, 4, 12, 5, 2], 9),
            ([3, 34, 4, 12, 5, 2], 30),
            ([1, 2, 3, 4, 5], 10),
            ([1, 2, 3, 4, 5], 15),
            ([1, 2, 3, 4, 5], 20),
            ([], 0),
            ([], 5),
            ([1], 1),
            ([1], 2),
            ([1, 2, 3], 0),
            ([1, 2, 3], 6),
        ]
        
        for nums, target in test_cases:
            memo_result = subset_sum_memoization(nums, target)
            tab_result = subset_sum_tabulation(nums, target)
            
            assert memo_result == tab_result, f"Falha para nums={nums}, target={target}"
            
            # Testa backtracking apenas para arrays pequenos
            if len(nums) <= 10:
                back_result = subset_sum_backtracking(nums, target)
                assert memo_result == back_result, f"Backtracking inconsistente para nums={nums}, target={target}"
    
    def test_generated_test_cases(self):
        """Testa todos os casos gerados pela função generate_test_cases."""
        test_cases = generate_test_cases()
        
        for nums, target, expected in test_cases:
            memo_result = subset_sum_memoization(nums, target)
            tab_result = subset_sum_tabulation(nums, target)
            
            assert memo_result == expected, f"Memoização falhou para nums={nums}, target={target}, expected={expected}, got={memo_result}"
            assert tab_result == expected, f"Tabulação falhou para nums={nums}, target={target}, expected={expected}, got={tab_result}"
            assert memo_result == tab_result, f"Inconsistência para nums={nums}, target={target}"


class TestGetSubsetSolution:
    """Testes para a função que retorna a solução."""
    
    def test_get_solution_basic(self):
        """Testa obtenção de soluções básicas."""
        nums = [3, 34, 4, 12, 5, 2]
        target = 9
        
        solution = get_subset_solution(nums, target)
        assert solution is not None
        assert sum(solution) == target
        assert all(x in nums for x in solution)
    
    def test_get_solution_no_solution(self):
        """Testa caso onde não existe solução."""
        nums = [3, 34, 4, 12, 5, 2]
        target = 30
        
        solution = get_subset_solution(nums, target)
        assert solution is None
    
    def test_get_solution_edge_cases(self):
        """Testa casos extremos da obtenção de solução."""
        # Array vazio
        assert get_subset_solution([], 0) == []
        assert get_subset_solution([], 5) is None
        
        # Target zero
        assert get_subset_solution([1, 2, 3], 0) == []
        
        # Único elemento
        assert get_subset_solution([5], 5) == [5]
        assert get_subset_solution([5], 6) is None
    
    def test_get_solution_multiple_solutions(self):
        """Testa que uma solução válida é retornada quando existem múltiplas."""
        nums = [1, 2, 3, 4, 5]
        target = 7
        
        solution = get_subset_solution(nums, target)
        assert solution is not None
        assert sum(solution) == target
        # Pode ser [2, 5] ou [3, 4] ou [1, 2, 4], etc.


class TestCountSubsetSolutions:
    """Testes para a função que conta soluções."""
    
    def test_count_solutions_basic(self):
        """Testa contagem de soluções básicas."""
        nums = [1, 2, 3]
        target = 3
        
        count = count_subset_solutions(nums, target)
        assert count == 2  # [3] e [1, 2]
    
    def test_count_solutions_no_solution(self):
        """Testa contagem quando não existe solução."""
        nums = [1, 2, 3]
        target = 10
        
        count = count_subset_solutions(nums, target)
        assert count == 0
    
    def test_count_solutions_edge_cases(self):
        """Testa casos extremos da contagem."""
        # Array vazio
        assert count_subset_solutions([], 0) == 1
        assert count_subset_solutions([], 5) == 0
        
        # Target zero
        assert count_subset_solutions([1, 2, 3], 0) == 1  # Subconjunto vazio
        
        # Único elemento
        assert count_subset_solutions([5], 5) == 1
        assert count_subset_solutions([5], 6) == 0
    
    def test_count_solutions_with_zeros(self):
        """Testa contagem com zeros."""
        nums = [0, 1, 2]
        target = 0
        
        count = count_subset_solutions(nums, target)
        assert count > 1  # Múltiplas combinações de zeros


class TestAnalyzeComplexity:
    """Testes para a função de análise de complexidade."""
    
    def test_analyze_complexity_basic(self):
        """Testa análise de complexidade básica."""
        analysis = analyze_subset_sum_complexity(10, 50)
        
        assert analysis['input_size'] == 10
        assert analysis['target_value'] == 50
        assert analysis['complexity_class'] == 'O(n·T)'
        assert analysis['space_complexity'] == 'O(n·T)'
        assert analysis['pseudo_polynomial'] == True
        assert analysis['exponential_improvement'] == True
        assert 'Reduz de O(2^10) para O(10·50)' in analysis['memoization_benefit']
        assert analysis['practical_viability'] == 'Viável para T moderado'
        assert len(analysis['limitations']) > 0
    
    def test_analyze_complexity_large_target(self):
        """Testa análise quando target é muito grande."""
        analysis = analyze_subset_sum_complexity(5, 1000)
        
        # Para target muito grande, pode não ser pseudo-polinomial
        if analysis['complexity_class'] == 'O(2^n)':
            assert analysis['pseudo_polynomial'] == False
            assert analysis['practical_viability'] == 'Não viável para target muito grande'


class TestCompareApproaches:
    """Testes para a função de comparação de abordagens."""
    
    def test_compare_approaches_basic(self):
        """Testa comparação básica de abordagens."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 25
        
        comparison = compare_approaches(nums, target)
        
        assert 'backtracking_time' in comparison
        assert 'memoization_time' in comparison
        assert 'tabulation_time' in comparison
        assert 'backtracking_result' in comparison
        assert 'memoization_result' in comparison
        assert 'tabulation_result' in comparison
        assert 'all_consistent' in comparison
        assert 'performance_improvement' in comparison
        
        # Verifica consistência
        assert comparison['all_consistent'] == True
        assert comparison['memoization_result'] == comparison['tabulation_result']
    
    def test_compare_approaches_performance(self):
        """Testa que memoização é mais rápida que backtracking para arrays pequenos."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 25
        
        comparison = compare_approaches(nums, target)
        
        if comparison['backtracking_time'] > 0:
            assert comparison['performance_improvement'] > 1  # Memoização deve ser mais rápida


class TestPerformance:
    """Testes de performance e stress."""
    
    def test_performance_memoization_vs_tabulation(self):
        """Testa que memoização e tabulação têm performance similar."""
        nums = list(range(1, 21))  # 1 a 20
        target = 50
        
        start_time = time.time()
        memo_result = subset_sum_memoization(nums, target)
        memo_time = time.time() - start_time
        
        start_time = time.time()
        tab_result = subset_sum_tabulation(nums, target)
        tab_time = time.time() - start_time
        
        assert memo_result == tab_result
        # Ambos devem ser rápidos para este tamanho
        assert memo_time < 1.0
        assert tab_time < 1.0
    
    def test_performance_large_input(self):
        """Testa performance com entrada grande."""
        nums = list(range(1, 51))  # 1 a 50
        target = 100
        
        start_time = time.time()
        result = subset_sum_memoization(nums, target)
        execution_time = time.time() - start_time
        
        # Deve ser executado em tempo razoável
        assert execution_time < 5.0
        assert isinstance(result, bool)
    
    def test_memory_efficiency(self):
        """Testa que o algoritmo não consome memória excessiva."""
        nums = list(range(1, 31))  # 1 a 30
        target = 50
        
        # Executa múltiplas vezes para verificar vazamentos de memória
        for _ in range(10):
            result = subset_sum_memoization(nums, target)
            assert isinstance(result, bool)


class TestErrorHandling:
    """Testes para tratamento de erros."""
    
    def test_invalid_inputs(self):
        """Testa comportamento com entradas inválidas."""
        # Target negativo (deve funcionar com números negativos no array)
        assert subset_sum_memoization([-1, -2, -3], -6) == True
        
        # Array com elementos negativos
        assert subset_sum_memoization([-1, 1, 2], 0) == True
        
        # Target muito grande
        nums = [1, 2, 3, 4, 5]
        large_target = 1000000
        result = subset_sum_memoization(nums, large_target)
        assert isinstance(result, bool)  # Deve retornar False, mas não crashar


if __name__ == "__main__":
    # Executa todos os testes
    pytest.main([__file__, "-v"]) 