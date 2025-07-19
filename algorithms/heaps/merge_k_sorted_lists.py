from __future__ import annotations
from typing import List

from algorithms.heaps.binary_heap import BinaryHeap


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    """Combina k listas ordenadas em uma única lista ordenada."""
    heap = BinaryHeap()
    result = []

    for i, arr in enumerate(lists):
        if arr:
            heap.insert((arr[0], i, 0))

    while heap.size() > 0:
        val, arr_idx, elem_idx = heap.extract_min()
        result.append(val)
        
        if elem_idx + 1 < len(lists[arr_idx]):
            next_val = lists[arr_idx][elem_idx + 1]
            heap.insert((next_val, arr_idx, elem_idx + 1))
    
    return result
