"""
LockOne Algorithm

Algoritmo de exclusão mútua para 2 threads baseado em flags booleanas.
Satisfaz mutual exclusion mas pode causar deadlock se threads executam
concorrentemente.

Propriedades:
- ✅ Mutual Exclusion
- ❌ Deadlock-Freedom (pode deadlock)
- ❌ Starvation-Freedom

TAREFA: Implementar os métodos lock() e unlock() para garantir exclusão mútua.
"""

import threading
from typing import List


class LockOne:
    """
    LockOne Algorithm
    
    Usa array de flags booleanas para indicar interesse em entrar na seção crítica.
    Thread i define flag[i] = True e aguarda flag[j] = False.
    
    TAREFA: Implementar a lógica de exclusão mútua usando flags.
    """
    
    def __init__(self):
        # Flags para indicar interesse em entrar na seção crítica
        self.flag: List[bool] = [False, False]
        
    def lock(self):
        """
        Adquire o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual (0 ou 1)
        2. Definir flag[i] = True para indicar interesse
        3. Aguardar até que flag[j] = False (outra thread desistiu)
        
        DICA: Use threading.current_thread().ident % 2 para obter thread ID
        """
        raise NotImplementedError("Implementar método lock()")
            
    def unlock(self):
        """
        Libera o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual
        2. Definir flag[i] = False para desistir do lock
        """
        raise NotImplementedError("Implementar método unlock()")


def test_lock_one():
    """Testa o algoritmo LockOne"""
    lock = LockOne()
    counter = 0
    iterations = 1000
    
    def worker():
        nonlocal counter
        for _ in range(iterations):
            lock.lock()
            try:
                # Seção crítica
                temp = counter
                counter = temp + 1
            finally:
                lock.unlock()
    
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
    expected = 2 * iterations
    actual = counter
    success = actual == expected
    
    print(f"LockOne Test:")
    print(f"  Expected: {expected}")
    print(f"  Actual: {actual}")
    print(f"  Success: {success}")
    
    return success


if __name__ == "__main__":
    test_lock_one() 