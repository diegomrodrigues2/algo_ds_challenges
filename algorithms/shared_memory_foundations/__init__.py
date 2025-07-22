"""
Fundamentos da Memória Compartilhada

Este módulo contém implementações dos fundamentos teóricos da computação concorrente
com memória compartilhada, incluindo diferentes tipos de registradores e snapshots atômicos.

Conceitos cobertos:
- Registradores Safe, Regular e Atomic
- Construções hierárquicas de registradores
- Snapshots atômicos wait-free
- Modelo de computação concorrente

Referências:
- Herlihy & Shavit: "The Art of Multiprocessor Programming"
- Lynch: "Distributed Algorithms"
"""

from .safe_register import SafeRegister
from .regular_register import RegularRegister
from .atomic_register import AtomicRegister
from .mrsw_register import MRSWRegister
from .mrmw_register import MRMWRegister
from .atomic_snapshot import AtomicSnapshot

__all__ = [
    'SafeRegister',
    'RegularRegister', 
    'AtomicRegister',
    'MRSWRegister',
    'MRMWRegister',
    'AtomicSnapshot'
] 