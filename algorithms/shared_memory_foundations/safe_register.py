"""
Safe Register

Registrador que satisfaz apenas a propriedade "safe".
Leitura sem sobreposição retorna último valor escrito.
Leitura com sobreposição pode retornar qualquer valor no intervalo permitido.

Propriedades:
- ✅ Safe: Leitura sem sobreposição retorna último valor
- ❌ Regular: Pode retornar valores não escritos
- ❌ Atomic: Não preserva ordem de leitura
- ✅ Wait-free: Cada operação termina em passos finitos

TAREFA: Implementar os métodos read() e write() para garantir propriedade safe.
"""

import threading
from typing import Any, Optional


class SafeRegister:
    """
    Safe Register
    
    Registrador que satisfaz apenas a propriedade "safe". 
    Leitura sem sobreposição retorna último valor escrito.
    Leitura com sobreposição pode retornar qualquer valor válido.
    
    TAREFA: Implementar a lógica para garantir propriedade safe.
    """
    
    def __init__(self, initial_value: Any = None, value_range: tuple = (0, 1)):
        """
        Inicializa o registrador safe
        
        Args:
            initial_value: Valor inicial do registrador
            value_range: Tupla (min, max) com valores permitidos
        """
        self.value = initial_value
        self.value_range = value_range
        self.lock = threading.Lock()
        
    def read(self) -> Any:
        """
        Lê o valor do registrador
        
        TAREFA: Implementar a lógica para:
        1. Se não há escrita concorrente: retornar último valor escrito
        2. Se há escrita concorrente: pode retornar qualquer valor no range
        
        DICA: Use self.lock para detectar sobreposição
        """
        raise NotImplementedError("Implementar método read()")
            
    def write(self, value: Any) -> None:
        """
        Escreve um valor no registrador
        
        TAREFA: Implementar a lógica para:
        1. Validar se valor está no range permitido
        2. Escrever valor de forma thread-safe
        
        DICA: Verificar se value está entre self.value_range[0] e self.value_range[1]
        """
        raise NotImplementedError("Implementar método write()")
    
    def _is_valid_value(self, value: Any) -> bool:
        """
        Verifica se valor está no range permitido
        
        Args:
            value: Valor a ser verificado
            
        Returns:
            True se valor é válido, False caso contrário
        """
        min_val, max_val = self.value_range
        return min_val <= value <= max_val


def test_safe_register():
    """Testa o registrador safe"""
    register = SafeRegister(0, (0, 10))
    results = []
    
    def writer_thread():
        # Escreve valores sequencialmente
        register.write(1)
        register.write(2)
        register.write(3)
    
    def reader_thread():
        # Lê valores (pode sobrepor com escrita)
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
    print(f"Safe Register Test:")
    print(f"  Results: {results}")
    print(f"  Final value: {register.read()}")
    
    return True


if __name__ == "__main__":
    test_safe_register() 