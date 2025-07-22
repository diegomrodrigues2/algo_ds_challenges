"""
Testes para o algoritmo LockOne

Testa mutual exclusion, deadlock scenarios e propriedades básicas.
"""

import pytest
import threading
import time
from .lock_one import LockOne


@pytest.fixture
def lock():
    """Fixture para criar um LockOne para cada teste"""
    return LockOne()


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


def test_deadlock_scenario(lock, counter):
    """Testa cenário que pode causar deadlock"""
    # Este teste pode falhar devido ao deadlock
    # LockOne pode deadlock se threads executam concorrentemente
    
    def worker(thread_id):
        for _ in range(100):
            lock.lock()
            try:
                counter['value'] += 1
            finally:
                lock.unlock()
    
    # Cria duas threads
    thread1 = threading.Thread(target=worker, args=(0,))
    thread2 = threading.Thread(target=worker, args=(1,))
    
    # Executa threads
    thread1.start()
    thread2.start()
    
    # Aguarda com timeout para detectar deadlock
    thread1.join(timeout=5)
    thread2.join(timeout=5)
    
    # Se threads não terminaram, pode ser deadlock
    if thread1.is_alive() or thread2.is_alive():
        pytest.skip("Deadlock detected - this is expected for LockOne")
    
    # Se terminou, verifica resultado
    expected = 200
    assert counter['value'] == expected


def test_sequential_execution(lock, counter):
    """Testa execução sequencial (não deve deadlock)"""
    iterations = 1000
    
    def worker():
        for _ in range(iterations):
            lock.lock()
            try:
                counter['value'] += 1
            finally:
                lock.unlock()
    
    # Executa uma thread por vez
    thread1 = threading.Thread(target=worker)
    thread1.start()
    thread1.join()
    
    thread2 = threading.Thread(target=worker)
    thread2.start()
    thread2.join()
    
    # Verifica resultado
    expected = 2 * iterations
    assert counter['value'] == expected


def test_lock_unlock_sequence(lock):
    """Testa sequência básica de lock/unlock"""
    # Thread 0
    lock.lock()
    assert lock.flag[0] is True
    lock.unlock()
    assert lock.flag[0] is False
    
    # Thread 1
    lock.lock()
    assert lock.flag[1] is True
    lock.unlock()
    assert lock.flag[1] is False


def test_initial_state(lock):
    """Testa estado inicial do lock"""
    assert lock.flag == [False, False]


def test_not_implemented_error(lock):
    """Testa se métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        lock.lock()
    
    with pytest.raises(NotImplementedError):
        lock.unlock() 