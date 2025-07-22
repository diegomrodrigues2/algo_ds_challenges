"""
Sincronização Assíncrona - Primitivas para asyncio

Implementa primitivas de sincronização para evitar condições de corrida
em código assíncrono usando asyncio.
"""

import asyncio
import time
from typing import Any, Dict, List, Optional
from collections import defaultdict


class AsyncCounter:
    """Contador thread-safe para operações assíncronas"""
    
    def __init__(self, initial_value: int = 0):
        """
        Inicializa contador assíncrono
        
        Args:
            initial_value: Valor inicial do contador
        """
        self._value = initial_value
        self._lock = asyncio.Lock()
    
    async def increment(self, amount: int = 1) -> int:
        """
        Incrementa o contador de forma thread-safe
        
        Args:
            amount: Quantidade a incrementar
            
        Returns:
            Novo valor do contador
        """
        # TODO: Implementar incremento thread-safe
        # Use self._lock para garantir atomicidade
        raise NotImplementedError("Incremento assíncrono não implementado")
    
    async def get_value(self) -> int:
        """Retorna valor atual do contador"""
        async with self._lock:
            return self._value


class AsyncResourcePool:
    """Pool de recursos com semáforo assíncrono"""
    
    def __init__(self, max_resources: int):
        """
        Inicializa pool de recursos
        
        Args:
            max_resources: Número máximo de recursos disponíveis
        """
        self.semaphore = asyncio.Semaphore(max_resources)
        self.resources = []
        self._lock = asyncio.Lock()
    
    async def acquire_resource(self) -> str:
        """
        Adquire um recurso do pool
        
        Returns:
            Identificador do recurso adquirido
        """
        # TODO: Implementar aquisição de recurso
        # Use semaphore para limitar concorrência
        # Gere ID único para o recurso
        raise NotImplementedError("Aquisição de recurso não implementada")
    
    async def release_resource(self, resource_id: str):
        """
        Libera um recurso do pool
        
        Args:
            resource_id: ID do recurso a ser liberado
        """
        # TODO: Implementar liberação de recurso
        # Remova recurso da lista e libere semáforo
        raise NotImplementedError("Liberação de recurso não implementada")


class AsyncBarrier:
    """Barreira assíncrona para sincronização de grupo"""
    
    def __init__(self, parties: int):
        """
        Inicializa barreira
        
        Args:
            parties: Número de tarefas que devem chegar na barreira
        """
        self.parties = parties
        self.count = parties
        self._lock = asyncio.Lock()
        self._event = asyncio.Event()
    
    async def wait(self) -> bool:
        """
        Aguarda na barreira até que todas as tarefas cheguem
        
        Returns:
            True se esta tarefa deve executar ação especial
        """
        # TODO: Implementar barreira assíncrona
        # Decremente count e aguarde até chegar a 0
        # Retorne True para a primeira tarefa que chega a 0
        raise NotImplementedError("Barreira assíncrona não implementada")


class AsyncProducerConsumer:
    """Produtor-Consumidor assíncrono usando Queue"""
    
    def __init__(self, maxsize: int = 10):
        """
        Inicializa produtor-consumidor assíncrono
        
        Args:
            maxsize: Tamanho máximo da fila
        """
        self.queue = asyncio.Queue(maxsize=maxsize)
        self.producers = []
        self.consumers = []
        self.running = False
    
    async def add_producer(self, producer_func):
        """Adiciona função produtora assíncrona"""
        self.producers.append(producer_func)
    
    async def add_consumer(self, consumer_func):
        """Adiciona função consumidora assíncrona"""
        self.consumers.append(consumer_func)
    
    async def start(self, num_producers: int = 1, num_consumers: int = 2):
        """
        Inicia execução do produtor-consumidor assíncrono
        
        Args:
            num_producers: Número de produtores
            num_consumers: Número de consumidores
        """
        # TODO: Implementar execução assíncrona
        # Use asyncio.create_task() para criar produtores e consumidores
        # Produtores devem chamar queue.put() e consumidores queue.get()
        raise NotImplementedError("Execução assíncrona não implementada")


class AsyncReadWriteLock:
    """Lock de leitura-escrita assíncrono"""
    
    def __init__(self):
        """Inicializa lock de leitura-escrita"""
        self._readers = 0
        self._writers = 0
        self._read_lock = asyncio.Lock()
        self._write_lock = asyncio.Lock()
        self._read_ready = asyncio.Condition(self._read_lock)
    
    async def acquire_read(self):
        """Adquire lock para leitura"""
        # TODO: Implementar aquisição de lock de leitura
        # Múltiplos leitores podem ler simultaneamente
        # Escritores devem aguardar todos os leitores terminarem
        raise NotImplementedError("Lock de leitura não implementado")
    
    async def release_read(self):
        """Libera lock de leitura"""
        # TODO: Implementar liberação de lock de leitura
        # Decremente contador de leitores
        # Notifique escritores se não há mais leitores
        raise NotImplementedError("Liberação de leitura não implementada")
    
    async def acquire_write(self):
        """Adquire lock para escrita"""
        # TODO: Implementar aquisição de lock de escrita
        # Apenas um escritor pode escrever por vez
        # Deve aguardar todos os leitores e escritores terminarem
        raise NotImplementedError("Lock de escrita não implementado")
    
    async def release_write(self):
        """Libera lock de escrita"""
        # TODO: Implementar liberação de lock de escrita
        # Decremente contador de escritores
        # Notifique leitores e escritores aguardando
        raise NotImplementedError("Liberação de escrita não implementada")


# Funções auxiliares para demonstração
async def simulate_async_work(duration: float, task_name: str = "task") -> str:
    """Simula trabalho assíncrono"""
    await asyncio.sleep(duration)
    return f"{task_name} completed in {duration}s"

async def producer_task(queue: asyncio.Queue, items: List[Any]):
    """Tarefa produtora assíncrona"""
    for item in items:
        await queue.put(item)
        await asyncio.sleep(0.01)  # Simula produção

async def consumer_task(queue: asyncio.Queue, consumer_id: int) -> List[Any]:
    """Tarefa consumidora assíncrona"""
    consumed = []
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=1.0)
            consumed.append(f"Consumer {consumer_id}: {item}")
            await asyncio.sleep(0.01)  # Simula processamento
            queue.task_done()
        except asyncio.TimeoutError:
            break  # Timeout - não há mais itens
    return consumed 