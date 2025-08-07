"""
Exemplo de Uso: Coloração de Grafos com Backtracking

Este arquivo demonstra como usar o algoritmo de coloração de grafos
implementado com backtracking para resolver problemas práticos.

Referências:
- InterviewBit: Graph Coloring Algorithm using Backtracking
- GeeksforGeeks: M-Coloring Problem
- TheAlgorithms/Python: coloring.py
"""

from typing import List, Optional
import time
from graph_coloring import (
    graph_coloring_backtracking,
    graph_coloring_optimized,
    graph_coloring_count_solutions,
    graph_coloring_all_solutions,
    graph_coloring_with_memoization,
    analyze_graph_coloring_complexity
)


def example_basic_coloring():
    """
    Exemplo básico de coloração de grafos.
    """
    print("=== Exemplo Básico: Coloração de Grafos ===\n")
    
    # Grafo simples: ciclo de 4 vértices
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
    
    # Testa com diferentes números de cores
    for m in [1, 2, 3]:
        result = graph_coloring_backtracking(graph, m)
        print(f"Com {m} cores: {result}")
        if result:
            print(f"Coloração válida: Vértices {list(range(len(result)))} → Cores {result}")
        else:
            print("Não é possível colorir com este número de cores")
        print()


def example_complex_graph():
    """
    Exemplo com grafo mais complexo que requer 3 cores.
    """
    print("=== Exemplo: Grafo Complexo ===\n")
    
    # Grafo que forma um triângulo com um vértice extra
    graph = [
        [0, 1, 1, 1],  # Vértice 0 conectado a 1, 2, 3
        [1, 0, 1, 0],  # Vértice 1 conectado a 0, 2
        [1, 1, 0, 1],  # Vértice 2 conectado a 0, 1, 3
        [1, 0, 1, 0]   # Vértice 3 conectado a 0, 2
    ]
    
    print("Grafo complexo:")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    # Testa diferentes números de cores
    for m in [2, 3, 4]:
        result = graph_coloring_backtracking(graph, m)
        print(f"Com {m} cores: {result}")
        if result:
            print(f"Coloração válida encontrada!")
            for i, color in enumerate(result):
                print(f"  Vértice {i} → Cor {color}")
        else:
            print("Não é possível colorir com este número de cores")
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
    
    m = 3
    
    print("Grafo de teste:")
    for i, row in enumerate(graph):
        print(f"Vértice {i}: {row}")
    print()
    
    # Testa diferentes implementações
    implementations = [
        ("Backtracking Básico", graph_coloring_backtracking),
        ("Backtracking Otimizado", graph_coloring_optimized),
        ("Com Memoização", graph_coloring_with_memoization)
    ]
    
    for name, func in implementations:
        start_time = time.time()
        result = func(graph, m)
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
    
    # Conta soluções para diferentes números de cores
    for m in [2, 3, 4]:
        count = graph_coloring_count_solutions(graph, m)
        print(f"Com {m} cores: {count} soluções")
        
        if count <= 10:  # Mostra todas as soluções se não forem muitas
            solutions = graph_coloring_all_solutions(graph, m)
            print("Todas as soluções:")
            for i, solution in enumerate(solutions):
                print(f"  Solução {i+1}: {solution}")
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
        analysis = analyze_graph_coloring_complexity(graph, 3)
        
        print(f"  Vértices: {analysis['vertices']}")
        print(f"  Arestas: {analysis['edges']}")
        print(f"  Grau máximo: {analysis['max_degree']}")
        print(f"  Grau médio: {analysis['avg_degree']:.2f}")
        print(f"  É esparso: {analysis['is_sparse']}")
        print(f"  É denso: {analysis['is_dense']}")
        print(f"  Limite superior do número cromático: {analysis['chromatic_number_upper_bound']}")
        print(f"  Limite inferior do número cromático: {analysis['chromatic_number_lower_bound']}")
        print(f"  Complexidade de tempo (pior caso): O({analysis['worst_case_time']})")
        print()


def example_practical_applications():
    """
    Demonstra aplicações práticas da coloração de grafos.
    """
    print("=== Aplicações Práticas ===\n")
    
    # 1. Problema do Sudoku (simplificado)
    print("1. Problema do Sudoku (simplificado):")
    print("   Cada célula é um vértice, células na mesma linha/coluna/bloco são adjacentes")
    print("   Cores representam números de 1 a 9")
    print()
    
    # 2. Coloração de mapas
    print("2. Coloração de Mapas:")
    print("   Cada país/estado é um vértice")
    print("   Países vizinhos são adjacentes")
    print("   Cores representam cores diferentes no mapa")
    print()
    
    # 3. Agendamento de exames
    print("3. Agendamento de Examens:")
    print("   Cada exame é um vértice")
    print("   Exames com estudantes em comum são adjacentes")
    print("   Cores representam horários diferentes")
    print()
    
    # 4. Alocação de registradores
    print("4. Alocação de Registradores:")
    print("   Cada variável é um vértice")
    print("   Variáveis usadas simultaneamente são adjacentes")
    print("   Cores representam registradores diferentes")
    print()


def run_all_examples():
    """
    Executa todos os exemplos.
    """
    print("=" * 60)
    print("EXEMPLOS: COLORAÇÃO DE GRAFOS COM BACKTRACKING")
    print("=" * 60)
    print()
    
    example_basic_coloring()
    example_complex_graph()
    example_performance_comparison()
    example_solution_counting()
    example_complexity_analysis()
    example_practical_applications()
    
    print("=" * 60)
    print("FIM DOS EXEMPLOS")
    print("=" * 60)


if __name__ == "__main__":
    run_all_examples() 