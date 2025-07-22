"""
Linearizable Queue

Fila FIFO que satisfaz linearizability.
Cada operação parece tomar efeito instantaneamente em algum momento entre invocação e resposta.

Propriedades:
- ✅ Linearizability
- ✅ Sequential Consistency
- ✅ Quiescent Consistency
- ✅ Composicional
- ✅ Non-blocking

TAREFA: Implementar os métodos enq() e deq() para garantir linearizability.
"""

import threading
from typing import Any, Optional


class LinearizableQueue:
    """
    Linearizable Queue
    
    Fila FIFO que satisfaz linearizability. Cada operação tem um
    linearization point onde ela toma efeito instantaneamente.
    
    TAREFA: Implementar a lógica para garantir linearizability.
    """
    
    def __init__(self, capacity: int = 1000):
        # Array para armazenar elementos
        self.items = [None] * capacity
        # Índices de cabeça e cauda
        self.head = 0
        self.tail = 0
        # Lock para sincronização
        self.lock = threading.Lock()
        
    def enq(self, item: Any):
        """
        Enfileira um item
        
        TAREFA: Implementar a lógica para:
        1. Adquirir lock
        2. Verificar se fila está cheia
        3. Inserir item na posição tail
        4. Incrementar tail
        5. Liberar lock
        
        DICA: Linearization point é o início da critical section
        """
        raise NotImplementedError("Implementar método enq()")
            
    def deq(self) -> Optional[Any]:
        """
        Desenfileira um item
        
        TAREFA: Implementar a lógica para:
        1. Adquirir lock
        2. Verificar se fila está vazia
        3. Remover item da posição head
        4. Incrementar head
        5. Liberar lock
        6. Retornar item removido
        
        DICA: Linearization point é o início da critical section
        """
        raise NotImplementedError("Implementar método deq()")


def test_linearizable_queue():
    """Testa a fila linearizável"""
    queue = LinearizableQueue()
    results = []
    
    def enqueuer():
        # Enfileira elementos
        queue.enq("A")
        queue.enq("B")
    
    def dequeuer():
        # Desenfileira elementos
        item1 = queue.deq()
        item2 = queue.deq()
        results.extend([item1, item2])
    
    # Cria threads
    enq_thread = threading.Thread(target=enqueuer)
    deq_thread = threading.Thread(target=dequeuer)
    
    # Executa threads
    enq_thread.start()
    deq_thread.start()
    
    # Aguarda conclusão
    enq_thread.join()
    deq_thread.join()
    
    # Verifica resultado
    print(f"Linearizable Queue Test:")
    print(f"  Results: {results}")
    print(f"  Queue empty: {queue.deq() is None}")
    
    return True


if __name__ == "__main__":
    test_linearizable_queue() 