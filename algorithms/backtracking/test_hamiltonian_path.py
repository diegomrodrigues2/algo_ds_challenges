"""
Testes para o Algoritmo do Caminho Hamiltoniano

Este módulo contém testes abrangentes para verificar a correção
e eficiência das implementações do Caminho Hamiltoniano.

Referências:
- Wikipedia: Hamiltonian path problem
- HackerEarth: Hamiltonian Path Tutorial
- TheAlgorithms/Python: hamiltonian_cycle.py
- NetworkX Implementation: mikkelam/hamilton.py
"""

import unittest
import time
from typing import List, Optional
from hamiltonian_path import (
    hamiltonian_path_backtracking,
    hamiltonian_cycle_backtracking,
    hamiltonian_path_optimized,
    hamiltonian_path_count_solutions,
    hamiltonian_path_all_solutions,
    hamiltonian_path_with_memoization,
    analyze_hamiltonian_path_complexity
)


class TestHamiltonianPath(unittest.TestCase):
    """
    Testes para o algoritmo do Caminho Hamiltoniano.
    """
    
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        # Grafo com caminho Hamiltoniano (ciclo de 4 vértices)
        self.valid_graph = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        
        # Grafo sem caminho Hamiltoniano (vértice isolado)
        self.invalid_graph = [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ]
        
        # Grafo completo de 3 vértices
        self.complete_graph = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        
        # Grafo vazio
        self.empty_graph = []
        
        # Grafo com um vértice
        self.single_vertex_graph = [[0]]
    
    def test_basic_hamiltonian_path(self):
        """
        Testa caminho Hamiltoniano básico.
        """
        result = hamiltonian_path_backtracking(self.valid_graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertTrue(self._is_valid_hamiltonian_path(self.valid_graph, result))
        
        # Testa grafo sem caminho Hamiltoniano
        result = hamiltonian_path_backtracking(self.invalid_graph)
        self.assertIsNone(result)
    
    def test_hamiltonian_cycle(self):
        """
        Testa ciclo Hamiltoniano.
        """
        result = hamiltonian_cycle_backtracking(self.valid_graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        self.assertTrue(self._is_valid_hamiltonian_cycle(self.valid_graph, result))
        
        # Testa grafo sem ciclo Hamiltoniano
        result = hamiltonian_cycle_backtracking(self.invalid_graph)
        self.assertIsNone(result)
    
    def test_complete_graph(self):
        """
        Testa grafo completo.
        """
        result = hamiltonian_path_backtracking(self.complete_graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        self.assertTrue(self._is_valid_hamiltonian_path(self.complete_graph, result))
        
        result = hamiltonian_cycle_backtracking(self.complete_graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        self.assertTrue(self._is_valid_hamiltonian_cycle(self.complete_graph, result))
    
    def test_edge_cases(self):
        """
        Testa casos extremos.
        """
        # Grafo vazio
        result = hamiltonian_path_backtracking(self.empty_graph)
        self.assertEqual(result, [])
        
        # Grafo com um vértice
        result = hamiltonian_path_backtracking(self.single_vertex_graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        
        # Grafo None
        with self.assertRaises(TypeError):
            hamiltonian_path_backtracking(None)
    
    def test_optimized_hamiltonian_path(self):
        """
        Testa a versão otimizada do algoritmo.
        """
        # Compara resultados com implementação básica
        basic_result = hamiltonian_path_backtracking(self.valid_graph)
        optimized_result = hamiltonian_path_optimized(self.valid_graph)
        
        # Ambos devem encontrar um caminho válido (pode ser diferente)
        self.assertIsNotNone(basic_result)
        self.assertIsNotNone(optimized_result)
        self.assertTrue(self._is_valid_hamiltonian_path(self.valid_graph, basic_result))
        self.assertTrue(self._is_valid_hamiltonian_path(self.valid_graph, optimized_result))
        
        # Testa com grafo inválido
        basic_result = hamiltonian_path_backtracking(self.invalid_graph)
        optimized_result = hamiltonian_path_optimized(self.invalid_graph)
        
        self.assertIsNone(basic_result)
        self.assertIsNone(optimized_result)
    
    def test_memoized_hamiltonian_path(self):
        """
        Testa a versão com memoização.
        """
        # Compara resultados com implementação básica
        basic_result = hamiltonian_path_backtracking(self.valid_graph)
        memoized_result = hamiltonian_path_with_memoization(self.valid_graph)
        
        self.assertIsNotNone(basic_result)
        self.assertIsNotNone(memoized_result)
        self.assertTrue(self._is_valid_hamiltonian_path(self.valid_graph, basic_result))
        self.assertTrue(self._is_valid_hamiltonian_path(self.valid_graph, memoized_result))
        
        # Testa com grafo inválido
        basic_result = hamiltonian_path_backtracking(self.invalid_graph)
        memoized_result = hamiltonian_path_with_memoization(self.invalid_graph)
        
        self.assertIsNone(basic_result)
        self.assertIsNone(memoized_result)
    
    def test_solution_counting(self):
        """
        Testa a contagem de soluções.
        """
        # Grafo válido
        count = hamiltonian_path_count_solutions(self.valid_graph)
        self.assertGreater(count, 0)
        
        # Grafo inválido
        count = hamiltonian_path_count_solutions(self.invalid_graph)
        self.assertEqual(count, 0)
        
        # Grafo completo
        count = hamiltonian_path_count_solutions(self.complete_graph)
        self.assertGreater(count, 0)
    
    def test_all_solutions(self):
        """
        Testa a busca por todas as soluções.
        """
        # Grafo válido
        solutions = hamiltonian_path_all_solutions(self.valid_graph)
        self.assertGreater(len(solutions), 0)
        
        # Verifica se todas as soluções são válidas
        for solution in solutions:
            self.assertTrue(self._is_valid_hamiltonian_path(self.valid_graph, solution))
        
        # Grafo inválido
        solutions = hamiltonian_path_all_solutions(self.invalid_graph)
        self.assertEqual(len(solutions), 0)
    
    def test_complexity_analysis(self):
        """
        Testa a análise de complexidade.
        """
        analysis = analyze_hamiltonian_path_complexity(self.valid_graph)
        
        self.assertEqual(analysis['vertices'], 4)
        self.assertEqual(analysis['edges'], 4)
        self.assertIn('max_degree', analysis)
        self.assertIn('avg_degree', analysis)
        self.assertIn('min_degree', analysis)
        self.assertIn('worst_case_time', analysis)
        self.assertIn('space_complexity', analysis)
    
    def test_performance_comparison(self):
        """
        Testa o desempenho das diferentes implementações.
        """
        # Grafo de teste
        test_graph = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        
        # Mede tempo da implementação básica
        start_time = time.time()
        basic_result = hamiltonian_path_backtracking(test_graph)
        basic_time = time.time() - start_time
        
        # Mede tempo da implementação otimizada
        start_time = time.time()
        optimized_result = hamiltonian_path_optimized(test_graph)
        optimized_time = time.time() - start_time
        
        # Mede tempo da implementação com memoização
        start_time = time.time()
        memoized_result = hamiltonian_path_with_memoization(test_graph)
        memoized_time = time.time() - start_time
        
        # Verifica que todos os resultados são válidos
        self.assertIsNotNone(basic_result)
        self.assertIsNotNone(optimized_result)
        self.assertIsNotNone(memoized_result)
        
        # Verifica que os tempos são razoáveis (não infinitos)
        self.assertLess(basic_time, 10.0)
        self.assertLess(optimized_time, 10.0)
        self.assertLess(memoized_time, 10.0)
    
    def test_large_graphs(self):
        """
        Testa com grafos maiores.
        """
        # Grafo de 5 vértices
        large_graph = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        
        result = hamiltonian_path_backtracking(large_graph)
        if result:
            self.assertTrue(self._is_valid_hamiltonian_path(large_graph, result))
    
    def test_invalid_inputs(self):
        """
        Testa entradas inválidas.
        """
        # Grafo None
        with self.assertRaises(TypeError):
            hamiltonian_path_backtracking(None)
        
        # Grafo com valores inválidos
        invalid_graph = [
            [0, 2, 1],  # Valor 2 não é válido
            [2, 0, 1],
            [1, 1, 0]
        ]
        
        # Deve lidar graciosamente com entrada inválida
        result = hamiltonian_path_backtracking(invalid_graph)
        # Pode retornar None ou levantar exceção, dependendo da implementação
    
    def _is_valid_hamiltonian_path(self, graph: List[List[int]], path: List[int]) -> bool:
        """
        Verifica se um caminho é um caminho Hamiltoniano válido.
        
        Args:
            graph: Matriz de adjacência do grafo
            path: Lista de vértices no caminho
            
        Returns:
            True se o caminho é válido, False caso contrário
        """
        if not path:
            return len(graph) == 0
        
        V = len(graph)
        if len(path) != V:
            return False
        
        # Verifica se todos os vértices são únicos
        if len(set(path)) != V:
            return False
        
        # Verifica se vértices consecutivos são adjacentes
        for i in range(len(path) - 1):
            current = path[i]
            next_vertex = path[i + 1]
            if graph[current][next_vertex] != 1:
                return False
        
        return True
    
    def _is_valid_hamiltonian_cycle(self, graph: List[List[int]], path: List[int]) -> bool:
        """
        Verifica se um caminho é um ciclo Hamiltoniano válido.
        
        Args:
            graph: Matriz de adjacência do grafo
            path: Lista de vértices no ciclo
            
        Returns:
            True se o ciclo é válido, False caso contrário
        """
        if not self._is_valid_hamiltonian_path(graph, path):
            return False
        
        # Verifica se o último vértice se conecta ao primeiro
        if len(path) > 0:
            last_vertex = path[-1]
            first_vertex = path[0]
            return graph[last_vertex][first_vertex] == 1
        
        return True


class TestHamiltonianPathExamples(unittest.TestCase):
    """
    Testes baseados em exemplos específicos.
    """
    
    def test_wikipedia_example(self):
        """
        Testa exemplo do Wikipedia.
        """
        # Grafo simples com caminho Hamiltoniano
        graph = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        
        result = hamiltonian_path_backtracking(graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        
        # Verifica se o caminho é válido
        for i in range(len(result) - 1):
            current = result[i]
            next_vertex = result[i + 1]
            self.assertEqual(graph[current][next_vertex], 1)
    
    def test_hackerearth_example(self):
        """
        Testa exemplo do HackerEarth.
        """
        # Grafo com caminho Hamiltoniano
        graph = [
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]
        ]
        
        result = hamiltonian_path_backtracking(graph)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)
        
        # Verifica se o caminho é válido
        for i in range(len(result) - 1):
            current = result[i]
            next_vertex = result[i + 1]
            self.assertEqual(graph[current][next_vertex], 1)
    
    def _is_valid_hamiltonian_path(self, graph: List[List[int]], path: List[int]) -> bool:
        """
        Verifica se um caminho é um caminho Hamiltoniano válido.
        """
        V = len(graph)
        if len(path) != V:
            return False
        
        # Verifica se todos os vértices são únicos
        if len(set(path)) != V:
            return False
        
        # Verifica se vértices consecutivos são adjacentes
        for i in range(len(path) - 1):
            current = path[i]
            next_vertex = path[i + 1]
            if graph[current][next_vertex] != 1:
                return False
        
        return True


def run_performance_tests():
    """
    Executa testes de performance.
    """
    print("=== Testes de Performance ===")
    
    # Grafo de teste
    graph = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0]
    ]
    
    implementations = [
        ("Backtracking Básico", hamiltonian_path_backtracking),
        ("Backtracking Otimizado", hamiltonian_path_optimized),
        ("Com Memoização", hamiltonian_path_with_memoization)
    ]
    
    for name, func in implementations:
        start_time = time.time()
        result = func(graph)
        end_time = time.time()
        
        print(f"{name}: {end_time - start_time:.6f} segundos")
        print(f"Resultado: {result}")
        print()


if __name__ == "__main__":
    # Executa testes unitários
    unittest.main(verbosity=2, exit=False)
    
    # Executa testes de performance
    run_performance_tests() 