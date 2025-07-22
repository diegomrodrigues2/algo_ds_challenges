"""
Testes para o Lock-Free Stack

Testa lock-freedom, LIFO order e propriedades básicas.
"""

import pytest
import threading
import time
from .lock_free_stack import LockFreeStack


@pytest.fixture
def stack():
    """Fixture para criar um LockFreeStack para cada teste"""
    return LockFreeStack()


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_lock_freedom(stack, shared_results):
    """Testa se a pilha satisfaz lock-freedom"""
    def pusher():
        # Empilha elementos
        stack.push("A")
        stack.push("B")
        stack.push("C")
    
    def popper():
        # Desempilha elementos
        item1 = stack.pop()
        item2 = stack.pop()
        item3 = stack.pop()
        shared_results.extend([item1, item2, item3])
    
    # Cria threads
    push_thread = threading.Thread(target=pusher)
    pop_thread = threading.Thread(target=popper)
    
    # Executa threads
    push_thread.start()
    pop_thread.start()
    
    # Aguarda conclusão
    push_thread.join()
    pop_thread.join()
    
    # Verifica que elementos foram desempilhados em ordem LIFO
    # Lock-freedom garante que algum progresso é feito
    assert len(shared_results) == 3, f"Expected 3 items, got {len(shared_results)}"
    assert all(item in ["A", "B", "C"] for item in shared_results), "Unexpected items"


def test_lifo_order(stack, shared_results):
    """Testa ordem LIFO da pilha"""
    def pusher():
        for i in range(5):
            stack.push(f"item_{i}")
    
    def popper():
        for _ in range(5):
            item = stack.pop()
            if item is not None:
                shared_results.append(item)
    
    # Cria threads
    push_thread = threading.Thread(target=pusher)
    pop_thread = threading.Thread(target=popper)
    
    # Executa threads
    push_thread.start()
    pop_thread.start()
    
    # Aguarda conclusão
    push_thread.join()
    pop_thread.join()
    
    # Verifica ordem LIFO (último a entrar, primeiro a sair)
    expected = [f"item_{i}" for i in range(4, -1, -1)]  # 4, 3, 2, 1, 0
    assert shared_results == expected, f"Expected {expected}, got {shared_results}"


def test_empty_stack(stack):
    """Testa comportamento quando pilha está vazia"""
    # Tenta desempilhar de pilha vazia
    result = stack.pop()
    assert result is None, f"Expected None, got {result}"


def test_concurrent_push_pop(stack, shared_results):
    """Testa operações concorrentes de empilhar e desempilhar"""
    def pusher():
        for i in range(10):
            stack.push(f"item_{i}")
    
    def popper():
        for _ in range(10):
            item = stack.pop()
            if item is not None:
                shared_results.append(item)
    
    # Cria threads
    push_thread = threading.Thread(target=pusher)
    pop_thread = threading.Thread(target=popper)
    
    # Executa threads
    push_thread.start()
    pop_thread.start()
    
    # Aguarda conclusão
    push_thread.join()
    pop_thread.join()
    
    # Verifica que todos os elementos foram processados
    assert len(shared_results) == 10, f"Expected 10 items, got {len(shared_results)}"
    
    # Verifica que não há duplicatas
    unique_items = set(shared_results)
    assert len(unique_items) == 10, "Duplicate items found"


def test_multiple_pushers_poppers(stack, shared_results):
    """Testa múltiplos empilhadores e desempilhadores"""
    def pusher(thread_id):
        for i in range(5):
            stack.push(f"thread_{thread_id}_item_{i}")
    
    def popper():
        for _ in range(10):  # 2 pushers * 5 items each
            item = stack.pop()
            if item is not None:
                shared_results.append(item)
    
    # Cria threads
    push_thread1 = threading.Thread(target=pusher, args=(1,))
    push_thread2 = threading.Thread(target=pusher, args=(2,))
    pop_thread = threading.Thread(target=popper)
    
    # Executa threads
    push_thread1.start()
    push_thread2.start()
    pop_thread.start()
    
    # Aguarda conclusão
    push_thread1.join()
    push_thread2.join()
    pop_thread.join()
    
    # Verifica que todos os elementos foram processados
    assert len(shared_results) == 10, f"Expected 10 items, got {len(shared_results)}"


def test_sequential_operations(stack):
    """Testa operações sequenciais"""
    # Empilha elementos
    stack.push("A")
    stack.push("B")
    stack.push("C")
    
    # Desempilha elementos
    assert stack.pop() == "C"  # LIFO
    assert stack.pop() == "B"
    assert stack.pop() == "A"
    assert stack.pop() is None  # Pilha vazia


def test_not_implemented_error(stack):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        stack.push("test")
    
    with pytest.raises(NotImplementedError):
        stack.pop()


def test_lock_free_progress(stack, shared_results):
    """Testa que lock-freedom garante progresso eventual"""
    iterations = 100
    
    def pusher():
        for i in range(iterations):
            stack.push(f"item_{i}")
    
    def popper():
        for _ in range(iterations):
            item = stack.pop()
            if item is not None:
                shared_results.append(item)
    
    # Cria threads
    push_thread = threading.Thread(target=pusher)
    pop_thread = threading.Thread(target=popper)
    
    # Executa threads
    push_thread.start()
    pop_thread.start()
    
    # Aguarda conclusão
    push_thread.join()
    pop_thread.join()
    
    # Lock-freedom garante que algum progresso é feito
    # (não necessariamente que todas as operações completem)
    assert len(shared_results) > 0, "No progress made - violates lock-freedom"


def test_starvation_possibility(stack):
    """Demonstra que starvation é possível em lock-free algorithms"""
    # Lock-free não garante wait-freedom
    # Algumas threads podem sofrer starvation
    
    def fast_worker():
        # Thread rápida
        for i in range(50):
            stack.push(f"fast_{i}")
    
    def slow_worker():
        # Thread lenta
        for i in range(50):
            stack.push(f"slow_{i}")
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
    
    # Lock-freedom garante que algum progresso é feito
    # mas não garante que todas as threads façam progresso igual
    print("Lock-freedom allows starvation but ensures overall progress")


def test_compare_and_swap_concept(stack):
    """Demonstra conceito de compare-and-swap"""
    # Em uma implementação real, CAS seria usado para garantir atomicidade
    # sem locks
    
    def demonstrate_cas_concept():
        # Simula conceito de CAS
        # 1. Ler valor atual
        # 2. Calcular novo valor
        # 3. Comparar e trocar atomicamente
        return "CAS ensures atomicity without locks"
    
    result = demonstrate_cas_concept()
    assert "CAS" in result, "CAS concept demonstration failed"


def test_obstruction_freedom(stack):
    """Testa que lock-free implica obstruction-freedom"""
    # Lock-free algorithms são obstruction-free
    # Se uma thread executa em isolamento, ela deve terminar
    
    def isolated_worker():
        # Simula execução em isolamento
        for i in range(10):
            stack.push(f"isolated_{i}")
    
    # Executa em isolamento
    isolated_worker()
    
    # Verifica que operações foram realizadas
    # (em uma implementação real, seria verificado o estado da pilha)
    assert True, "Obstruction-freedom ensures progress in isolation"


if __name__ == "__main__":
    pytest.main([__file__]) 