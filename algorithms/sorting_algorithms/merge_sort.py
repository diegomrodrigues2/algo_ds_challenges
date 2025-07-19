"""
Merge Sort Implementation

Implemente o algoritmo Merge Sort usando a estratégia divide-and-conquer.
O algoritmo divide o array ao meio, ordena recursivamente cada metade e
combina os resultados usando a operação merge.

Complexidade: O(n log n) no pior caso, melhor caso e caso médio
Espaço: O(n) - requer espaço extra
Estável: Sim
"""

def merge_sort(arr):
    """
    Ordena um array usando Merge Sort.
    
    Args:
        arr: Lista de números a ser ordenada
        
    Returns:
        Lista ordenada (cria uma nova lista)
        
    Exemplo:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> result = merge_sort(arr)
        >>> result
        [11, 12, 22, 25, 34, 64, 90]
    """
    raise NotImplementedError("Implemente o Merge Sort")


def merge_sort_inplace(arr, left=0, right=None):
    """
    Ordena um array usando Merge Sort in-place.
    
    Args:
        arr: Lista de números a ser ordenada
        left: Índice inicial do subarray
        right: Índice final do subarray (None para ordenar tudo)
        
    Returns:
        None (modifica o array original)
        
    Exemplo:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> merge_sort_inplace(arr)
        >>> arr
        [11, 12, 22, 25, 34, 64, 90]
    """
    raise NotImplementedError("Implemente o Merge Sort in-place")


def merge(left_arr, right_arr):
    """
    Combina dois arrays ordenados em um único array ordenado.
    
    Args:
        left_arr: Array ordenado da esquerda
        right_arr: Array ordenado da direita
        
    Returns:
        Array combinado e ordenado
        
    Exemplo:
        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge([1, 2], [3, 4, 5])
        [1, 2, 3, 4, 5]
    """
    raise NotImplementedError("Implemente a função merge")


def merge_inplace(arr, left, mid, right):
    """
    Combina dois subarrays ordenados in-place.
    
    Args:
        arr: Array contendo os dois subarrays
        left: Índice inicial do primeiro subarray
        mid: Índice final do primeiro subarray (inclusive)
        right: Índice final do segundo subarray (inclusive)
        
    Returns:
        None (modifica o array original)
        
    Exemplo:
        >>> arr = [1, 3, 5, 2, 4, 6]
        >>> merge_inplace(arr, 0, 2, 5)
        >>> arr
        [1, 2, 3, 4, 5, 6]
    """
    raise NotImplementedError("Implemente a função merge in-place")


def count_inversions(arr):
    """
    Conta o número de inversões em um array usando Merge Sort.
    Uma inversão é um par (i, j) onde i < j e arr[i] > arr[j].
    
    Args:
        arr: Lista de números
        
    Returns:
        Número de inversões
        
    Exemplo:
        >>> count_inversions([2, 4, 1, 3, 5])
        3
        >>> count_inversions([1, 2, 3, 4, 5])
        0
    """
    raise NotImplementedError("Implemente a contagem de inversões") 