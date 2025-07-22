"""
Testes para o MRMW Register

Testa propriedades multi-reader, multi-writer e atomicidade com timestamps.
"""

import pytest
import threading
import time
from .mrmw_register import MRMWRegister


@pytest.fixture
def mrmw_register():
    """Fixture para criar um MRMWRegister para cada teste"""
    return MRMWRegister(0, 4)


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_multi_reader_multi_writer(mrmw_register, shared_results):
    """Testa que múltiplos leitores e escritores podem operar simultaneamente"""
    def writer_thread(thread_id):
        # Escreve valores sequencialmente
        mrmw_register.write(thread_id * 10 + 1)
        time.sleep(0.01)
        mrmw_register.write(thread_id * 10 + 2)
        time.sleep(0.01)
        mrmw_register.write(thread_id * 10 + 3)
    
    def reader_thread(thread_id):
        # Lê valores
        for _ in range(3):
            value = mrmw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.005)
    
    # Cria threads
    writers = []
    for i in range(2):
        writer = threading.Thread(target=writer_thread, args=(i,))
        writers.append(writer)
    
    readers = []
    for i in range(2):
        reader = threading.Thread(target=reader_thread, args=(i,))
        readers.append(reader)
    
    # Executa threads
    for writer in writers:
        writer.start()
    for reader in readers:
        reader.start()
    
    # Aguarda conclusão
    for writer in writers:
        writer.join()
    for reader in readers:
        reader.join()
    
    # Verifica que todos os leitores leram valores válidos
    assert len(shared_results) == 6, f"Expected 6 reads, got {len(shared_results)}"
    valid_values = {0, 1, 2, 3, 11, 12, 13, 21, 22, 23}  # Inclui valor inicial
    for thread_id, value in shared_results:
        assert value in valid_values, f"Invalid value {value} from thread {thread_id}"


def test_atomic_property(mrmw_register, shared_results):
    """Testa propriedade atômica com múltiplos escritores"""
    def writer_thread(thread_id):
        for i in range(5):
            mrmw_register.write(thread_id * 100 + i)
            time.sleep(0.01)
    
    def reader_thread(thread_id):
        # Lê rapidamente
        for _ in range(5):
            value = mrmw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.002)
    
    # Cria threads
    writers = []
    for i in range(2):
        writer = threading.Thread(target=writer_thread, args=(i,))
        writers.append(writer)
    
    readers = []
    for i in range(2):
        reader = threading.Thread(target=reader_thread, args=(i,))
        readers.append(reader)
    
    # Executa threads
    for writer in writers:
        writer.start()
    for reader in readers:
        reader.start()
    
    # Aguarda conclusão
    for writer in writers:
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


def test_initial_value(mrmw_register):
    """Testa valor inicial do registrador"""
    value = mrmw_register.read()
    assert value == 0, f"Expected initial value 0, got {value}"


def test_custom_initial_value():
    """Testa registrador com valor inicial customizado"""
    register = MRMWRegister(42, 2)
    value = register.read()
    assert value == 42, f"Expected initial value 42, got {value}"


def test_concurrent_writes(mrmw_register):
    """Testa escritas concorrentes de múltiplos threads"""
    def writer(thread_id):
        for i in range(10):
            mrmw_register.write(thread_id * 10 + i)
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
    final_value = mrmw_register.read()
    valid_final_values = {9, 19, 29}  # Últimos valores de cada writer
    assert final_value in valid_final_values, f"Final value {final_value} not expected"


def test_concurrent_reads(mrmw_register, shared_results):
    """Testa leituras concorrentes de múltiplos threads"""
    mrmw_register.write(5)
    
    def reader(thread_id):
        for _ in range(5):
            value = mrmw_register.read()
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
    assert len(shared_results) == 20, f"Expected 20 reads, got {len(shared_results)}"
    for thread_id, value in shared_results:
        assert value in [0, 5], f"Value {value} not expected from thread {thread_id}"


def test_not_implemented_error(mrmw_register):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        mrmw_register.read()
    
    with pytest.raises(NotImplementedError):
        mrmw_register.write(5)


def test_thread_id_generation(mrmw_register):
    """Testa geração de IDs únicos para threads"""
    thread_ids = set()
    
    def worker():
        thread_id = mrmw_register._get_thread_id()
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
        assert 0 <= thread_id < mrmw_register.num_threads, f"Thread ID {thread_id} out of range"


def test_thread_safety(mrmw_register, shared_results):
    """Testa thread safety básico"""
    def worker(thread_id):
        for i in range(10):
            mrmw_register.write(thread_id * 10 + i)
            value = mrmw_register.read()
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
    
    # Verifica que não houve crash
    assert len(shared_results) == 30, f"Expected 30 operations, got {len(shared_results)}"


def test_register_array_size(mrmw_register):
    """Testa que array de registradores tem tamanho correto"""
    assert len(mrmw_register.registers) == mrmw_register.num_threads, f"Expected {mrmw_register.num_threads} registers, got {len(mrmw_register.registers)}"


def test_different_num_threads():
    """Testa registrador com diferentes números de threads"""
    # Testa com 2 threads
    register_2 = MRMWRegister(0, 2)
    assert len(register_2.registers) == 2
    
    # Testa com 8 threads
    register_8 = MRMWRegister(0, 8)
    assert len(register_8.registers) == 8


def test_edge_cases(mrmw_register):
    """Testa casos extremos"""
    # Valor None
    register_none = MRMWRegister(None, 2)
    assert register_none.read() is None
    
    # String vazia
    register_empty = MRMWRegister("", 2)
    assert register_empty.read() == ""
    
    # Lista vazia
    register_list = MRMWRegister([], 2)
    assert register_list.read() == []


def test_sequential_writes(mrmw_register):
    """Testa escritas sequenciais"""
    # Escreve valores sequencialmente
    for i in range(10):
        mrmw_register.write(i)
    
    # Verifica valor final
    final_value = mrmw_register.read()
    assert final_value == 9, f"Expected final value 9, got {final_value}"


def test_rapid_writes_and_reads(mrmw_register, shared_results):
    """Testa escritas e leituras rápidas"""
    def writer(thread_id):
        for i in range(20):
            mrmw_register.write(thread_id * 10 + i)
            time.sleep(0.0001)  # Muito rápido
    
    def reader(thread_id):
        for _ in range(10):
            value = mrmw_register.read()
            shared_results.append((thread_id, value))
            time.sleep(0.0001)  # Muito rápido
    
    # Cria threads
    writers = []
    for i in range(2):
        writer_thread = threading.Thread(target=writer, args=(i,))
        writers.append(writer_thread)
    
    readers = []
    for i in range(2):
        reader_thread = threading.Thread(target=reader, args=(i,))
        readers.append(reader_thread)
    
    # Executa threads
    for writer_thread in writers:
        writer_thread.start()
    for reader_thread in readers:
        reader_thread.start()
    
    # Aguarda conclusão
    for writer_thread in writers:
        writer_thread.join()
    for reader_thread in readers:
        reader_thread.join()
    
    # Verifica que não houve crash
    assert len(shared_results) == 20, f"Expected 20 reads, got {len(shared_results)}"
    for thread_id, value in shared_results:
        assert 0 <= value <= 29, f"Value {value} out of range from thread {thread_id}"


def test_timestamp_ordering(mrmw_register, shared_results):
    """Testa ordenação por timestamps"""
    def writer(thread_id):
        # Escreve valores com delays diferentes
        mrmw_register.write(thread_id * 100)
        time.sleep(0.01 * (thread_id + 1))  # Delays diferentes
        mrmw_register.write(thread_id * 100 + 1)
    
    def reader():
        # Lê durante as escritas
        for _ in range(5):
            value = mrmw_register.read()
            shared_results.append(value)
            time.sleep(0.005)
    
    # Cria threads
    writers = []
    for i in range(3):
        writer_thread = threading.Thread(target=writer, args=(i,))
        writers.append(writer_thread)
    
    reader_thread = threading.Thread(target=reader)
    
    # Executa threads
    for writer_thread in writers:
        writer_thread.start()
    reader_thread.start()
    
    # Aguarda conclusão
    for writer_thread in writers:
        writer_thread.join()
    reader_thread.join()
    
    # Verifica que valores estão em ordem crescente (timestamps)
    for i in range(1, len(shared_results)):
        assert shared_results[i] >= shared_results[i-1], f"Timestamp ordering violated: {shared_results[i-1]} -> {shared_results[i]}"


def test_concurrent_writers_consistency(mrmw_register, shared_results):
    """Testa consistência com escritores concorrentes"""
    def writer(thread_id):
        # Escreve valores rapidamente
        for i in range(5):
            mrmw_register.write(thread_id * 1000 + i)
            time.sleep(0.001)
    
    def reader():
        # Lê durante as escritas
        for _ in range(10):
            value = mrmw_register.read()
            shared_results.append(value)
            time.sleep(0.001)
    
    # Cria threads
    writers = []
    for i in range(3):
        writer_thread = threading.Thread(target=writer, args=(i,))
        writers.append(writer_thread)
    
    reader_thread = threading.Thread(target=reader)
    
    # Executa threads
    for writer_thread in writers:
        writer_thread.start()
    reader_thread.start()
    
    # Aguarda conclusão
    for writer_thread in writers:
        writer_thread.join()
    reader_thread.join()
    
    # Verifica que valores estão em ordem crescente
    for i in range(1, len(shared_results)):
        assert shared_results[i] >= shared_results[i-1], f"Consistency violated: {shared_results[i-1]} -> {shared_results[i]}" 