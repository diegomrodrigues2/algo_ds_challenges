"""
Selection Sort Implementation

Implemente o algoritmo Selection Sort que ordena um array encontrando repetidamente
o menor elemento do array não ordenado e colocando-o no início.

Complexidade: O(n²) no pior caso, melhor caso e caso médio
Espaço: O(1) - in-place
Estável: Não
"""

def selection_sort(arr):
    """
    Ordena um array usando Selection Sort.
    
    Args:
        arr: Lista de números a ser ordenada
        
    Returns:
        Lista ordenada (modifica o array original)
        
    Exemplo:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> selection_sort(arr)
        >>> arr
        [11, 12, 22, 25, 34, 64, 90]
    """
    raise NotImplementedError("Implemente o Selection Sort")


def find_min_index(arr, start_index):
    """
    Encontra o índice do menor elemento a partir de start_index.
    
    Args:
        arr: Lista de números
        start_index: Índice inicial para buscar
        
    Returns:
        Índice do menor elemento encontrado
        
    Exemplo:
        >>> find_min_index([64, 34, 25, 12, 22], 0)
        3
        >>> find_min_index([64, 34, 25, 12, 22], 1)
        3
    """
    raise NotImplementedError("Implemente a busca do menor elemento")


def selection_sort_recursive(arr, n=None):
    """
    Implementação recursiva do Selection Sort.
    
    Args:
        arr: Lista de números a ser ordenada
        n: Tamanho da parte não ordenada (None para ordenar tudo)
        
    Returns:
        None (modifica o array original)
        
    Exemplo:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> selection_sort_recursive(arr)
        >>> arr
        [11, 12, 22, 25, 34, 64, 90]
    """
    raise NotImplementedError("Implemente o Selection Sort recursivo") 