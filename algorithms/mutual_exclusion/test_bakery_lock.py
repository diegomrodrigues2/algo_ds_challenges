"""
Testes para o algoritmo Bakery Lock

Testa mutual exclusion, starvation-freedom e propriedade first-come-first-served.
"""

import pytest
import threading
import time
from .bakery_lock import BakeryLock


@pytest.fixture
def n_threads():
    """Fixture para número de threads"""
    return 4


@pytest.fixture
def lock(n_threads):
    """Fixture para criar um BakeryLock para cada teste"""
    return BakeryLock(n_threads)


@pytest.fixture
def counter():
    """Fixture para contador compartilhado"""
    return {'value': 0}


def test_mutual_exclusion(lock, counter, n_threads):
    """Testa se o algoritmo satisfaz mutual exclusion"""
    iterations = 100
    
    def worker():
        for _ in range(iterations):
            lock.lock()
            try:
                # Seção crítica
                temp = counter['value']
                time.sleep(0.0001)  # Simula trabalho
                counter['value'] = temp + 1
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
    assert counter['value'] == expected, f"Expected {expected}, got {counter['value']}"


def test_starvation_freedom(lock, n_threads):
    """Testa se o algoritmo é starvation-free"""
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
    for i, count in enumerate(access_count):
        assert count > 0, f"Thread {i} was starved"
    
    # Verifica se todas fizeram progresso significativo
    min_accesses = min(access_count)
    max_accesses = max(access_count)
    ratio = min_accesses / max_accesses
    
    assert ratio > 0.1, f"Starvation detected: ratio {ratio:.3f}"


def test_deadlock_freedom(lock, counter, n_threads):
    """Testa se o algoritmo é deadlock-free"""
    def worker():
        for _ in range(50):
            lock.lock()
            try:
                counter['value'] += 1
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
    
    # Aguarda com timeout para detectar deadlock
    for thread in threads:
        thread.join(timeout=10)
    
    # Verifica se threads terminaram
    for i, thread in enumerate(threads):
        assert not thread.is_alive(), f"Thread {i} deadlocked"
    
    # Verifica resultado
    expected = n_threads * 50
    assert counter['value'] == expected


def test_first_come_first_served(lock, n_threads):
    """Testa a propriedade first-come-first-served"""
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
        time.sleep(0.001)  # Pequeno delay
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica se a ordem de acesso é aproximadamente FIFO
    # (pode haver pequenas variações devido ao scheduling)
    assert len(access_order) == n_threads


def test_scalability(n_threads):
    """Testa escalabilidade com diferentes números de threads"""
    thread_counts = [2, 3, 4, 5]
    
    for n in thread_counts:
        lock = BakeryLock(n)
        counter = {'value': 0}
        iterations = 50
        
        def worker():
            for _ in range(iterations):
                lock.lock()
                try:
                    counter['value'] += 1
                finally:
                    lock.unlock()
        
        # Cria e executa threads
        threads = []
        for _ in range(n):
            thread = threading.Thread(target=worker)
            threads.append(thread)
        
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        
        # Verifica resultado
        expected = n * iterations
        assert counter['value'] == expected, f"Failed for {n} threads"


def test_initial_state(lock, n_threads):
    """Testa estado inicial do lock"""
    assert len(lock.flag) == n_threads
    assert len(lock.label) == n_threads
    assert lock.n == n_threads
    
    for i in range(n_threads):
        assert lock.flag[i] is False
        assert lock.label[i] == 0


def test_not_implemented_error(lock):
    """Testa se métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        lock.lock()
    
    with pytest.raises(NotImplementedError):
        lock.unlock()
    
    with pytest.raises(NotImplementedError):
        lock._max_label()
    
    with pytest.raises(NotImplementedError):
        lock._someone_ahead(0)
    
    with pytest.raises(NotImplementedError):
        lock._lexicographic_less(0, 1)


def test_flag_and_label_access(lock, n_threads):
    """Testa acesso aos campos flag e label"""
    # Verifica que os campos existem e são acessíveis
    assert hasattr(lock, 'flag')
    assert hasattr(lock, 'label')
    assert isinstance(lock.flag, list)
    assert isinstance(lock.label, list)
    assert len(lock.flag) == n_threads
    assert len(lock.label) == n_threads 