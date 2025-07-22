"""
Testes para o Atomic Snapshot

Testa propriedades wait-free, atomicidade e snapshots consistentes.
"""

import pytest
import threading
import time
from .atomic_snapshot import AtomicSnapshot, StampedSnapshot


@pytest.fixture
def atomic_snapshot():
    """Fixture para criar um AtomicSnapshot para cada teste"""
    return AtomicSnapshot(3, 0)


@pytest.fixture
def shared_results():
    """Fixture para resultados compartilhados entre threads"""
    return []


def test_stamped_snapshot_creation():
    """Testa criação de StampedSnapshot"""
    # Testa criação básica
    snap1 = StampedSnapshot(1, "value1")
    assert snap1.stamp == 1
    assert snap1.value == "value1"
    assert snap1.snap == []
    
    # Testa criação com snapshot
    snap2 = StampedSnapshot(2, "value2", [1, 2, 3])
    assert snap2.stamp == 2
    assert snap2.value == "value2"
    assert snap2.snap == [1, 2, 3]


def test_initial_snapshot(atomic_snapshot):
    """Testa snapshot inicial"""
    snap = atomic_snapshot.scan()
    assert len(snap) == 3, f"Expected 3 values, got {len(snap)}"
    assert all(value == 0 for value in snap), f"Expected all zeros, got {snap}"


def test_single_update(atomic_snapshot):
    """Testa atualização de um único thread"""
    def writer():
        atomic_snapshot.update(42)
    
    # Executa writer
    writer_thread = threading.Thread(target=writer)
    writer_thread.start()
    writer_thread.join()
    
    # Verifica snapshot
    snap = atomic_snapshot.scan()
    assert len(snap) == 3, f"Expected 3 values, got {len(snap)}"
    # Pelo menos um valor deve ser 42
    assert 42 in snap, f"Expected 42 in snapshot, got {snap}"


def test_multiple_updates(atomic_snapshot, shared_results):
    """Testa múltiplas atualizações de diferentes threads"""
    def writer(thread_id):
        for i in range(3):
            atomic_snapshot.update(thread_id * 10 + i)
            time.sleep(0.01)
    
    def reader():
        for _ in range(5):
            snap = atomic_snapshot.scan()
            shared_results.append(snap)
            time.sleep(0.005)
    
    # Cria threads
    writer1 = threading.Thread(target=writer, args=(0,))
    writer2 = threading.Thread(target=writer, args=(1,))
    reader_thread = threading.Thread(target=reader)
    
    # Executa threads
    writer1.start()
    writer2.start()
    reader_thread.start()
    
    # Aguarda conclusão
    writer1.join()
    writer2.join()
    reader_thread.join()
    
    # Verifica resultados
    assert len(shared_results) == 5, f"Expected 5 snapshots, got {len(shared_results)}"
    for snap in shared_results:
        assert len(snap) == 3, f"Expected 3 values per snapshot, got {len(snap)}"


def test_snapshot_consistency(atomic_snapshot, shared_results):
    """Testa consistência dos snapshots"""
    def writer(thread_id):
        atomic_snapshot.update(thread_id * 100)
        time.sleep(0.01)
        atomic_snapshot.update(thread_id * 100 + 1)
    
    def reader():
        for _ in range(3):
            snap = atomic_snapshot.scan()
            shared_results.append(snap)
            time.sleep(0.005)
    
    # Cria threads
    writer1 = threading.Thread(target=writer, args=(0,))
    writer2 = threading.Thread(target=writer, args=(1,))
    reader_thread = threading.Thread(target=reader)
    
    # Executa threads
    writer1.start()
    writer2.start()
    reader_thread.start()
    
    # Aguarda conclusão
    writer1.join()
    writer2.join()
    reader_thread.join()
    
    # Verifica que snapshots são consistentes
    for snap in shared_results:
        assert len(snap) == 3, f"Expected 3 values per snapshot, got {len(snap)}"
        # Verifica que valores estão no range esperado
        for value in snap:
            assert 0 <= value <= 101, f"Value {value} out of expected range"


def test_wait_free_property(atomic_snapshot, shared_results):
    """Testa propriedade wait-free"""
    def writer(thread_id):
        for i in range(10):
            atomic_snapshot.update(thread_id * 10 + i)
            time.sleep(0.001)
    
    def reader():
        # Faz snapshots rapidamente
        for _ in range(20):
            snap = atomic_snapshot.scan()
            shared_results.append(snap)
            time.sleep(0.0005)  # Muito rápido
    
    # Cria threads
    writers = []
    for i in range(2):
        writer_thread = threading.Thread(target=writer, args=(i,))
        writers.append(writer_thread)
    
    reader_thread = threading.Thread(target=reader)
    
    # Executa threads
    for writer_thread in writers:
        writer_thread.start()
    reader_thread.start()
    
    # Aguarda conclusão
    for writer_thread in writers:
        writer_thread.join()
    reader_thread.join()
    
    # Verifica que reader completou (wait-free)
    assert len(shared_results) == 20, f"Expected 20 snapshots, got {len(shared_results)}"


def test_not_implemented_error(atomic_snapshot):
    """Testa que métodos não implementados lançam NotImplementedError"""
    with pytest.raises(NotImplementedError):
        atomic_snapshot.update(5)
    
    with pytest.raises(NotImplementedError):
        atomic_snapshot.scan()


def test_thread_id_generation(atomic_snapshot):
    """Testa geração de IDs únicos para threads"""
    thread_ids = set()
    
    def worker():
        thread_id = atomic_snapshot._get_thread_id()
        thread_ids.add(thread_id)
    
    # Cria múltiplos threads
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=worker)
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica que IDs estão no range correto
    for thread_id in thread_ids:
        assert 0 <= thread_id < atomic_snapshot.num_threads, f"Thread ID {thread_id} out of range"


def test_collect_method(atomic_snapshot):
    """Testa método _collect"""
    # Faz collect inicial
    collected = atomic_snapshot._collect()
    assert len(collected) == 3, f"Expected 3 values, got {len(collected)}"
    
    # Verifica que todos são StampedSnapshot
    for item in collected:
        assert isinstance(item, StampedSnapshot), f"Expected StampedSnapshot, got {type(item)}"


def test_different_num_threads():
    """Testa snapshot com diferentes números de threads"""
    # Testa com 2 threads
    snapshot_2 = AtomicSnapshot(2, 0)
    snap_2 = snapshot_2.scan()
    assert len(snap_2) == 2, f"Expected 2 values, got {len(snap_2)}"
    
    # Testa com 5 threads
    snapshot_5 = AtomicSnapshot(5, 0)
    snap_5 = snapshot_5.scan()
    assert len(snap_5) == 5, f"Expected 5 values, got {len(snap_5)}"


def test_edge_cases(atomic_snapshot):
    """Testa casos extremos"""
    # Valor None
    snapshot_none = AtomicSnapshot(2, None)
    snap_none = snapshot_none.scan()
    assert all(value is None for value in snap_none), f"Expected all None, got {snap_none}"
    
    # String vazia
    snapshot_empty = AtomicSnapshot(2, "")
    snap_empty = snapshot_empty.scan()
    assert all(value == "" for value in snap_empty), f"Expected all empty strings, got {snap_empty}"


def test_concurrent_updates(atomic_snapshot, shared_results):
    """Testa atualizações concorrentes"""
    def updater(thread_id):
        for i in range(5):
            atomic_snapshot.update(thread_id * 100 + i)
            time.sleep(0.001)
    
    # Cria múltiplos updaters
    threads = []
    for i in range(3):
        thread = threading.Thread(target=updater, args=(i,))
        threads.append(thread)
    
    # Executa threads
    for thread in threads:
        thread.start()
    
    # Aguarda conclusão
    for thread in threads:
        thread.join()
    
    # Verifica snapshot final
    final_snap = atomic_snapshot.scan()
    assert len(final_snap) == 3, f"Expected 3 values, got {len(final_snap)}"
    
    # Verifica que pelo menos um valor foi atualizado
    max_value = max(final_snap)
    assert max_value > 0, f"Expected some updates, got {final_snap}"


def test_snapshot_atomicity(atomic_snapshot, shared_results):
    """Testa atomicidade dos snapshots"""
    def writer(thread_id):
        # Escreve valores sequencialmente
        for i in range(3):
            atomic_snapshot.update(thread_id * 10 + i)
            time.sleep(0.01)
    
    def reader():
        # Faz snapshots durante as escritas
        for _ in range(5):
            snap = atomic_snapshot.scan()
            shared_results.append(snap)
            time.sleep(0.005)
    
    # Cria threads
    writer1 = threading.Thread(target=writer, args=(0,))
    writer2 = threading.Thread(target=writer, args=(1,))
    reader_thread = threading.Thread(target=reader)
    
    # Executa threads
    writer1.start()
    writer2.start()
    reader_thread.start()
    
    # Aguarda conclusão
    writer1.join()
    writer2.join()
    reader_thread.join()
    
    # Verifica que snapshots são consistentes
    for snap in shared_results:
        assert len(snap) == 3, f"Expected 3 values per snapshot, got {len(snap)}"
        # Verifica que valores estão no range esperado
        for value in snap:
            assert 0 <= value <= 12, f"Value {value} out of expected range"


def test_rapid_updates_and_scans(atomic_snapshot, shared_results):
    """Testa atualizações e scans rápidos"""
    def updater(thread_id):
        for i in range(20):
            atomic_snapshot.update(thread_id * 10 + i)
            time.sleep(0.0001)  # Muito rápido
    
    def scanner():
        for _ in range(30):
            snap = atomic_snapshot.scan()
            shared_results.append(snap)
            time.sleep(0.0001)  # Muito rápido
    
    # Cria threads
    updaters = []
    for i in range(2):
        updater_thread = threading.Thread(target=updater, args=(i,))
        updaters.append(updater_thread)
    
    scanner_thread = threading.Thread(target=scanner)
    
    # Executa threads
    for updater_thread in updaters:
        updater_thread.start()
    scanner_thread.start()
    
    # Aguarda conclusão
    for updater_thread in updaters:
        updater_thread.join()
    scanner_thread.join()
    
    # Verifica que não houve crash
    assert len(shared_results) == 30, f"Expected 30 scans, got {len(shared_results)}"
    for snap in shared_results:
        assert len(snap) == 3, f"Expected 3 values per snapshot, got {len(snap)}" 