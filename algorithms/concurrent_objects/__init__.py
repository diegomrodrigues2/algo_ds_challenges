"""
Objetos Concorrentes

Este módulo implementa objetos concorrentes com diferentes condições de correção:
- Quiescent Consistency
- Sequential Consistency  
- Linearizability

E diferentes condições de progresso:
- Blocking
- Non-blocking (Wait-free, Lock-free, Obstruction-free)

Todos os objetos implementam interfaces específicas para demonstração das propriedades.
"""

from .quiescent_counter import QuiescentCounter
from .sequential_register import SequentialRegister
from .linearizable_queue import LinearizableQueue
from .wait_free_counter import WaitFreeCounter
from .lock_free_stack import LockFreeStack

__all__ = [
    'QuiescentCounter',
    'SequentialRegister', 
    'LinearizableQueue',
    'WaitFreeCounter',
    'LockFreeStack'
] 