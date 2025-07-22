"""
Peterson Lock Algorithm

Algoritmo de exclusão mútua para 2 threads que combina LockOne e LockTwo.
É starvation-free e considerado o mais elegante algoritmo para 2 threads.

Propriedades:
- ✅ Mutual Exclusion
- ✅ Deadlock-Freedom
- ✅ Starvation-Freedom

TAREFA: Implementar os métodos lock() e unlock() combinando flags e victim.
"""

import threading
from typing import List


class PetersonLock:
    """
    Peterson Lock Algorithm
    
    Combina flags booleanas (LockOne) com campo victim (LockTwo).
    Thread i define flag[i] = True, victim = i, e aguarda até que
    flag[j] = False OU victim != i.
    
    TAREFA: Implementar a lógica combinando ambos os mecanismos.
    """
    
    def __init__(self):
        # Flags para indicar interesse em entrar na seção crítica
        self.flag: List[bool] = [False, False]
        # Campo victim indica qual thread deve esperar
        self.victim = 0
        
    def lock(self):
        """
        Adquire o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual (0 ou 1) e da outra thread (1 ou 0)
        2. Definir flag[i] = True (indica interesse - LockOne)
        3. Definir victim = i (deixa outra ir primeiro - LockTwo)
        4. Aguardar até que flag[j] = False OU victim != i
        
        DICA: Combine as condições de LockOne e LockTwo para evitar deadlock
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


def test_peterson_lock():
    """Testa o algoritmo Peterson Lock"""
    lock = PetersonLock()
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
    
    print(f"Peterson Lock Test:")
    print(f"  Expected: {expected}")
    print(f"  Actual: {actual}")
    print(f"  Success: {success}")
    
    return success


def test_starvation_freedom():
    """Testa se o algoritmo é starvation-free"""
    lock = PetersonLock()
    access_count = [0, 0]  # Conta acessos de cada thread
    max_iterations = 10000
    
    def worker(thread_id):
        for _ in range(max_iterations):
            lock.lock()
            try:
                access_count[thread_id] += 1
            finally:
                lock.unlock()
    
    # Cria duas threads
    thread1 = threading.Thread(target=worker, args=(0,))
    thread2 = threading.Thread(target=worker, args=(1,))
    
    # Executa threads
    thread1.start()
    thread2.start()
    
    # Aguarda conclusão
    thread1.join()
    thread2.join()
    
    # Verifica se ambas as threads conseguiram acessar
    success = access_count[0] > 0 and access_count[1] > 0
    
    print(f"Starvation Freedom Test:")
    print(f"  Thread 0 accesses: {access_count[0]}")
    print(f"  Thread 1 accesses: {access_count[1]}")
    print(f"  Success: {success}")
    
    return success


if __name__ == "__main__":
    test_peterson_lock()
    test_starvation_freedom() 