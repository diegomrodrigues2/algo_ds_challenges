"""
Testes para o algoritmo Peterson Lock

Testa mutual exclusion, starvation-freedom e propriedades avançadas.
"""

import pytest
import threading
import time
from .peterson_lock import PetersonLock


@pytest.fixture
def lock():
    """Fixture para criar um PetersonLock para cada teste"""
    return PetersonLock()


@pytest.fixture
def counter():
    """Fixture para contador compartilhado"""
    return {'value': 0}


def test_mutual_exclusion(lock, counter):
    """Testa se o algoritmo satisfaz mutual exclusion"""
    iterations = 1000
    
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
    assert counter['value'] == expected, f"Expected {expected}, got {counter['value']}"


def test_starvation_freedom(lock):
    """Testa se o algoritmo é starvation-free"""
    access_count = [0, 0]  # Conta acessos de cada thread
    max_iterations = 5000
    
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
    assert access_count[0] > 0, "Thread 0 was starved"
    assert access_count[1] > 0, "Thread 1 was starved"
    
    # Verifica se ambas fizeram progresso significativo
    min_accesses = min(access_count)
    max_accesses = max(access_count)
    ratio = min_accesses / max_accesses
    
    assert ratio > 0.1, f"Starvation detected: ratio {ratio:.3f}"


def test_deadlock_freedom(lock, counter):
    """Testa se o algoritmo é deadlock-free"""
    def worker():
        for _ in range(100):
            lock.lock()
            try:
                counter['value'] += 1
            finally:
                lock.unlock()
    
    # Cria duas threads
    thread1 = threading.Thread(target=worker)
    thread2 = threading.Thread(target=worker)
    
    # Executa threads
    thread1.start()
    thread2.start()
    
    # Aguarda com timeout para detectar deadlock
    thread1.join(timeout=10)
    thread2.join(timeout=10)
    
    # Verifica se threads terminaram
    assert not thread1.is_alive(), "Thread 1 deadlocked"
    assert not thread2.is_alive(), "Thread 2 deadlocked"
    
    # Verifica resultado
    expected = 200
    assert counter['value'] == expected


def test_concurrent_access(lock, counter):
    """Testa acesso concorrente intenso"""
    iterations = 1000
    
    def worker():
        for _ in range(iterations):
            lock.lock()
            try:
                counter['value'] += 1
            finally:
                lock.unlock()
    
    # Cria múltiplas threads
    threads = []
    for _ in range(4):  # Testa com mais threads que o algoritmo suporta
        thread = threading.Thread(target=worker)
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica resultado
    expected = 4 * iterations
    assert counter['value'] == expected


def test_lock_state_consistency(lock):
    """Testa consistência do estado do lock"""
    # Thread 0 adquire lock
    lock.lock()
    assert lock.flag[0] is True
    assert lock.victim == 0
    
    # Thread 0 libera lock
    lock.unlock()
    assert lock.flag[0] is False
    
    # Thread 1 adquire lock
    lock.lock()
    assert lock.flag[1] is True
    assert lock.victim == 1
    
    # Thread 1 libera lock
    lock.unlock()
    assert lock.flag[1] is False


def test_initial_state(lock):
    """Testa estado inicial do lock"""
    assert lock.flag == [False, False]
    assert lock.victim == 0


def test_not_implemented_error(lock):
    """Testa se métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        lock.lock()
    
    with pytest.raises(NotImplementedError):
        lock.unlock() 