"""
Testes para o Atomic Register

Testa propriedade atomic, linearizabilidade e preservação de ordem de leitura.
"""

import pytest
import threading
import time
from .atomic_register import AtomicRegister, StampedValue


@pytest.fixture
def atomic_register():
    """Fixture para criar um AtomicRegister para cada teste"""
    return AtomicRegister(0)


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_stamped_value_comparison():
    """Testa comparação de StampedValue"""
    # Cria valores com timestamps diferentes
    val1 = StampedValue(1, "a")
    val2 = StampedValue(2, "b")
    val3 = StampedValue(1, "c")
    
    # Testa comparação
    assert val1 < val2, "Timestamp 1 should be less than 2"
    assert not (val2 < val1), "Timestamp 2 should not be less than 1"
    assert val1 == val3, "Same timestamp should be equal"
    assert val1 != val2, "Different timestamps should not be equal"


def test_atomic_property_no_overlap(atomic_register):
    """Testa que leitura sem sobreposição retorna último valor escrito"""
    # Escreve valores sequencialmente
    atomic_register.write(5)
    atomic_register.write(7)
    atomic_register.write(3)
    
    # Lê após todas as escritas (sem sobreposição)
    value = atomic_register.read()
    assert value == 3, f"Expected 3, got {value}"


def test_atomic_property_with_overlap(atomic_register, shared_results):
    """Testa que leitura com sobreposição preserva ordem atômica"""
    def writer_thread():
        # Escreve valores sequencialmente
        atomic_register.write(1)
        time.sleep(0.01)
        atomic_register.write(2)
        time.sleep(0.01)
        atomic_register.write(3)
    
    def reader_thread():
        # Lê durante as escritas (com sobreposição)
        for _ in range(5):
            value = atomic_register.read()
            shared_results.append(value)
            time.sleep(0.005)
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Verifica que valores estão em ordem crescente (atomicidade)
    for i in range(1, len(shared_results)):
        assert shared_results[i] >= shared_results[i-1], f"Atomic property violated: {shared_results[i-1]} -> {shared_results[i]}"


def test_linearizability(atomic_register, shared_results):
    """Testa linearizabilidade (ordem total de operações)"""
    def writer1():
        atomic_register.write(10)
        atomic_register.write(20)
    
    def writer2():
        atomic_register.write(30)
        atomic_register.write(40)
    
    def reader():
        for _ in range(4):
            value = atomic_register.read()
            shared_results.append(value)
            time.sleep(0.001)
    
    # Cria threads
    thread1 = threading.Thread(target=writer1)
    thread2 = threading.Thread(target=writer2)
    reader_thread = threading.Thread(target=reader)
    
    # Executa threads
    thread1.start()
    thread2.start()
    reader_thread.start()
    
    # Aguarda conclusão
    thread1.join()
    thread2.join()
    reader_thread.join()
    
    # Verifica que valores estão em ordem crescente
    for i in range(1, len(shared_results)):
        assert shared_results[i] >= shared_results[i-1], f"Linearizability violated: {shared_results[i-1]} -> {shared_results[i]}"


def test_read_order_preservation(atomic_register, shared_results):
    """Testa que ordem de leitura é preservada"""
    def writer_thread():
        for i in range(10):
            atomic_register.write(i)
            time.sleep(0.001)
    
    def reader_thread():
        # Lê rapidamente
        for _ in range(10):
            value = atomic_register.read()
            shared_results.append(value)
            time.sleep(0.0005)  # Muito rápido
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Verifica que valores estão em ordem crescente
    for i in range(1, len(shared_results)):
        assert shared_results[i] >= shared_results[i-1], f"Read order not preserved: {shared_results[i-1]} -> {shared_results[i]}"


def test_initial_value(atomic_register):
    """Testa valor inicial do registrador"""
    value = atomic_register.read()
    assert value == 0, f"Expected initial value 0, got {value}"


def test_custom_initial_value():
    """Testa registrador com valor inicial customizado"""
    register = AtomicRegister(42)
    value = register.read()
    assert value == 42, f"Expected initial value 42, got {value}"


def test_concurrent_writes(atomic_register):
    """Testa escritas concorrentes"""
    def writer(value):
        for _ in range(10):
            atomic_register.write(value)
            time.sleep(0.001)
    
    # Cria múltiplos writers
    threads = []
    for i in range(3):
        thread = threading.Thread(target=writer, args=(i,))
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica valor final (deve ser um dos valores escritos)
    final_value = atomic_register.read()
    assert final_value in [0, 1, 2], f"Final value {final_value} not expected"


def test_concurrent_reads(atomic_register, shared_results):
    """Testa leituras concorrentes"""
    atomic_register.write(5)
    
    def reader():
        for _ in range(5):
            value = atomic_register.read()
            shared_results.append(value)
            time.sleep(0.001)
    
    # Cria múltiplos readers
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=reader)
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que todas as leituras retornaram valores válidos
    assert len(shared_results) == 15, f"Expected 15 reads, got {len(shared_results)}"
    for value in shared_results:
        assert value in [0, 5], f"Value {value} not expected"


def test_not_implemented_error(atomic_register):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        atomic_register.read()
    
    with pytest.raises(NotImplementedError):
        atomic_register.write(5)
    
    # Testa StampedValue
    val1 = StampedValue(1, "a")
    val2 = StampedValue(2, "b")
    with pytest.raises(NotImplementedError):
        val1 < val2


def test_thread_safety(atomic_register, shared_results):
    """Testa thread safety básico"""
    def worker(thread_id):
        for i in range(10):
            atomic_register.write(thread_id * 10 + i)
            value = atomic_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.001)
    
    # Cria múltiplos workers
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que não houve crash e todos os valores são válidos
    assert len(shared_results) == 30, f"Expected 30 operations, got {len(shared_results)}"
    valid_values = {0}  # Valor inicial
    for i in range(3):
        for j in range(10):
            valid_values.add(i * 10 + j)
    
    for thread_id, value in shared_results:
        assert value in valid_values, f"Invalid value {value} from thread {thread_id}"


def test_atomic_vs_regular_property(atomic_register, shared_results):
    """Testa que atomic é mais forte que regular"""
    def writer_thread():
        atomic_register.write(1)
        time.sleep(0.01)
        atomic_register.write(2)
        time.sleep(0.01)
        atomic_register.write(3)
    
    def reader_thread():
        # Lê durante as escritas (com sobreposição)
        for _ in range(5):
            value = atomic_register.read()
            shared_results.append(value)
            time.sleep(0.005)
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Verifica propriedade atomic: valores em ordem crescente
    for i in range(1, len(shared_results)):
        assert shared_results[i] >= shared_results[i-1], f"Atomic property violated: {shared_results[i-1]} -> {shared_results[i]}"


def test_timestamp_uniqueness(atomic_register):
    """Testa que timestamps são únicos"""
    # Escreve valores rapidamente
    for i in range(100):
        atomic_register.write(i)
    
    # Verifica que não houve crash (timestamps únicos)
    final_value = atomic_register.read()
    assert final_value == 99, f"Expected final value 99, got {final_value}"


def test_edge_cases(atomic_register):
    """Testa casos extremos"""
    # Valor None
    register_none = AtomicRegister(None)
    assert register_none.read() is None
    
    # String vazia
    register_empty = AtomicRegister("")
    assert register_empty.read() == ""
    
    # Lista vazia
    register_list = AtomicRegister([])
    assert register_list.read() == []
    
    # Número negativo
    register_neg = AtomicRegister(-42)
    assert register_neg.read() == -42 