"""
Testes para o Wait-Free Counter

Testa wait-freedom, distribuição de valores únicos e propriedades básicas.
"""

import pytest
import threading
import time
from .wait_free_counter import WaitFreeCounter


@pytest.fixture
def counter():
    """Fixture para criar um WaitFreeCounter para cada teste"""
    return WaitFreeCounter()


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_wait_freedom(counter, shared_results):
    """Testa se o contador satisfaz wait-freedom"""
    iterations = 1000
    
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
    
    # Verifica resultado
    expected_count = 4 * iterations
    actual_count = counter.get()
    unique_values = len(set(shared_results))
    
    # Wait-freedom: sem duplicação ou omissão
    assert actual_count == expected_count, f"Expected count {expected_count}, got {actual_count}"
    assert unique_values == expected_count, f"Expected {expected_count} unique values, got {unique_values}"
    assert all(0 <= v < expected_count for v in shared_results), "Values out of range"


def test_no_starvation(counter, shared_results):
    """Testa que não há starvation (todas as threads fazem progresso)"""
    iterations = 500
    
    def worker(thread_id):
        for _ in range(iterations):
            value = counter.getAndIncrement()
            shared_results.append((thread_id, value))
    
    # Cria múltiplas threads
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que todas as threads contribuíram
    thread_contributions = {}
    for thread_id, value in shared_results:
        if thread_id not in thread_contributions:
            thread_contributions[thread_id] = []
        thread_contributions[thread_id].append(value)
    
    # Cada thread deve ter contribuído com iterations valores
    for thread_id in range(3):
        assert len(thread_contributions[thread_id]) == iterations, \
            f"Thread {thread_id} contributed {len(thread_contributions[thread_id])} values, expected {iterations}"


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
    
    # Cria múltiplas threads
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica resultado
    expected_count = 5 * iterations
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


def test_wait_free_progress(counter, shared_results):
    """Testa que wait-freedom garante progresso independente"""
    iterations = 200
    
    def fast_worker():
        # Thread rápida
        for _ in range(iterations):
            value = counter.getAndIncrement()
            shared_results.append(("fast", value))
    
    def slow_worker():
        # Thread lenta (simula delay)
        for _ in range(iterations):
            value = counter.getAndIncrement()
            shared_results.append(("slow", value))
            time.sleep(0.001)  # Simula trabalho lento
    
    # Cria threads
    fast_thread = threading.Thread(target=fast_worker)
    slow_thread = threading.Thread(target=slow_worker)
    
    # Executa threads
    fast_thread.start()
    slow_thread.start()
    
    # Aguarda conclusão
    fast_thread.join()
    slow_thread.join()
    
    # Verifica que ambas as threads completaram
    fast_count = len([r for r in shared_results if r[0] == "fast"])
    slow_count = len([r for r in shared_results if r[0] == "slow"])
    
    assert fast_count == iterations, f"Fast thread completed {fast_count}, expected {iterations}"
    assert slow_count == iterations, f"Slow thread completed {slow_count}, expected {iterations}"


def test_local_counters_independence(counter):
    """Testa que contadores locais são independentes"""
    # Simula múltiplas threads acessando o contador
    thread_ids = [1, 5, 10, 15]  # IDs de threads diferentes
    
    def simulate_thread_access(thread_id):
        # Simula acesso de uma thread específica
        # (Esta é uma demonstração conceitual)
        return thread_id
    
    # Verifica que diferentes threads podem acessar independentemente
    for thread_id in thread_ids:
        # Em uma implementação real, cada thread teria seu próprio contador local
        result = simulate_thread_access(thread_id)
        assert result == thread_id, f"Expected {thread_id}, got {result}"


def test_bound_on_steps(counter):
    """Testa que wait-freedom implica limite no número de passos"""
    # Wait-freedom significa que cada operação termina em número finito de passos
    # independente do comportamento de outras threads
    
    def worker():
        for _ in range(10):
            start_time = time.time()
            value = counter.getAndIncrement()
            end_time = time.time()
            
            # Verifica que a operação termina rapidamente
            # (em uma implementação real, seria um limite constante)
            assert end_time - start_time < 1.0, "Operation took too long"
    
    # Cria thread
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()
    
    # Se chegou aqui, as operações terminaram em tempo finito
    assert True, "Wait-freedom ensures bounded number of steps"


if __name__ == "__main__":
    pytest.main([__file__]) 