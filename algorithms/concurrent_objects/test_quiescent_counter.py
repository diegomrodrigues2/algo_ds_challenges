"""
Testes para o Quiescent Counter

Testa quiescent consistency, distribuição de valores únicos e propriedades básicas.
"""

import pytest
import threading
import time
from .quiescent_counter import QuiescentCounter


@pytest.fixture
def counter():
    """Fixture para criar um QuiescentCounter para cada teste"""
    return QuiescentCounter()


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_quiescent_consistency(counter, shared_results):
    """Testa se o contador satisfaz quiescent consistency"""
    iterations = 1000
    
    def worker():
        for _ in range(iterations):
            value = counter.getAndIncrement()
            shared_results.append(value)
    
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
    expected_count = 2 * iterations
    actual_count = counter.get()
    unique_values = len(set(shared_results))
    
    # Quiescent consistency: sem duplicação ou omissão
    assert actual_count == expected_count, f"Expected count {expected_count}, got {actual_count}"
    assert unique_values == expected_count, f"Expected {expected_count} unique values, got {unique_values}"
    assert all(0 <= v < expected_count for v in shared_results), "Values out of range"


def test_no_duplicates(counter, shared_results):
    """Testa que não há valores duplicados"""
    iterations = 500
    
    def worker():
        for _ in range(iterations):
            value = counter.getAndIncrement()
            shared_results.append(value)
    
    # Cria múltiplas threads
    threads = []
    for _ in range(4):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que não há duplicatas
    unique_values = set(shared_results)
    assert len(unique_values) == len(shared_results), "Duplicate values found"


def test_sequential_execution(counter):
    """Testa execução sequencial (deve funcionar corretamente)"""
    results = []
    
    # Execução sequencial
    for i in range(100):
        value = counter.getAndIncrement()
        results.append(value)
    
    # Verifica ordem sequencial
    assert results == list(range(100)), "Sequential execution should be ordered"


def test_get_operation(counter):
    """Testa operação get()"""
    # Incrementa algumas vezes
    for _ in range(10):
        counter.getAndIncrement()
    
    # Verifica valor atual
    current_value = counter.get()
    assert current_value == 10, f"Expected 10, got {current_value}"


def test_concurrent_get_and_increment(counter, shared_results):
    """Testa operações getAndIncrement() concorrentes"""
    iterations = 100
    
    def worker():
        for _ in range(iterations):
            value = counter.getAndIncrement()
            shared_results.append(value)
    
    # Cria três threads
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica resultado
    expected_count = 3 * iterations
    actual_count = counter.get()
    unique_values = len(set(shared_results))
    
    assert actual_count == expected_count, f"Expected {expected_count}, got {actual_count}"
    assert unique_values == expected_count, f"Expected {expected_count} unique values, got {unique_values}"


def test_initial_state(counter):
    """Testa estado inicial do contador"""
    initial_value = counter.get()
    assert initial_value == 0, f"Expected 0, got {initial_value}"


def test_not_implemented_error(counter):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        counter.getAndIncrement()
    
    with pytest.raises(NotImplementedError):
        counter.get()


def test_quiescent_period(counter, shared_results):
    """Testa comportamento durante período de quiescência"""
    # Primeira fase: operações concorrentes
    def worker1():
        for _ in range(50):
            value = counter.getAndIncrement()
            shared_results.append(value)
    
    def worker2():
        for _ in range(50):
            value = counter.getAndIncrement()
            shared_results.append(value)
    
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    # Período de quiescência
    time.sleep(0.1)
    
    # Segunda fase: operações sequenciais
    sequential_results = []
    for _ in range(20):
        value = counter.getAndIncrement()
        sequential_results.append(value)
    
    # Verifica que valores sequenciais são consecutivos
    expected_start = 100  # 50 + 50 da primeira fase
    assert sequential_results == list(range(expected_start, expected_start + 20)), \
        "Sequential operations after quiescence should be ordered"


if __name__ == "__main__":
    pytest.main([__file__]) 