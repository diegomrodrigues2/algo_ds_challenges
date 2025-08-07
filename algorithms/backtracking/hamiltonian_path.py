"""
Hamiltonian Path Problem - Backtracking Implementation

Este módulo implementa o algoritmo de Caminho Hamiltoniano (Hamiltonian Path)
usando backtracking recursivo. O problema é NP-completo e envolve encontrar
um caminho que visite todos os vértices do grafo exatamente uma vez.

Referências:
- Wikipedia: Hamiltonian path problem
- HackerEarth: Hamiltonian Path Tutorial
- TheAlgorithms/Python: hamiltonian_cycle.py
- NetworkX Implementation: mikkelam/hamilton.py
"""

from typing import List, Optional, Dict, Tuple
import copy


def hamiltonian_path_backtracking(graph: List[List[int]]) -> Optional[List[int]]:
    """
    Resolve o problema do Caminho Hamiltoniano usando backtracking recursivo.
    
    Constrói um caminho passo a passo, tentando adicionar vértices adjacentes
    que ainda não foram visitados. Se um caminho não pode ser estendido,
    faz backtrack e tenta outro vizinho.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        
    Returns:
        Lista com a ordem dos vértices no caminho Hamiltoniano, ou None se não existir
        
    Complexidade:
        Tempo: O(V!) - no pior caso, explora todas as permutações possíveis
        Espaço: O(V) - profundidade da pilha de recursão
    """
    if not graph:
        return None
    
    V = len(graph)
    if V == 0:
        return []
    
    # Inicializa array de vértices visitados
    visited = [False] * V
    path = []
    
    def hamiltonian_path_util(vertex: int, path_count: int) -> bool:
        """
        Função recursiva de backtracking para encontrar o caminho Hamiltoniano.
        
        Args:
            vertex: Vértice atual sendo visitado
            path_count: Número de vértices já visitados
            
        Returns:
            True se encontrou um caminho Hamiltoniano, False caso contrário
        """
        # Marca o vértice atual como visitado
        visited[vertex] = True
        path.append(vertex)
        
        # Caso base: todos os vértices foram visitados
        if path_count == V:
            return True
        
        # Tenta todos os vértices adjacentes
        for next_vertex in range(V):
            if (graph[vertex][next_vertex] == 1 and 
                not visited[next_vertex]):
                
                # Recursão para o próximo vértice
                if hamiltonian_path_util(next_vertex, path_count + 1):
                    return True
        
        # Backtrack: remove o vértice do caminho se não levou à solução
        visited[vertex] = False
        path.pop()
        return False
    
    # Tenta começar de cada vértice
    for start_vertex in range(V):
        if hamiltonian_path_util(start_vertex, 1):
            return path.copy()
    
    return None


def hamiltonian_cycle_backtracking(graph: List[List[int]]) -> Optional[List[int]]:
    """
    Resolve o problema do Ciclo Hamiltoniano usando backtracking recursivo.
    
    Similar ao caminho Hamiltoniano, mas exige que o último vértice se conecte
    ao primeiro vértice do caminho.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        
    Returns:
        Lista com a ordem dos vértices no ciclo Hamiltoniano, ou None se não existir
    """
    if not graph:
        return None
    
    V = len(graph)
    if V == 0:
        return []
    
    # Inicializa array de vértices visitados
    visited = [False] * V
    path = []
    
    def hamiltonian_cycle_util(vertex: int, path_count: int) -> bool:
        """
        Função recursiva de backtracking para encontrar o ciclo Hamiltoniano.
        """
        # Marca o vértice atual como visitado
        visited[vertex] = True
        path.append(vertex)
        
        # Caso base: todos os vértices foram visitados
        if path_count == V:
            # Verifica se o último vértice se conecta ao primeiro
            if graph[vertex][path[0]] == 1:
                return True
            else:
                # Backtrack se não forma um ciclo
                visited[vertex] = False
                path.pop()
                return False
        
        # Tenta todos os vértices adjacentes
        for next_vertex in range(V):
            if (graph[vertex][next_vertex] == 1 and 
                not visited[next_vertex]):
                
                # Recursão para o próximo vértice
                if hamiltonian_cycle_util(next_vertex, path_count + 1):
                    return True
        
        # Backtrack: remove o vértice do caminho se não levou à solução
        visited[vertex] = False
        path.pop()
        return False
    
    # Tenta começar de cada vértice
    for start_vertex in range(V):
        if hamiltonian_cycle_util(start_vertex, 1):
            return path.copy()
    
    return None


def hamiltonian_path_optimized(graph: List[List[int]]) -> Optional[List[int]]:
    """
    Versão otimizada do algoritmo de Caminho Hamiltoniano.
    
    Otimizações:
    1. Ordenação de vértices por grau (heurística)
    2. Verificação mais eficiente de adjacência
    3. Early termination quando possível
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        
    Returns:
        Lista com a ordem dos vértices no caminho Hamiltoniano, ou None se não existir
    """
    if not graph:
        return None
    
    V = len(graph)
    if V == 0:
        return []
    
    # Calcula graus dos vértices para ordenação
    degrees = [sum(graph[i]) for i in range(V)]
    
    # Ordena vértices por grau decrescente (heurística)
    vertex_order = sorted(range(V), key=lambda x: degrees[x], reverse=True)
    
    visited = [False] * V
    path = []
    
    def hamiltonian_path_util_optimized(vertex: int, path_count: int) -> bool:
        """
        Função recursiva otimizada.
        """
        visited[vertex] = True
        path.append(vertex)
        
        if path_count == V:
            return True
        
        # Tenta vértices adjacentes em ordem de grau
        for next_vertex in vertex_order:
            if (graph[vertex][next_vertex] == 1 and 
                not visited[next_vertex]):
                
                if hamiltonian_path_util_optimized(next_vertex, path_count + 1):
                    return True
        
        visited[vertex] = False
        path.pop()
        return False
    
    # Tenta começar dos vértices de maior grau primeiro
    for start_vertex in vertex_order:
        if hamiltonian_path_util_optimized(start_vertex, 1):
            return path.copy()
    
    return None


def hamiltonian_path_count_solutions(graph: List[List[int]]) -> int:
    """
    Conta quantas soluções existem para o problema do Caminho Hamiltoniano.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        
    Returns:
        Número de caminhos Hamiltonianos válidos
    """
    if not graph:
        return 0
    
    V = len(graph)
    if V == 0:
        return 1
    
    visited = [False] * V
    solution_count = [0]
    
    def count_solutions_util(vertex: int, path_count: int) -> None:
        visited[vertex] = True
        
        if path_count == V:
            solution_count[0] += 1
            visited[vertex] = False
            return
        
        for next_vertex in range(V):
            if (graph[vertex][next_vertex] == 1 and 
                not visited[next_vertex]):
                count_solutions_util(next_vertex, path_count + 1)
        
        visited[vertex] = False
    
    # Conta soluções começando de cada vértice
    for start_vertex in range(V):
        count_solutions_util(start_vertex, 1)
    
    return solution_count[0]


def hamiltonian_path_all_solutions(graph: List[List[int]]) -> List[List[int]]:
    """
    Encontra todas as soluções para o problema do Caminho Hamiltoniano.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        
    Returns:
        Lista de todos os caminhos Hamiltonianos válidos
    """
    if not graph:
        return []
    
    V = len(graph)
    if V == 0:
        return [[]]
    
    visited = [False] * V
    solutions = []
    
    def find_all_solutions_util(vertex: int, path_count: int, current_path: List[int]) -> None:
        visited[vertex] = True
        current_path.append(vertex)
        
        if path_count == V:
            solutions.append(current_path.copy())
            visited[vertex] = False
            current_path.pop()
            return
        
        for next_vertex in range(V):
            if (graph[vertex][next_vertex] == 1 and 
                not visited[next_vertex]):
                find_all_solutions_util(next_vertex, path_count + 1, current_path)
        
        visited[vertex] = False
        current_path.pop()
    
    # Encontra soluções começando de cada vértice
    for start_vertex in range(V):
        find_all_solutions_util(start_vertex, 1, [])
    
    return solutions


def hamiltonian_path_with_memoization(graph: List[List[int]]) -> Optional[List[int]]:
    """
    Versão com memoização para evitar recálculos.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        
    Returns:
        Lista com a ordem dos vértices no caminho Hamiltoniano, ou None se não existir
    """
    if not graph:
        return None
    
    V = len(graph)
    if V == 0:
        return []
    
    visited = [False] * V
    path = []
    memo = {}
    
    def get_state_key(vertex: int, path_count: int) -> str:
        """Gera chave para memoização baseada no estado atual."""
        return f"{vertex}:{path_count}:{tuple(visited)}"
    
    def hamiltonian_path_memoized(vertex: int, path_count: int) -> bool:
        if path_count == V:
            return True
        
        state_key = get_state_key(vertex, path_count)
        if state_key in memo:
            return memo[state_key]
        
        visited[vertex] = True
        path.append(vertex)
        
        for next_vertex in range(V):
            if (graph[vertex][next_vertex] == 1 and 
                not visited[next_vertex]):
                
                if hamiltonian_path_memoized(next_vertex, path_count + 1):
                    memo[state_key] = True
                    return True
        
        visited[vertex] = False
        path.pop()
        memo[state_key] = False
        return False
    
    # Tenta começar de cada vértice
    for start_vertex in range(V):
        if hamiltonian_path_memoized(start_vertex, 1):
            return path.copy()
    
    return None


def analyze_hamiltonian_path_complexity(graph: List[List[int]]) -> Dict:
    """
    Analisa a complexidade do problema do Caminho Hamiltoniano para os dados fornecidos.
    
    Args:
        graph: Matriz de adjacência do grafo (V x V)
        
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
    min_degree = min(degrees) if degrees else 0
    
    # Análise de complexidade
    worst_case_time = 1
    for i in range(V):
        worst_case_time *= (V - i)  # V! = V × (V-1) × ... × 1
    
    best_case_time = V  # Se encontrar rapidamente
    
    # Estimativa baseada na estrutura do grafo
    estimated_time = V * (avg_degree ** (V - 1))
    
    return {
        "vertices": V,
        "edges": E,
        "max_degree": max_degree,
        "avg_degree": avg_degree,
        "min_degree": min_degree,
        "worst_case_time": worst_case_time,
        "best_case_time": best_case_time,
        "estimated_time": estimated_time,
        "space_complexity": V,
        "is_sparse": E < V * (V - 1) / 4,
        "is_dense": E > V * (V - 1) / 2,
        "is_complete": E == V * (V - 1) / 2,
        "has_hamiltonian_path_necessary_condition": min_degree >= 1,
        "has_hamiltonian_cycle_necessary_condition": min_degree >= 2
    }


def demonstrate_hamiltonian_path_example():
    """
    Demonstra o uso do algoritmo do Caminho Hamiltoniano.
    """
    print("=== Demonstração: Caminho Hamiltoniano ===\n")
    
    # Exemplo 1: Grafo com caminho Hamiltoniano
    print("Exemplo 1: Grafo com caminho Hamiltoniano")
    graph1 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    result1 = hamiltonian_path_backtracking(graph1)
    print(f"Grafo: {graph1}")
    print(f"Caminho Hamiltoniano: {result1}")
    print(f"É válido: {result1 is not None}")
    print()
    
    # Exemplo 2: Grafo sem caminho Hamiltoniano
    print("Exemplo 2: Grafo sem caminho Hamiltoniano")
    graph2 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    
    result2 = hamiltonian_path_backtracking(graph2)
    print(f"Grafo: {graph2}")
    print(f"Caminho Hamiltoniano: {result2}")
    print(f"É válido: {result2 is not None}")
    print()
    
    # Exemplo 3: Ciclo Hamiltoniano
    print("Exemplo 3: Ciclo Hamiltoniano")
    result3 = hamiltonian_cycle_backtracking(graph1)
    print(f"Ciclo Hamiltoniano: {result3}")
    print(f"É válido: {result3 is not None}")
    print()
    
    # Exemplo 4: Análise de complexidade
    print("Exemplo 4: Análise de Complexidade")
    analysis = analyze_hamiltonian_path_complexity(graph1)
    for key, value in analysis.items():
        print(f"{key}: {value}")
    print()
    
    # Exemplo 5: Contagem de soluções
    print("Exemplo 5: Contagem de Soluções")
    count = hamiltonian_path_count_solutions(graph1)
    print(f"Número de caminhos Hamiltonianos: {count}")
    
    all_solutions = hamiltonian_path_all_solutions(graph1)
    print(f"Todos os caminhos: {all_solutions}")
    print()


if __name__ == "__main__":
    demonstrate_hamiltonian_path_example() 