"""
Subsequência Crescente Mais Longa (LIS) com Memoização

Este módulo implementa o problema da Longest Increasing Subsequence (LIS) usando memoização,
demonstrando a transição de backtracking exponencial O(2^n) para programação
dinâmica O(n²).

Referências:
- Erickson, "Algorithms", Capítulo 3, Seção 3.6, "First Recurrence: Is This Next?"
- GeeksforGeeks: https://www.geeksforgeeks.org/dsa/longest-increasing-subsequence-dp-3/
"""

from typing import List, Dict, Optional, Tuple
import time


def lis_memoization(arr: List[int]) -> int:
    """
    Resolve LIS usando memoização com formulação LISbigger(i, j).
    
    O estado do subproblema é definido por dois parâmetros:
    - i: índice atual no array
    - j: índice do elemento anterior na subsequência (ou -1 se não há anterior)
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Comprimento da subsequência crescente mais longa
        
    Exemplo:
        >>> lis_memoization([3, 10, 2, 1, 20])
        3
        >>> lis_memoization([10, 22, 9, 33, 21, 50, 41, 60])
        5
        >>> lis_memoization([30, 20, 10])
        1
    """
    if not arr:
        return 0
    
    n = len(arr)
    memo: Dict[Tuple[int, int], int] = {}
    
    def lis_bigger(i: int, prev_idx: int) -> int:
        """
        Função auxiliar para memoização.
        
        Args:
            i: índice atual
            prev_idx: índice do elemento anterior (-1 se não há anterior)
            
        Returns:
            Comprimento da LIS começando do índice i com elemento anterior em prev_idx
        """
        # Verifica se já calculamos este subproblema
        if (i, prev_idx) in memo:
            return memo[(i, prev_idx)]
        
        # Caso base: chegamos ao final do array
        if i == n:
            memo[(i, prev_idx)] = 0
            return 0
        
        # Opção 1: Não incluir o elemento atual
        result = lis_bigger(i + 1, prev_idx)
        
        # Opção 2: Incluir o elemento atual (se possível)
        if prev_idx == -1 or arr[i] > arr[prev_idx]:
            result = max(result, 1 + lis_bigger(i + 1, i))
        
        memo[(i, prev_idx)] = result
        return result
    
    return lis_bigger(0, -1)


def lis_backtracking(arr: List[int]) -> int:
    """
    Solução de backtracking puro para comparação de performance.
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Comprimento da subsequência crescente mais longa
    """
    # TODO: Implementar solução de backtracking
    # Dica: Use recursão sem cache para explorar todas as possibilidades
    # Para cada elemento, decida se inclui ou não na subsequência
    raise NotImplementedError("Implementar solução de backtracking")


def lis_tabulation(arr: List[int]) -> int:
    """
    Solução bottom-up usando tabulação.
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Comprimento da subsequência crescente mais longa
    """
    # TODO: Implementar solução bottom-up com tabulação
    # Dica: Construa uma tabela dp[i] onde dp[i] = comprimento da LIS terminando em i
    # Para cada i, considere todos os j < i onde arr[j] < arr[i]
    raise NotImplementedError("Implementar solução bottom-up com tabulação")


def lis_binary_search(arr: List[int]) -> int:
    """
    Solução otimizada usando busca binária (O(n log n)).
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Comprimento da subsequência crescente mais longa
    """
    # TODO: Implementar solução otimizada com busca binária
    # Dica: Use um array auxiliar para manter os menores elementos finais
    # Para cada elemento, use busca binária para encontrar a posição
    raise NotImplementedError("Implementar solução otimizada com busca binária")


def lis_with_sequence(arr: List[int]) -> Tuple[int, List[int]]:
    """
    Encontra o comprimento da LIS e retorna uma das subsequências.
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Tupla (comprimento, subsequência)
    """
    # TODO: Implementar solução que retorna a subsequência
    # Dica: Use memoização e mantenha informações para reconstruir a solução
    # Rastreie as escolhas feitas durante a recursão
    raise NotImplementedError("Implementar solução que retorna a subsequência")


def lis_count_all(arr: List[int]) -> int:
    """
    Conta o número de subsequências crescentes de comprimento máximo.
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Número de LIS possíveis
    """
    # TODO: Implementar solução que conta todas as LIS
    # Dica: Use programação dinâmica para contar as subsequências
    # Mantenha tanto o comprimento quanto a contagem
    raise NotImplementedError("Implementar solução que conta todas as LIS")


def lis_ending_at_each_index(arr: List[int]) -> List[int]:
    """
    Calcula o comprimento da LIS terminando em cada índice.
    
    Args:
        arr: Lista de números inteiros
        
    Returns:
        Lista onde result[i] = comprimento da LIS terminando no índice i
    """
    # TODO: Implementar solução que calcula LIS para cada índice
    # Dica: Para cada índice i, encontre a maior LIS terminando em i
    # Considere todos os elementos anteriores menores que arr[i]
    raise NotImplementedError("Implementar solução para LIS terminando em cada índice")


def lis_with_constraints(arr: List[int], max_length: int = None, min_diff: int = 1) -> int:
    """
    LIS com restrições adicionais.
    
    Args:
        arr: Lista de números inteiros
        max_length: Comprimento máximo permitido da subsequência
        min_diff: Diferença mínima entre elementos consecutivos
        
    Returns:
        Comprimento da LIS respeitando as restrições
    """
    # TODO: Implementar solução com restrições
    # Dica: Adicione verificações de restrições na recursão
    # Considere max_length e min_diff nas decisões
    raise NotImplementedError("Implementar solução com restrições")


def analyze_lis_complexity(n: int) -> Dict:
    """
    Analisa a complexidade do algoritmo para diferentes entradas.
    
    Args:
        n: Tamanho do array
        
    Returns:
        Dicionário com análise detalhada de complexidade
    """
    analysis = {
        'input_size': n,
        'complexity_class': 'O(n²)',
        'space_complexity': 'O(n²)',
        'exponential_improvement': True,
        'memoization_benefit': f'Reduz de O(2^{n}) para O({n}²)',
        'practical_viability': 'Viável para arrays de tamanho moderado',
        'subproblem_analysis': {
            'state_definition': 'Par (índice_atual, índice_anterior)',
            'state_count': n * n,
            'overlapping_subproblems': True,
            'optimal_substructure': True
        },
        'optimization_techniques': [
            'Memoização com cache 2D',
            'Pruning baseado em elementos anteriores',
            'Reconstrução da subsequência'
        ],
        'further_optimizations': [
            'Busca binária para O(n log n)',
            'Segment tree para consultas de range',
            'Coordinate compression para valores grandes'
        ],
        'limitations': [
            'Ainda pode ser lento para arrays muito grandes',
            'Uso de memória proporcional a n²',
            'Requer comparação de todos os pares de elementos'
        ]
    }
    
    return analysis


def compare_lis_approaches(arr: List[int]) -> Dict:
    """
    Compara diferentes abordagens para LIS.
    
    Args:
        arr: Lista para testar
        
    Returns:
        Dicionário com comparação de performance e resultados
    """
    results = {}
    
    # Teste com memoização
    start_time = time.time()
    memoization_result = lis_memoization(arr)
    memoization_time = time.time() - start_time
    
    # Teste com backtracking (apenas para arrays pequenos)
    backtracking_result = None
    backtracking_time = 0
    if len(arr) <= 15:
        try:
            start_time = time.time()
            backtracking_result = lis_backtracking(arr)
            backtracking_time = time.time() - start_time
        except NotImplementedError:
            backtracking_result = "Não implementado"
            backtracking_time = 0
    else:
        backtracking_result = "Muito lento (pulado)"
        backtracking_time = 0
    
    # Teste com tabulação
    try:
        start_time = time.time()
        tabulation_result = lis_tabulation(arr)
        tabulation_time = time.time() - start_time
    except NotImplementedError:
        tabulation_result = "Não implementado"
        tabulation_time = 0
    
    # Teste com busca binária
    try:
        start_time = time.time()
        binary_search_result = lis_binary_search(arr)
        binary_search_time = time.time() - start_time
    except NotImplementedError:
        binary_search_result = "Não implementado"
        binary_search_time = 0
    
    # Evita divisão por zero
    performance_improvement = {}
    if memoization_time > 0 and backtracking_time > 0:
        performance_improvement['memoization_vs_backtracking'] = f'{backtracking_time/memoization_time:.2f}x mais rápido'
    else:
        performance_improvement['memoization_vs_backtracking'] = 'Muito rápido (tempo < 0.001s)'
    
    if binary_search_time > 0 and memoization_time > 0:
        performance_improvement['binary_search_vs_memoization'] = f'{memoization_time/binary_search_time:.2f}x mais rápido'
    else:
        performance_improvement['binary_search_vs_memoization'] = 'Comparação não disponível'
    
    results = {
        'input_array': arr,
        'array_size': len(arr),
        'approaches': {
            'backtracking': {
                'result': backtracking_result,
                'time': backtracking_time,
                'complexity': 'O(2^n)',
                'space': 'O(n)'
            },
            'memoization': {
                'result': memoization_result,
                'time': memoization_time,
                'complexity': 'O(n²)',
                'space': 'O(n²)'
            },
            'tabulation': {
                'result': tabulation_result,
                'time': tabulation_time,
                'complexity': 'O(n²)',
                'space': 'O(n)'
            },
            'binary_search': {
                'result': binary_search_result,
                'time': binary_search_time,
                'complexity': 'O(n log n)',
                'space': 'O(n)'
            }
        },
        'performance_improvement': performance_improvement
    }
    
    return results


def generate_lis_test_cases() -> List[tuple]:
    """
    Gera casos de teste para validação.
    
    Returns:
        Lista de tuplas (array, expected_lis_length)
    """
    test_cases = [
        # Casos básicos
        ([3, 10, 2, 1, 20], 3),  # [3, 10, 20]
        ([10, 22, 9, 33, 21, 50, 41, 60], 5),  # [10, 22, 33, 50, 60]
        ([30, 20, 10], 1),  # [30] ou [20] ou [10]
        ([10, 20, 35, 80], 4),  # [10, 20, 35, 80]
        ([2, 2, 2], 1),  # [2] (apenas estritamente crescente)
        
        # Casos extremos
        ([], 0),  # Array vazio
        ([5], 1),  # Um elemento
        ([1, 2, 3, 4, 5], 5),  # Array já ordenado
        ([5, 4, 3, 2, 1], 1),  # Array em ordem decrescente
        
        # Casos com múltiplas LIS
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),  # [1, 3, 6, 7, 9, 10]
        
        # Casos longos
        (list(range(100)), 100),  # 0 a 99
        (list(range(100, 0, -1)), 1),  # 100 a 1 (decrescente)
    ]
    
    return test_cases


def benchmark_lis_performance():
    """
    Executa benchmark de performance para diferentes tamanhos de entrada.
    """
    print("=== Benchmark de Performance: LIS ===\n")
    
    # Testes com diferentes tamanhos
    test_sizes = [10, 20, 50, 100, 200]
    
    for size in test_sizes:
        # Cria array de teste (pior caso: todos elementos iguais seguidos de crescente)
        arr = [1] * (size // 2) + list(range(size // 2))
        
        print(f"Testando com array de tamanho {size}:")
        
        # Memoização
        start_time = time.time()
        lis_result = lis_memoization(arr)
        memoization_time = time.time() - start_time
        print(f"  Memoização: {memoization_time:.4f}s (LIS = {lis_result})")
        
        # Backtracking (apenas para tamanhos pequenos)
        if size <= 20:
            try:
                start_time = time.time()
                backtracking_result = lis_backtracking(arr)
                backtracking_time = time.time() - start_time
                print(f"  Backtracking: {backtracking_time:.4f}s (LIS = {backtracking_result})")
            except NotImplementedError:
                print(f"  Backtracking: Não implementado")
        else:
            print(f"  Backtracking: Muito lento (pulado)")
        
        print()


if __name__ == "__main__":
    # Testes básicos
    print("=== Testes de LIS com Memoização ===\n")
    
    test_cases = generate_lis_test_cases()
    
    for i, (arr, expected) in enumerate(test_cases):
        print(f"Teste {i+1}: {arr}")
        try:
            result = lis_memoization(arr)
            status = "✓" if result == expected else "✗"
            print(f"  Resultado: {result}")
            print(f"  Esperado: {expected}")
            print(f"  Status: {status}\n")
        except Exception as e:
            print(f"  Erro: {e}\n")
    
    # Benchmark de performance
    benchmark_lis_performance()