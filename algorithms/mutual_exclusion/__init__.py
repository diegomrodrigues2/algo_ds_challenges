"""
Algoritmos de Mutual Exclusion

Este módulo implementa algoritmos clássicos de exclusão mútua:
- LockOne e LockTwo (para 2 threads)
- Peterson Lock (para 2 threads)
- Filter Lock (para n threads)
- Bakery Lock (para n threads)

Todos os algoritmos implementam a interface Lock com métodos lock() e unlock().
"""

from .lock_one import LockOne
from .lock_two import LockTwo
from .peterson_lock import PetersonLock
from .filter_lock import FilterLock
from .bakery_lock import BakeryLock

__all__ = [
    'LockOne',
    'LockTwo', 
    'PetersonLock',
    'FilterLock',
    'BakeryLock'
] 