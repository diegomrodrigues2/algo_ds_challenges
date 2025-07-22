"""
Lock-Free Stack

Pilha que satisfaz lock-free progress condition.
Infinitamente frequentemente algum método termina em número finito de passos.

Propriedades:
- ✅ Lock-Free
- ✅ Obstruction-Free
- ❌ Wait-Free (pode haver starvation)
- ✅ Non-blocking

TAREFA: Implementar os métodos push() e pop() para garantir lock-freedom.
"""

import threading
from typing import Any, Optional


class Node:
    """Nó da pilha lock-free"""
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LockFreeStack:
    """
    Lock-Free Stack
    
    Pilha que satisfaz lock-free progress condition. Infinitamente frequentemente
    algum método termina em número finito de passos.
    
    TAREFA: Implementar a lógica para garantir lock-freedom.
    """
    
    def __init__(self):
        # Cabeça da pilha (topo)
        self.head = None
        
    def push(self, value: Any):
        """
        Empilha um valor
        
        TAREFA: Implementar a lógica para:
        1. Criar novo nó
        2. Definir next do novo nó como head atual
        3. Atualizar head para o novo nó
        4. Usar compare-and-swap para garantir atomicidade
        
        DICA: Use uma abordagem lock-free com CAS
        """
        raise NotImplementedError("Implementar método push()")
            
    def pop(self) -> Optional[Any]:
        """
        Desempilha um valor
        
        TAREFA: Implementar a lógica para:
        1. Ler head atual
        2. Se head é None, retornar None
        3. Definir novo head como head.next
        4. Usar compare-and-swap para garantir atomicidade
        5. Retornar valor do nó removido
        
        DICA: Use uma abordagem lock-free com CAS
        """
        raise NotImplementedError("Implementar método pop()")


def test_lock_free_stack():
    """Testa a pilha lock-free"""
    stack = LockFreeStack()
    results = []
    
    def pusher():
        # Empilha elementos
        stack.push("A")
        stack.push("B")
    
    def popper():
        # Desempilha elementos
        item1 = stack.pop()
        item2 = stack.pop()
        results.extend([item1, item2])
    
    # Cria threads
    push_thread = threading.Thread(target=pusher)
    pop_thread = threading.Thread(target=popper)
    
    # Executa threads
    push_thread.start()
    pop_thread.start()
    
    # Aguarda conclusão
    push_thread.join()
    pop_thread.join()
    
    # Verifica resultado
    print(f"Lock-Free Stack Test:")
    print(f"  Results: {results}")
    print(f"  Stack empty: {stack.pop() is None}")
    
    return True


if __name__ == "__main__":
    test_lock_free_stack() 