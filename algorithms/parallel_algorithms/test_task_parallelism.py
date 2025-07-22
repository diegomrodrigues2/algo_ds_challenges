"""
Testes para Paralelismo de Tarefas

Testa diferentes padrões de paralelismo de tarefas:
1. Pipeline de processamento
2. Produtor-Consumidor  
3. Map-Reduce
4. Grafo de dependências
"""

import pytest
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
import threading
from queue import Queue

from .task_parallelism import (
    TaskPipeline, ProducerConsumer, MapReduce, DependencyGraph,
    simulate_work, process_stage, map_function, reduce_function,
    producer_function, consumer_function
)


class TestTaskPipeline:
    """Testes para pipeline de processamento"""
    
    def test_pipeline_initialization(self):
        """Testa inicialização do pipeline"""
        stages = [lambda x: x * 2, lambda x: x + 1]
        pipeline = TaskPipeline(stages)
        
        assert len(pipeline.stages) == 2
        assert pipeline.results == []
    
    @pytest.mark.asyncio
    async def test_pipeline_sequential_processing(self):
        """Testa processamento sequencial básico"""
        def stage1(data):
            return [x * 2 for x in data]
        
        def stage2(data):
            return [x + 1 for x in data]
        
        pipeline = TaskPipeline([stage1, stage2])
        data = [1, 2, 3, 4, 5]
        
        # TODO: Implementar pipeline para passar este teste
        # Resultado esperado: [3, 5, 7, 9, 11] (2x + 1)
        with pytest.raises(NotImplementedError):
            result = await pipeline.process_data(data)
    
    @pytest.mark.asyncio
    async def test_pipeline_parallel_stages(self):
        """Testa execução paralela de estágios independentes"""
        async def async_stage1(data):
            await asyncio.sleep(0.1)  # Simula I/O
            return [x * 2 for x in data]
        
        async def async_stage2(data):
            await asyncio.sleep(0.1)  # Simula I/O
            return [x + 1 for x in data]
        
        pipeline = TaskPipeline([async_stage1, async_stage2])
        data = [1, 2, 3]
        
        start_time = time.time()
        with pytest.raises(NotImplementedError):
            result = await pipeline.process_data(data)
        
        # TODO: Implementar para que tempo total < 0.3s (paralelo)
        # Tempo sequencial seria ~0.2s, paralelo deve ser ~0.1s


class TestProducerConsumer:
    """Testes para padrão produtor-consumidor"""
    
    def test_producer_consumer_initialization(self):
        """Testa inicialização do produtor-consumidor"""
        pc = ProducerConsumer(buffer_size=5)
        
        assert pc.queue.maxsize == 5
        assert len(pc.producers) == 0
        assert len(pc.consumers) == 0
        assert not pc.running
    
    def test_add_producer_and_consumer(self):
        """Testa adição de produtores e consumidores"""
        pc = ProducerConsumer()
        
        def producer():
            pass
        
        def consumer():
            pass
        
        pc.add_producer(producer)
        pc.add_consumer(consumer)
        
        assert len(pc.producers) == 1
        assert len(pc.consumers) == 1
    
    def test_producer_consumer_execution(self):
        """Testa execução básica do padrão produtor-consumidor"""
        pc = ProducerConsumer(buffer_size=3)
        
        items = ["item1", "item2", "item3", "item4", "item5"]
        
        # Adiciona produtor e consumidores
        pc.add_producer(lambda: producer_function(pc.queue, items))
        pc.add_consumer(lambda: consumer_function(pc.queue, 1))
        pc.add_consumer(lambda: consumer_function(pc.queue, 2))
        
        # TODO: Implementar execução para passar este teste
        with pytest.raises(NotImplementedError):
            pc.start(num_producers=1, num_consumers=2)
    
    def test_producer_consumer_thread_safety(self):
        """Testa thread-safety da fila compartilhada"""
        queue = Queue(maxsize=10)
        
        # Testa concorrência de produtores
        def producer1():
            for i in range(5):
                queue.put(f"prod1_{i}")
        
        def producer2():
            for i in range(5):
                queue.put(f"prod2_{i}")
        
        with ThreadPoolExecutor(max_workers=2) as executor:
            future1 = executor.submit(producer1)
            future2 = executor.submit(producer2)
            future1.result()
            future2.result()
        
        # Verifica que todos os itens foram produzidos
        items = []
        while not queue.empty():
            items.append(queue.get())
        
        assert len(items) == 10
        assert any("prod1_" in item for item in items)
        assert any("prod2_" in item for item in items)


class TestMapReduce:
    """Testes para padrão Map-Reduce"""
    
    def test_mapreduce_initialization(self):
        """Testa inicialização do MapReduce"""
        mr = MapReduce(num_workers=4)
        
        assert mr.num_workers == 4
        assert mr.executor._max_workers == 4
    
    def test_mapreduce_basic_operation(self):
        """Testa operação básica map-reduce"""
        mr = MapReduce(num_workers=2)
        data = [1, 2, 3, 4, 5]
        
        # TODO: Implementar map-reduce para passar este teste
        with pytest.raises(NotImplementedError):
            result = mr.map_reduce(data, map_function, reduce_function)
        
        # Resultado esperado: 1² + 2² + 3² + 4² + 5² = 55
    
    def test_mapreduce_large_dataset(self):
        """Testa MapReduce com dataset grande"""
        mr = MapReduce(num_workers=4)
        data = list(range(1000))
        
        start_time = time.time()
        with pytest.raises(NotImplementedError):
            result = mr.map_reduce(data, map_function, reduce_function)
        
        # TODO: Implementar para que seja mais rápido que sequencial
        # Tempo sequencial seria ~10s, paralelo deve ser ~2.5s
    
    def test_mapreduce_custom_functions(self):
        """Testa MapReduce com funções customizadas"""
        mr = MapReduce(num_workers=2)
        data = ["a", "bb", "ccc", "dddd"]
        
        def custom_map(s):
            return len(s)
        
        def custom_reduce(lengths):
            return max(lengths)
        
        with pytest.raises(NotImplementedError):
            result = mr.map_reduce(data, custom_map, custom_reduce)
        
        # Resultado esperado: max([1, 2, 3, 4]) = 4


class TestDependencyGraph:
    """Testes para grafo de dependências"""
    
    def test_dependency_graph_initialization(self):
        """Testa inicialização do grafo de dependências"""
        dg = DependencyGraph()
        
        assert len(dg.tasks) == 0
        assert len(dg.results) == 0
    
    def test_add_task(self):
        """Testa adição de tarefas ao grafo"""
        dg = DependencyGraph()
        
        def task_a():
            return "A"
        
        def task_b():
            return "B"
        
        dg.add_task("A", task_a)
        dg.add_task("B", task_b, dependencies=["A"])
        
        assert "A" in dg.tasks
        assert "B" in dg.tasks
        assert dg.tasks["A"][1] == []  # Sem dependências
        assert dg.tasks["B"][1] == ["A"]  # Depende de A
    
    @pytest.mark.asyncio
    async def test_dependency_graph_execution(self):
        """Testa execução de tarefas com dependências"""
        dg = DependencyGraph()
        
        def task_a():
            time.sleep(0.1)
            return "A"
        
        def task_b():
            time.sleep(0.1)
            return "B"
        
        def task_c():
            time.sleep(0.1)
            return "C"
        
        # A e B são independentes, C depende de ambos
        dg.add_task("A", task_a)
        dg.add_task("B", task_b)
        dg.add_task("C", task_c, dependencies=["A", "B"])
        
        start_time = time.time()
        with pytest.raises(NotImplementedError):
            results = await dg.execute()
        
        # TODO: Implementar para que A e B executem em paralelo
        # Tempo total deve ser ~0.2s (A||B, depois C) não 0.3s (sequencial)
    
    @pytest.mark.asyncio
    async def test_circular_dependency_detection(self):
        """Testa detecção de dependências circulares"""
        dg = DependencyGraph()
        
        def task_a():
            return "A"
        
        def task_b():
            return "B"
        
        # Cria dependência circular: A -> B -> A
        dg.add_task("A", task_a, dependencies=["B"])
        dg.add_task("B", task_b, dependencies=["A"])
        
        # TODO: Implementar detecção de dependência circular
        with pytest.raises(NotImplementedError):
            await dg.execute()
        
        # Deve detectar e reportar dependência circular


class TestRaceConditions:
    """Testes para condições de corrida"""
    
    def test_counter_race_condition(self):
        """Testa condição de corrida em contador compartilhado"""
        counter = 0
        lock = threading.Lock()
        
        def increment_without_lock():
            nonlocal counter
            current = counter
            time.sleep(0.001)  # Simula processamento
            counter = current + 1
        
        def increment_with_lock():
            nonlocal counter
            with lock:
                current = counter
                time.sleep(0.001)  # Simula processamento
                counter = current + 1
        
        # Testa sem lock (pode ter race condition)
        counter = 0
        threads = []
        for _ in range(10):
            t = threading.Thread(target=increment_without_lock)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        # Resultado pode ser < 10 devido a race condition
        print(f"Counter without lock: {counter}")
        
        # Testa com lock (deve ser thread-safe)
        counter = 0
        threads = []
        for _ in range(10):
            t = threading.Thread(target=increment_with_lock)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        assert counter == 10  # Sempre deve ser 10 com lock


class TestPerformanceMetrics:
    """Testes para métricas de performance"""
    
    def test_work_span_analysis(self):
        """Testa análise de trabalho vs span"""
        # Simula algoritmo com trabalho T₁ e span T∞
        def sequential_work():
            time.sleep(0.1)  # T₁ = 0.1s
            time.sleep(0.1)  # T₁ = 0.2s
            time.sleep(0.1)  # T₁ = 0.3s
        
        def parallel_work():
            # Estas operações podem ser paralelas
            with ThreadPoolExecutor(max_workers=3) as executor:
                futures = [
                    executor.submit(time.sleep, 0.1),
                    executor.submit(time.sleep, 0.1),
                    executor.submit(time.sleep, 0.1)
                ]
                for future in futures:
                    future.result()
        
        # Mede tempo sequencial (T₁)
        start = time.time()
        sequential_work()
        t1 = time.time() - start
        
        # Mede tempo paralelo (T∞)
        start = time.time()
        parallel_work()
        t_infinity = time.time() - start
        
        # Calcula paralelismo
        parallelism = t1 / t_infinity
        
        print(f"T₁ (Work): {t1:.3f}s")
        print(f"T∞ (Span): {t_infinity:.3f}s")
        print(f"Paralelismo: {parallelism:.2f}")
        
        # Paralelismo deve ser próximo a 3 (3 operações paralelas)
        assert parallelism > 2.5


if __name__ == "__main__":
    pytest.main([__file__]) 