"""
Quiescent Counter

Contador que satisfaz quiescent consistency.
Retorna números sem duplicar ou omitir, mas não necessariamente em ordem.

Propriedades:
- ✅ Quiescent Consistency
- ❌ Sequential Consistency
- ❌ Linearizability
- ✅ Non-blocking

TAREFA: Implementar os métodos getAndIncrement() e get() para garantir quiescent consistency.
"""

import threading
from typing import List


class QuiescentCounter:
    """
    Quiescent Counter
    
    Contador que satisfaz quiescent consistency. Em períodos de quiescência,
    as operações devem aparecer em ordem temporal real.
    
    TAREFA: Implementar a lógica para distribuir índices únicos sem duplicação.
    """
    
    def __init__(self):
        # Contador compartilhado
        self.counter = 0
        # Lock para sincronização
        self.lock = threading.Lock()
        
    def getAndIncrement(self):
        """
        Incrementa o contador e retorna o valor anterior
        
        TAREFA: Implementar a lógica para:
        1. Adquirir lock
        2. Ler valor atual
        3. Incrementar contador
        4. Liberar lock
        5. Retornar valor anterior
        
        DICA: Use self.lock.acquire() e self.lock.release()
        """
        raise NotImplementedError("Implementar método getAndIncrement()")
            
    def get(self):
        """
        Retorna o valor atual do contador
        
        TAREFA: Implementar a lógica para:
        1. Adquirir lock
        2. Ler valor atual
        3. Liberar lock
        4. Retornar valor
        """
        raise NotImplementedError("Implementar método get()")


def test_quiescent_counter():
    """Testa o contador quiescentemente consistente"""
    counter = QuiescentCounter()
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
    
    print(f"Quiescent Counter Test:")
    print(f"  Expected count: {expected_count}")
    print(f"  Actual count: {actual_count}")
    print(f"  Unique values: {unique_values}")
    print(f"  Success: {success}")
    
    return success


if __name__ == "__main__":
    test_quiescent_counter() 