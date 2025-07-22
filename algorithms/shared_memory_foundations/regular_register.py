"""
Regular Register

Registrador que satisfaz propriedade "regular".
Leitura sem sobreposição retorna último valor escrito.
Leitura com sobreposição pode retornar qualquer valor escrito (não valores arbitrários).

Propriedades:
- ✅ Safe: Leitura sem sobreposição retorna último valor
- ✅ Regular: Só retorna valores escritos por alguma operação
- ❌ Atomic: Não preserva ordem de leitura
- ✅ Wait-free: Cada operação termina em passos finitos

TAREFA: Implementar os métodos read() e write() para garantir propriedade regular.
"""

import threading
from typing import Any, Optional


class RegularRegister:
    """
    Regular Register
    
    Registrador que satisfaz propriedade "regular".
    Leitura sem sobreposição retorna último valor escrito.
    Leitura com sobreposição pode "piscar" entre valores antigo e novo.
    
    TAREFA: Implementar a lógica para garantir propriedade regular.
    """
    
    def __init__(self, initial_value: Any = None):
        """
        Inicializa o registrador regular
        
        Args:
            initial_value: Valor inicial do registrador
        """
        self.value = initial_value
        self.lock = threading.Lock()
        self.last_written = initial_value
        
    def read(self) -> Any:
        """
        Lê o valor do registrador
        
        TAREFA: Implementar a lógica para:
        1. Se não há escrita concorrente: retornar último valor escrito
        2. Se há escrita concorrente: pode retornar valor antigo ou novo
        
        DICA: Use self.lock para detectar sobreposição
        """
        raise NotImplementedError("Implementar método read()")
            
    def write(self, value: Any) -> None:
        """
        Escreve um valor no registrador
        
        TAREFA: Implementar a lógica para:
        1. Escrever valor de forma thread-safe
        2. Atualizar last_written apenas se valor for diferente
        
        DICA: Evitar escrita desnecessária quando valor é igual ao anterior
        """
        raise NotImplementedError("Implementar método write()")


def test_regular_register():
    """Testa o registrador regular"""
    register = RegularRegister(0)
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
    print(f"Regular Register Test:")
    print(f"  Results: {results}")
    print(f"  Final value: {register.read()}")
    
    return True


if __name__ == "__main__":
    test_regular_register() 