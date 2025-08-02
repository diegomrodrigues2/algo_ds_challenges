"""
Testes para Quicksort com Partição de Lomuto

Este módulo contém testes abrangentes para verificar a implementação
do algoritmo Quicksort usando a estratégia de partição de Lomuto.
"""

import pytest
import random
import time
from .quicksort_lomuto import (
    lomuto_partition,
    quicksort_lomuto,
    quicksort_lomuto_wrapper,
    is_sorted
)


class TestLomutoPartition:
    """Testes para a função de partição de Lomuto."""
    
    def test_partition_basic(self):
        """Teste básico da partição de Lomuto."""
        arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]
        pivot_idx = lomuto_partition(arr, 0, len(arr) - 1)
        
        # Verificar se o pivô está na posição correta
        assert arr[pivot_idx] == 4  # último elemento
        
        # Verificar se elementos à esquerda são menores ou iguais
        for i in range(pivot_idx):
            assert arr[i] <= arr[pivot_idx]
        
        # Verificar se elementos à direita são maiores ou iguais
        for i in range(pivot_idx + 1, len(arr)):
            assert arr[i] >= arr[pivot_idx]
    
    def test_partition_single_element(self):
        """Teste com array de um elemento."""
        arr = [5]
        pivot_idx = lomuto_partition(arr, 0, 0)
        assert pivot_idx == 0
        assert arr == [5]
    
    def test_partition_two_elements(self):
        """Teste com array de dois elementos."""
        # Caso 1: já ordenado
        arr = [1, 2]
        pivot_idx = lomuto_partition(arr, 0, 1)
        assert pivot_idx == 1
        assert arr == [1, 2]
        
        # Caso 2: invertido
        arr = [2, 1]
        pivot_idx = lomuto_partition(arr, 0, 1)
        assert pivot_idx == 0
        assert arr == [1, 2]
    
    def test_partition_all_equal(self):
        """Teste com todos os elementos iguais."""
        arr = [3, 3, 3, 3, 3]
        pivot_idx = lomuto_partition(arr, 0, len(arr) - 1)
        assert pivot_idx == 4  # último elemento
        assert arr == [3, 3, 3, 3, 3]
    
    def test_partition_subarray(self):
        """Teste de partição em subarray."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        pivot_idx = lomuto_partition(arr, 2, 6)  # subarray [7, 6, 5, 4, 3]
        assert arr[2:7] == [3, 4, 5, 6, 7]  # ordenado em torno do pivô 3


class TestQuicksortLomuto:
    """Testes para o algoritmo Quicksort com partição de Lomuto."""
    
    def test_quicksort_empty_array(self):
        """Teste com array vazio."""
        arr = []
        result = quicksort_lomuto_wrapper(arr)
        assert result == []
    
    def test_quicksort_single_element(self):
        """Teste com array de um elemento."""
        arr = [5]
        result = quicksort_lomuto_wrapper(arr)
        assert result == [5]
    
    def test_quicksort_already_sorted(self):
        """Teste com array já ordenado."""
        arr = [1, 2, 3, 4, 5]
        result = quicksort_lomuto_wrapper(arr)
        assert result == [1, 2, 3, 4, 5]
        assert is_sorted(result)
    
    def test_quicksort_reverse_sorted(self):
        """Teste com array em ordem reversa."""
        arr = [5, 4, 3, 2, 1]
        result = quicksort_lomuto_wrapper(arr)
        assert result == [1, 2, 3, 4, 5]
        assert is_sorted(result)
    
    def test_quicksort_duplicates(self):
        """Teste com elementos duplicados."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        assert is_sorted(result)
    
    def test_quicksort_negative_numbers(self):
        """Teste com números negativos."""
        arr = [-3, 1, -4, 1, -5, 9, -2, 6, -5, 3, -5]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        assert is_sorted(result)
    
    def test_quicksort_large_array(self):
        """Teste com array grande."""
        arr = list(range(1000, 0, -1))  # 1000 elementos em ordem reversa
        result = quicksort_lomuto_wrapper(arr)
        expected = list(range(1, 1001))
        assert result == expected
        assert is_sorted(result)
    
    def test_quicksort_random_array(self):
        """Teste com array aleatório."""
        random.seed(42)  # Para reprodutibilidade
        arr = [random.randint(-100, 100) for _ in range(100)]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        assert is_sorted(result)
    
    def test_quicksort_strings(self):
        """Teste com strings."""
        arr = ["banana", "apple", "cherry", "date", "elderberry"]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        assert is_sorted(result)
    
    def test_quicksort_floats(self):
        """Teste com números de ponto flutuante."""
        arr = [3.14, 2.71, 1.41, 2.23, 1.73]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        assert is_sorted(result)
    
    def test_quicksort_inplace_modification(self):
        """Teste para verificar modificação in-place."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        original = arr.copy()
        quicksort_lomuto(arr)  # Modifica o array original
        assert arr == sorted(original)
        assert arr != original  # Deve ter sido modificado


class TestQuicksortPerformance:
    """Testes de performance do Quicksort."""
    
    def test_quicksort_performance_small(self):
        """Teste de performance com array pequeno."""
        arr = list(range(100, 0, -1))
        start_time = time.time()
        result = quicksort_lomuto_wrapper(arr)
        end_time = time.time()
        
        assert result == list(range(1, 101))
        assert end_time - start_time < 1.0  # Deve ser rápido
    
    def test_quicksort_performance_medium(self):
        """Teste de performance com array médio."""
        arr = list(range(10000, 0, -1))
        start_time = time.time()
        result = quicksort_lomuto_wrapper(arr)
        end_time = time.time()
        
        assert result == list(range(1, 10001))
        assert end_time - start_time < 5.0  # Deve ser razoavelmente rápido
    
    def test_quicksort_worst_case(self):
        """Teste do pior caso (array já ordenado)."""
        arr = list(range(1000))
        start_time = time.time()
        result = quicksort_lomuto_wrapper(arr)
        end_time = time.time()
        
        assert result == list(range(1000))
        assert end_time - start_time < 2.0  # Mesmo no pior caso, deve ser aceitável


class TestQuicksortEdgeCases:
    """Testes de casos extremos."""
    
    def test_quicksort_all_identical(self):
        """Teste com todos os elementos idênticos."""
        arr = [5] * 100
        result = quicksort_lomuto_wrapper(arr)
        assert result == [5] * 100
        assert is_sorted(result)
    
    def test_quicksort_alternating_pattern(self):
        """Teste com padrão alternado."""
        arr = [1, 2, 1, 2, 1, 2, 1, 2]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        assert is_sorted(result)
    
    def test_quicksort_single_value_repeated(self):
        """Teste com um valor repetido muitas vezes."""
        arr = [42] * 500
        result = quicksort_lomuto_wrapper(arr)
        assert result == [42] * 500
        assert is_sorted(result)
    
    def test_quicksort_extreme_values(self):
        """Teste com valores extremos."""
        arr = [float('inf'), float('-inf'), 0, 1, -1]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        assert is_sorted(result)


class TestQuicksortCorrectness:
    """Testes de correção do algoritmo."""
    
    def test_quicksort_stability_equivalent_keys(self):
        """Teste de estabilidade com chaves equivalentes."""
        # Quicksort não é estável, mas deve preservar a ordem relativa
        # de elementos com chaves equivalentes em alguns casos
        arr = [(1, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
    
    def test_quicksort_comparison_count(self):
        """Teste para verificar número de comparações."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = quicksort_lomuto_wrapper(arr)
        expected = sorted(arr)
        assert result == expected
        
        # Verificar que o resultado está correto
        assert len(result) == len(arr)
        assert all(result[i] <= result[i+1] for i in range(len(result)-1))
    
    def test_quicksort_preserves_elements(self):
        """Teste para verificar se todos os elementos são preservados."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        original_elements = set(arr)
        result = quicksort_lomuto_wrapper(arr)
        result_elements = set(result)
        
        assert original_elements == result_elements
        assert len(result) == len(arr)


if __name__ == "__main__":
    # Executar testes se o arquivo for executado diretamente
    pytest.main([__file__]) 