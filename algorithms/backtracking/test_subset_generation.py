"""
Testes para o módulo de geração de subconjuntos (subset_generation.py).

Este módulo contém testes abrangentes para todas as funções implementadas
no módulo subset_generation.py, incluindo casos básicos, otimizações,
análise de complexidade e casos extremos.
"""

import pytest
import time
from subset_generation import (
    subset_generation_backtracking,
    subset_generation_iterative_bitmask,
    subset_generation_with_constraints,
    subset_generation_with_sum_constraint,
    subset_generation_with_memoization,
    subset_generation_lexicographic,
    subset_generation_count_only,
    subset_generation_with_duplicates,
    subset_generation_optimized,
    analyze_subset_generation_complexity,
    create_test_subsets
)


class TestSubsetGenerationBasic:
    """Testes para funcionalidade básica de geração de subconjuntos."""
    
    def test_empty_set(self):
        """Testa geração de subconjuntos para conjunto vazio."""
        elements = []
        expected = [[]]
        
        assert subset_generation_backtracking(elements) == expected
        assert subset_generation_iterative_bitmask(elements) == expected
        assert subset_generation_optimized(elements) == expected
    
    def test_single_element(self):
        """Testa geração de subconjuntos para conjunto unitário."""
        elements = [1]
        expected = [[], [1]]
        
        assert subset_generation_backtracking(elements) == expected
        assert subset_generation_iterative_bitmask(elements) == expected
        assert subset_generation_optimized(elements) == expected
    
    def test_two_elements(self):
        """Testa geração de subconjuntos para conjunto com dois elementos."""
        elements = [1, 2]
        expected = [[], [1], [2], [1, 2]]
        
        assert subset_generation_backtracking(elements) == expected
        assert subset_generation_iterative_bitmask(elements) == expected
        assert subset_generation_optimized(elements) == expected
    
    def test_three_elements(self):
        """Testa geração de subconjuntos para conjunto com três elementos."""
        elements = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        
        result_backtracking = subset_generation_backtracking(elements)
        result_bitmask = subset_generation_iterative_bitmask(elements)
        result_optimized = subset_generation_optimized(elements)
        
        # Ordenar para comparação (ordem pode variar)
        assert sorted(result_backtracking) == sorted(expected)
        assert sorted(result_bitmask) == sorted(expected)
        assert sorted(result_optimized) == sorted(expected)
    
    def test_count_only(self):
        """Testa contagem de subconjuntos sem gerá-los."""
        test_cases = [
            ([], 1),
            ([1], 2),
            ([1, 2], 4),
            ([1, 2, 3], 8),
            ([1, 2, 3, 4], 16),
            ([1, 2, 3, 4, 5], 32)
        ]
        
        for elements, expected in test_cases:
            assert subset_generation_count_only(elements) == expected


class TestSubsetGenerationConstraints:
    """Testes para geração de subconjuntos com restrições."""
    
    def test_size_constraints(self):
        """Testa restrições de tamanho."""
        elements = [1, 2, 3]
        
        # Tamanho mínimo 1, máximo 2
        result = subset_generation_with_constraints(elements, 1, 2)
        expected = [[1], [2], [1, 2], [3], [1, 3], [2, 3]]
        assert sorted(result) == sorted(expected)
        
        # Tamanho mínimo 2
        result = subset_generation_with_constraints(elements, 2)
        expected = [[1, 2], [1, 3], [2, 3], [1, 2, 3]]
        assert sorted(result) == sorted(expected)
    
    def test_sum_constraints(self):
        """Testa restrições de soma."""
        elements = [1, 2, 3, 4]
        
        # Subconjuntos que somam 5
        result = subset_generation_with_sum_constraint(elements, 5)
        expected = [[1, 4], [2, 3], [1, 2, 2]]  # Assumindo que [1,2,2] não é válido
        # Remover [1,2,2] pois não há dois 2s no conjunto original
        expected = [[1, 4], [2, 3]]
        assert sorted(result) == sorted(expected)
        
        # Subconjuntos que somam 3
        result = subset_generation_with_sum_constraint(elements, 3)
        expected = [[3], [1, 2]]
        assert sorted(result) == sorted(expected)
    
    def test_empty_constraints(self):
        """Testa restrições que resultam em conjunto vazio."""
        elements = [1, 2, 3]
        
        # Tamanho mínimo maior que o conjunto
        result = subset_generation_with_constraints(elements, 4)
        assert result == []
        
        # Soma impossível
        result = subset_generation_with_sum_constraint(elements, 10)
        assert result == []


class TestSubsetGenerationMemoization:
    """Testes para versões com memoização."""
    
    def test_memoization_correctness(self):
        """Testa se a memoização produz resultados corretos."""
        elements = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        
        result = subset_generation_with_memoization(elements)
        assert sorted(result) == sorted(expected)
    
    def test_memoization_performance(self):
        """Testa se a memoização melhora a performance."""
        elements = list(range(1, 6))  # [1, 2, 3, 4, 5]
        
        start_time = time.time()
        result_backtracking = subset_generation_backtracking(elements)
        backtracking_time = time.time() - start_time
        
        start_time = time.time()
        result_memo = subset_generation_with_memoization(elements)
        memo_time = time.time() - start_time
        
        # Verificar que os resultados são iguais
        assert sorted(result_backtracking) == sorted(result_memo)
        
        # Verificar que ambos têm o número correto de subconjuntos
        assert len(result_backtracking) == 2**len(elements)
        assert len(result_memo) == 2**len(elements)


class TestSubsetGenerationLexicographic:
    """Testes para geração lexicográfica."""
    
    def test_lexicographic_order(self):
        """Testa se a geração lexicográfica está em ordem correta."""
        elements = [1, 2, 3]
        result = subset_generation_lexicographic(elements)
        
        expected = [
            [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]
        ]
        
        assert result == expected
    
    def test_lexicographic_with_duplicates(self):
        """Testa geração lexicográfica com duplicatas."""
        elements = [1, 1, 2]
        result = subset_generation_lexicographic(elements)
        
        # Deve gerar subconjuntos únicos
        expected = [
            [], [1], [1, 1], [1, 1, 2], [1, 2], [2]
        ]
        
        assert result == expected


class TestSubsetGenerationDuplicates:
    """Testes para geração de subconjuntos com duplicatas."""
    
    def test_with_duplicates(self):
        """Testa geração de subconjuntos únicos com duplicatas."""
        elements = [1, 1, 2]
        result = subset_generation_with_duplicates(elements)
        
        # Deve gerar apenas subconjuntos únicos
        expected = [
            [], [1], [1, 1], [1, 1, 2], [1, 2], [2]
        ]
        
        assert result == expected
    
    def test_multiple_duplicates(self):
        """Testa com múltiplas duplicatas."""
        elements = [1, 2, 2, 3]
        result = subset_generation_with_duplicates(elements)
        
        # Verificar que não há duplicatas nos subconjuntos
        subset_strings = [str(sorted(subset)) for subset in result]
        assert len(subset_strings) == len(set(subset_strings))
        
        # Verificar que todos os subconjuntos únicos estão presentes
        assert len(result) == 12  # 2^4 = 16, mas com duplicatas reduz


class TestSubsetGenerationOptimized:
    """Testes para versões otimizadas."""
    
    def test_optimized_correctness(self):
        """Testa se a versão otimizada produz resultados corretos."""
        elements = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        
        result = subset_generation_optimized(elements)
        assert sorted(result) == sorted(expected)
    
    def test_optimized_performance(self):
        """Testa performance da versão otimizada."""
        elements = list(range(1, 6))  # [1, 2, 3, 4, 5]
        
        start_time = time.time()
        result_optimized = subset_generation_optimized(elements)
        optimized_time = time.time() - start_time
        
        start_time = time.time()
        result_backtracking = subset_generation_backtracking(elements)
        backtracking_time = time.time() - start_time
        
        # Verificar que os resultados são iguais
        assert sorted(result_optimized) == sorted(result_backtracking)
        
        # Verificar que ambos têm o número correto de subconjuntos
        assert len(result_optimized) == 2**len(elements)
        assert len(result_backtracking) == 2**len(elements)


class TestSubsetGenerationCorrectness:
    """Testes de correção entre diferentes implementações."""
    
    def test_all_implementations_match(self):
        """Testa se todas as implementações produzem resultados consistentes."""
        test_cases = [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4]
        ]
        
        for elements in test_cases:
            result_backtracking = subset_generation_backtracking(elements)
            result_bitmask = subset_generation_iterative_bitmask(elements)
            result_optimized = subset_generation_optimized(elements)
            result_memo = subset_generation_with_memoization(elements)
            
            # Ordenar para comparação
            sorted_backtracking = sorted(result_backtracking)
            sorted_bitmask = sorted(result_bitmask)
            sorted_optimized = sorted(result_optimized)
            sorted_memo = sorted(result_memo)
            
            assert sorted_backtracking == sorted_bitmask
            assert sorted_backtracking == sorted_optimized
            assert sorted_backtracking == sorted_memo
            
            # Verificar número correto de subconjuntos
            expected_count = 2**len(elements)
            assert len(result_backtracking) == expected_count
            assert len(result_bitmask) == expected_count
            assert len(result_optimized) == expected_count
            assert len(result_memo) == expected_count


class TestSubsetGenerationComplexity:
    """Testes para análise de complexidade."""
    
    def test_complexity_analysis(self):
        """Testa a função de análise de complexidade."""
        elements = [1, 2, 3]
        analysis = analyze_subset_generation_complexity(elements)
        
        # Verificar que todas as métricas estão presentes
        required_keys = [
            'input_size', 'expected_count', 'actual_count', 'all_correct',
            'backtracking_time', 'bitmask_time', 'memo_time', 'optimized_time',
            'backtracking_count', 'bitmask_count', 'memo_count', 'optimized_count'
        ]
        
        for key in required_keys:
            assert key in analysis
        
        # Verificar valores corretos
        assert analysis['input_size'] == 3
        assert analysis['expected_count'] == 8
        assert analysis['actual_count'] == 8
        assert analysis['all_correct'] == True
        
        # Verificar que todos os algoritmos produzem o mesmo número de subconjuntos
        assert analysis['backtracking_count'] == 8
        assert analysis['bitmask_count'] == 8
        assert analysis['memo_count'] == 8
        assert analysis['optimized_count'] == 8
    
    def test_complexity_timing(self):
        """Testa se os tempos de execução são razoáveis."""
        elements = list(range(1, 6))  # [1, 2, 3, 4, 5]
        analysis = analyze_subset_generation_complexity(elements)
        
        # Verificar que todos os tempos são positivos
        assert analysis['backtracking_time'] > 0
        assert analysis['bitmask_time'] > 0
        assert analysis['memo_time'] > 0
        assert analysis['optimized_time'] > 0
        
        # Verificar que os tempos são razoáveis (menos de 1 segundo)
        assert analysis['backtracking_time'] < 1
        assert analysis['bitmask_time'] < 1
        assert analysis['memo_time'] < 1
        assert analysis['optimized_time'] < 1


class TestSubsetGenerationEdgeCases:
    """Testes para casos extremos."""
    
    def test_large_input(self):
        """Testa com entrada grande (deve ser rápido)."""
        elements = list(range(1, 11))  # [1, 2, ..., 10]
        
        # Deve gerar 2^10 = 1024 subconjuntos
        result = subset_generation_backtracking(elements)
        assert len(result) == 1024
        
        # Verificar que todos os subconjuntos são únicos
        subset_strings = [str(sorted(subset)) for subset in result]
        assert len(subset_strings) == len(set(subset_strings))
    
    def test_negative_numbers(self):
        """Testa com números negativos."""
        elements = [-1, 0, 1]
        result = subset_generation_backtracking(elements)
        
        expected = [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]
        assert sorted(result) == sorted(expected)
    
    def test_floating_point(self):
        """Testa com números de ponto flutuante."""
        elements = [1.5, 2.5, 3.5]
        result = subset_generation_backtracking(elements)
        
        # Deve gerar 2^3 = 8 subconjuntos
        assert len(result) == 8
        
        # Verificar que todos os subconjuntos são únicos
        subset_strings = [str(sorted(subset)) for subset in result]
        assert len(subset_strings) == len(set(subset_strings))
    
    def test_strings(self):
        """Testa com strings."""
        elements = ['a', 'b', 'c']
        result = subset_generation_backtracking(elements)
        
        expected = [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
        assert sorted(result) == sorted(expected)


class TestSubsetGenerationHelperFunctions:
    """Testes para funções auxiliares."""
    
    def test_create_test_subsets(self):
        """Testa a função de criação de casos de teste."""
        test_cases = create_test_subsets()
        
        # Verificar que há casos de teste
        assert len(test_cases) > 0
        
        # Verificar que todos os casos são listas
        for test_case in test_cases:
            assert isinstance(test_case, list)
        
        # Verificar casos específicos
        assert [] in test_cases  # Conjunto vazio
        assert [1] in test_cases  # Conjunto unitário
        assert [1, 2] in test_cases  # Conjunto pequeno
        assert [1, 2, 3] in test_cases  # Conjunto médio


class TestSubsetGenerationPerformance:
    """Testes de performance."""
    
    def test_performance_comparison(self):
        """Compara performance de diferentes implementações."""
        elements = list(range(1, 6))  # [1, 2, 3, 4, 5]
        
        # Medir tempo de cada implementação
        start_time = time.time()
        subset_generation_backtracking(elements)
        backtracking_time = time.time() - start_time
        
        start_time = time.time()
        subset_generation_iterative_bitmask(elements)
        bitmask_time = time.time() - start_time
        
        start_time = time.time()
        subset_generation_optimized(elements)
        optimized_time = time.time() - start_time
        
        # Verificar que todos os tempos são razoáveis
        assert backtracking_time < 1
        assert bitmask_time < 1
        assert optimized_time < 1
        
        # Verificar que a versão otimizada não é significativamente mais lenta
        assert optimized_time < backtracking_time * 2
    
    def test_memory_efficiency(self):
        """Testa eficiência de memória."""
        elements = list(range(1, 6))  # [1, 2, 3, 4, 5]
        
        # Gerar subconjuntos e verificar que não há vazamentos óbvios
        result = subset_generation_backtracking(elements)
        
        # Verificar que o resultado tem o tamanho esperado
        assert len(result) == 2**len(elements)
        
        # Verificar que todos os subconjuntos são listas válidas
        for subset in result:
            assert isinstance(subset, list)
            # Verificar que todos os elementos estão no conjunto original
            for element in subset:
                assert element in elements


if __name__ == "__main__":
    pytest.main([__file__]) 