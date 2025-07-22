"""
Testes para o algoritmo Filter Lock

Testa mutual exclusion, starvation-freedom e escalabilidade para n threads.
"""

import pytest
import threading
import time
from .filter_lock import FilterLock


@pytest.fixture
def n_threads():
    """Fixture para número de threads"""
    return 4


@pytest.fixture
def lock(n_threads):
    """Fixture para criar um FilterLock para cada teste"""
    return FilterLock(n_threads)


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


def test_scalability(n_threads):
    """Testa escalabilidade com diferentes números de threads"""
    thread_counts = [2, 3, 4, 5]
    
    for n in thread_counts:
        lock = FilterLock(n)
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


def test_level_progression(lock, n_threads):
    """Testa progressão pelos níveis"""
    def worker(thread_id):
        lock.lock()
        try:
            # Verifica se chegou ao nível mais alto
            assert lock.level[thread_id] == n_threads - 1
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


def test_victim_mechanism(lock, n_threads):
    """Testa o mecanismo de victim"""
    # Verifica se victim é usado corretamente
    assert len(lock.victim) == n_threads
    assert len(lock.level) == n_threads
    
    # Verifica estado inicial
    for i in range(n_threads):
        assert lock.level[i] == 0


def test_initial_state(lock, n_threads):
    """Testa estado inicial do lock"""
    assert len(lock.level) == n_threads
    assert len(lock.victim) == n_threads
    assert lock.n == n_threads
    
    for i in range(n_threads):
        assert lock.level[i] == 0


def test_not_implemented_error(lock):
    """Testa se métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        lock.lock()
    
    with pytest.raises(NotImplementedError):
        lock.unlock()
    
    with pytest.raises(NotImplementedError):
        lock._conflict_exists(0, 1) 