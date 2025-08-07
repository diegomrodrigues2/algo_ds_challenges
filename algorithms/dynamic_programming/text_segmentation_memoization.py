"""
Segmentação de Texto com Memoização

Este módulo implementa o problema da Segmentação de Texto (Word Break) usando memoização,
demonstrando a transição de backtracking exponencial O(2^n) para programação
dinâmica O(n²).

Referências:
- Erickson, "Algorithms", Capítulo 3, Seção 3.3, "Interpunctio Verborum Redux"
- GeeksforGeeks: https://www.geeksforgeeks.org/dsa/word-break-problem-dp-32/
- Tutorial Horizon: https://tutorialhorizon.com/algorithms/the-word-break-problem/
"""

from typing import List, Dict, Optional, Set, Callable
import time


def text_segmentation_memoization(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Resolve Segmentação de Texto usando memoização.
    
    O estado do subproblema é definido pelo índice inicial do sufixo da string.
    Para cada posição i, perguntamos: "O sufixo text[i..n] pode ser segmentado?"
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
        
    Exemplo:
        >>> dictionary = {"i", "like", "gfg"}
        >>> text_segmentation_memoization("ilike", dictionary)
        ['i', 'like']
        >>> text_segmentation_memoization("ilikegfg", dictionary)
        ['i', 'like', 'gfg']
        >>> text_segmentation_memoization("ilikemangoes", dictionary)
        None
    """
    if not text:
        return []
    
    n = len(text)
    memo: Dict[int, Optional[List[str]]] = {}
    
    def can_segment(start: int) -> Optional[List[str]]:
        # Verifica se já calculamos este subproblema
        if start in memo:
            return memo[start]
        
        # Caso base: chegamos ao final da string
        if start == n:
            memo[start] = []
            return []
        
        # Tenta todos os prefixos possíveis a partir da posição atual
        for end in range(start + 1, n + 1):
            prefix = text[start:end]
            
            # Se o prefixo é uma palavra válida
            if prefix in dictionary:
                # Recursivamente tenta segmentar o restante
                remaining = can_segment(end)
                if remaining is not None:
                    result = [prefix] + remaining
                    memo[start] = result
                    return result
        
        # Nenhuma segmentação encontrada
        memo[start] = None
        return None
    
    return can_segment(0)


def text_segmentation_backtracking(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Solução de backtracking puro para comparação de performance.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    if not text:
        return []
    
    n = len(text)
    
    def backtrack(start: int) -> Optional[List[str]]:
        # Caso base: chegamos ao final da string
        if start == n:
            return []
        
        # Tenta todos os prefixos possíveis a partir da posição atual
        for end in range(start + 1, n + 1):
            prefix = text[start:end]
            
            # Se o prefixo é uma palavra válida
            if prefix in dictionary:
                # Recursivamente tenta segmentar o restante
                remaining = backtrack(end)
                if remaining is not None:
                    return [prefix] + remaining
        
        # Nenhuma segmentação encontrada
        return None
    
    return backtrack(0)


def text_segmentation_tabulation(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Solução bottom-up usando tabulação.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    if not text:
        return []
    
    n = len(text)
    
    # dp[i] = True se text[0:i] pode ser segmentado
    dp = [False] * (n + 1)
    dp[0] = True  # String vazia é sempre segmentável
    
    # Para reconstruir a solução
    parent = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i):
            # Se text[0:j] pode ser segmentado e text[j:i] é uma palavra válida
            if dp[j] and text[j:i] in dictionary:
                dp[i] = True
                parent[i] = j
                break
    
    # Reconstruir a solução
    if not dp[n]:
        return None
    
    solution = []
    pos = n
    while pos > 0:
        prev = parent[pos]
        solution.append(text[prev:pos])
        pos = prev
    
    return solution[::-1]


def text_segmentation_optimized_memoization(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Implementação otimizada com memoização e ordenação de tentativas.
    
    Otimizações:
    1. Tenta prefixos em ordem decrescente de tamanho
    2. Usa memoização para evitar recálculos
    3. Poda precoce quando possível
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    # TODO: Implementar solução otimizada com memoização
    # Dica: Use memoização com tentativas em ordem decrescente de tamanho
    # Estado (i): "O sufixo text[i..n] pode ser segmentado?"
    raise NotImplementedError("Implementar solução otimizada com memoização")


def text_segmentation_with_trie(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Implementação usando Trie para otimização de busca de palavras.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    # TODO: Implementar solução usando Trie
    # Dica: Construa um Trie com o dicionário para busca eficiente
    # Use memoização para evitar recálculos
    raise NotImplementedError("Implementar solução usando Trie")


def text_segmentation_with_bfs(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Implementação usando BFS para encontrar segmentação.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    # TODO: Implementar solução usando BFS
    # Dica: Use BFS para explorar todas as possíveis segmentações
    # Mantenha um caminho para reconstruir a solução
    raise NotImplementedError("Implementar solução usando BFS")


def text_segmentation_with_dfs(text: str, dictionary: Set[str]) -> Optional[List[str]]:
    """
    Implementação usando DFS para encontrar segmentação.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    # TODO: Implementar solução usando DFS
    # Dica: Use DFS com memoização para explorar segmentações
    # Retorne a primeira segmentação válida encontrada
    raise NotImplementedError("Implementar solução usando DFS")


def text_segmentation_all_solutions(text: str, dictionary: Set[str]) -> List[List[str]]:
    """
    Encontra todas as possíveis segmentações da string.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Lista de todas as segmentações possíveis
    """
    # TODO: Implementar solução que encontra todas as segmentações
    # Dica: Use backtracking para explorar todas as possibilidades
    # Armazene todas as soluções válidas encontradas
    raise NotImplementedError("Implementar solução que encontra todas as segmentações")


def text_segmentation_count_solutions(text: str, dictionary: Set[str]) -> int:
    """
    Conta o número de segmentações possíveis da string.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Número de segmentações possíveis
    """
    # TODO: Implementar solução que conta segmentações
    # Dica: Use programação dinâmica para contar soluções
    # Estado (i): "Número de segmentações possíveis para text[i..n]"
    raise NotImplementedError("Implementar solução que conta segmentações")


def text_segmentation_with_constraints(text: str, dictionary: Set[str], max_words: int = None, min_word_length: int = 1) -> Optional[List[str]]:
    """
    Implementação com restrições adicionais.
    
    Args:
        text: String sem espaços para segmentar
        dictionary: Conjunto de palavras válidas
        max_words: Número máximo de palavras permitidas
        min_word_length: Comprimento mínimo das palavras
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    # TODO: Implementar solução com restrições
    # Dica: Adicione verificações de restrições na recursão
    # Considere max_words e min_word_length nas decisões
    raise NotImplementedError("Implementar solução com restrições")


def analyze_text_segmentation_complexity(n: int, dictionary_size: int) -> Dict:
    """
    Analisa a complexidade do algoritmo para diferentes entradas.
    
    Args:
        n: Tamanho da string
        dictionary_size: Tamanho do dicionário
        
    Returns:
        Dicionário com análise detalhada de complexidade
    """
    analysis = {
        'input_size': n,
        'dictionary_size': dictionary_size,
        'complexity_class': 'O(n²)',
        'space_complexity': 'O(n)',
        'exponential_improvement': True,
        'memoization_benefit': f'Reduz de O(2^{n}) para O({n}²)',
        'practical_viability': 'Altamente viável para strings moderadas',
        'subproblem_analysis': {
            'state_definition': 'Índice inicial do sufixo',
            'state_count': n,
            'overlapping_subproblems': True,
            'optimal_substructure': True
        },
        'optimization_techniques': [
            'Memoização com dicionário',
            'Ordenação de tentativas (prefixos maiores primeiro)',
            'Poda precoce quando possível'
        ],
        'limitations': [
            'Ainda pode ser lento para strings muito longas',
            'Depende da distribuição de palavras no dicionário',
            'Complexidade de verificação de palavras no dicionário'
        ]
    }
    
    return analysis


def compare_approaches(text: str, dictionary: Set[str]) -> Dict:
    """
    Compara diferentes abordagens para segmentação de texto.
    
    Args:
        text: String para segmentar
        dictionary: Conjunto de palavras válidas
        
    Returns:
        Dicionário com comparação de performance e resultados
    """
    results = {}
    
    # Teste com backtracking puro
    start_time = time.time()
    backtracking_result = text_segmentation_backtracking(text, dictionary)
    backtracking_time = time.time() - start_time
    
    # Teste com memoização
    start_time = time.time()
    memoization_result = text_segmentation_memoization(text, dictionary)
    memoization_time = time.time() - start_time
    
    # Teste com tabulação
    start_time = time.time()
    tabulation_result = text_segmentation_tabulation(text, dictionary)
    tabulation_time = time.time() - start_time
    
    # Teste com memoização otimizada
    start_time = time.time()
    optimized_result = text_segmentation_optimized_memoization(text, dictionary)
    optimized_time = time.time() - start_time
    
    # Evita divisão por zero
    performance_improvement = {}
    if memoization_time > 0:
        performance_improvement['memoization_vs_backtracking'] = f'{backtracking_time/memoization_time:.2f}x mais rápido'
    else:
        performance_improvement['memoization_vs_backtracking'] = 'Muito rápido (tempo < 0.001s)'
    
    if tabulation_time > 0:
        performance_improvement['tabulation_vs_backtracking'] = f'{backtracking_time/tabulation_time:.2f}x mais rápido'
    else:
        performance_improvement['tabulation_vs_backtracking'] = 'Muito rápido (tempo < 0.001s)'
    
    if optimized_time > 0:
        performance_improvement['optimized_vs_backtracking'] = f'{backtracking_time/optimized_time:.2f}x mais rápido'
    else:
        performance_improvement['optimized_vs_backtracking'] = 'Muito rápido (tempo < 0.001s)'
    
    results = {
        'input_text': text,
        'dictionary_size': len(dictionary),
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
                'space': 'O(n)'
            },
            'tabulation': {
                'result': tabulation_result,
                'time': tabulation_time,
                'complexity': 'O(n²)',
                'space': 'O(n)'
            },
            'optimized_memoization': {
                'result': optimized_result,
                'time': optimized_time,
                'complexity': 'O(n²)',
                'space': 'O(n)'
            }
        },
        'performance_improvement': performance_improvement
    }
    
    return results


def generate_test_cases() -> List[tuple]:
    """
    Gera casos de teste para validação.
    
    Returns:
        Lista de tuplas (text, dictionary, expected_result)
    """
    test_cases = [
        # Casos básicos
        ("ilike", {"i", "like", "gfg"}, ["i", "like"]),
        ("ilikegfg", {"i", "like", "gfg"}, ["i", "like", "gfg"]),
        ("ilikemangoes", {"i", "like", "gfg"}, None),
        
        # Casos com múltiplas soluções
        ("catsanddog", {"cat", "cats", "and", "sand", "dog"}, ["cat", "sand", "dog"]),
        
        # Casos extremos
        ("", {"a", "b"}, []),
        ("a", {"a"}, ["a"]),
        ("a", {"b"}, None),
        
        # Casos com palavras sobrepostas
        ("pineapple", {"pine", "pineapple", "apple"}, ["pine", "apple"]),  # Pode encontrar qualquer solução válida
        ("pineapple", {"pine", "apple"}, ["pine", "apple"]),
        
        # Casos longos
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
         {"a", "aa", "aaa", "aaaa"}, 
         ["a"] * 100)
    ]
    
    return test_cases


def benchmark_performance():
    """
    Executa benchmark de performance para diferentes tamanhos de entrada.
    """
    print("=== Benchmark de Performance: Segmentação de Texto ===\n")
    
    # Dicionário de teste
    dictionary = {"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"}
    
    # Testes com diferentes tamanhos
    test_sizes = [10, 20, 30, 40, 50]
    
    for size in test_sizes:
        text = "a" * size
        print(f"Testando com string de tamanho {size}:")
        
        # Backtracking (pode ser muito lento para tamanhos grandes)
        if size <= 20:
            start_time = time.time()
            backtracking_result = text_segmentation_backtracking(text, dictionary)
            backtracking_time = time.time() - start_time
            print(f"  Backtracking: {backtracking_time:.4f}s")
        else:
            print(f"  Backtracking: Muito lento (pulado)")
        
        # Memoização
        start_time = time.time()
        memoization_result = text_segmentation_memoization(text, dictionary)
        memoization_time = time.time() - start_time
        print(f"  Memoização: {memoization_time:.4f}s")
        
        # Tabulação
        start_time = time.time()
        tabulation_result = text_segmentation_tabulation(text, dictionary)
        tabulation_time = time.time() - start_time
        print(f"  Tabulação: {tabulation_time:.4f}s")
        
        # Memoização otimizada
        start_time = time.time()
        optimized_result = text_segmentation_optimized_memoization(text, dictionary)
        optimized_time = time.time() - start_time
        print(f"  Memoização Otimizada: {optimized_time:.4f}s")
        
        print()


if __name__ == "__main__":
    # Testes básicos
    print("=== Testes de Segmentação de Texto ===\n")
    
    test_cases = generate_test_cases()
    
    for i, (text, dictionary, expected) in enumerate(test_cases):
        print(f"Teste {i+1}: '{text}'")
        result = text_segmentation_memoization(text, dictionary)
        status = "✓" if result == expected else "✗"
        print(f"  Resultado: {result}")
        print(f"  Esperado: {expected}")
        print(f"  Status: {status}\n")
    
    # Benchmark de performance
    benchmark_performance() 