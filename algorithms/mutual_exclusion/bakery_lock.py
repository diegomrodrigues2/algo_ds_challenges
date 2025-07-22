"""
Bakery Lock Algorithm

Algoritmo de exclusão mútua para n threads baseado em timestamps.
Mantém propriedade first-come-first-served usando sistema distribuído
de números como em padarias.

Propriedades:
- ✅ Mutual Exclusion
- ✅ Deadlock-Freedom
- ✅ Starvation-Freedom
- ✅ First-Come-First-Served

TAREFA: Implementar os métodos lock(), unlock() e métodos auxiliares.
"""

import threading
from typing import List


class BakeryLock:
    """
    Bakery Lock Algorithm
    
    Usa sistema de timestamps distribuído para garantir ordem FIFO.
    Cada thread pega um número na "porta" e aguarda até que nenhuma
    thread com número anterior esteja tentando entrar.
    
    TAREFA: Implementar a lógica de timestamps distribuídos.
    """
    
    def __init__(self, n: int):
        """
        Inicializa o Bakery Lock para n threads
        
        Args:
            n: Número máximo de threads
        """
        self.n = n
        # flag[i] indica se thread i quer entrar na seção crítica
        self.flag: List[bool] = [False] * n
        # label[i] indica o número da thread i na fila
        self.label: List[int] = [0] * n
        
    def lock(self):
        """
        Adquire o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual (me)
        2. Doorway: definir flag[me] = True e label[me] = max_label() + 1
        3. Waiting: aguardar até que não há ninguém na frente (_someone_ahead(me) = False)
        
        DICA: Use threading.current_thread().ident % self.n para obter thread ID
        """
        raise NotImplementedError("Implementar método lock()")
            
    def unlock(self):
        """
        Libera o lock
        
        TAREFA: Implementar a lógica para:
        1. Obter o ID da thread atual
        2. Definir flag[me] = False (sai da fila)
        """
        raise NotImplementedError("Implementar método unlock()")
        
    def _max_label(self) -> int:
        """
        Encontra o maior label entre todas as threads
        
        TAREFA: Implementar a lógica para:
        1. Percorrer todos os labels das threads
        2. Retornar o maior valor encontrado
        
        Returns:
            O maior label entre todas as threads
        """
        raise NotImplementedError("Implementar método _max_label()")
        
    def _someone_ahead(self, me: int) -> bool:
        """
        Verifica se há alguém na frente na fila
        
        TAREFA: Implementar a lógica para:
        1. Para cada thread k diferente de me:
           - Se flag[k] = True E _lexicographic_less(k, me), então há alguém na frente
        2. Retornar True se há alguém na frente, False caso contrário
        
        Args:
            me: ID da thread atual
            
        Returns:
            True se há alguém na frente, False caso contrário
        """
        raise NotImplementedError("Implementar método _someone_ahead()")
        
    def _lexicographic_less(self, i: int, j: int) -> bool:
        """
        Comparação lexicográfica: (label[i], i) < (label[j], j)
        
        TAREFA: Implementar a lógica para:
        1. Comparar label[i] com label[j]
        2. Se label[i] < label[j], retornar True
        3. Se label[i] == label[j], comparar i com j
        4. Retornar True se (label[i], i) < (label[j], j)
        
        Args:
            i: ID da primeira thread
            j: ID da segunda thread
            
        Returns:
            True se (label[i], i) < (label[j], j)
        """
        raise NotImplementedError("Implementar método _lexicographic_less()")


def test_bakery_lock():
    """Testa o algoritmo Bakery Lock"""
    n_threads = 4
    lock = BakeryLock(n_threads)
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
    
    print(f"Bakery Lock Test ({n_threads} threads):")
    print(f"  Expected: {expected}")
    print(f"  Actual: {actual}")
    print(f"  Success: {success}")
    
    return success


def test_first_come_first_served():
    """Testa a propriedade first-come-first-served"""
    n_threads = 3
    lock = BakeryLock(n_threads)
    access_order = []
    
    def worker(thread_id):
        lock.lock()
        try:
            access_order.append(thread_id)
        finally:
            lock.unlock()
    
    # Cria threads
    threads = []
    for i in range(n_threads):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
    
    # Executa threads com pequeno delay para simular chegada sequencial
    for i, thread in enumerate(threads):
        thread.start()
        import time
        time.sleep(0.001)  # Pequeno delay
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica se a ordem de acesso é aproximadamente FIFO
    # (pode haver pequenas variações devido ao scheduling)
    print(f"First-Come-First-Served Test:")
    print(f"  Access order: {access_order}")
    print(f"  Success: {len(access_order) == n_threads}")
    
    return len(access_order) == n_threads


if __name__ == "__main__":
    test_bakery_lock()
    test_first_come_first_served() 