import pytest
from .priority_queue import PriorityQueue


class TestPriorityQueue:
    """Testes para a classe PriorityQueue."""
    
    def test_empty_queue(self):
        """Testa fila vazia."""
        pq = PriorityQueue[int]()
        assert pq.is_empty()
        assert pq.size() == 0
    
    def test_single_item(self):
        """Testa com um único item."""
        pq = PriorityQueue[int]()
        pq.push(5, 10)
        assert not pq.is_empty()
        assert pq.size() == 1
        assert pq.peek() == 10
        assert pq.peek_priority() == 5
    
    def test_multiple_items(self):
        """Testa com múltiplos itens."""
        pq = PriorityQueue[int]()
        pq.push(3, 30)
        pq.push(1, 10)
        pq.push(2, 20)
        
        assert pq.size() == 3
        assert pq.peek_priority() == 1  # Menor prioridade primeiro
        assert pq.pop() == 10
        assert pq.pop() == 20
        assert pq.pop() == 30
        assert pq.is_empty()
    
    def test_tie_breaking(self):
        """Testa o desempate com prioridades iguais."""
        pq = PriorityQueue[str]()
        pq.push(1, "primeiro")
        pq.push(1, "segundo")
        pq.push(1, "terceiro")
        
        # Deve retornar na ordem FIFO para prioridades iguais
        assert pq.pop() == "primeiro"
        assert pq.pop() == "segundo"
        assert pq.pop() == "terceiro"
    
    def test_negative_priorities(self):
        """Testa com prioridades negativas."""
        pq = PriorityQueue[int]()
        pq.push(-1, 10)
        pq.push(-5, 20)
        pq.push(-3, 30)
        
        assert pq.peek_priority() == -5
        assert pq.pop() == 20
        assert pq.pop() == 30
        assert pq.pop() == 10
    
    def test_large_priorities(self):
        """Testa com prioridades grandes."""
        pq = PriorityQueue[int]()
        pq.push(1000, 1)
        pq.push(500, 2)
        pq.push(2000, 3)
        
        assert pq.peek_priority() == 500
        assert pq.pop() == 2
        assert pq.pop() == 1
        assert pq.pop() == 3
    
    def test_pop_empty_queue(self):
        """Testa pop em fila vazia."""
        pq = PriorityQueue[int]()
        with pytest.raises(IndexError):
            pq.pop()
    
    def test_peek_empty_queue(self):
        """Testa peek em fila vazia."""
        pq = PriorityQueue[int]()
        with pytest.raises(IndexError):
            pq.peek()
    
    def test_peek_priority_empty_queue(self):
        """Testa peek_priority em fila vazia."""
        pq = PriorityQueue[int]()
        with pytest.raises(IndexError):
            pq.peek_priority()
    
    def test_clear_queue(self):
        """Testa limpar a fila."""
        pq = PriorityQueue[int]()
        pq.push(1, 10)
        pq.push(2, 20)
        pq.clear()
        
        assert pq.is_empty()
        assert pq.size() == 0
    
    def test_string_items(self):
        """Testa com itens do tipo string."""
        pq = PriorityQueue[str]()
        pq.push(3, "c")
        pq.push(1, "a")
        pq.push(2, "b")
        
        assert pq.pop() == "a"
        assert pq.pop() == "b"
        assert pq.pop() == "c"
    
    def test_mixed_operations(self):
        """Testa operações mistas."""
        pq = PriorityQueue[int]()
        
        # Adiciona alguns itens
        pq.push(5, 50)
        pq.push(1, 10)
        
        # Verifica peek sem remover
        assert pq.peek() == 10
        assert pq.peek_priority() == 1
        assert pq.size() == 2
        
        # Remove um item
        assert pq.pop() == 10
        assert pq.size() == 1
        
        # Adiciona mais itens
        pq.push(3, 30)
        pq.push(2, 20)
        
        # Remove todos
        assert pq.pop() == 20
        assert pq.pop() == 30
        assert pq.pop() == 50
        assert pq.is_empty() 