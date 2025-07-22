"""
Filter Lock Algorithm

Algoritmo de exclusão mútua para n threads que generaliza o Peterson Lock.
Cria n-1 "salas de espera" (níveis) que threads devem atravessar antes de
adquirir o lock.

Propriedades:
- ✅ Mutual Exclusion
- ✅ Deadlock-Freedom
- ✅ Starvation-Freedom

TAREFA: Implementar os métodos lock(), unlock() e _conflict_exists().
"""

import threading
from typing import List


class FilterLock:
    """
    Filter Lock Algorithm
    
    Generalização do Peterson Lock para n threads.
    Threads passam por n-1 níveis antes de entrar na seção crítica.
    Cada nível filtra uma thread, garantindo que apenas uma chegue ao final.
    
    TAREFA: Implementar a lógica de filtragem por níveis.
    """
    
    def __init__(self, n: int):
        """
        Inicializa o Filter Lock para n threads
        
        Args:
            n: Número máximo de threads
        """
        self.n = n
        # level[i] indica o nível mais alto que thread i está tentando entrar
        self.level: List[int] = [0] * n
        # victim[level] indica qual thread foi "filtrada" no nível
        self.victim: List[int] = [0] * n
        
    def lock(self):
        """
        Adquire o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual (me)
        2. Para cada nível de 1 até n-1:
           - Definir level[me] = i
           - Definir victim[i] = me
           - Aguardar até que não haja conflitos no nível i
        
        DICA: Use threading.current_thread().ident % self.n para obter thread ID
        """
        raise NotImplementedError("Implementar método lock()")
                
    def unlock(self):
        """
        Libera o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual
        2. Definir level[me] = 0 (volta ao nível 0)
        """
        raise NotImplementedError("Implementar método unlock()")
        
    def _conflict_exists(self, me: int, level: int) -> bool:
        """
        Verifica se existe conflito no nível especificado
        
        TAREFA: Implementar a lógica para:
        1. Para cada thread k diferente de me:
           - Se level[k] >= level E victim[level] == me, então há conflito
        2. Retornar True se há conflito, False caso contrário
        
        Args:
            me: ID da thread atual
            level: Nível a verificar
            
        Returns:
            True se existe conflito, False caso contrário
        """
        raise NotImplementedError("Implementar método _conflict_exists()")


def test_filter_lock():
    """Testa o algoritmo Filter Lock"""
    n_threads = 4
    lock = FilterLock(n_threads)
    counter = 0
    iterations = 100
    
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
    
    # Cria threads
    threads = []
    for _ in range(n_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica resultado
    expected = n_threads * iterations
    actual = counter
    success = actual == expected
    
    print(f"Filter Lock Test ({n_threads} threads):")
    print(f"  Expected: {expected}")
    print(f"  Actual: {actual}")
    print(f"  Success: {success}")
    
    return success


def test_starvation_freedom_filter():
    """Testa se o Filter Lock é starvation-free"""
    n_threads = 3
    lock = FilterLock(n_threads)
    access_count = [0] * n_threads
    max_iterations = 1000
    
    def worker(thread_id):
        for _ in range(max_iterations):
            lock.lock()
            try:
                access_count[thread_id] += 1
            finally:
                lock.unlock()
    
    # Cria threads
    threads = []
    for i in range(n_threads):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica se todas as threads conseguiram acessar
    success = all(count > 0 for count in access_count)
    
    print(f"Filter Lock Starvation Freedom Test:")
    for i, count in enumerate(access_count):
        print(f"  Thread {i} accesses: {count}")
    print(f"  Success: {success}")
    
    return success


if __name__ == "__main__":
    test_filter_lock()
    test_starvation_freedom_filter() 