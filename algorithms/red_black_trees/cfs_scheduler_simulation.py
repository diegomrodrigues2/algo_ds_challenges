from __future__ import annotations
from typing import Optional, List
import time


class Task:
    """Representa uma tarefa no sistema, similar ao sched_entity do CFS."""
    
    def __init__(self, pid: int, priority: int = 0):
        self.pid = pid
        self.priority = priority
        self.vruntime = 0.0  # Tempo de execução virtual
        self.sum_exec_runtime = 0.0  # Tempo total de execução
        self.weight = 1024  # Peso da tarefa (nice level)


class RBNode:
    """Nó da árvore Red-Black para simular o CFS."""
    
    def __init__(self, task: Task, color: str = "RED"):
        self.task = task
        self.color = color
        self.left: Optional[RBNode] = None
        self.right: Optional[RBNode] = None
        self.parent: Optional[RBNode] = None


class CFSScheduler:
    """Simulação do Completely Fair Scheduler usando Red-Black Trees.
    
    Esta implementação simula o comportamento do CFS do Linux kernel,
    demonstrando por que Red-Black Trees são preferidas para cargas
    write-heavy como agendamento de tarefas.
    """
    
    def __init__(self):
        self.root: Optional[RBNode] = None
        self.nr_running = 0
        self.min_vruntime = 0.0
        self.leftmost: Optional[RBNode] = None
    
    def add_task(self, task: Task) -> None:
        """Adiciona uma tarefa à fila de execução (quando se torna executável).
        
        Esta operação simula quando uma tarefa bloqueada se torna executável
        e precisa ser adicionada à árvore Red-Black ordenada por vruntime.
        
        Args:
            task: Tarefa a ser adicionada
        """
        raise NotImplementedError("Implementar esta função")
    
    def remove_task(self, task: Task) -> None:
        """Remove uma tarefa da fila de execução (quando bloqueia).
        
        Esta operação simula quando uma tarefa bloqueia por I/O ou
        por outro motivo e precisa ser removida da árvore.
        
        Args:
            task: Tarefa a ser removida
        """
        raise NotImplementedError("Implementar esta função")
    
    def pick_next_task(self) -> Optional[Task]:
        """Seleciona a próxima tarefa para execução (menor vruntime).
        
        Esta operação simula a seleção da tarefa com menor vruntime,
        que é o nó mais à esquerda da árvore Red-Black.
        
        Returns:
            Tarefa com menor vruntime ou None se não há tarefas
        """
        raise NotImplementedError("Implementar esta função")
    
    def update_task_runtime(self, task: Task, exec_time: float) -> None:
        """Atualiza o vruntime de uma tarefa após execução.
        
        Esta operação simula o que acontece após uma tarefa executar:
        1. Remove a tarefa da árvore
        2. Atualiza seu vruntime
        3. Reinsere a tarefa na árvore
        
        Args:
            task: Tarefa que executou
            exec_time: Tempo de execução real
        """
        raise NotImplementedError("Implementar esta função")
    
    def get_scheduler_stats(self) -> dict:
        """Retorna estatísticas do agendador para análise de performance.
        
        Returns:
            Dicionário com estatísticas do agendador
        """
        return {
            "nr_running": self.nr_running,
            "min_vruntime": self.min_vruntime,
            "has_leftmost": self.leftmost is not None
        }


def simulate_cfs_workload(scheduler: CFSScheduler, num_tasks: int, 
                         simulation_ticks: int) -> dict:
    """Simula uma carga de trabalho típica do CFS.
    
    Esta função demonstra o padrão write-heavy do CFS:
    - Muitas operações de inserção/remoção
    - Atualizações frequentes de vruntime
    - Seleção constante da próxima tarefa
    
    Args:
        scheduler: Instância do agendador CFS
        num_tasks: Número de tarefas para simular
        simulation_ticks: Número de ticks de simulação
        
    Returns:
        Estatísticas da simulação
    """
    # Criar tarefas
    tasks = [Task(pid=i) for i in range(num_tasks)]
    
    # Adicionar todas as tarefas
    for task in tasks:
        scheduler.add_task(task)
    
    # Simular execução
    start_time = time.time()
    
    for tick in range(simulation_ticks):
        # Selecionar próxima tarefa (read operation)
        next_task = scheduler.pick_next_task()
        
        if next_task:
            # Simular execução
            exec_time = 0.001  # 1ms de execução
            
            # Atualizar vruntime (write operations)
            scheduler.update_task_runtime(next_task, exec_time)
            
            # Simular bloqueio ocasional (10% das vezes)
            if tick % 10 == 0:
                scheduler.remove_task(next_task)
                # Reativar após alguns ticks
                if tick % 20 == 0:
                    scheduler.add_task(next_task)
    
    end_time = time.time()
    
    return {
        "simulation_time": end_time - start_time,
        "total_ticks": simulation_ticks,
        "final_stats": scheduler.get_scheduler_stats()
    }


def compare_with_avl_simulation() -> dict:
    """Compara performance do CFS com Red-Black vs AVL Trees.
    
    Esta função demonstra por que Red-Black Trees são preferidas
    no CFS real do Linux kernel.
    
    Returns:
        Comparação de performance entre as duas estruturas
    """
    # Simular com Red-Black Trees (implementação atual)
    rb_scheduler = CFSScheduler()
    rb_stats = simulate_cfs_workload(rb_scheduler, num_tasks=100, 
                                   simulation_ticks=10000)
    
    # Nota: AVL simulation seria similar mas com mais rotações
    # Na implementação real, AVL teria mais overhead
    
    return {
        "red_black_performance": rb_stats,
        "note": "AVL trees would have more rotations, making them slower for this write-heavy workload"
    }


# Casos de teste para demonstrar o comportamento do CFS
def test_cfs_basic_operations():
    """Testa operações básicas do CFS."""
    scheduler = CFSScheduler()
    
    # Criar tarefas
    task1 = Task(pid=1, priority=0)
    task2 = Task(pid=2, priority=0)
    task3 = Task(pid=3, priority=0)
    
    # Adicionar tarefas
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)
    
    # Verificar seleção
    next_task = scheduler.pick_next_task()
    assert next_task is not None, "Deve haver uma tarefa para executar"
    
    # Simular execução
    scheduler.update_task_runtime(next_task, 0.001)
    
    # Verificar que vruntime foi atualizado
    assert next_task.vruntime > 0, "vruntime deve ser atualizado após execução"
    
    print("✅ Teste básico do CFS passou!")


def test_cfs_workload_simulation():
    """Testa simulação de carga de trabalho do CFS."""
    scheduler = CFSScheduler()
    
    # Simular carga de trabalho
    stats = simulate_cfs_workload(scheduler, num_tasks=10, simulation_ticks=100)
    
    # Verificar que a simulação completou
    assert stats["total_ticks"] == 100, "Simulação deve completar todos os ticks"
    assert stats["simulation_time"] > 0, "Tempo de simulação deve ser positivo"
    
    print("✅ Teste de simulação do CFS passou!")
    print(f"📊 Estatísticas: {stats}")


if __name__ == "__main__":
    print("🐧 Simulação do CFS (Completely Fair Scheduler)")
    print("=" * 50)
    
    # Executar testes
    test_cfs_basic_operations()
    test_cfs_workload_simulation()
    
    print("\n🎯 Este desafio demonstra por que Red-Black Trees são usadas no CFS:")
    print("   - Carga de trabalho write-heavy (inserção/remoção frequente)")
    print("   - Menos rotações que AVL Trees")
    print("   - Performance previsível para agendamento crítico")
    print("   - Adequada para software de sistema") 