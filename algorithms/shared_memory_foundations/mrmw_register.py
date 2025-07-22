"""
MRMW Register (Multi-Reader, Multi-Writer)

Registrador que suporta múltiplos leitores e múltiplos escritores.
Implementado usando array de registradores MRSW atômicos e algoritmo de timestamps.

Propriedades:
- ✅ Multi-Reader: Múltiplos threads podem ler
- ✅ Multi-Writer: Múltiplos threads podem escrever
- ✅ Atomic: Linearizável
- ✅ Wait-free: Cada operação termina em passos finitos

TAREFA: Implementar os métodos read() e write() usando algoritmo de timestamps.
"""

import threading
from typing import Any, List
from .atomic_register import AtomicRegister, StampedValue


class MRMWRegister:
    """
    MRMW Register (Multi-Reader, Multi-Writer)
    
    Registrador que suporta múltiplos leitores e múltiplos escritores.
    Usa array de registradores MRSW atômicos e algoritmo de timestamps.
    
    TAREFA: Implementar a lógica para garantir atomicidade com múltiplos escritores.
    """
    
    def __init__(self, initial_value: Any = None, num_threads: int = 4):
        """
        Inicializa o registrador MRMW
        
        Args:
            initial_value: Valor inicial do registrador
            num_threads: Número máximo de threads
        """
        self.num_threads = num_threads
        # Array de registradores MRSW atômicos
        self.registers = [AtomicRegister(StampedValue(0, initial_value)) for _ in range(num_threads)]
        
    def read(self) -> Any:
        """
        Lê o valor do registrador
        
        TAREFA: Implementar a lógica para:
        1. Ler todos os registradores
        2. Encontrar valor com maior timestamp
        3. Retornar valor (não o timestamp)
        
        DICA: Use max() com key=lambda para encontrar StampedValue com maior timestamp
        """
        raise NotImplementedError("Implementar método read()")
            
    def write(self, value: Any) -> None:
        """
        Escreve um valor no registrador
        
        TAREFA: Implementar a lógica para:
        1. Obter ID do thread atual
        2. Ler todos os registradores para encontrar maior timestamp
        3. Criar novo StampedValue com timestamp + 1
        4. Escrever no registrador do thread
        
        DICA: Use self._get_thread_id() para obter ID do thread
        """
        raise NotImplementedError("Implementar método write()")
    
    def _get_thread_id(self) -> int:
        """
        Obtém ID único para o thread atual
        
        Returns:
            ID único do thread (0 a num_threads-1)
        """
        thread = threading.current_thread()
        return hash(thread) % self.num_threads


def test_mrmw_register():
    """Testa o registrador MRMW"""
    register = MRMWRegister(0, 3)
    results = []
    
    def writer_thread(thread_id):
        # Escreve valores sequencialmente
        register.write(thread_id * 10 + 1)
        register.write(thread_id * 10 + 2)
        register.write(thread_id * 10 + 3)
    
    def reader_thread():
        # Lê valores
        for _ in range(3):
            value = register.read()
            results.append(value)
    
    # Cria threads
    writer1 = threading.Thread(target=writer_thread, args=(0,))
    writer2 = threading.Thread(target=writer_thread, args=(1,))
    reader = threading.Thread(target=reader_thread)
    
    # Executa threads
    writer1.start()
    writer2.start()
    reader.start()
    
    # Aguarda conclusão
    writer1.join()
    writer2.join()
    reader.join()
    
    # Verifica resultado
    print(f"MRMW Register Test:")
    print(f"  Results: {results}")
    print(f"  Final value: {register.read()}")
    
    return True


if __name__ == "__main__":
    test_mrmw_register() 