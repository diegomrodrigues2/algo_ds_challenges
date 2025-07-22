"""
Atomic Register

Registrador que satisfaz propriedade "atomic" (linearizável).
Cada read() retorna o "último" valor escrito, preservando ordem de leitura.

Propriedades:
- ✅ Safe: Leitura sem sobreposição retorna último valor
- ✅ Regular: Só retorna valores escritos por alguma operação
- ✅ Atomic: Preserva ordem de leitura (linearizável)
- ✅ Wait-free: Cada operação termina em passos finitos

TAREFA: Implementar os métodos read() e write() usando timestamps para garantir atomicidade.
"""

import threading
from typing import Any, Optional


class StampedValue:
    """
    Valor com timestamp para ordenação atômica
    
    TAREFA: Implementar métodos para comparação de timestamps.
    """
    
    def __init__(self, stamp: int, value: Any):
        """
        Inicializa valor com timestamp
        
        Args:
            stamp: Timestamp único para ordenação
            value: Valor a ser armazenado
        """
        self.stamp = stamp
        self.value = value
    
    def __lt__(self, other):
        """
        Compara timestamps para ordenação
        
        TAREFA: Implementar comparação baseada em timestamp
        """
        raise NotImplementedError("Implementar comparação de timestamps")
    
    def __eq__(self, other):
        """Compara igualdade de timestamps"""
        if not isinstance(other, StampedValue):
            return False
        return self.stamp == other.stamp
    
    def __repr__(self):
        return f"StampedValue(stamp={self.stamp}, value={self.value})"


class AtomicRegister:
    """
    Atomic Register
    
    Registrador que satisfaz propriedade "atomic" (linearizável).
    Usa timestamps para garantir ordem total de operações.
    
    TAREFA: Implementar a lógica para garantir atomicidade usando timestamps.
    """
    
    def __init__(self, initial_value: Any = None):
        """
        Inicializa o registrador atômico
        
        Args:
            initial_value: Valor inicial do registrador
        """
        self.stamped_value = StampedValue(0, initial_value)
        self.lock = threading.Lock()
        self.timestamp_counter = 0
        
    def read(self) -> Any:
        """
        Lê o valor do registrador
        
        TAREFA: Implementar a lógica para:
        1. Ler valor atual com timestamp
        2. Retornar valor (timestamp é usado internamente)
        
        DICA: Use self.stamped_value para acessar valor atual
        """
        raise NotImplementedError("Implementar método read()")
            
    def write(self, value: Any) -> None:
        """
        Escreve um valor no registrador
        
        TAREFA: Implementar a lógica para:
        1. Incrementar timestamp
        2. Criar novo StampedValue
        3. Atualizar registrador de forma thread-safe
        
        DICA: Use self.timestamp_counter para gerar timestamps únicos
        """
        raise NotImplementedError("Implementar método write()")


def test_atomic_register():
    """Testa o registrador atômico"""
    register = AtomicRegister(0)
    results = []
    
    def writer_thread():
        # Escreve valores sequencialmente
        register.write(1)
        register.write(2)
        register.write(3)
    
    def reader_thread():
        # Lê valores (deve preservar ordem)
        val1 = register.read()
        val2 = register.read()
        val3 = register.read()
        results.extend([val1, val2, val3])
    
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
    print(f"Atomic Register Test:")
    print(f"  Results: {results}")
    print(f"  Final value: {register.read()}")
    
    return True


if __name__ == "__main__":
    test_atomic_register() 