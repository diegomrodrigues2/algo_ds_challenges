"""
Text Segmentation (Segmentação de Texto)
========================================

Implementação do algoritmo de backtracking para segmentação de texto.
Baseado em Erickson, "Algorithms", Capítulo 2, Seção 2.5, "Text Segmentation".

O problema: Dada uma string sem espaços e uma função is_word(substring), 
determinar se a string pode ser segmentada em uma sequência de palavras válidas.
"""

from typing import List, Optional, Dict, Set


def text_segmentation_backtracking(text: str, is_word_func) -> Optional[List[str]]:
    """
    Implementação básica de backtracking para segmentação de texto.
    
    Args:
        text: String sem espaços para segmentar
        is_word_func: Função que retorna True se a substring for uma palavra válida
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    if not text:
        return []
    
    def backtrack(start: int) -> Optional[List[str]]:
        # Caso base: chegamos ao final da string
        if start == len(text):
            return []
        
        # Tenta todos os prefixos possíveis a partir da posição atual
        for end in range(start + 1, len(text) + 1):
            prefix = text[start:end]
            
            # Se o prefixo é uma palavra válida
            if is_word_func(prefix):
                # Recursivamente tenta segmentar o restante
                remaining = backtrack(end)
                if remaining is not None:
                    return [prefix] + remaining
        
        # Nenhuma segmentação encontrada
        return None
    
    return backtrack(0)


def text_segmentation_with_memoization(text: str, is_word_func) -> Optional[List[str]]:
    """
    Implementação de backtracking com memoização para segmentação de texto.
    
    Args:
        text: String sem espaços para segmentar
        is_word_func: Função que retorna True se a substring for uma palavra válida
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    if not text:
        return []
    
    memo: Dict[int, Optional[List[str]]] = {}
    
    def backtrack(start: int) -> Optional[List[str]]:
        # Verifica se já calculamos este subproblema
        if start in memo:
            return memo[start]
        
        # Caso base: chegamos ao final da string
        if start == len(text):
            memo[start] = []
            return []
        
        # Tenta todos os prefixos possíveis a partir da posição atual
        for end in range(start + 1, len(text) + 1):
            prefix = text[start:end]
            
            # Se o prefixo é uma palavra válida
            if is_word_func(prefix):
                # Recursivamente tenta segmentar o restante
                remaining = backtrack(end)
                if remaining is not None:
                    result = [prefix] + remaining
                    memo[start] = result
                    return result
        
        # Nenhuma segmentação encontrada
        memo[start] = None
        return None
    
    return backtrack(0)


def text_segmentation_all_solutions(text: str, is_word_func) -> List[List[str]]:
    """
    Encontra todas as possíveis segmentações da string.
    
    Args:
        text: String sem espaços para segmentar
        is_word_func: Função que retorna True se a substring for uma palavra válida
        
    Returns:
        Lista de todas as segmentações possíveis
    """
    if not text:
        return [[]]
    
    solutions = []
    
    def backtrack(start: int, current_segmentation: List[str]):
        # Caso base: chegamos ao final da string
        if start == len(text):
            solutions.append(current_segmentation[:])
            return
        
        # Tenta todos os prefixos possíveis a partir da posição atual
        for end in range(start + 1, len(text) + 1):
            prefix = text[start:end]
            
            # Se o prefixo é uma palavra válida
            if is_word_func(prefix):
                current_segmentation.append(prefix)
                backtrack(end, current_segmentation)
                current_segmentation.pop()  # Backtrack
    
    backtrack(0, [])
    return solutions


def text_segmentation_count_solutions(text: str, is_word_func) -> int:
    """
    Conta o número total de segmentações possíveis.
    
    Args:
        text: String sem espaços para segmentar
        is_word_func: Função que retorna True se a substring for uma palavra válida
        
    Returns:
        Número de segmentações possíveis
    """
    if not text:
        return 1
    
    memo: Dict[int, int] = {}
    
    def backtrack(start: int) -> int:
        # Verifica se já calculamos este subproblema
        if start in memo:
            return memo[start]
        
        # Caso base: chegamos ao final da string
        if start == len(text):
            memo[start] = 1
            return 1
        
        count = 0
        
        # Tenta todos os prefixos possíveis a partir da posição atual
        for end in range(start + 1, len(text) + 1):
            prefix = text[start:end]
            
            # Se o prefixo é uma palavra válida
            if is_word_func(prefix):
                # Soma o número de segmentações do restante
                count += backtrack(end)
        
        memo[start] = count
        return count
    
    return backtrack(0)


def text_segmentation_optimized(text: str, is_word_func) -> Optional[List[str]]:
    """
    Implementação otimizada com poda e ordenação de tentativas.
    
    Args:
        text: String sem espaços para segmentar
        is_word_func: Função que retorna True se a substring for uma palavra válida
        
    Returns:
        Lista de palavras se a segmentação for possível, None caso contrário
    """
    if not text:
        return []
    
    memo: Dict[int, Optional[List[str]]] = {}
    
    def backtrack(start: int) -> Optional[List[str]]:
        # Verifica se já calculamos este subproblema
        if start in memo:
            return memo[start]
        
        # Caso base: chegamos ao final da string
        if start == len(text):
            memo[start] = []
            return []
        
        # Tenta prefixos em ordem decrescente de tamanho (otimização)
        # Isso pode encontrar soluções mais rapidamente em alguns casos
        for end in range(len(text), start, -1):
            prefix = text[start:end]
            
            # Se o prefixo é uma palavra válida
            if is_word_func(prefix):
                # Recursivamente tenta segmentar o restante
                remaining = backtrack(end)
                if remaining is not None:
                    result = [prefix] + remaining
                    memo[start] = result
                    return result
        
        # Nenhuma segmentação encontrada
        memo[start] = None
        return None
    
    return backtrack(0)


def analyze_text_segmentation_complexity(text: str, is_word_func) -> Dict[str, any]:
    """
    Análise de complexidade para segmentação de texto.
    
    Args:
        text: String para analisar
        is_word_func: Função que verifica se uma substring é palavra válida
        
    Returns:
        Dicionário com análise de complexidade
    """
    n = len(text)
    
    # Análise de complexidade
    analysis = {
        "input_size": n,
        "time_complexity": {
            "worst_case": "O(2^n)",
            "average_case": "O(n^2)",
            "best_case": "O(n)"
        },
        "space_complexity": {
            "recursion_stack": "O(n)",
            "memoization": "O(n)",
            "total": "O(n)"
        },
        "recurrence_relation": "T(n) = Σ T(n-i) para i de 1 a n",
        "optimizations": [
            "Memoização para evitar recálculo de subproblemas",
            "Poda de ramos impossíveis",
            "Ordenação de tentativas (prefixos maiores primeiro)"
        ]
    }
    
    return analysis


# Função auxiliar para criar dicionário de palavras
def create_word_dict(words: List[str]) -> Set[str]:
    """Cria um conjunto de palavras válidas."""
    return set(words)


# Função auxiliar para verificar se uma substring é palavra válida
def is_word_in_dict(substring: str, word_dict: Set[str]) -> bool:
    """Verifica se uma substring está no dicionário de palavras."""
    return substring in word_dict 