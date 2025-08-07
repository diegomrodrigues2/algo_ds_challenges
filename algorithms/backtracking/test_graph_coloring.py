"""
Testes para o Algoritmo de Coloração de Grafos

Este módulo contém testes abrangentes para verificar a correção
e eficiência das implementações de coloração de grafos.

Referências:
- InterviewBit: Graph Coloring Algorithm using Backtracking
- GeeksforGeeks: M-Coloring Problem
- TheAlgorithms/Python: coloring.py
"""

import unittest
import time
from typing import List, Optional
from graph_coloring import (
    graph_coloring_backtracking,
    graph_coloring_optimized,
    graph_coloring_count_solutions,
    graph_coloring_all_solutions,
    graph_coloring_with_memoization,
    analyze_graph_coloring_complexity
)


class TestGraphColoring(unittest.TestCase):
    """
    Testes para o algoritmo de coloração de grafos.
    """
    
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        # Grafo simples: ciclo de 4 vértices (requer 2 cores)
        self.simple_graph = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        
        # Grafo que requer 3 cores
        self.complex_graph = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        
        # Grafo completo de 3 vértices (requer 3 cores)
        self.complete_graph = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        
        # Grafo vazio
        self.empty_graph = []
        
        # Grafo com um vértice
        self.single_vertex_graph = [[0]]
    
    def test_basic_coloring(self):
        """
        Testa coloração básica com grafo simples.
        """
        # Testa com 2 cores (deve funcionar)
        result = graph_coloring_backtracking(self.simple_graph, 2)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertTrue(self._is_valid_coloring(self.simple_graph, result))
        
        # Testa com 1 cor (não deve funcionar)
        result = graph_coloring_backtracking(self.simple_graph, 1)
        self.assertIsNone(result)
    
    def test_complex_graph_coloring(self):
        """
        Testa coloração com grafo mais complexo.
        """
        # Testa com 2 cores (não deve funcionar)
        result = graph_coloring_backtracking(self.complex_graph, 2)
        self.assertIsNone(result)
        
        # Testa com 3 cores (deve funcionar)
        result = graph_coloring_backtracking(self.complex_graph, 3)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertTrue(self._is_valid_coloring(self.complex_graph, result))
    
    def test_complete_graph(self):
        """
        Testa coloração de grafo completo.
        """
        # Grafo completo de 3 vértices requer 3 cores
        result = graph_coloring_backtracking(self.complete_graph, 2)
        self.assertIsNone(result)
        
        result = graph_coloring_backtracking(self.complete_graph, 3)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        self.assertTrue(self._is_valid_coloring(self.complete_graph, result))
    
    def test_edge_cases(self):
        """
        Testa casos extremos.
        """
        # Grafo vazio
        result = graph_coloring_backtracking(self.empty_graph, 3)
        self.assertEqual(result, [])
        
        # Grafo com um vértice
        result = graph_coloring_backtracking(self.single_vertex_graph, 1)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        
        # Número de cores inválido
        result = graph_coloring_backtracking(self.simple_graph, 0)
        self.assertIsNone(result)
        
        result = graph_coloring_backtracking(self.simple_graph, -1)
        self.assertIsNone(result)
    
    def test_optimized_coloring(self):
        """
        Testa a versão otimizada do algoritmo.
        """
        # Compara resultados com implementação básica
        basic_result = graph_coloring_backtracking(self.simple_graph, 2)
        optimized_result = graph_coloring_optimized(self.simple_graph, 2)
        
        self.assertEqual(basic_result, optimized_result)
        
        # Testa com grafo complexo
        basic_result = graph_coloring_backtracking(self.complex_graph, 3)
        optimized_result = graph_coloring_optimized(self.complex_graph, 3)
        
        self.assertEqual(basic_result, optimized_result)
    
    def test_memoized_coloring(self):
        """
        Testa a versão com memoização.
        """
        # Compara resultados com implementação básica
        basic_result = graph_coloring_backtracking(self.simple_graph, 2)
        memoized_result = graph_coloring_with_memoization(self.simple_graph, 2)
        
        self.assertEqual(basic_result, memoized_result)
        
        # Testa com grafo complexo
        basic_result = graph_coloring_backtracking(self.complex_graph, 3)
        memoized_result = graph_coloring_with_memoization(self.complex_graph, 3)
        
        self.assertEqual(basic_result, memoized_result)
    
    def test_solution_counting(self):
        """
        Testa a contagem de soluções.
        """
        # Grafo simples com 2 cores
        count = graph_coloring_count_solutions(self.simple_graph, 2)
        self.assertGreater(count, 0)
        
        # Grafo simples com 1 cor (deve ser 0)
        count = graph_coloring_count_solutions(self.simple_graph, 1)
        self.assertEqual(count, 0)
        
        # Grafo complexo com 3 cores
        count = graph_coloring_count_solutions(self.complex_graph, 3)
        self.assertGreater(count, 0)
    
    def test_all_solutions(self):
        """
        Testa a busca por todas as soluções.
        """
        # Grafo simples com 2 cores
        solutions = graph_coloring_all_solutions(self.simple_graph, 2)
        self.assertGreater(len(solutions), 0)
        
        # Verifica se todas as soluções são válidas
        for solution in solutions:
            self.assertTrue(self._is_valid_coloring(self.simple_graph, solution))
        
        # Grafo simples com 1 cor (deve ser vazio)
        solutions = graph_coloring_all_solutions(self.simple_graph, 1)
        self.assertEqual(len(solutions), 0)
    
    def test_complexity_analysis(self):
        """
        Testa a análise de complexidade.
        """
        analysis = analyze_graph_coloring_complexity(self.simple_graph, 2)
        
        self.assertEqual(analysis['vertices'], 4)
        self.assertEqual(analysis['edges'], 4)
        self.assertEqual(analysis['colors'], 2)
        self.assertIn('max_degree', analysis)
        self.assertIn('avg_degree', analysis)
        self.assertIn('worst_case_time', analysis)
        self.assertIn('space_complexity', analysis)
    
    def test_performance_comparison(self):
        """
        Testa o desempenho das diferentes implementações.
        """
        # Grafo de teste para performance
        test_graph = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        
        m = 3
        
        # Mede tempo da implementação básica
        start_time = time.time()
        basic_result = graph_coloring_backtracking(test_graph, m)
        basic_time = time.time() - start_time
        
        # Mede tempo da implementação otimizada
        start_time = time.time()
        optimized_result = graph_coloring_optimized(test_graph, m)
        optimized_time = time.time() - start_time
        
        # Mede tempo da implementação com memoização
        start_time = time.time()
        memoized_result = graph_coloring_with_memoization(test_graph, m)
        memoized_time = time.time() - start_time
        
        # Verifica que todos os resultados são iguais
        self.assertEqual(basic_result, optimized_result)
        self.assertEqual(basic_result, memoized_result)
        
        # Verifica que os tempos são razoáveis (não infinitos)
        self.assertLess(basic_time, 10.0)
        self.assertLess(optimized_time, 10.0)
        self.assertLess(memoized_time, 10.0)
    
    def test_large_graphs(self):
        """
        Testa com grafos maiores.
        """
        # Grafo de 6 vértices
        large_graph = [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 0]
        ]
        
        # Testa com diferentes números de cores
        for m in [2, 3, 4]:
            result = graph_coloring_backtracking(large_graph, m)
            if result:
                self.assertTrue(self._is_valid_coloring(large_graph, result))
    
    def test_invalid_inputs(self):
        """
        Testa entradas inválidas.
        """
        # Grafo None
        with self.assertRaises(TypeError):
            graph_coloring_backtracking(None, 3)
        
        # Grafo com valores inválidos
        invalid_graph = [
            [0, 2, 1],  # Valor 2 não é válido
            [2, 0, 1],
            [1, 1, 0]
        ]
        
        # Deve lidar graciosamente com entrada inválida
        result = graph_coloring_backtracking(invalid_graph, 3)
        # Pode retornar None ou levantar exceção, dependendo da implementação
    
    def _is_valid_coloring(self, graph: List[List[int]], colors: List[int]) -> bool:
        """
        Verifica se uma coloração é válida.
        
        Args:
            graph: Matriz de adjacência do grafo
            colors: Lista de cores atribuídas aos vértices
            
        Returns:
            True se a coloração é válida, False caso contrário
        """
        if not colors:
            return len(graph) == 0
        
        V = len(graph)
        if len(colors) != V:
            return False
        
        # Verifica se vértices adjacentes têm cores diferentes
        for i in range(V):
            for j in range(i + 1, V):
                if graph[i][j] == 1 and colors[i] == colors[j]:
                    return False
        
        return True


class TestGraphColoringExamples(unittest.TestCase):
    """
    Testes baseados em exemplos específicos.
    """
    
    def test_interviewbit_example(self):
        """
        Testa o exemplo do InterviewBit.
        """
        graph = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        m = 3
        
        result = graph_coloring_backtracking(graph, m)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        
        # Verifica se a coloração é válida
        for i in range(4):
            for j in range(i + 1, 4):
                if graph[i][j] == 1:
                    self.assertNotEqual(result[i], result[j])
    
    def test_geeksforgeeks_example(self):
        """
        Testa exemplo do GeeksforGeeks.
        """
        graph = [
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        
        # Testa com diferentes números de cores
        for m in [2, 3, 4]:
            result = graph_coloring_backtracking(graph, m)
            if result:
                self.assertTrue(self._is_valid_coloring(graph, result))
    
    def _is_valid_coloring(self, graph: List[List[int]], colors: List[int]) -> bool:
        """
        Verifica se uma coloração é válida.
        """
        V = len(graph)
        for i in range(V):
            for j in range(i + 1, V):
                if graph[i][j] == 1 and colors[i] == colors[j]:
                    return False
        return True


def run_performance_tests():
    """
    Executa testes de performance.
    """
    print("=== Testes de Performance ===")
    
    # Grafo de teste
    graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 0]
    ]
    
    m = 3
    
    implementations = [
        ("Backtracking Básico", graph_coloring_backtracking),
        ("Backtracking Otimizado", graph_coloring_optimized),
        ("Com Memoização", graph_coloring_with_memoization)
    ]
    
    for name, func in implementations:
        start_time = time.time()
        result = func(graph, m)
        end_time = time.time()
        
        print(f"{name}: {end_time - start_time:.6f} segundos")
        print(f"Resultado: {result}")
        print()


if __name__ == "__main__":
    # Executa testes unitários
    unittest.main(verbosity=2, exit=False)
    
    # Executa testes de performance
    run_performance_tests() 