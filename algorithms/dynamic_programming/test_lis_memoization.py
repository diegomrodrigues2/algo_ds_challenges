"""
Testes para LIS (Longest Increasing Subsequence) com Memoização

Este módulo contém testes abrangentes para validar a implementação
do Desafio 23: LIS com Memoização.
"""

import unittest
import time
from typing import List

from lis_memoization import (
    lis_memoization,
    lis_backtracking,
    lis_tabulation,
    lis_binary_search,
    lis_with_sequence,
    lis_count_all,
    lis_ending_at_each_index,
    lis_with_constraints,
    compare_lis_approaches,
    analyze_lis_complexity,
    generate_lis_test_cases
)


class TestLISMemoization(unittest.TestCase):
    """Testes para LIS com memoização."""
    
    def setUp(self):
        """Configuração inicial para os testes."""
        self.basic_cases = [
            ([3, 10, 2, 1, 20], 3),
            ([10, 22, 9, 33, 21, 50, 41, 60], 5),
            ([30, 20, 10], 1),
            ([10, 20, 35, 80], 4),
            ([2, 2, 2], 1)
        ]
        
        self.edge_cases = [
            ([], 0),
            ([5], 1),
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 1)
        ]
    
    def test_basic_cases(self):
        """Testa casos básicos de LIS."""
        for arr, expected in self.basic_cases:
            with self.subTest(arr=arr):
                result = lis_memoization(arr)
                self.assertEqual(result, expected, 
                    f"LIS de {arr} deveria ser {expected}, mas foi {result}")
    
    def test_edge_cases(self):
        """Testa casos extremos."""
        for arr, expected in self.edge_cases:
            with self.subTest(arr=arr):
                result = lis_memoization(arr)
                self.assertEqual(result, expected,
                    f"LIS de {arr} deveria ser {expected}, mas foi {result}")
    
    def test_empty_array(self):
        """Testa array vazio."""
        result = lis_memoization([])
        self.assertEqual(result, 0)
    
    def test_single_element(self):
        """Testa array com um elemento."""
        result = lis_memoization([42])
        self.assertEqual(result, 1)
    
    def test_sorted_array(self):
        """Testa array já ordenado."""
        arr = list(range(1, 11))  # [1, 2, 3, ..., 10]
        result = lis_memoization(arr)
        self.assertEqual(result, 10)
    
    def test_reverse_sorted_array(self):
        """Testa array em ordem decrescente."""
        arr = list(range(10, 0, -1))  # [10, 9, 8, ..., 1]
        result = lis_memoization(arr)
        self.assertEqual(result, 1)
    
    def test_duplicate_elements(self):
        """Testa array com elementos duplicados."""
        arr = [1, 1, 2, 2, 3, 3]
        result = lis_memoization(arr)
        self.assertEqual(result, 3)  # [1, 2, 3] (estritamente crescente)
    
    def test_large_array(self):
        """Testa array grande."""
        # Array que alterna entre pequeno e grande
        arr = []
        for i in range(50):
            arr.extend([i, 100 + i])
        
        result = lis_memoization(arr)
        self.assertGreater(result, 50)  # Deve ser maior que 50
    
    def test_consistency_with_generated_cases(self):
        """Testa consistência com casos gerados."""
        test_cases = generate_lis_test_cases()
        
        for arr, expected in test_cases:
            with self.subTest(arr=arr):
                result = lis_memoization(arr)
                self.assertEqual(result, expected,
                    f"LIS de {arr} deveria ser {expected}, mas foi {result}")
    
    def test_memoization_effectiveness(self):
        """Testa se a memoização está funcionando."""
        # Array que força muitos subproblemas sobrepostos
        arr = [1, 5, 2, 6, 3, 7, 4, 8]
        
        # Primeira execução
        start_time = time.time()
        result1 = lis_memoization(arr)
        time1 = time.time() - start_time
        
        # Segunda execução (deve ser mais rápida devido ao cache)
        start_time = time.time()
        result2 = lis_memoization(arr)
        time2 = time.time() - start_time
        
        # Resultados devem ser iguais
        self.assertEqual(result1, result2)
        
        # Segunda execução deve ser mais rápida (ou pelo menos não muito mais lenta)
        self.assertLessEqual(time2, time1 * 2)  # Margem de tolerância
    
    def test_complexity_analysis(self):
        """Testa a análise de complexidade."""
        analysis = analyze_lis_complexity(100)
        
        # Verifica se a análise contém os campos esperados
        expected_fields = [
            'input_size', 'complexity_class', 'space_complexity',
            'exponential_improvement', 'memoization_benefit',
            'practical_viability', 'subproblem_analysis'
        ]
        
        for field in expected_fields:
            self.assertIn(field, analysis)
        
        # Verifica valores específicos
        self.assertEqual(analysis['input_size'], 100)
        self.assertEqual(analysis['complexity_class'], 'O(n²)')
        self.assertEqual(analysis['space_complexity'], 'O(n²)')
        self.assertTrue(analysis['exponential_improvement'])
    
    def test_compare_approaches(self):
        """Testa a função de comparação de abordagens."""
        arr = [3, 10, 2, 1, 20]
        
        comparison = compare_lis_approaches(arr)
        
        # Verifica estrutura da comparação
        self.assertIn('input_array', comparison)
        self.assertIn('array_size', comparison)
        self.assertIn('approaches', comparison)
        self.assertIn('performance_improvement', comparison)
        
        # Verifica que a memoização foi testada
        approaches = comparison['approaches']
        self.assertIn('memoization', approaches)
        
        # Verifica que o resultado da memoização está correto
        self.assertEqual(approaches['memoization']['result'], 3)
    
    def test_generate_test_cases(self):
        """Testa a geração de casos de teste."""
        test_cases = generate_lis_test_cases()
        
        # Verifica que há casos de teste
        self.assertGreater(len(test_cases), 0)
        
        # Verifica estrutura dos casos de teste
        for arr, expected in test_cases:
            self.assertIsInstance(arr, list)
            self.assertIsInstance(expected, int)
            self.assertGreaterEqual(expected, 0)
            
            # Testa se o caso de teste funciona
            result = lis_memoization(arr)
            self.assertEqual(result, expected)
    
    def test_performance_scalability(self):
        """Testa a escalabilidade da solução."""
        # Testa com diferentes tamanhos
        sizes = [10, 20, 50]
        
        for size in sizes:
            with self.subTest(size=size):
                # Cria array de teste
                arr = list(range(size)) + list(range(size-1, -1, -1))
                
                # Deve completar em tempo razoável
                start_time = time.time()
                result = lis_memoization(arr)
                execution_time = time.time() - start_time
                
                # Verifica que completou
                self.assertIsInstance(result, int)
                self.assertGreater(result, 0)
                
                # Verifica que não demorou muito (5 segundos é muito generoso)
                self.assertLess(execution_time, 5.0, 
                    f"Execução com tamanho {size} demorou {execution_time:.2f}s")


class TestLISNotImplementedFunctions(unittest.TestCase):
    """Testes para funções que devem ser implementadas."""
    
    def test_lis_backtracking_not_implemented(self):
        """Testa se lis_backtracking levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            lis_backtracking([1, 2, 3])
    
    def test_lis_tabulation_not_implemented(self):
        """Testa se lis_tabulation levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            lis_tabulation([1, 2, 3])
    
    def test_lis_binary_search_not_implemented(self):
        """Testa se lis_binary_search levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            lis_binary_search([1, 2, 3])
    
    def test_lis_with_sequence_not_implemented(self):
        """Testa se lis_with_sequence levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            lis_with_sequence([1, 2, 3])
    
    def test_lis_count_all_not_implemented(self):
        """Testa se lis_count_all levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            lis_count_all([1, 2, 3])
    
    def test_lis_ending_at_each_index_not_implemented(self):
        """Testa se lis_ending_at_each_index levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            lis_ending_at_each_index([1, 2, 3])
    
    def test_lis_with_constraints_not_implemented(self):
        """Testa se lis_with_constraints levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            lis_with_constraints([1, 2, 3])


class TestLISPerformance(unittest.TestCase):
    """Testes de performance para LIS."""
    
    def test_memory_efficiency(self):
        """Testa a eficiência de memória."""
        # Testa com array moderadamente grande
        arr = list(range(200)) + list(range(199, -1, -1))
        
        # Deve completar sem erro de memória
        result = lis_memoization(arr)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
    
    def test_worst_case_performance(self):
        """Testa performance no pior caso."""
        # Pior caso: muitos elementos iguais seguidos de crescente
        arr = [1] * 50 + list(range(50))
        
        start_time = time.time()
        result = lis_memoization(arr)
        execution_time = time.time() - start_time
        
        # Verifica resultado correto
        self.assertEqual(result, 50)  # Apenas a parte crescente
        
        # Verifica que não demorou muito
        self.assertLess(execution_time, 2.0, 
            f"Pior caso demorou {execution_time:.2f}s")
    
    def test_best_case_performance(self):
        """Testa performance no melhor caso."""
        # Melhor caso: array já ordenado
        arr = list(range(100))
        
        start_time = time.time()
        result = lis_memoization(arr)
        execution_time = time.time() - start_time
        
        # Verifica resultado correto
        self.assertEqual(result, 100)
        
        # Verifica que foi rápido
        self.assertLess(execution_time, 1.0,
            f"Melhor caso demorou {execution_time:.2f}s")


class TestLISEdgeCasesExtended(unittest.TestCase):
    """Testes para casos extremos estendidos."""
    
    def test_negative_numbers(self):
        """Testa array com números negativos."""
        arr = [-5, -1, -3, 0, 2, -2, 3]
        result = lis_memoization(arr)
        # Uma LIS possível: [-5, -1, 0, 2, 3]
        self.assertGreaterEqual(result, 4)
    
    def test_large_numbers(self):
        """Testa array com números grandes."""
        arr = [1000000, 2000000, 500000, 3000000]
        result = lis_memoization(arr)
        self.assertEqual(result, 3)  # [1000000, 2000000, 3000000]
    
    def test_mixed_positive_negative(self):
        """Testa array misto com positivos e negativos."""
        arr = [-10, -5, 0, 5, 10, -2, 15]
        result = lis_memoization(arr)
        # Uma LIS possível: [-10, -5, 0, 5, 10, 15]
        self.assertGreaterEqual(result, 5)
    
    def test_very_small_array(self):
        """Testa arrays muito pequenos."""
        # Array vazio
        self.assertEqual(lis_memoization([]), 0)
        
        # Array com um elemento
        self.assertEqual(lis_memoization([42]), 1)
        
        # Array com dois elementos crescentes
        self.assertEqual(lis_memoization([1, 2]), 2)
        
        # Array com dois elementos decrescentes
        self.assertEqual(lis_memoization([2, 1]), 1)


if __name__ == "__main__":
    # Executa os testes
    unittest.main(verbosity=2)