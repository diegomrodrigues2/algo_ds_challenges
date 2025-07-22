"""
Testes para o MRSW Register

Testa propriedades multi-reader, single-writer e atomicidade.
"""

import pytest
import threading
import time
from .mrsw_register import MRSWRegister


@pytest.fixture
def mrsw_register():
    """Fixture para criar um MRSWRegister para cada teste"""
    return MRSWRegister(0, 4)


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_multi_reader_single_writer(mrsw_register, shared_results):
    """Testa que múltiplos leitores podem ler simultaneamente"""
    def writer_thread():
        # Escreve valores sequencialmente
        mrsw_register.write(10)
        time.sleep(0.01)
        mrsw_register.write(20)
        time.sleep(0.01)
        mrsw_register.write(30)
    
    def reader_thread(thread_id):
        # Lê valores (cada thread lê do seu registrador)
        for _ in range(3):
            value = mrsw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.005)
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    readers = []
    for i in range(3):
        reader = threading.Thread(target=reader_thread, args=(i,))
        readers.append(reader)
    
    # Executa threads
    writer.start()
    for reader in readers:
        reader.start()
    
    # Aguarda conclusão
    writer.join()
    for reader in readers:
        reader.join()
    
    # Verifica que todos os leitores leram valores válidos
    assert len(shared_results) == 9, f"Expected 9 reads, got {len(shared_results)}"
    valid_values = {0, 10, 20, 30}  # Inclui valor inicial
    for thread_id, value in shared_results:
        assert value in valid_values, f"Invalid value {value} from thread {thread_id}"


def test_atomic_property(mrsw_register, shared_results):
    """Testa propriedade atômica com múltiplos leitores"""
    def writer_thread():
        for i in range(5):
            mrsw_register.write(i)
            time.sleep(0.01)
    
    def reader_thread(thread_id):
        # Lê rapidamente
        for _ in range(5):
            value = mrsw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.002)
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    readers = []
    for i in range(3):
        reader = threading.Thread(target=reader_thread, args=(i,))
        readers.append(reader)
    
    # Executa threads
    writer.start()
    for reader in readers:
        reader.start()
    
    # Aguarda conclusão
    writer.join()
    for reader in readers:
        reader.join()
    
    # Verifica que valores estão em ordem crescente para cada thread
    thread_values = {}
    for thread_id, value in shared_results:
        if thread_id not in thread_values:
            thread_values[thread_id] = []
        thread_values[thread_id].append(value)
    
    for thread_id, values in thread_values.items():
        for i in range(1, len(values)):
            assert values[i] >= values[i-1], f"Atomic property violated for thread {thread_id}: {values[i-1]} -> {values[i]}"


def test_initial_value(mrsw_register):
    """Testa valor inicial do registrador"""
    value = mrsw_register.read()
    assert value == 0, f"Expected initial value 0, got {value}"


def test_custom_initial_value():
    """Testa registrador com valor inicial customizado"""
    register = MRSWRegister(42, 2)
    value = register.read()
    assert value == 42, f"Expected initial value 42, got {value}"


def test_concurrent_reads(mrsw_register, shared_results):
    """Testa leituras concorrentes de múltiplos threads"""
    mrsw_register.write(5)
    
    def reader(thread_id):
        for _ in range(3):
            value = mrsw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.001)
    
    # Cria múltiplos readers
    threads = []
    for i in range(4):
        thread = threading.Thread(target=reader, args=(i,))
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que todas as leituras retornaram valores válidos
    assert len(shared_results) == 12, f"Expected 12 reads, got {len(shared_results)}"
    for thread_id, value in shared_results:
        assert value in [0, 5], f"Value {value} not expected from thread {thread_id}"


def test_not_implemented_error(mrsw_register):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        mrsw_register.read()
    
    with pytest.raises(NotImplementedError):
        mrsw_register.write(5)


def test_thread_id_generation(mrsw_register):
    """Testa geração de IDs únicos para threads"""
    thread_ids = set()
    
    def worker():
        thread_id = mrsw_register._get_thread_id()
        thread_ids.add(thread_id)
    
    # Cria múltiplos threads
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=worker)
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que IDs estão no range correto
    for thread_id in thread_ids:
        assert 0 <= thread_id < mrsw_register.num_threads, f"Thread ID {thread_id} out of range"


def test_thread_safety(mrsw_register, shared_results):
    """Testa thread safety básico"""
    def worker(thread_id):
        for i in range(5):
            mrsw_register.write(thread_id * 10 + i)
            value = mrsw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.001)
    
    # Cria múltiplos workers (mas apenas um pode escrever)
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
    
    # Verifica que não houve crash
    assert len(shared_results) == 15, f"Expected 15 operations, got {len(shared_results)}"


def test_register_array_size(mrsw_register):
    """Testa que array de registradores tem tamanho correto"""
    assert len(mrsw_register.registers) == mrsw_register.num_threads, f"Expected {mrsw_register.num_threads} registers, got {len(mrsw_register.registers)}"


def test_different_num_threads():
    """Testa registrador com diferentes números de threads"""
    # Testa com 2 threads
    register_2 = MRSWRegister(0, 2)
    assert len(register_2.registers) == 2
    
    # Testa com 8 threads
    register_8 = MRSWRegister(0, 8)
    assert len(register_8.registers) == 8


def test_edge_cases(mrsw_register):
    """Testa casos extremos"""
    # Valor None
    register_none = MRSWRegister(None, 2)
    assert register_none.read() is None
    
    # String vazia
    register_empty = MRSWRegister("", 2)
    assert register_empty.read() == ""
    
    # Lista vazia
    register_list = MRSWRegister([], 2)
    assert register_list.read() == []


def test_sequential_writes(mrsw_register):
    """Testa escritas sequenciais"""
    # Escreve valores sequencialmente
    for i in range(10):
        mrsw_register.write(i)
    
    # Verifica valor final
    final_value = mrsw_register.read()
    assert final_value == 9, f"Expected final value 9, got {final_value}"


def test_rapid_writes_and_reads(mrsw_register, shared_results):
    """Testa escritas e leituras rápidas"""
    def writer():
        for i in range(20):
            mrsw_register.write(i)
            time.sleep(0.0001)  # Muito rápido
    
    def reader(thread_id):
        for _ in range(10):
            value = mrsw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.0001)  # Muito rápido
    
    # Cria threads
    writer_thread = threading.Thread(target=writer)
    readers = []
    for i in range(3):
        reader_thread = threading.Thread(target=reader, args=(i,))
        readers.append(reader_thread)
    
    # Executa threads
    writer_thread.start()
    for reader_thread in readers:
        reader_thread.start()
    
    # Aguarda conclusão
    writer_thread.join()
    for reader_thread in readers:
        reader_thread.join()
    
    # Verifica que não houve crash
    assert len(shared_results) == 30, f"Expected 30 reads, got {len(shared_results)}"
    for thread_id, value in shared_results:
        assert 0 <= value <= 19, f"Value {value} out of range from thread {thread_id}" 