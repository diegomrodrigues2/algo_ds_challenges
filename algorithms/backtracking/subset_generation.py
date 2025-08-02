"""
Desafio 16: Geração de Subconjuntos (Subset Generation)

Este módulo implementa algoritmos de backtracking para gerar todos os subconjuntos
de um conjunto dado, também conhecido como "conjunto das partes" ou "power set".

Vínculo Conceitual: Relacionado à estrutura de decisão do problema Subset Sum,
mas com o objetivo de enumerar todas as possibilidades.

Referências:
- Erickson, "Algorithms", Chapter 2, Section 2.3 (estrutura de decisão)
- GeeksforGeeks: Backtracking to find all subsets
- Bitmask approach for iterative generation
"""

from typing import List, Set, Tuple, Optional
import time
from collections import defaultdict


def subset_generation_backtracking(elements: List) -> List[List]:
    """
    Gera todos os subconjuntos usando backtracking recursivo.
    
    Para cada elemento, a recursão explora dois caminhos:
    1. Incluir o elemento no subconjunto atual
    2. Excluir o elemento do subconjunto atual
    
    Args:
        elements: Lista de elementos para gerar subconjuntos
        
    Returns:
        Lista de todos os subconjuntos possíveis
        
    Time Complexity: O(2^n)
    Space Complexity: O(n) para recursão + O(2^n) para resultado
    """
    if not elements:
        return [[]]
    
    result = []
    
    def backtrack(index: int, current_subset: List) -> None:
        # Base case: chegamos ao final dos elementos
        if index == len(elements):
            result.append(current_subset[:])
            return
        
        # Opção 1: Excluir o elemento atual
        backtrack(index + 1, current_subset)
        
        # Opção 2: Incluir o elemento atual
        current_subset.append(elements[index])
        backtrack(index + 1, current_subset)
        current_subset.pop()  # Backtrack
    
    backtrack(0, [])
    return result


def subset_generation_iterative_bitmask(elements: List) -> List[List]:
    """
    Gera todos os subconjuntos usando abordagem iterativa com bitmask.
    
    Cada inteiro de 0 a 2^n - 1 representa um subconjunto:
    - O k-ésimo bit indica se o k-ésimo elemento está presente
    
    Args:
        elements: Lista de elementos para gerar subconjuntos
        
    Returns:
        Lista de todos os subconjuntos possíveis
        
    Time Complexity: O(n * 2^n)
    Space Complexity: O(2^n) para resultado
    """
    n = len(elements)
    result = []
    
    # Para cada número de 0 a 2^n - 1
    for i in range(2**n):
        subset = []
        # Para cada bit do número
        for j in range(n):
            # Se o j-ésimo bit está ligado, incluir o j-ésimo elemento
            if i & (1 << j):
                subset.append(elements[j])
        result.append(subset)
    
    return result


def subset_generation_with_constraints(elements: List, min_size: int = 0, max_size: Optional[int] = None) -> List[List]:
    """
    Gera subconjuntos com restrições de tamanho usando backtracking.
    
    Args:
        elements: Lista de elementos para gerar subconjuntos
        min_size: Tamanho mínimo dos subconjuntos (padrão: 0)
        max_size: Tamanho máximo dos subconjuntos (padrão: sem limite)
        
    Returns:
        Lista de subconjuntos que satisfazem as restrições
    """
    if max_size is None:
        max_size = len(elements)
    
    result = []
    
    def backtrack(index: int, current_subset: List) -> None:
        # Verificar se o subconjunto atual satisfaz as restrições
        if min_size <= len(current_subset) <= max_size:
            result.append(current_subset[:])
        
        # Se chegamos ao final ou atingimos o tamanho máximo
        if index == len(elements) or len(current_subset) >= max_size:
            return
        
        # Opção 1: Excluir o elemento atual
        backtrack(index + 1, current_subset)
        
        # Opção 2: Incluir o elemento atual
        current_subset.append(elements[index])
        backtrack(index + 1, current_subset)
        current_subset.pop()  # Backtrack
    
    backtrack(0, [])
    return result


def subset_generation_with_sum_constraint(elements: List, target_sum: int) -> List[List]:
    """
    Gera subconjuntos que somam exatamente o valor alvo.
    
    Args:
        elements: Lista de elementos para gerar subconjuntos
        target_sum: Soma alvo que os subconjuntos devem ter
        
    Returns:
        Lista de subconjuntos que somam exatamente target_sum
    """
    result = []
    
    def backtrack(index: int, current_subset: List, current_sum: int) -> None:
        # Se a soma atual excede o alvo, podar
        if current_sum > target_sum:
            return
        
        # Se chegamos ao final dos elementos
        if index == len(elements):
            if current_sum == target_sum:
                result.append(current_subset[:])
            return
        
        # Opção 1: Excluir o elemento atual
        backtrack(index + 1, current_subset, current_sum)
        
        # Opção 2: Incluir o elemento atual
        current_subset.append(elements[index])
        backtrack(index + 1, current_subset, current_sum + elements[index])
        current_subset.pop()  # Backtrack
    
    backtrack(0, [], 0)
    return result


def subset_generation_with_memoization(elements: List) -> List[List]:
    """
    Gera todos os subconjuntos usando backtracking com memoização.
    
    A memoização é menos eficaz aqui porque cada subconjunto é único,
    mas demonstra o conceito para problemas mais complexos.
    
    Args:
        elements: Lista de elementos para gerar subconjuntos
        
    Returns:
        Lista de todos os subconjuntos possíveis
    """
    if not elements:
        return [[]]
    
    memo = {}
    result = []
    
    def backtrack(index: int, current_subset: Tuple) -> List[List]:
        # Converter para tupla para usar como chave do memo
        key = (index, current_subset)
        
        if key in memo:
            return memo[key]
        
        if index == len(elements):
            memo[key] = [list(current_subset)]
            return memo[key]
        
        # Gerar subconjuntos sem incluir o elemento atual
        subsets_without = backtrack(index + 1, current_subset)
        
        # Gerar subconjuntos incluindo o elemento atual
        new_subset = current_subset + (elements[index],)
        subsets_with = backtrack(index + 1, new_subset)
        
        # Combinar resultados
        all_subsets = subsets_without + subsets_with
        memo[key] = all_subsets
        
        return all_subsets
    
    result = backtrack(0, ())
    return result


def subset_generation_lexicographic(elements: List) -> List[List]:
    """
    Gera subconjuntos em ordem lexicográfica usando backtracking.
    
    Args:
        elements: Lista de elementos para gerar subconjuntos
        
    Returns:
        Lista de subconjuntos em ordem lexicográfica
    """
    if not elements:
        return [[]]
    
    # Ordenar elementos para garantir ordem lexicográfica
    sorted_elements = sorted(elements)
    result = []
    
    def backtrack(index: int, current_subset: List) -> None:
        # Adicionar o subconjunto atual
        result.append(current_subset[:])
        
        # Tentar adicionar elementos restantes
        for i in range(index, len(sorted_elements)):
            current_subset.append(sorted_elements[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()  # Backtrack
    
    backtrack(0, [])
    return result


def subset_generation_count_only(elements: List) -> int:
    """
    Conta o número total de subconjuntos sem gerá-los.
    
    Args:
        elements: Lista de elementos
        
    Returns:
        Número total de subconjuntos possíveis (2^n)
    """
    return 2 ** len(elements)


def subset_generation_with_duplicates(elements: List) -> List[List]:
    """
    Gera subconjuntos únicos quando há elementos duplicados.
    
    Args:
        elements: Lista de elementos (pode conter duplicatas)
        
    Returns:
        Lista de subconjuntos únicos
    """
    if not elements:
        return [[]]
    
    # Ordenar para agrupar duplicatas
    sorted_elements = sorted(elements)
    result = []
    
    def backtrack(index: int, current_subset: List) -> None:
        # Adicionar o subconjunto atual
        result.append(current_subset[:])
        
        # Tentar adicionar elementos restantes
        for i in range(index, len(sorted_elements)):
            # Pular duplicatas consecutivas
            if i > index and sorted_elements[i] == sorted_elements[i - 1]:
                continue
            current_subset.append(sorted_elements[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()  # Backtrack
    
    backtrack(0, [])
    return result


def subset_generation_optimized(elements: List) -> List[List]:
    """
    Versão otimizada da geração de subconjuntos com backtracking.
    
    Otimizações:
    1. Usa lista em vez de tupla para melhor performance
    2. Minimiza alocações de memória
    3. Usa append/pop em vez de slicing
    
    Args:
        elements: Lista de elementos para gerar subconjuntos
        
    Returns:
        Lista de todos os subconjuntos possíveis
    """
    if not elements:
        return [[]]
    
    result = []
    current_subset = []
    
    def backtrack(index: int) -> None:
        if index == len(elements):
            result.append(current_subset[:])
            return
        
        # Excluir elemento atual
        backtrack(index + 1)
        
        # Incluir elemento atual
        current_subset.append(elements[index])
        backtrack(index + 1)
        current_subset.pop()
    
    backtrack(0)
    return result


def analyze_subset_generation_complexity(elements: List) -> dict:
    """
    Analisa a complexidade e performance dos diferentes algoritmos.
    
    Args:
        elements: Lista de elementos para teste
        
    Returns:
        Dicionário com métricas de performance
    """
    results = {}
    
    # Teste 1: Backtracking recursivo
    start_time = time.time()
    backtracking_result = subset_generation_backtracking(elements)
    backtracking_time = time.time() - start_time
    
    # Teste 2: Iterativo com bitmask
    start_time = time.time()
    bitmask_result = subset_generation_iterative_bitmask(elements)
    bitmask_time = time.time() - start_time
    
    # Teste 3: Com memoização
    start_time = time.time()
    memo_result = subset_generation_with_memoization(elements)
    memo_time = time.time() - start_time
    
    # Teste 4: Otimizado
    start_time = time.time()
    optimized_result = subset_generation_optimized(elements)
    optimized_time = time.time() - start_time
    
    # Verificar correção
    all_correct = (
        len(backtracking_result) == len(bitmask_result) == 
        len(memo_result) == len(optimized_result) == 2**len(elements)
    )
    
    results = {
        'input_size': len(elements),
        'expected_count': 2**len(elements),
        'actual_count': len(backtracking_result),
        'all_correct': all_correct,
        'backtracking_time': backtracking_time,
        'bitmask_time': bitmask_time,
        'memo_time': memo_time,
        'optimized_time': optimized_time,
        'backtracking_count': len(backtracking_result),
        'bitmask_count': len(bitmask_result),
        'memo_count': len(memo_result),
        'optimized_count': len(optimized_result)
    }
    
    return results


def create_test_subsets() -> List[List]:
    """
    Cria casos de teste para geração de subconjuntos.
    
    Returns:
        Lista de casos de teste
    """
    test_cases = [
        [],  # Conjunto vazio
        [1],  # Conjunto unitário
        [1, 2],  # Conjunto pequeno
        [1, 2, 3],  # Conjunto médio
        [1, 2, 3, 4],  # Conjunto maior
        [1, 1, 2],  # Com duplicatas
        [1, 2, 2, 3],  # Múltiplas duplicatas
        list(range(1, 6)),  # Sequência
        [10, 20, 30, 40, 50],  # Números maiores
    ]
    
    return test_cases


def demonstrate_subset_generation():
    """
    Demonstra o uso dos algoritmos de geração de subconjuntos.
    """
    print("=== Demonstração: Geração de Subconjuntos ===\n")
    
    # Teste básico
    elements = [1, 2, 3]
    print(f"Elementos: {elements}")
    print(f"Número esperado de subconjuntos: {2**len(elements)}")
    
    # Backtracking
    subsets = subset_generation_backtracking(elements)
    print(f"\nSubconjuntos (backtracking): {subsets}")
    print(f"Total: {len(subsets)}")
    
    # Bitmask
    subsets_bitmask = subset_generation_iterative_bitmask(elements)
    print(f"\nSubconjuntos (bitmask): {subsets_bitmask}")
    print(f"Total: {len(subsets_bitmask)}")
    
    # Verificar se são iguais
    print(f"\nResultados idênticos: {subsets == subsets_bitmask}")
    
    # Teste com restrições
    print(f"\n=== Teste com Restrições ===")
    print(f"Subconjuntos com tamanho 1-2: {subset_generation_with_constraints(elements, 1, 2)}")
    print(f"Subconjuntos que somam 3: {subset_generation_with_sum_constraint(elements, 3)}")
    
    # Teste com duplicatas
    elements_with_duplicates = [1, 1, 2]
    print(f"\n=== Teste com Duplicatas ===")
    print(f"Elementos: {elements_with_duplicates}")
    print(f"Subconjuntos únicos: {subset_generation_with_duplicates(elements_with_duplicates)}")
    
    # Análise de complexidade
    print(f"\n=== Análise de Complexidade ===")
    analysis = analyze_subset_generation_complexity(elements)
    print(f"Tamanho da entrada: {analysis['input_size']}")
    print(f"Subconjuntos esperados: {analysis['expected_count']}")
    print(f"Todos corretos: {analysis['all_correct']}")
    print(f"Tempo backtracking: {analysis['backtracking_time']:.6f}s")
    print(f"Tempo bitmask: {analysis['bitmask_time']:.6f}s")
    print(f"Tempo memoização: {analysis['memo_time']:.6f}s")
    print(f"Tempo otimizado: {analysis['optimized_time']:.6f}s")


if __name__ == "__main__":
    demonstrate_subset_generation() 