"""
Atomic Snapshot

Snapshot atômico que permite ler múltiplos registradores atomicamente.
Implementação wait-free usando double collect e mecanismo de ajuda.

Propriedades:
- ✅ Atomic: Linearizável
- ✅ Wait-free: Cada operação termina em passos finitos
- ✅ Multi-thread: Suporta múltiplos threads
- ✅ Snapshot: Visão instantânea de array de registradores

TAREFA: Implementar os métodos update() e scan() para garantir atomicidade wait-free.
"""

import threading
import time
from typing import Any, List, Optional
from .atomic_register import AtomicRegister, StampedValue


class StampedSnapshot:
    """
    Valor com timestamp e snapshot para ordenação atômica
    
    TAREFA: Implementar estrutura para armazenar timestamp, valor e snapshot.
    """
    
    def __init__(self, stamp: int, value: Any, snap: Optional[List[Any]] = None):
        """
        Inicializa snapshot com timestamp
        
        Args:
            stamp: Timestamp único para ordenação
            value: Valor do registrador
            snap: Snapshot opcional
        """
        self.stamp = stamp
        self.value = value
        self.snap = snap or []
    
    def __repr__(self):
        return f"StampedSnapshot(stamp={self.stamp}, value={self.value}, snap={self.snap})"


class AtomicSnapshot:
    """
    Atomic Snapshot
    
    Snapshot atômico wait-free que permite ler múltiplos registradores atomicamente.
    Usa double collect e mecanismo de ajuda para garantir wait-freedom.
    
    TAREFA: Implementar a lógica para garantir atomicidade wait-free.
    """
    
    def __init__(self, num_threads: int, initial_value: Any = None):
        """
        Inicializa o snapshot atômico
        
        Args:
            num_threads: Número de threads (registradores)
            initial_value: Valor inicial para cada registrador
        """
        self.num_threads = num_threads
        # Array de registradores atômicos
        self.registers = [AtomicRegister(StampedSnapshot(0, initial_value)) for _ in range(num_threads)]
        self.timestamp_counter = 0
        
    def update(self, value: Any) -> None:
        """
        Atualiza valor do thread atual
        
        TAREFA: Implementar a lógica para:
        1. Obter ID do thread atual
        2. Incrementar timestamp
        3. Fazer scan() para obter snapshot atual
        4. Criar novo StampedSnapshot
        5. Escrever no registrador do thread
        
        DICA: Use self._get_thread_id() para obter ID do thread
        """
        raise NotImplementedError("Implementar método update()")
    
    def scan(self) -> List[Any]:
        """
        Retorna snapshot atômico de todos os registradores
        
        TAREFA: Implementar algoritmo wait-free usando:
        1. Double collect para detectar estabilidade
        2. Mecanismo de ajuda quando double collect falha
        3. Detecção de movimento duplo para usar snapshot de helper
        
        DICA: Use self._collect() para coletar valores dos registradores
        """
        raise NotImplementedError("Implementar método scan()")
    
    def _get_thread_id(self) -> int:
        """
        Obtém ID único para o thread atual
        
        Returns:
            ID único do thread (0 a num_threads-1)
        """
        thread = threading.current_thread()
        return hash(thread) % self.num_threads
    
    def _collect(self) -> List[StampedSnapshot]:
        """
        Coleta valores de todos os registradores
        
        Returns:
            Lista de StampedSnapshot de todos os registradores
        """
        result = []
        for i in range(self.num_threads):
            stamped_value = self.registers[i].read()
            result.append(stamped_value)
        return result


def test_atomic_snapshot():
    """Testa o snapshot atômico"""
    snapshot = AtomicSnapshot(3, 0)
    results = []
    
    def writer_thread(thread_id):
        # Atualiza valores sequencialmente
        snapshot.update(thread_id * 10 + 1)
        time.sleep(0.01)
        snapshot.update(thread_id * 10 + 2)
        time.sleep(0.01)
        snapshot.update(thread_id * 10 + 3)
    
    def reader_thread():
        # Faz snapshots
        for _ in range(3):
            snap = snapshot.scan()
            results.append(snap)
            time.sleep(0.005)
    
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
    print(f"Atomic Snapshot Test:")
    print(f"  Results: {results}")
    print(f"  Final snapshot: {snapshot.scan()}")
    
    return True


if __name__ == "__main__":
    test_atomic_snapshot() 