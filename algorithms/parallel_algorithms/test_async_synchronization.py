"""
Testes para Sincronização Assíncrona

Testa primitivas de sincronização para asyncio:
1. Contador thread-safe
2. Pool de recursos
3. Barreira assíncrona
4. Produtor-Consumidor assíncrono
5. Lock de leitura-escrita
"""

import pytest
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

from .async_synchronization import (
    AsyncCounter, AsyncResourcePool, AsyncBarrier, 
    AsyncProducerConsumer, AsyncReadWriteLock,
    simulate_async_work, producer_task, consumer_task
)


class TestAsyncCounter:
    """Testes para contador assíncrono thread-safe"""
    
    def test_counter_initialization(self):
        """Testa inicialização do contador"""
        counter = AsyncCounter(initial_value=10)
        assert counter._value == 10
    
    @pytest.mark.asyncio
    async def test_counter_increment(self):
        """Testa incremento básico do contador"""
        counter = AsyncCounter()
        
        # TODO: Implementar incremento para passar este teste
        with pytest.raises(NotImplementedError):
            result = await counter.increment()
        
        # Deve retornar 1 após primeiro incremento
        # assert result == 1
    
    @pytest.mark.asyncio
    async def test_counter_concurrent_increments(self):
        """Testa incrementos concorrentes"""
        counter = AsyncCounter()
        
        async def increment_worker():
            for _ in range(100):
                await counter.increment()
        
        # Cria 10 workers incrementando 100 vezes cada
        workers = [increment_worker() for _ in range(10)]
        
        # TODO: Implementar para que passe este teste
        with pytest.raises(NotImplementedError):
            await asyncio.gather(*workers)
        
        # Resultado final deve ser 1000 (10 workers × 100 incrementos)
        # final_value = await counter.get_value()
        # assert final_value == 1000


class TestAsyncResourcePool:
    """Testes para pool de recursos assíncrono"""
    
    def test_pool_initialization(self):
        """Testa inicialização do pool"""
        pool = AsyncResourcePool(max_resources=5)
        assert pool.semaphore._value == 5
        assert len(pool.resources) == 0
    
    @pytest.mark.asyncio
    async def test_resource_acquisition(self):
        """Testa aquisição de recursos"""
        pool = AsyncResourcePool(max_resources=2)
        
        # TODO: Implementar aquisição para passar este teste
        with pytest.raises(NotImplementedError):
            resource1 = await pool.acquire_resource()
            resource2 = await pool.acquire_resource()
        
        # Deve conseguir adquirir 2 recursos
        # assert resource1 != resource2
        # assert len(pool.resources) == 2
    
    @pytest.mark.asyncio
    async def test_resource_pool_concurrency_limit(self):
        """Testa limite de concorrência do pool"""
        pool = AsyncResourcePool(max_resources=2)
        
        async def acquire_and_hold(duration):
            resource = await pool.acquire_resource()
            await asyncio.sleep(duration)
            await pool.release_resource(resource)
            return resource
        
        start_time = time.time()
        
        # TODO: Implementar para que passe este teste
        with pytest.raises(NotImplementedError):
            # 3 tarefas tentando adquirir 2 recursos
            tasks = [
                acquire_and_hold(0.1),
                acquire_and_hold(0.1),
                acquire_and_hold(0.1)
            ]
            results = await asyncio.gather(*tasks)
        
        # Tempo total deve ser ~0.2s (2 batches de 0.1s cada)
        # elapsed = time.time() - start_time
        # assert elapsed >= 0.15  # Pelo menos 0.15s devido ao limite


class TestAsyncBarrier:
    """Testes para barreira assíncrona"""
    
    def test_barrier_initialization(self):
        """Testa inicialização da barreira"""
        barrier = AsyncBarrier(parties=3)
        assert barrier.parties == 3
        assert barrier.count == 3
    
    @pytest.mark.asyncio
    async def test_barrier_synchronization(self):
        """Testa sincronização da barreira"""
        barrier = AsyncBarrier(parties=3)
        results = []
        
        async def worker(worker_id):
            await asyncio.sleep(0.1 * worker_id)  # Diferentes tempos de chegada
            is_first = await barrier.wait()
            results.append(f"Worker {worker_id}: {is_first}")
        
        # TODO: Implementar barreira para passar este teste
        with pytest.raises(NotImplementedError):
            workers = [worker(i) for i in range(3)]
            await asyncio.gather(*workers)
        
        # Todas as tarefas devem chegar na barreira antes de continuar
        # assert len(results) == 3
        # assert any("True" in result for result in results)  # Uma deve ser primeira


class TestAsyncProducerConsumer:
    """Testes para produtor-consumidor assíncrono"""
    
    def test_async_pc_initialization(self):
        """Testa inicialização do produtor-consumidor assíncrono"""
        pc = AsyncProducerConsumer(maxsize=5)
        assert pc.queue.maxsize == 5
        assert len(pc.producers) == 0
        assert len(pc.consumers) == 0
    
    @pytest.mark.asyncio
    async def test_async_producer_consumer_execution(self):
        """Testa execução do produtor-consumidor assíncrono"""
        pc = AsyncProducerConsumer(maxsize=3)
        
        items = ["item1", "item2", "item3", "item4", "item5"]
        
        # Adiciona produtor e consumidores
        await pc.add_producer(lambda: producer_task(pc.queue, items))
        await pc.add_consumer(lambda: consumer_task(pc.queue, 1))
        await pc.add_consumer(lambda: consumer_task(pc.queue, 2))
        
        # TODO: Implementar execução para passar este teste
        with pytest.raises(NotImplementedError):
            await pc.start(num_producers=1, num_consumers=2)
        
        # Todos os itens devem ser processados pelos consumidores


class TestAsyncReadWriteLock:
    """Testes para lock de leitura-escrita assíncrono"""
    
    def test_rw_lock_initialization(self):
        """Testa inicialização do lock de leitura-escrita"""
        rw_lock = AsyncReadWriteLock()
        assert rw_lock._readers == 0
        assert rw_lock._writers == 0
    
    @pytest.mark.asyncio
    async def test_multiple_readers(self):
        """Testa múltiplos leitores simultâneos"""
        rw_lock = AsyncReadWriteLock()
        readers_active = 0
        max_readers = 0
        
        async def reader(reader_id):
            nonlocal readers_active, max_readers
            await rw_lock.acquire_read()
            readers_active += 1
            max_readers = max(max_readers, readers_active)
            await asyncio.sleep(0.1)  # Simula leitura
            readers_active -= 1
            await rw_lock.release_read()
        
        # TODO: Implementar lock para passar este teste
        with pytest.raises(NotImplementedError):
            readers = [reader(i) for i in range(5)]
            await asyncio.gather(*readers)
        
        # Múltiplos leitores devem poder ler simultaneamente
        # assert max_readers > 1
    
    @pytest.mark.asyncio
    async def test_writer_exclusivity(self):
        """Testa exclusividade do escritor"""
        rw_lock = AsyncReadWriteLock()
        readers_active = 0
        writer_active = False
        
        async def reader():
            nonlocal readers_active
            await rw_lock.acquire_read()
            readers_active += 1
            await asyncio.sleep(0.2)  # Leitura longa
            readers_active -= 1
            await rw_lock.release_read()
        
        async def writer():
            nonlocal writer_active
            await rw_lock.acquire_write()
            writer_active = True
            await asyncio.sleep(0.1)  # Escrita
            writer_active = False
            await rw_lock.release_write()
        
        # TODO: Implementar para que passe este teste
        with pytest.raises(NotImplementedError):
            # Inicia leitores, depois escritor
            reader_task = asyncio.create_task(reader())
            await asyncio.sleep(0.05)  # Leitor começa primeiro
            writer_task = asyncio.create_task(writer())
            await asyncio.sleep(0.05)  # Escritor tenta escrever
            
            await asyncio.gather(reader_task, writer_task)
        
        # Escritor deve aguardar leitores terminarem
        # assert not (readers_active > 0 and writer_active)


class TestRaceConditions:
    """Testes para condições de corrida assíncronas"""
    
    @pytest.mark.asyncio
    async def test_async_counter_race_condition(self):
        """Testa condição de corrida em contador assíncrono"""
        counter = 0
        lock = asyncio.Lock()
        
        async def increment_without_lock():
            nonlocal counter
            current = counter
            await asyncio.sleep(0.001)  # Simula processamento
            counter = current + 1
        
        async def increment_with_lock():
            nonlocal counter
            async with lock:
                current = counter
                await asyncio.sleep(0.001)  # Simula processamento
                counter = current + 1
        
        # Testa sem lock (pode ter race condition)
        counter = 0
        tasks = [increment_without_lock() for _ in range(10)]
        await asyncio.gather(*tasks)
        
        # Resultado pode ser < 10 devido a race condition
        print(f"Counter without lock: {counter}")
        
        # Testa com lock (deve ser thread-safe)
        counter = 0
        tasks = [increment_with_lock() for _ in range(10)]
        await asyncio.gather(*tasks)
        
        assert counter == 10  # Sempre deve ser 10 com lock
    
    @pytest.mark.asyncio
    async def test_async_shared_state_race(self):
        """Testa race condition em estado compartilhado assíncrono"""
        shared_list = []
        
        async def append_without_sync(item):
            # Simula operação não atômica
            current_length = len(shared_list)
            await asyncio.sleep(0.001)  # Simula processamento
            shared_list.append(item)
        
        async def append_with_sync(item):
            # Usa lock para sincronização
            async with asyncio.Lock():
                current_length = len(shared_list)
                await asyncio.sleep(0.001)  # Simula processamento
                shared_list.append(item)
        
        # Testa sem sincronização
        shared_list.clear()
        tasks = [append_without_sync(f"item_{i}") for i in range(10)]
        await asyncio.gather(*tasks)
        
        # Pode haver problemas de consistência
        print(f"List without sync: {len(shared_list)} items")
        
        # Testa com sincronização
        shared_list.clear()
        tasks = [append_with_sync(f"item_{i}") for i in range(10)]
        await asyncio.gather(*tasks)
        
        assert len(shared_list) == 10  # Sempre deve ter 10 itens


class TestPerformanceComparison:
    """Testes de comparação de performance"""
    
    @pytest.mark.asyncio
    async def test_async_vs_sync_performance(self):
        """Compara performance assíncrona vs síncrona"""
        
        async def async_work():
            await asyncio.sleep(0.1)
            return "async_result"
        
        def sync_work():
            time.sleep(0.1)
            return "sync_result"
        
        # Mede tempo assíncrono
        start = time.time()
        tasks = [async_work() for _ in range(10)]
        async_results = await asyncio.gather(*tasks)
        async_time = time.time() - start
        
        # Mede tempo síncrono
        start = time.time()
        sync_results = []
        for _ in range(10):
            sync_results.append(sync_work())
        sync_time = time.time() - start
        
        print(f"Async time: {async_time:.3f}s")
        print(f"Sync time: {sync_time:.3f}s")
        print(f"Speedup: {sync_time / async_time:.2f}x")
        
        # Assíncrono deve ser mais rápido para I/O-bound tasks
        assert async_time < sync_time
        assert len(async_results) == 10
        assert len(sync_results) == 10


if __name__ == "__main__":
    pytest.main([__file__]) 