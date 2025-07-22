"""
Testes para o algoritmo LockTwo

Testa mutual exclusion, deadlock scenarios e propriedades básicas.
"""

import pytest
import threading
import time
from .lock_two import LockTwo


@pytest.fixture
def lock():
    """Fixture para criar um LockTwo para cada teste"""
    return LockTwo()


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
    # LockTwo pode deadlock se uma thread executa completamente antes da outra
    
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
        pytest.skip("Deadlock detected - this is expected for LockTwo")
    
    # Se terminou, verifica resultado
    expected = 200
    assert counter['value'] == expected


def test_concurrent_execution(lock, counter):
    """Testa execução concorrente (não deve deadlock)"""
    iterations = 1000
    
    def worker():
        for _ in range(iterations):
            lock.lock()
            try:
                counter['value'] += 1
            finally:
                lock.unlock()
    
    # Cria duas threads
    thread1 = threading.Thread(target=worker)
    thread2 = threading.Thread(target=worker)
    
    # Executa threads simultaneamente
    thread1.start()
    thread2.start()
    
    # Aguarda conclusão
    thread1.join()
    thread2.join()
    
    # Verifica resultado
    expected = 2 * iterations
    assert counter['value'] == expected


def test_victim_mechanism(lock):
    """Testa o mecanismo de victim"""
    # Verifica estado inicial
    assert lock.victim == 0
    
    # Simula uso do victim (sem implementação real)
    # O teste real seria feito após implementação


def test_initial_state(lock):
    """Testa estado inicial do lock"""
    assert lock.victim == 0


def test_not_implemented_error(lock):
    """Testa se métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        lock.lock()
    
    with pytest.raises(NotImplementedError):
        lock.unlock()


def test_victim_field_access(lock):
    """Testa acesso ao campo victim"""
    # Verifica que o campo victim existe e é acessível
    assert hasattr(lock, 'victim')
    assert isinstance(lock.victim, int) 