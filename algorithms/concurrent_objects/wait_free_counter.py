"""
Wait-Free Counter

Contador que satisfaz wait-free progress condition.
Todo método termina em número finito de passos, independente de outras threads.

Propriedades:
- ✅ Wait-Free
- ✅ Lock-Free
- ✅ Obstruction-Free
- ✅ Non-blocking

TAREFA: Implementar os métodos getAndIncrement() e get() para garantir wait-freedom.
"""

import threading
from typing import List


class WaitFreeCounter:
    """
    Wait-Free Counter
    
    Contador que satisfaz wait-free progress condition. Todo método
    termina em número finito de passos, independente de outras threads.
    
    TAREFA: Implementar a lógica para garantir wait-freedom.
    """
    
    def __init__(self):
        # Array de contadores locais por thread
        self.local_counters = [0] * 100  # Assume máximo 100 threads
        # Lock para sincronização
        self.lock = threading.Lock()
        
    def getAndIncrement(self):
        """
        Incrementa o contador e retorna o valor anterior
        
        TAREFA: Implementar a lógica para:
        1. Obter ID da thread atual
        2. Incrementar contador local
        3. Retornar valor anterior
        
        DICA: Use threading.current_thread().ident % 100 para obter thread ID
        """
        raise NotImplementedError("Implementar método getAndIncrement()")
            
    def get(self):
        """
        Retorna o valor atual do contador
        
        TAREFA: Implementar a lógica para:
        1. Somar todos os contadores locais
        2. Retornar soma total
        """
        raise NotImplementedError("Implementar método get()")


def test_wait_free_counter():
    """Testa o contador wait-free"""
    counter = WaitFreeCounter()
    results = []
    iterations = 1000
    
    def worker():
        for _ in range(iterations):
            value = counter.getAndIncrement()
            results.append(value)
    
    # Cria duas threads
    thread1 = threading.Thread(target=worker)
    thread2 = threading.Thread(target=worker)
    
    # Executa threads
    thread1.start()
    thread2.start()
    
    # Aguarda conclusão
    thread1.join()
    thread2.join()
    
    # Verifica resultado
    expected_count = 2 * iterations
    actual_count = counter.get()
    unique_values = len(set(results))
    
    success = (actual_count == expected_count and 
               unique_values == expected_count and
               all(0 <= v < expected_count for v in results))
    
    print(f"Wait-Free Counter Test:")
    print(f"  Expected count: {expected_count}")
    print(f"  Actual count: {actual_count}")
    print(f"  Unique values: {unique_values}")
    print(f"  Success: {success}")
    
    return success


if __name__ == "__main__":
    test_wait_free_counter() 