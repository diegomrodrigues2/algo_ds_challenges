from __future__ import annotations
from typing import TypeVar, Generic, Optional
import heapq

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    """Fila de prioridade avançada com suporte a desempate."""
    
    def __init__(self) -> None:
        """Inicializa a fila de prioridade."""
        raise NotImplementedError("Implementar esta função")
    
    def push(self, priority: int, item: T) -> None:
        """Adiciona um item à fila com a prioridade especificada."""
        raise NotImplementedError("Implementar esta função")
    
    def pop(self) -> T:
        """Remove e retorna o item com maior prioridade."""
        raise NotImplementedError("Implementar esta função")
    
    def peek(self) -> T:
        """Retorna o item com maior prioridade sem removê-lo."""
        raise NotImplementedError("Implementar esta função")
    
    def peek_priority(self) -> int:
        """Retorna a prioridade do item no topo da fila."""
        raise NotImplementedError("Implementar esta função")
    
    def size(self) -> int:
        """Retorna o número de elementos na fila."""
        raise NotImplementedError("Implementar esta função")
    
    def is_empty(self) -> bool:
        """Verifica se a fila está vazia."""
        raise NotImplementedError("Implementar esta função")
    
    def clear(self) -> None:
        """Remove todos os elementos da fila."""
        raise NotImplementedError("Implementar esta função") 