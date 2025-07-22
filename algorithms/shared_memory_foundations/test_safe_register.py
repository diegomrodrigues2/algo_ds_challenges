"""
Testes para o Safe Register

Testa propriedade safe, comportamento com sobreposição e casos extremos.
"""

import pytest
import threading
import time
from .safe_register import SafeRegister


@pytest.fixture
def safe_register():
    """Fixture para criar um SafeRegister para cada teste"""
    return SafeRegister(0, (0, 10))


@pytest.fixture
def boolean_register():
    """Fixture para registrador Boolean (0, 1)"""
    return SafeRegister(0, (0, 1))


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_safe_property_no_overlap(safe_register):
    """Testa que leitura sem sobreposição retorna último valor escrito"""
    # Escreve valores sequencialmente
    safe_register.write(5)
    safe_register.write(7)
    safe_register.write(3)
    
    # Lê após todas as escritas (sem sobreposição)
    value = safe_register.read()
    assert value == 3, f"Expected 3, got {value}"


def test_safe_property_with_overlap(safe_register, shared_results):
    """Testa que leitura com sobreposição pode retornar qualquer valor válido"""
    def writer_thread():
        # Escreve valores sequencialmente
        safe_register.write(1)
        time.sleep(0.01)  # Pequena pausa
        safe_register.write(2)
        time.sleep(0.01)
        safe_register.write(3)
    
    def reader_thread():
        # Lê durante as escritas (com sobreposição)
        for _ in range(5):
            value = safe_register.read()
            shared_results.append(value)
            time.sleep(0.005)  # Pausa menor que writer
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Verifica que todos os valores estão no range válido
    for value in shared_results:
        assert 0 <= value <= 10, f"Value {value} outside valid range"


def test_boolean_register_behavior(boolean_register, shared_results):
    """Testa registrador Boolean com valores 0 e 1"""
    def writer_thread():
        boolean_register.write(0)
        time.sleep(0.01)
        boolean_register.write(1)
        time.sleep(0.01)
        boolean_register.write(0)
    
    def reader_thread():
        for _ in range(3):
            value = boolean_register.read()
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
    
    # Verifica que todos os valores são 0 ou 1
    for value in shared_results:
        assert value in [0, 1], f"Boolean register returned {value}"


def test_initial_value(safe_register):
    """Testa valor inicial do registrador"""
    value = safe_register.read()
    assert value == 0, f"Expected initial value 0, got {value}"


def test_custom_initial_value():
    """Testa registrador com valor inicial customizado"""
    register = SafeRegister(42, (0, 100))
    value = register.read()
    assert value == 42, f"Expected initial value 42, got {value}"


def test_value_validation(safe_register):
    """Testa validação de valores no range permitido"""
    # Valores válidos
    assert safe_register._is_valid_value(0) == True
    assert safe_register._is_valid_value(5) == True
    assert safe_register._is_valid_value(10) == True
    
    # Valores inválidos
    assert safe_register._is_valid_value(-1) == False
    assert safe_register._is_valid_value(11) == False


def test_concurrent_writes(safe_register):
    """Testa escritas concorrentes"""
    def writer(value):
        for _ in range(10):
            safe_register.write(value)
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
    final_value = safe_register.read()
    assert final_value in [0, 1, 2], f"Final value {final_value} not expected"


def test_concurrent_reads(safe_register, shared_results):
    """Testa leituras concorrentes"""
    safe_register.write(5)
    
    def reader():
        for _ in range(5):
            value = safe_register.read()
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
        assert 0 <= value <= 10, f"Value {value} outside valid range"


def test_not_implemented_error(safe_register):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        safe_register.read()
    
    with pytest.raises(NotImplementedError):
        safe_register.write(5)


def test_edge_cases(safe_register):
    """Testa casos extremos"""
    # Range mínimo
    min_register = SafeRegister(0, (0, 0))
    assert min_register._is_valid_value(0) == True
    assert min_register._is_valid_value(1) == False
    
    # Range grande
    large_register = SafeRegister(100, (0, 1000))
    assert large_register._is_valid_value(500) == True
    assert large_register._is_valid_value(1000) == True
    assert large_register._is_valid_value(1001) == False


def test_thread_safety(safe_register, shared_results):
    """Testa thread safety básico"""
    def worker(thread_id):
        for i in range(10):
            safe_register.write(thread_id * 10 + i)
            value = safe_register.read()
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
    for thread_id, value in shared_results:
        assert 0 <= value <= 10, f"Invalid value {value} from thread {thread_id}" 