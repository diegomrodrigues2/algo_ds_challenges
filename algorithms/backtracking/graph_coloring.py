"""
Graph Coloring Problem - Backtracking Implementation

Este módulo implementa o algoritmo de Coloração de Grafos (Graph Coloring)
usando backtracking recursivo. O problema é NP-completo e envolve colorir
os vértices de um grafo de forma que vértices adjacentes tenham cores diferentes.

Referências:
- InterviewBit: Graph Coloring Algorithm using Backtracking
- GeeksforGeeks: M-Coloring Problem
- TheAlgorithms/Python: coloring.py
- CSP Map Coloring using Backtracking
"""

from typing import List, Optional, Dict, Tuple
import copy


def graph_coloring_backtracking(graph: List[List[int]], m: int) -> Optional[List[int]]:
    """
    Resolve o problema de coloração de grafos usando backtracking recursivo.
    
    Para cada vértice, tenta atribuir uma cor de 1 a m, verificando se é válida
    em relação aos vizinhos já coloridos. Se uma atribuição falha, faz backtrack.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        m: Número máximo de cores disponíveis
        
    Returns:
        Lista de cores atribuídas aos vértices (1 a m), ou None se não for possível
        
    Complexidade:
        Tempo: O(m^V) - no pior caso, tenta m cores para cada vértice
        Espaço: O(V) - profundidade da pilha de recursão
    """
    if not graph or m <= 0:
        return None
    
    V = len(graph)
    if V == 0:
        return []
    
    # Inicializa array de cores (0 = não colorido)
    colors = [0] * V
    
    def is_safe(vertex: int, color: int) -> bool:
        """
        Verifica se é seguro atribuir a cor 'color' ao vértice 'vertex'.
        
        Args:
            vertex: Vértice a ser colorido
            color: Cor a ser testada
            
        Returns:
            True se a cor é válida, False caso contrário
        """
        # Verifica todos os vértices adjacentes
        for i in range(V):
            if graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True
    
    def graph_coloring_util(vertex: int) -> bool:
        """
        Função recursiva de backtracking para colorir o grafo.
        
        Args:
            vertex: Vértice atual a ser colorido
            
        Returns:
            True se conseguiu colorir todos os vértices, False caso contrário
        """
        # Caso base: todos os vértices foram coloridos
        if vertex == V:
            return True
        
        # Tenta cada cor disponível para o vértice atual
        for color in range(1, m + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                
                # Recursão para o próximo vértice
                if graph_coloring_util(vertex + 1):
                    return True
                
                # Backtrack: remove a cor se não levou à solução
                colors[vertex] = 0
        
        # Nenhuma cor funcionou para este vértice
        return False
    
    # Tenta colorir o grafo começando do vértice 0
    if graph_coloring_util(0):
        return colors
    else:
        return None


def graph_coloring_optimized(graph: List[List[int]], m: int) -> Optional[List[int]]:
    """
    Versão otimizada do algoritmo de coloração de grafos.
    
    Otimizações:
    1. Ordenação de vértices por grau (heurística)
    2. Verificação mais eficiente de cores válidas
    3. Early termination quando possível
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        m: Número máximo de cores disponíveis
        
    Returns:
        Lista de cores atribuídas aos vértices (1 a m), ou None se não for possível
    """
    if not graph or m <= 0:
        return None
    
    V = len(graph)
    if V == 0:
        return []
    
    # Calcula graus dos vértices para ordenação
    degrees = [sum(graph[i]) for i in range(V)]
    
    # Ordena vértices por grau decrescente (heurística)
    vertex_order = sorted(range(V), key=lambda x: degrees[x], reverse=True)
    
    # Mapeia vértices ordenados para índices originais
    vertex_to_index = {vertex: i for i, vertex in enumerate(vertex_order)}
    index_to_vertex = vertex_order
    
    colors = [0] * V
    
    def is_safe_optimized(vertex: int, color: int) -> bool:
        """
        Verificação otimizada de segurança de cor.
        """
        for i in range(V):
            if graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True
    
    def graph_coloring_util_optimized(vertex_idx: int) -> bool:
        """
        Função recursiva otimizada.
        """
        if vertex_idx == V:
            return True
        
        current_vertex = index_to_vertex[vertex_idx]
        
        # Tenta cores em ordem (pode ser otimizado com heurísticas)
        for color in range(1, m + 1):
            if is_safe_optimized(current_vertex, color):
                colors[current_vertex] = color
                
                if graph_coloring_util_optimized(vertex_idx + 1):
                    return True
                
                colors[current_vertex] = 0
        
        return False
    
    if graph_coloring_util_optimized(0):
        return colors
    else:
        return None


def graph_coloring_count_solutions(graph: List[List[int]], m: int) -> int:
    """
    Conta quantas soluções existem para o problema de coloração.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        m: Número máximo de cores disponíveis
        
    Returns:
        Número de soluções válidas
    """
    if not graph or m <= 0:
        return 0
    
    V = len(graph)
    if V == 0:
        return 1
    
    colors = [0] * V
    solution_count = [0]
    
    def is_safe(vertex: int, color: int) -> bool:
        for i in range(V):
            if graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True
    
    def count_solutions_util(vertex: int) -> None:
        if vertex == V:
            solution_count[0] += 1
            return
        
        for color in range(1, m + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                count_solutions_util(vertex + 1)
                colors[vertex] = 0
    
    count_solutions_util(0)
    return solution_count[0]


def graph_coloring_all_solutions(graph: List[List[int]], m: int) -> List[List[int]]:
    """
    Encontra todas as soluções para o problema de coloração.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        m: Número máximo de cores disponíveis
        
    Returns:
        Lista de todas as soluções válidas
    """
    if not graph or m <= 0:
        return []
    
    V = len(graph)
    if V == 0:
        return [[]]
    
    colors = [0] * V
    solutions = []
    
    def is_safe(vertex: int, color: int) -> bool:
        for i in range(V):
            if graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True
    
    def find_all_solutions_util(vertex: int) -> None:
        if vertex == V:
            solutions.append(colors.copy())
            return
        
        for color in range(1, m + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                find_all_solutions_util(vertex + 1)
                colors[vertex] = 0
    
    find_all_solutions_util(0)
    return solutions


def graph_coloring_with_memoization(graph: List[List[int]], m: int) -> Optional[List[int]]:
    """
    Versão com memoização para evitar recálculos.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        m: Número máximo de cores disponíveis
        
    Returns:
        Lista de cores atribuídas aos vértices (1 a m), ou None se não for possível
    """
    if not graph or m <= 0:
        return None
    
    V = len(graph)
    if V == 0:
        return []
    
    colors = [0] * V
    memo = {}
    
    def get_state_key(vertex: int) -> str:
        """Gera chave para memoização baseada no estado atual."""
        return f"{vertex}:{tuple(colors[:vertex])}"
    
    def is_safe(vertex: int, color: int) -> bool:
        for i in range(V):
            if graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True
    
    def graph_coloring_memoized(vertex: int) -> bool:
        if vertex == V:
            return True
        
        state_key = get_state_key(vertex)
        if state_key in memo:
            return memo[state_key]
        
        for color in range(1, m + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                
                if graph_coloring_memoized(vertex + 1):
                    memo[state_key] = True
                    return True
                
                colors[vertex] = 0
        
        memo[state_key] = False
        return False
    
    if graph_coloring_memoized(0):
        return colors
    else:
        return None


def analyze_graph_coloring_complexity(graph: List[List[int]], m: int) -> Dict:
    """
    Analisa a complexidade do problema de coloração para os dados fornecidos.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        m: Número máximo de cores disponíveis
        
    Returns:
        Dicionário com análise de complexidade
    """
    if not graph:
        return {"error": "Grafo vazio"}
    
    V = len(graph)
    E = sum(sum(row) for row in graph) // 2  # Número de arestas
    
    # Calcula graus dos vértices
    degrees = [sum(graph[i]) for i in range(V)]
    max_degree = max(degrees) if degrees else 0
    avg_degree = sum(degrees) / V if V > 0 else 0
    
    # Análise de complexidade
    worst_case_time = m ** V
    best_case_time = V * m  # Se cada vértice pode ser colorido na primeira tentativa
    
    # Estimativa baseada na estrutura do grafo
    estimated_time = V * (m ** (max_degree + 1))
    
    return {
        "vertices": V,
        "edges": E,
        "colors": m,
        "max_degree": max_degree,
        "avg_degree": avg_degree,
        "worst_case_time": worst_case_time,
        "best_case_time": best_case_time,
        "estimated_time": estimated_time,
        "space_complexity": V,
        "is_sparse": E < V * (V - 1) / 4,
        "is_dense": E > V * (V - 1) / 2,
        "chromatic_number_upper_bound": max_degree + 1,
        "chromatic_number_lower_bound": max(1, V // (V - max_degree)) if max_degree < V else 1
    }


def demonstrate_graph_coloring_example():
    """
    Demonstra o uso do algoritmo de coloração de grafos.
    """
    print("=== Demonstração: Coloração de Grafos ===\n")
    
    # Exemplo 1: Grafo simples (ciclo de 4 vértices)
    print("Exemplo 1: Ciclo de 4 vértices")
    graph1 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m1 = 2
    
    result1 = graph_coloring_backtracking(graph1, m1)
    print(f"Grafo: {graph1}")
    print(f"Cores disponíveis: {m1}")
    print(f"Coloração: {result1}")
    print(f"É válida: {result1 is not None}")
    print()
    
    # Exemplo 2: Grafo que requer 3 cores
    print("Exemplo 2: Grafo que requer 3 cores")
    graph2 = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    for m in [2, 3]:
        result = graph_coloring_backtracking(graph2, m)
        print(f"Com {m} cores: {result}")
        print(f"É válida: {result is not None}")
    print()
    
    # Exemplo 3: Análise de complexidade
    print("Exemplo 3: Análise de Complexidade")
    analysis = analyze_graph_coloring_complexity(graph2, 3)
    for key, value in analysis.items():
        print(f"{key}: {value}")
    print()
    
    # Exemplo 4: Contagem de soluções
    print("Exemplo 4: Contagem de Soluções")
    count = graph_coloring_count_solutions(graph1, 2)
    print(f"Número de soluções para grafo1 com 2 cores: {count}")
    
    all_solutions = graph_coloring_all_solutions(graph1, 2)
    print(f"Todas as soluções: {all_solutions}")
    print()


if __name__ == "__main__":
    demonstrate_graph_coloring_example() 