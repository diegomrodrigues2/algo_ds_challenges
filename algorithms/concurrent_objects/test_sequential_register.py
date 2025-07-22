"""
Testes para o Sequential Register

Testa sequential consistency, program order e propriedades básicas.
"""

import pytest
import threading
import time
from .sequential_register import SequentialRegister


@pytest.fixture
def register():
    """Fixture para criar um SequentialRegister para cada teste"""
    return SequentialRegister(0)


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_program_order_preservation(register, shared_results):
    """Testa que program order é preservado dentro de cada thread"""
    def writer_thread():
        # Program order: write(1), write(2), write(3)
        register.write(1)
        register.write(2)
        register.write(3)
    
    def reader_thread():
        # Program order: read(), read(), read()
        val1 = register.read()
        val2 = register.read()
        val3 = register.read()
        shared_results.extend([val1, val2, val3])
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Verifica que program order foi preservado
    # Os valores devem estar em ordem crescente (program order)
    assert shared_results == sorted(shared_results), "Program order not preserved"


def test_sequential_consistency(register):
    """Testa sequential consistency básica"""
    def worker1():
        register.write(10)
        register.write(20)
    
    def worker2():
        register.write(30)
        register.write(40)
    
    # Cria threads
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    
    # Executa threads
    thread1.start()
    thread2.start()
    
    # Aguarda conclusão
    thread1.join()
    thread2.join()
    
    # Verifica valor final
    final_value = register.read()
    assert final_value in [20, 40], f"Final value should be 20 or 40, got {final_value}"


def test_read_write_operations(register):
    """Testa operações básicas de read e write"""
    # Testa write
    register.write(42)
    assert register.read() == 42, "Write operation failed"
    
    # Testa múltiplos writes
    register.write(100)
    register.write(200)
    assert register.read() == 200, "Multiple writes failed"


def test_concurrent_reads(register, shared_results):
    """Testa múltiplas leituras concorrentes"""
    register.write(50)
    
    def reader():
        for _ in range(10):
            value = register.read()
            shared_results.append(value)
    
    # Cria múltiplas threads leitoras
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=reader)
        threads.append(thread)
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que todas as leituras retornaram o mesmo valor
    assert all(val == 50 for val in shared_results), "Concurrent reads should return same value"


def test_concurrent_writes(register):
    """Testa múltiplas escritas concorrentes"""
    def writer(value):
        register.write(value)
    
    # Cria múltiplas threads escritoras
    threads = []
    for i in range(10):
        thread = threading.Thread(target=writer, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que uma das escritas foi aplicada
    final_value = register.read()
    assert 0 <= final_value <= 9, f"Final value should be between 0 and 9, got {final_value}"


def test_initial_value(register):
    """Testa valor inicial do register"""
    initial_value = register.read()
    assert initial_value == 0, f"Expected 0, got {initial_value}"


def test_custom_initial_value():
    """Testa register com valor inicial customizado"""
    custom_register = SequentialRegister("initial")
    value = custom_register.read()
    assert value == "initial", f"Expected 'initial', got {value}"


def test_not_implemented_error(register):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        register.read()
    
    with pytest.raises(NotImplementedError):
        register.write(42)


def test_program_order_violation_demonstration(register, shared_results):
    """Demonstra que ordem temporal entre threads pode ser violada"""
    def writer_thread():
        # Program order: write(1), write(2)
        register.write(1)
        time.sleep(0.001)  # Pequena pausa
        register.write(2)
    
    def reader_thread():
        # Program order: read(), read()
        val1 = register.read()
        val2 = register.read()
        shared_results.extend([val1, val2])
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Em sequential consistency, program order é preservado
    # mas ordem temporal entre threads pode ser violada
    # Isso significa que o reader pode ver [2, 1] em vez de [1, 2]
    print(f"Reader results: {shared_results}")
    print("Note: Sequential consistency preserves program order within threads")


def test_composition_violation():
    """Demonstra que sequential consistency não é composicional"""
    # Cria dois registers
    reg1 = SequentialRegister(0)
    reg2 = SequentialRegister(0)
    
    def worker1():
        reg1.write(1)
        reg2.write(1)
    
    def worker2():
        reg2.write(2)
        reg1.write(2)
    
    # Cria threads
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    
    # Executa threads
    thread1.start()
    thread2.start()
    
    # Aguarda conclusão
    thread1.join()
    thread2.join()
    
    # Verifica valores finais
    val1 = reg1.read()
    val2 = reg2.read()
    
    print(f"Register 1 final value: {val1}")
    print(f"Register 2 final value: {val2}")
    print("Note: Sequential consistency is not compositional")


if __name__ == "__main__":
    pytest.main([__file__]) 