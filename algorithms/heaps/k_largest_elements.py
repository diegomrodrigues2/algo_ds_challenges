from __future__ import annotations
from typing import List
from .binary_heap import BinaryHeap

def k_largest_elements(arr: List[int], k: int) -> List[int]:
    """Retorna os ``k`` maiores elementos da lista em ordem decrescente."""
    if k <= 0:
        return []
    
    if k >= len(arr):
        return sorted(arr, reverse=True)
    
    # Usa nossa própria implementação de min-heap
    heap = BinaryHeap()
    
    for num in arr:
        if heap.size() < k:
            heap.insert(num)
        elif num > heap.peek():
            heap.extract_min()  # Remove o menor elemento
            heap.insert(num)    # Insere o novo elemento
    
    # Extrai todos os elementos da heap e ordena em ordem decrescente
    result = []
    while heap.size() > 0:
        result.append(heap.extract_min())
    
    return sorted(result, reverse=True)



