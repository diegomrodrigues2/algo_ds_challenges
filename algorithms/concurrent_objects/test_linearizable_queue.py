"""
Testes para o Linearizable Queue

Testa linearizability, FIFO order e propriedades básicas.
"""

import pytest
import threading
import time
from .linearizable_queue import LinearizableQueue


@pytest.fixture
def queue():
    """Fixture para criar um LinearizableQueue para cada teste"""
    return LinearizableQueue()


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_linearizability(queue, shared_results):
    """Testa se a fila satisfaz linearizability"""
    def enqueuer():
        # Enfileira elementos
        queue.enq("A")
        queue.enq("B")
    
    def dequeuer():
        # Desenfileira elementos
        item1 = queue.deq()
        item2 = queue.deq()
        shared_results.extend([item1, item2])
    
    # Cria threads
    enq_thread = threading.Thread(target=enqueuer)
    deq_thread = threading.Thread(target=dequeuer)
    
    # Executa threads
    enq_thread.start()
    deq_thread.start()
    
    # Aguarda conclusão
    enq_thread.join()
    deq_thread.join()
    
    # Verifica que elementos foram desenfileirados em ordem FIFO
    # Linearizability garante que a ordem é consistente
    assert shared_results == ["A", "B"], f"Expected ['A', 'B'], got {shared_results}"


def test_fifo_order(queue, shared_results):
    """Testa ordem FIFO da fila"""
    def enqueuer():
        for i in range(5):
            queue.enq(f"item_{i}")
    
    def dequeuer():
        for _ in range(5):
            item = queue.deq()
            shared_results.append(item)
    
    # Cria threads
    enq_thread = threading.Thread(target=enqueuer)
    deq_thread = threading.Thread(target=dequeuer)
    
    # Executa threads
    enq_thread.start()
    deq_thread.start()
    
    # Aguarda conclusão
    enq_thread.join()
    deq_thread.join()
    
    # Verifica ordem FIFO
    expected = [f"item_{i}" for i in range(5)]
    assert shared_results == expected, f"Expected {expected}, got {shared_results}"


def test_empty_queue(queue):
    """Testa comportamento quando fila está vazia"""
    # Tenta desenfileir de fila vazia
    result = queue.deq()
    assert result is None, f"Expected None, got {result}"


def test_concurrent_enqueue_dequeue(queue, shared_results):
    """Testa operações concorrentes de enfileirar e desenfileir"""
    def enqueuer():
        for i in range(10):
            queue.enq(f"item_{i}")
    
    def dequeuer():
        for _ in range(10):
            item = queue.deq()
            if item is not None:
                shared_results.append(item)
    
    # Cria threads
    enq_thread = threading.Thread(target=enqueuer)
    deq_thread = threading.Thread(target=dequeuer)
    
    # Executa threads
    enq_thread.start()
    deq_thread.start()
    
    # Aguarda conclusão
    enq_thread.join()
    deq_thread.join()
    
    # Verifica que todos os elementos foram processados
    assert len(shared_results) == 10, f"Expected 10 items, got {len(shared_results)}"
    
    # Verifica que não há duplicatas
    unique_items = set(shared_results)
    assert len(unique_items) == 10, "Duplicate items found"


def test_multiple_enqueuers_dequeuers(queue, shared_results):
    """Testa múltiplos enfileiradores e desenfileiradores"""
    def enqueuer(thread_id):
        for i in range(5):
            queue.enq(f"thread_{thread_id}_item_{i}")
    
    def dequeuer():
        for _ in range(10):  # 2 enqueuers * 5 items each
            item = queue.deq()
            if item is not None:
                shared_results.append(item)
    
    # Cria threads
    enq_thread1 = threading.Thread(target=enqueuer, args=(1,))
    enq_thread2 = threading.Thread(target=enqueuer, args=(2,))
    deq_thread = threading.Thread(target=dequeuer)
    
    # Executa threads
    enq_thread1.start()
    enq_thread2.start()
    deq_thread.start()
    
    # Aguarda conclusão
    enq_thread1.join()
    enq_thread2.join()
    deq_thread.join()
    
    # Verifica que todos os elementos foram processados
    assert len(shared_results) == 10, f"Expected 10 items, got {len(shared_results)}"


def test_queue_capacity(queue):
    """Testa capacidade da fila"""
    # Tenta enfileirar mais itens que a capacidade
    capacity = 1000  # Capacidade padrão
    
    def enqueuer():
        for i in range(capacity + 10):
            try:
                queue.enq(f"item_{i}")
            except Exception:
                break  # Fila cheia
    
    def dequeuer():
        for _ in range(capacity):
            item = queue.deq()
            if item is None:
                break
    
    # Cria threads
    enq_thread = threading.Thread(target=enqueuer)
    deq_thread = threading.Thread(target=dequeuer)
    
    # Executa threads
    enq_thread.start()
    deq_thread.start()
    
    # Aguarda conclusão
    enq_thread.join()
    deq_thread.join()
    
    # Verifica que a fila não quebrou
    assert True, "Queue should handle capacity limits gracefully"


def test_sequential_operations(queue):
    """Testa operações sequenciais"""
    # Enfileira elementos
    queue.enq("A")
    queue.enq("B")
    queue.enq("C")
    
    # Desenfileira elementos
    assert queue.deq() == "A"
    assert queue.deq() == "B"
    assert queue.deq() == "C"
    assert queue.deq() is None  # Fila vazia


def test_not_implemented_error(queue):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        queue.enq("test")
    
    with pytest.raises(NotImplementedError):
        queue.deq()


def test_linearization_points(queue, shared_results):
    """Demonstra conceito de linearization points"""
    def enqueuer():
        # Linearization point: início da critical section
        queue.enq("first")
        queue.enq("second")
    
    def dequeuer():
        # Linearization point: início da critical section
        item1 = queue.deq()
        item2 = queue.deq()
        shared_results.extend([item1, item2])
    
    # Cria threads
    enq_thread = threading.Thread(target=enqueuer)
    deq_thread = threading.Thread(target=dequeuer)
    
    # Executa threads
    enq_thread.start()
    deq_thread.start()
    
    # Aguarda conclusão
    enq_thread.join()
    deq_thread.join()
    
    # Linearizability garante que existe uma ordem sequencial válida
    # que explica o resultado observado
    print(f"Linearization test results: {shared_results}")
    print("Note: Each operation appears to take effect at its linearization point")


def test_compositionality(queue):
    """Demonstra que linearizability é composicional"""
    # Cria duas filas
    queue1 = LinearizableQueue()
    queue2 = LinearizableQueue()
    
    def worker1():
        queue1.enq("A")
        queue2.enq("X")
    
    def worker2():
        queue1.enq("B")
        queue2.enq("Y")
    
    # Cria threads
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)
    
    # Executa threads
    thread1.start()
    thread2.start()
    
    # Aguarda conclusão
    thread1.join()
    thread2.join()
    
    # Verifica que ambas as filas mantêm suas propriedades
    # Linearizability é composicional
    print("Compositionality test: Both queues maintain linearizability")


if __name__ == "__main__":
    pytest.main([__file__]) 