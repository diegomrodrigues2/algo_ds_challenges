"""
Testes para o Regular Register

Testa propriedade regular, comportamento com sobreposição e casos extremos.
"""

import pytest
import threading
import time
from .regular_register import RegularRegister


@pytest.fixture
def regular_register():
    """Fixture para criar um RegularRegister para cada teste"""
    return RegularRegister(0)


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_regular_property_no_overlap(regular_register):
    """Testa que leitura sem sobreposição retorna último valor escrito"""
    # Escreve valores sequencialmente
    regular_register.write(5)
    regular_register.write(7)
    regular_register.write(3)
    
    # Lê após todas as escritas (sem sobreposição)
    value = regular_register.read()
    assert value == 3, f"Expected 3, got {value}"


def test_regular_property_with_overlap(regular_register, shared_results):
    """Testa que leitura com sobreposição só retorna valores escritos"""
    def writer_thread():
        # Escreve valores sequencialmente
        regular_register.write(1)
        time.sleep(0.01)
        regular_register.write(2)
        time.sleep(0.01)
        regular_register.write(3)
    
    def reader_thread():
        # Lê durante as escritas (com sobreposição)
        for _ in range(5):
            value = regular_register.read()
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
    
    # Verifica que todos os valores foram escritos por alguma operação
    written_values = {0, 1, 2, 3}  # Inclui valor inicial
    for value in shared_results:
        assert value in written_values, f"Value {value} was never written"


def test_boolean_regular_behavior(shared_results):
    """Testa registrador Boolean regular com valores 0 e 1"""
    register = RegularRegister(0)
    
    def writer_thread():
        register.write(0)
        time.sleep(0.01)
        register.write(1)
        time.sleep(0.01)
        register.write(0)
    
    def reader_thread():
        for _ in range(3):
            value = register.read()
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
    
    # Verifica que todos os valores são 0 ou 1 (valores escritos)
    for value in shared_results:
        assert value in [0, 1], f"Regular register returned {value}"


def test_initial_value(regular_register):
    """Testa valor inicial do registrador"""
    value = regular_register.read()
    assert value == 0, f"Expected initial value 0, got {value}"


def test_custom_initial_value():
    """Testa registrador com valor inicial customizado"""
    register = RegularRegister(42)
    value = register.read()
    assert value == 42, f"Expected initial value 42, got {value}"


def test_concurrent_writes(regular_register):
    """Testa escritas concorrentes"""
    def writer(value):
        for _ in range(10):
            regular_register.write(value)
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
    final_value = regular_register.read()
    assert final_value in [0, 1, 2], f"Final value {final_value} not expected"


def test_concurrent_reads(regular_register, shared_results):
    """Testa leituras concorrentes"""
    regular_register.write(5)
    
    def reader():
        for _ in range(5):
            value = regular_register.read()
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
    
    # Verifica que todas as leituras retornaram valores escritos
    assert len(shared_results) == 15, f"Expected 15 reads, got {len(shared_results)}"
    written_values = {0, 5}  # Inclui valor inicial e valor escrito
    for value in shared_results:
        assert value in written_values, f"Value {value} was never written"


def test_not_implemented_error(regular_register):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        regular_register.read()
    
    with pytest.raises(NotImplementedError):
        regular_register.write(5)


def test_thread_safety(regular_register, shared_results):
    """Testa thread safety básico"""
    def worker(thread_id):
        for i in range(10):
            regular_register.write(thread_id * 10 + i)
            value = regular_register.read()
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
    
    # Verifica que não houve crash e todos os valores foram escritos
    assert len(shared_results) == 30, f"Expected 30 operations, got {len(shared_results)}"
    written_values = {0}  # Valor inicial
    for i in range(3):
        for j in range(10):
            written_values.add(i * 10 + j)
    
    for thread_id, value in shared_results:
        assert value in written_values, f"Value {value} from thread {thread_id} was never written"


def test_regular_vs_safe_property(regular_register, shared_results):
    """Testa que regular é mais forte que safe"""
    def writer_thread():
        regular_register.write(1)
        time.sleep(0.01)
        regular_register.write(2)
    
    def reader_thread():
        # Lê durante a escrita (com sobreposição)
        for _ in range(3):
            value = regular_register.read()
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
    
    # Verifica propriedade regular: só valores escritos
    written_values = {0, 1, 2}  # Inclui valor inicial
    for value in shared_results:
        assert value in written_values, f"Regular property violated: {value}"


def test_flickering_behavior(regular_register, shared_results):
    """Testa comportamento de 'piscar' entre valores antigo e novo"""
    def writer_thread():
        regular_register.write(10)
        time.sleep(0.01)
        regular_register.write(20)
        time.sleep(0.01)
        regular_register.write(30)
    
    def reader_thread():
        # Lê rapidamente durante as escritas
        for _ in range(10):
            value = regular_register.read()
            shared_results.append(value)
            time.sleep(0.002)  # Muito rápido
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Verifica que valores mudam gradualmente (flickering)
    written_values = {0, 10, 20, 30}  # Inclui valor inicial
    for value in shared_results:
        assert value in written_values, f"Value {value} not in written values"
    
    # Verifica que há transições entre valores
    transitions = 0
    for i in range(1, len(shared_results)):
        if shared_results[i] != shared_results[i-1]:
            transitions += 1
    
    assert transitions > 0, "No transitions detected (no flickering)"


def test_edge_cases(regular_register):
    """Testa casos extremos"""
    # Valor None
    register_none = RegularRegister(None)
    assert register_none.read() is None
    
    # String vazia
    register_empty = RegularRegister("")
    assert register_empty.read() == ""
    
    # Lista vazia
    register_list = RegularRegister([])
    assert register_list.read() == [] 