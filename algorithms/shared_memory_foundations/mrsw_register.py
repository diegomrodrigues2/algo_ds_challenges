"""
MRSW Register (Multi-Reader, Single-Writer)

Registrador que suporta múltiplos leitores e um único escritor.
Implementado usando array de registradores SRSW atômicos.

Propriedades:
- ✅ Multi-Reader: Múltiplos threads podem ler
- ✅ Single-Writer: Apenas um thread pode escrever
- ✅ Atomic: Linearizável
- ✅ Wait-free: Cada operação termina em passos finitos

TAREFA: Implementar os métodos read() e write() usando array de registradores SRSW.
"""

import threading
from typing import Any, List
from .atomic_register import AtomicRegister


class MRSWRegister:
    """
    MRSW Register (Multi-Reader, Single-Writer)
    
    Registrador que suporta múltiplos leitores e um único escritor.
    Usa array de registradores SRSW atômicos para comunicação.
    
    TAREFA: Implementar a lógica para garantir atomicidade com múltiplos leitores.
    """
    
    def __init__(self, initial_value: Any = None, num_threads: int = 4):
        """
        Inicializa o registrador MRSW
        
        Args:
            initial_value: Valor inicial do registrador
            num_threads: Número máximo de threads (leitores)
        """
        self.num_threads = num_threads
        # Array de registradores SRSW atômicos
        self.registers = [AtomicRegister(initial_value) for _ in range(num_threads)]
        self.thread_id = 0  # ID do thread atual
        
    def read(self) -> Any:
        """
        Lê o valor do registrador
        
        TAREFA: Implementar a lógica para:
        1. Obter ID do thread atual
        2. Ler do registrador correspondente ao ID
        3. Retornar valor lido
        
        DICA: Use threading.current_thread() para obter thread ID
        """
        raise NotImplementedError("Implementar método read()")
            
    def write(self, value: Any) -> None:
        """
        Escreve um valor no registrador
        
        TAREFA: Implementar a lógica para:
        1. Escrever valor em todos os registradores
        2. Garantir que todos os leitores vejam o mesmo valor
        
        DICA: Escreva em todos os registradores do array
        """
        raise NotImplementedError("Implementar método write()")
    
    def _get_thread_id(self) -> int:
        """
        Obtém ID único para o thread atual
        
        Returns:
            ID único do thread (0 a num_threads-1)
        """
        thread = threading.current_thread()
        # Usa hash do thread para gerar ID único
        return hash(thread) % self.num_threads


def test_mrsw_register():
    """Testa o registrador MRSW"""
    register = MRSWRegister(0, 3)
    results = []
    
    def writer_thread():
        # Escreve valores sequencialmente
        register.write(1)
        register.write(2)
        register.write(3)
    
    def reader_thread(thread_id):
        # Lê valores (cada thread lê do seu registrador)
        val1 = register.read()
        val2 = register.read()
        val3 = register.read()
        results.append((thread_id, [val1, val2, val3]))
    
    # Cria threads
    writer = threading.Thread(target=writer_thread)
    reader1 = threading.Thread(target=reader_thread, args=(1,))
    reader2 = threading.Thread(target=reader_thread, args=(2,))
    
    # Executa threads
    writer.start()
    reader1.start()
    reader2.start()
    
    # Aguarda conclusão
    writer.join()
    reader1.join()
    reader2.join()
    
    # Verifica resultado
    print(f"MRSW Register Test:")
    print(f"  Results: {results}")
    print(f"  Final value: {register.read()}")
    
    return True


if __name__ == "__main__":
    test_mrsw_register() 