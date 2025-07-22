"""
LockTwo Algorithm

Algoritmo de exclusão mútua para 2 threads baseado em campo victim.
Satisfaz mutual exclusion mas pode causar deadlock se uma thread executa
completamente antes da outra.

Propriedades:
- ✅ Mutual Exclusion
- ❌ Deadlock-Freedom (pode deadlock)
- ❌ Starvation-Freedom

TAREFA: Implementar os métodos lock() e unlock() usando o mecanismo victim.
"""

import threading


class LockTwo:
    """
    LockTwo Algorithm
    
    Usa campo victim para indicar qual thread deve esperar.
    Thread i define victim = i e aguarda victim != i.
    
    TAREFA: Implementar a lógica de exclusão mútua usando victim.
    """
    
    def __init__(self):
        # Campo victim indica qual thread deve esperar
        self.victim = 0
        
    def lock(self):
        """
        Adquire o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual (0 ou 1)
        2. Definir victim = i (deixa a outra thread ir primeiro)
        3. Aguardar até que victim != i (não sou mais a vítima)
        
        DICA: Use threading.current_thread().ident % 2 para obter thread ID
        """
        raise NotImplementedError("Implementar método lock()")
            
    def unlock(self):
        """
        Libera o lock
        
        TAREFA: Implementar a lógica para:
        Neste algoritmo, unlock() não precisa fazer nada explicitamente.
        O victim já foi alterado durante o lock().
        """
        raise NotImplementedError("Implementar método unlock()")


def test_lock_two():
    """Testa o algoritmo LockTwo"""
    lock = LockTwo()
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
    
    print(f"LockTwo Test:")
    print(f"  Expected: {expected}")
    print(f"  Actual: {actual}")
    print(f"  Success: {success}")
    
    return success


if __name__ == "__main__":
    test_lock_two() 