"""
Paralelismo de Tarefas - Implementações de Padrões Comuns

Este módulo demonstra diferentes padrões de paralelismo de tarefas:
1. Pipeline de processamento
2. Produtor-Consumidor
3. Map-Reduce
4. Fork-Join com dependências
"""

import asyncio
import time
from typing import List, Callable, Any, Dict
from concurrent.futures import ThreadPoolExecutor
import threading
from queue import Queue
import random


class TaskPipeline:
    """Pipeline de processamento com múltiplas etapas"""
    
    def __init__(self, stages: List[Callable]):
        """
        Inicializa pipeline com lista de funções de processamento
        
        Args:
            stages: Lista de funções que processam dados sequencialmente
        """
        self.stages = stages
        self.results = []
    
    async def process_data(self, data: List[Any]) -> List[Any]:
        """
        Processa dados através do pipeline de forma assíncrona
        
        Args:
            data: Lista de dados para processar
            
        Returns:
            Lista de dados processados
        """
        # TODO: Implementar pipeline assíncrono
        # Cada estágio deve processar dados em paralelo quando possível
        # Use asyncio.gather() para executar estágios independentes
        raise NotImplementedError("Pipeline assíncrono não implementado")


class ProducerConsumer:
    """Padrão Produtor-Consumidor com fila thread-safe"""
    
    def __init__(self, buffer_size: int = 10):
        """
        Inicializa produtor-consumidor
        
        Args:
            buffer_size: Tamanho máximo da fila
        """
        self.queue = Queue(maxsize=buffer_size)
        self.producers = []
        self.consumers = []
        self.running = False
    
    def add_producer(self, producer_func: Callable):
        """Adiciona função produtora"""
        self.producers.append(producer_func)
    
    def add_consumer(self, consumer_func: Callable):
        """Adiciona função consumidora"""
        self.consumers.append(consumer_func)
    
    def start(self, num_producers: int = 1, num_consumers: int = 2):
        """
        Inicia execução do padrão produtor-consumidor
        
        Args:
            num_producers: Número de threads produtores
            num_consumers: Número de threads consumidores
        """
        # TODO: Implementar execução paralela
        # Use ThreadPoolExecutor para criar produtores e consumidores
        # Produtores devem chamar queue.put() e consumidores queue.get()
        # Implemente shutdown graceful quando todos os produtores terminarem
        raise NotImplementedError("Execução produtor-consumidor não implementada")


class MapReduce:
    """Implementação simplificada do padrão Map-Reduce"""
    
    def __init__(self, num_workers: int = 4):
        """
        Inicializa MapReduce
        
        Args:
            num_workers: Número de workers para processamento paralelo
        """
        self.num_workers = num_workers
        self.executor = ThreadPoolExecutor(max_workers=num_workers)
    
    def map_reduce(self, data: List[Any], 
                   map_func: Callable, 
                   reduce_func: Callable) -> Any:
        """
        Executa operação map-reduce
        
        Args:
            data: Dados de entrada
            map_func: Função para mapear cada item
            reduce_func: Função para reduzir resultados
            
        Returns:
            Resultado da operação reduce
        """
        # TODO: Implementar map-reduce paralelo
        # Divida dados em chunks para workers
        # Use executor.submit() para executar map_func em paralelo
        # Colete resultados e aplique reduce_func
        raise NotImplementedError("Map-reduce paralelo não implementado")


class DependencyGraph:
    """Grafo de dependências para execução de tarefas"""
    
    def __init__(self):
        """Inicializa grafo de dependências"""
        self.tasks = {}  # task_id -> (func, dependencies)
        self.results = {}
        self.lock = threading.Lock()
    
    def add_task(self, task_id: str, func: Callable, 
                 dependencies: List[str] = None):
        """
        Adiciona tarefa ao grafo
        
        Args:
            task_id: Identificador único da tarefa
            func: Função a ser executada
            dependencies: Lista de IDs de tarefas dependentes
        """
        self.tasks[task_id] = (func, dependencies or [])
    
    async def execute(self) -> Dict[str, Any]:
        """
        Executa tarefas respeitando dependências
        
        Returns:
            Dicionário com resultados de todas as tarefas
        """
        # TODO: Implementar execução com dependências
        # Use asyncio para executar tarefas independentes em paralelo
        # Implemente detecção de dependências circulares
        # Use semáforos para limitar concorrência se necessário
        raise NotImplementedError("Execução com dependências não implementada")


# Funções auxiliares para demonstração
def simulate_work(duration: float, task_name: str = "task") -> str:
    """Simula trabalho com duração específica"""
    time.sleep(duration)
    return f"{task_name} completed in {duration}s"

def process_stage(data: Any, stage_name: str) -> str:
    """Simula processamento de estágio do pipeline"""
    time.sleep(0.1)  # Simula processamento
    return f"{stage_name}: {data}"

def map_function(item: int) -> int:
    """Função de mapeamento para MapReduce"""
    time.sleep(0.01)  # Simula processamento
    return item * item

def reduce_function(results: List[int]) -> int:
    """Função de redução para MapReduce"""
    return sum(results)

def producer_function(queue: Queue, items: List[Any]):
    """Função produtora para ProducerConsumer"""
    for item in items:
        queue.put(item)
        time.sleep(0.01)  # Simula produção

def consumer_function(queue: Queue, consumer_id: int) -> List[Any]:
    """Função consumidora para ProducerConsumer"""
    consumed = []
    while True:
        try:
            item = queue.get(timeout=1)  # Timeout para detectar fim
            consumed.append(f"Consumer {consumer_id}: {item}")
            time.sleep(0.01)  # Simula processamento
            queue.task_done()
        except:
            break  # Timeout - não há mais itens
    return consumed 