"""
Sequential Register

Register que satisfaz sequential consistency.
Preserva program order dentro de cada thread, mas não ordem temporal entre threads.

Propriedades:
- ✅ Sequential Consistency
- ❌ Linearizability
- ✅ Non-blocking
- ❌ Composicional

TAREFA: Implementar os métodos read() e write() para garantir sequential consistency.
"""

import threading
from typing import Any


class SequentialRegister:
    """
    Sequential Register
    
    Register que satisfaz sequential consistency. Preserva program order
    dentro de cada thread, mas pode reordenar operações entre threads.
    
    TAREFA: Implementar a lógica para preservar program order.
    """
    
    def __init__(self, initial_value: Any = None):
        # Valor do register
        self.value = initial_value
        # Lock para sincronização
        self.lock = threading.Lock()
        
    def read(self):
        """
        Lê o valor do register
        
        TAREFA: Implementar a lógica para:
        1. Adquirir lock
        2. Ler valor atual
        3. Liberar lock
        4. Retornar valor
        
        DICA: Use self.lock.acquire() e self.lock.release()
        """
        raise NotImplementedError("Implementar método read()")
            
    def write(self, value: Any):
        """
        Escreve um valor no register
        
        TAREFA: Implementar a lógica para:
        1. Adquirir lock
        2. Escrever novo valor
        3. Liberar lock
        """
        raise NotImplementedError("Implementar método write()")


def test_sequential_register():
    """Testa o register sequencialmente consistente"""
    register = SequentialRegister(0)
    results = []
    
    def writer_thread():
        # Program order: write(1), write(2)
        register.write(1)
        register.write(2)
    
    def reader_thread():
        # Program order: read(), read()
        val1 = register.read()
        val2 = register.read()
        results.extend([val1, val2])
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer.start()
    reader.start()
    
    # Aguarda conclusão
    writer.join()
    reader.join()
    
    # Verifica resultado
    # Sequential consistency: program order preservado
    # Mas ordem temporal entre threads pode ser violada
    print(f"Sequential Register Test:")
    print(f"  Results: {results}")
    print(f"  Final value: {register.read()}")
    
    return True


if __name__ == "__main__":
    test_sequential_register() 