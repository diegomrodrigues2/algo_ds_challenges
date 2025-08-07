"""
Exemplo de Uso: Caminho Hamiltoniano com Backtracking

Este arquivo demonstra como usar o algoritmo do Caminho Hamiltoniano
implementado com backtracking para resolver problemas práticos.

Referências:
- Wikipedia: Hamiltonian path problem
- HackerEarth: Hamiltonian Path Tutorial
- TheAlgorithms/Python: hamiltonian_cycle.py
- NetworkX Implementation: mikkelam/hamilton.py
"""

from typing import List, Optional
import time
from hamiltonian_path import (
    hamiltonian_path_backtracking,
    hamiltonian_cycle_backtracking,
    hamiltonian_path_optimized,
    hamiltonian_path_count_solutions,
    hamiltonian_path_all_solutions,
    hamiltonian_path_with_memoization,
    analyze_hamiltonian_path_complexity
)


def example_basic_hamiltonian_path():
    """
    Exemplo básico do Caminho Hamiltoniano.
    """
    print("=== Exemplo Básico: Caminho Hamiltoniano ===\n")
    
    # Grafo com caminho Hamiltoniano (ciclo de 4 vértices)
    graph = [
        [0, 1, 0, 1],  # Vértice 0 conectado a 1 e 3
        [1, 0, 1, 0],  # Vértice 1 conectado a 0 e 2
        [0, 1, 0, 1],  # Vértice 2 conectado a 1 e 3
        [1, 0, 1, 0]   # Vértice 3 conectado a 0 e 2
    ]
    
    print("Grafo (matriz de adjacência):")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    # Encontra caminho Hamiltoniano
    result = hamiltonian_path_backtracking(graph)
    print(f"Caminho Hamiltoniano: {result}")
    if result:
        print(f"Sequência de vértices: {' → '.join(map(str, result))}")
        print("Verificação:")
        for i in range(len(result) - 1):
            current = result[i]
            next_vertex = result[i + 1]
            print(f"  {current} → {next_vertex}: {'✓' if graph[current][next_vertex] == 1 else '✗'}")
    else:
        print("Não existe caminho Hamiltoniano neste grafo")
    print()


def example_hamiltonian_cycle():
    """
    Exemplo de Ciclo Hamiltoniano.
    """
    print("=== Exemplo: Ciclo Hamiltoniano ===\n")
    
    # Grafo que forma um ciclo completo
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    print("Grafo para ciclo Hamiltoniano:")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    # Encontra ciclo Hamiltoniano
    result = hamiltonian_cycle_backtracking(graph)
    print(f"Ciclo Hamiltoniano: {result}")
    if result:
        print(f"Sequência de vértices: {' → '.join(map(str, result))} → {result[0]}")
        print("Verificação:")
        for i in range(len(result)):
            current = result[i]
            next_vertex = result[(i + 1) % len(result)]
            print(f"  {current} → {next_vertex}: {'✓' if graph[current][next_vertex] == 1 else '✗'}")
    else:
        print("Não existe ciclo Hamiltoniano neste grafo")
    print()


def example_no_hamiltonian_path():
    """
    Exemplo de grafo sem caminho Hamiltoniano.
    """
    print("=== Exemplo: Grafo sem Caminho Hamiltoniano ===\n")
    
    # Grafo com vértice isolado
    graph = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]  # Vértice 3 isolado
    ]
    
    print("Grafo sem caminho Hamiltoniano:")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    result = hamiltonian_path_backtracking(graph)
    print(f"Caminho Hamiltoniano: {result}")
    print("Razão: Vértice 3 está isolado, impossibilitando visitar todos os vértices")
    print()


def example_performance_comparison():
    """
    Compara o desempenho das diferentes implementações.
    """
    print("=== Comparação de Desempenho ===\n")
    
    # Grafo de teste
    graph = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0]
    ]
    
    print("Grafo de teste:")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    # Testa diferentes implementações
    implementations = [
        ("Backtracking Básico", hamiltonian_path_backtracking),
        ("Backtracking Otimizado", hamiltonian_path_optimized),
        ("Com Memoização", hamiltonian_path_with_memoization)
    ]
    
    for name, func in implementations:
        start_time = time.time()
        result = func(graph)
        end_time = time.time()
        
        print(f"{name}:")
        print(f"  Tempo: {end_time - start_time:.6f} segundos")
        print(f"  Resultado: {result}")
        print()


def example_solution_counting():
    """
    Demonstra a contagem de soluções.
    """
    print("=== Contagem de Soluções ===\n")
    
    # Grafo simples
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    print("Grafo para contagem:")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    # Conta soluções
    count = hamiltonian_path_count_solutions(graph)
    print(f"Número de caminhos Hamiltonianos: {count}")
    
    # Mostra todas as soluções se não forem muitas
    if count <= 10:
        all_solutions = hamiltonian_path_all_solutions(graph)
        print("Todos os caminhos:")
        for i, solution in enumerate(all_solutions):
            print(f"  Caminho {i+1}: {' → '.join(map(str, solution))}")
    print()


def example_complexity_analysis():
    """
    Demonstra a análise de complexidade.
    """
    print("=== Análise de Complexidade ===\n")
    
    # Diferentes grafos para análise
    graphs = [
        ("Grafo Pequeno", [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]),
        ("Grafo Médio", [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]),
        ("Grafo Grande", [
            [0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 0]
        ])
    ]
    
    for name, graph in graphs:
        print(f"{name}:")
        analysis = analyze_hamiltonian_path_complexity(graph)
        
        print(f"  Vértices: {analysis['vertices']}")
        print(f"  Arestas: {analysis['edges']}")
        print(f"  Grau máximo: {analysis['max_degree']}")
        print(f"  Grau médio: {analysis['avg_degree']:.2f}")
        print(f"  Grau mínimo: {analysis['min_degree']}")
        print(f"  É esparso: {analysis['is_sparse']}")
        print(f"  É denso: {analysis['is_dense']}")
        print(f"  É completo: {analysis['is_complete']}")
        print(f"  Condição necessária para caminho: {analysis['has_hamiltonian_path_necessary_condition']}")
        print(f"  Condição necessária para ciclo: {analysis['has_hamiltonian_cycle_necessary_condition']}")
        print(f"  Complexidade de tempo (pior caso): O({analysis['worst_case_time']})")
        print()


def example_practical_applications():
    """
    Demonstra aplicações práticas do Caminho Hamiltoniano.
    """
    print("=== Aplicações Práticas ===\n")
    
    # 1. Problema do Caixeiro Viajante (TSP)
    print("1. Problema do Caixeiro Viajante (TSP):")
    print("   Encontrar rota mais curta visitando todas as cidades uma vez")
    print("   Caminho Hamiltoniano com custos mínimos")
    print()
    
    # 2. Sequenciamento de DNA
    print("2. Sequenciamento de DNA:")
    print("   Reconstruir sequência genética a partir de fragmentos")
    print("   Fragmentos são vértices, sobreposições são arestas")
    print()
    
    # 3. Design de Circuitos
    print("3. Design de Circuitos:")
    print("   Conectar componentes sem cruzar fios")
    print("   Componentes são vértices, conexões são arestas")
    print()
    
    # 4. Agendamento de Tarefas
    print("4. Agendamento de Tarefas:")
    print("   Ordenar tarefas com dependências")
    print("   Tarefas são vértices, dependências são arestas")
    print()
    
    # 5. Roteamento de Pacotes
    print("5. Roteamento de Pacotes:")
    print("   Encontrar rota ótima em rede de computadores")
    print("   Nós são vértices, links são arestas")
    print()


def example_networkx_style():
    """
    Demonstra uso similar ao NetworkX.
    """
    print("=== Estilo NetworkX ===\n")
    
    # Simula representação de grafo estilo NetworkX
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)]
    V = 4
    
    # Converte para matriz de adjacência
    graph = [[0] * V for _ in range(V)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1  # Grafo não direcionado
    
    print("Grafo representado por arestas:")
    print(f"Arestas: {edges}")
    print()
    
    print("Matriz de adjacência:")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    # Encontra caminho Hamiltoniano
    result = hamiltonian_path_backtracking(graph)
    print(f"Caminho Hamiltoniano: {result}")
    if result:
        print(f"Sequência: {' → '.join(map(str, result))}")
    print()


def run_all_examples():
    """
    Executa todos os exemplos.
    """
    print("=" * 60)
    print("EXEMPLOS: CAMINHO HAMILTONIANO COM BACKTRACKING")
    print("=" * 60)
    print()
    
    example_basic_hamiltonian_path()
    example_hamiltonian_cycle()
    example_no_hamiltonian_path()
    example_performance_comparison()
    example_solution_counting()
    example_complexity_analysis()
    example_practical_applications()
    example_networkx_style()
    
    print("=" * 60)
    print("FIM DOS EXEMPLOS")
    print("=" * 60)


if __name__ == "__main__":
    run_all_examples() 