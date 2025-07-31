import pytest
from .cfs_scheduler_simulation import (
    Task, RBNode, CFSScheduler, 
    simulate_cfs_workload, compare_with_avl_simulation
)


class TestCFSScheduler:
    """Testes para a simulação do CFS usando Red-Black Trees."""
    
    def test_task_creation(self):
        """Testa criação de tarefas."""
        task = Task(pid=1, priority=0)
        assert task.pid == 1
        assert task.priority == 0
        assert task.vruntime == 0.0
        assert task.weight == 1024
    
    def test_scheduler_initialization(self):
        """Testa inicialização do agendador."""
        scheduler = CFSScheduler()
        assert scheduler.root is None
        assert scheduler.nr_running == 0
        assert scheduler.min_vruntime == 0.0
        assert scheduler.leftmost is None
    
    def test_add_task_not_implemented(self):
        """Testa que add_task ainda não foi implementada."""
        scheduler = CFSScheduler()
        task = Task(pid=1)
        
        with pytest.raises(NotImplementedError):
            scheduler.add_task(task)
    
    def test_remove_task_not_implemented(self):
        """Testa que remove_task ainda não foi implementada."""
        scheduler = CFSScheduler()
        task = Task(pid=1)
        
        with pytest.raises(NotImplementedError):
            scheduler.remove_task(task)
    
    def test_pick_next_task_not_implemented(self):
        """Testa que pick_next_task ainda não foi implementada."""
        scheduler = CFSScheduler()
        
        with pytest.raises(NotImplementedError):
            scheduler.pick_next_task()
    
    def test_update_task_runtime_not_implemented(self):
        """Testa que update_task_runtime ainda não foi implementada."""
        scheduler = CFSScheduler()
        task = Task(pid=1)
        
        with pytest.raises(NotImplementedError):
            scheduler.update_task_runtime(task, 0.001)
    
    def test_get_scheduler_stats(self):
        """Testa obtenção de estatísticas do agendador."""
        scheduler = CFSScheduler()
        stats = scheduler.get_scheduler_stats()
        
        assert "nr_running" in stats
        assert "min_vruntime" in stats
        assert "has_leftmost" in stats
        assert stats["nr_running"] == 0
        assert stats["min_vruntime"] == 0.0
        assert stats["has_leftmost"] is False


class TestCFSSimulation:
    """Testes para simulação de carga de trabalho do CFS."""
    
    def test_simulate_cfs_workload_structure(self):
        """Testa estrutura da função de simulação."""
        scheduler = CFSScheduler()
        
        # A função deve retornar um dicionário com estatísticas
        # mesmo que as operações não estejam implementadas
        try:
            stats = simulate_cfs_workload(scheduler, num_tasks=5, simulation_ticks=10)
            assert isinstance(stats, dict)
        except NotImplementedError:
            # Esperado, pois as operações não estão implementadas
            pass
    
    def test_compare_with_avl_simulation_structure(self):
        """Testa estrutura da função de comparação."""
        result = compare_with_avl_simulation()
        
        assert isinstance(result, dict)
        assert "red_black_performance" in result
        assert "note" in result
        assert "AVL trees would have more rotations" in result["note"]


class TestTaskAndNode:
    """Testes para classes Task e RBNode."""
    
    def test_task_attributes(self):
        """Testa atributos da classe Task."""
        task = Task(pid=42, priority=5)
        
        assert task.pid == 42
        assert task.priority == 5
        assert task.vruntime == 0.0
        assert task.sum_exec_runtime == 0.0
        assert task.weight == 1024
    
    def test_rbnode_creation(self):
        """Testa criação de nós da árvore Red-Black."""
        task = Task(pid=1)
        node = RBNode(task, color="BLACK")
        
        assert node.task == task
        assert node.color == "BLACK"
        assert node.left is None
        assert node.right is None
        assert node.parent is None
    
    def test_rbnode_default_color(self):
        """Testa cor padrão dos nós."""
        task = Task(pid=1)
        node = RBNode(task)  # Sem especificar cor
        
        assert node.color == "RED"  # Cor padrão


def test_cfs_workload_characteristics():
    """Testa características da carga de trabalho do CFS."""
    
    # O CFS tem uma carga de trabalho write-heavy
    # Vamos simular isso conceitualmente
    
    # Em um tick típico do CFS:
    operations_per_tick = {
        "read": 1,      # Selecionar próxima tarefa
        "write": 2      # Remover tarefa + reinserir tarefa
    }
    
    total_operations = operations_per_tick["read"] + operations_per_tick["write"]
    write_ratio = operations_per_tick["write"] / total_operations
    
    # O CFS deve ter uma razão write-heavy
    assert write_ratio > 0.5, "CFS deve ter carga write-heavy"
    assert write_ratio == 2/3, "CFS deve ter 66% de operações de escrita"


def test_red_black_vs_avl_for_cfs():
    """Testa por que Red-Black Trees são preferidas no CFS."""
    
    # Características da carga de trabalho do CFS:
    cfs_characteristics = {
        "write_heavy": True,
        "frequent_rotations": False,  # Red-Black tem menos rotações
        "predictable_performance": True,
        "system_critical": True
    }
    
    # Red-Black Trees são adequadas para:
    rb_advantages = {
        "less_rotations": True,
        "predictable_height": True,
        "good_write_performance": True
    }
    
    # AVL Trees seriam menos adequadas para:
    avl_disadvantages = {
        "more_rotations": True,
        "higher_write_overhead": True
    }
    
    # Verificar que Red-Black é a escolha correta para CFS
    assert cfs_characteristics["write_heavy"] == rb_advantages["good_write_performance"]
    assert cfs_characteristics["frequent_rotations"] != rb_advantages["less_rotations"]


if __name__ == "__main__":
    print("🧪 Executando testes do CFS Scheduler Simulation")
    print("=" * 50)
    
    # Executar testes básicos
    test_cfs_workload_characteristics()
    test_red_black_vs_avl_for_cfs()
    
    print("✅ Testes conceituais passaram!")
    print("\n📝 Nota: Os testes de implementação falharão até que as funções sejam implementadas.")
    print("   Isso é esperado e demonstra que o desafio está pronto para implementação.") 