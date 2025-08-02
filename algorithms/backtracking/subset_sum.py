"""
Subset Sum Problem - Backtracking Implementation

Este módulo implementa o algoritmo de Soma de Subconjuntos (Subset Sum)
usando backtracking recursivo. O problema é NP-completo, mas a solução
de backtracking explora todas as possibilidades de forma sistemática.

Referências:
- Erickson, "Algorithms", Capítulo 2, Seção 2.3, "Subset Sum"
- https://github.com/parthnan/SubsetSum-BacktrackAlgorithm
- https://courses.grainger.illinois.edu/cs473/sp2010/notes/02-backtracking.pdf
"""

from typing import List, Optional, Tuple


def subset_sum_backtracking(numbers: List[int], target: int) -> Optional[List[int]]:
    """
    Resolve o problema Subset Sum usando backtracking recursivo.
    
    Para cada elemento, a recursão decide se incluí-lo ou não no subconjunto.
    Isso cria uma árvore de decisão binária de profundidade n.
    
    Args:
        numbers: Lista de inteiros positivos
        target: Soma alvo a ser encontrada
        
    Returns:
        Lista com os elementos que somam target, ou None se não existir solução
        
    Complexidade:
        Tempo: O(2^n) - explora todos os 2^n subconjuntos possíveis
        Espaço: O(n) - profundidade da pilha de recursão
    """
    if not numbers or target < 0:
        return None
    
    # Ordena os números em ordem decrescente para otimização
    sorted_numbers = sorted(numbers, reverse=True)
    
    def backtrack(index: int, current_sum: int, current_subset: List[int]) -> Optional[List[int]]:
        """
        Função recursiva de backtracking.
        
        Args:
            index: Índice atual no array de números
            current_sum: Soma atual dos elementos selecionados
            current_subset: Subconjunto atual sendo construído
            
        Returns:
            Subconjunto válido ou None
        """
        # Caso base: encontrou uma solução
        if current_sum == target:
            return current_subset.copy()
        
        # Caso base: passou do target ou chegou ao fim
        if current_sum > target or index >= len(sorted_numbers):
            return None
        
        # Otimização: se a soma atual + soma dos elementos restantes < target
        remaining_sum = sum(sorted_numbers[index:])
        if current_sum + remaining_sum < target:
            return None
        
        # Tenta incluir o elemento atual
        current_subset.append(sorted_numbers[index])
        result = backtrack(index + 1, current_sum + sorted_numbers[index], current_subset)
        if result:
            return result
        
        # Backtrack: remove o elemento e tenta sem ele
        current_subset.pop()
        return backtrack(index + 1, current_sum, current_subset)
    
    return backtrack(0, 0, [])


def subset_sum_backtracking_optimized(numbers: List[int], target: int) -> Optional[List[int]]:
    """
    Versão otimizada do Subset Sum com podas adicionais.
    
    Otimizações:
    1. Ordenação decrescente para encontrar soluções mais rapidamente
    2. Poda por soma restante
    3. Early termination quando possível
    
    Args:
        numbers: Lista de inteiros positivos
        target: Soma alvo a ser encontrada
        
    Returns:
        Lista com os elementos que somam target, ou None se não existir solução
    """
    if not numbers or target < 0:
        return None
    
    # Ordena em ordem decrescente (mantém duplicatas)
    sorted_numbers = sorted(numbers, reverse=True)
    
    # Calcula soma total para poda
    total_sum = sum(sorted_numbers)
    
    # Se o target é maior que a soma total, não há solução
    if target > total_sum:
        return None
    
    # Se o target é igual à soma total, retorna todos os elementos
    if target == total_sum:
        return sorted_numbers.copy()
    
    def backtrack_optimized(index: int, current_sum: int, current_subset: List[int]) -> Optional[List[int]]:
        """
        Função recursiva otimizada de backtracking.
        """
        # Caso base: encontrou uma solução
        if current_sum == target:
            return current_subset.copy()
        
        # Caso base: passou do target
        if current_sum > target:
            return None
        
        # Caso base: chegou ao fim
        if index >= len(sorted_numbers):
            return None
        
        # Poda: se não é possível alcançar o target com os elementos restantes
        remaining_sum = sum(sorted_numbers[index:])
        if current_sum + remaining_sum < target:
            return None
        
        # Poda: se o elemento atual é maior que o que falta
        if sorted_numbers[index] > target - current_sum:
            return None
        
        # Tenta incluir o elemento atual
        current_subset.append(sorted_numbers[index])
        result = backtrack_optimized(index + 1, current_sum + sorted_numbers[index], current_subset)
        if result:
            return result
        
        # Backtrack: remove o elemento e tenta sem ele
        current_subset.pop()
        return backtrack_optimized(index + 1, current_sum, current_subset)
    
    return backtrack_optimized(0, 0, [])


def subset_sum_count_solutions(numbers: List[int], target: int) -> int:
    """
    Conta quantas soluções existem para o problema Subset Sum.
    
    Args:
        numbers: Lista de inteiros positivos
        target: Soma alvo a ser encontrada
        
    Returns:
        Número de soluções distintas
    """
    if not numbers or target < 0:
        return 0
    
    sorted_numbers = sorted(numbers, reverse=True)
    count = 0
    
    def backtrack_count(index: int, current_sum: int) -> None:
        """
        Função recursiva para contar soluções.
        """
        nonlocal count
        
        # Caso base: encontrou uma solução
        if current_sum == target:
            count += 1
            return
        
        # Caso base: passou do target ou chegou ao fim
        if current_sum > target or index >= len(sorted_numbers):
            return
        
        # Poda: se não é possível alcançar o target
        remaining_sum = sum(sorted_numbers[index:])
        if current_sum + remaining_sum < target:
            return
        
        # Inclui o elemento atual
        backtrack_count(index + 1, current_sum + sorted_numbers[index])
        
        # Não inclui o elemento atual
        backtrack_count(index + 1, current_sum)
    
    backtrack_count(0, 0)
    return count


def subset_sum_all_solutions(numbers: List[int], target: int) -> List[List[int]]:
    """
    Encontra todas as soluções para o problema Subset Sum.
    
    Args:
        numbers: Lista de inteiros positivos
        target: Soma alvo a ser encontrada
        
    Returns:
        Lista de todas as soluções (cada solução é uma lista de elementos)
    """
    if not numbers or target < 0:
        return []
    
    sorted_numbers = sorted(numbers, reverse=True)
    solutions = []
    
    def backtrack_all(index: int, current_sum: int, current_subset: List[int]) -> None:
        """
        Função recursiva para encontrar todas as soluções.
        """
        # Caso base: encontrou uma solução
        if current_sum == target:
            solutions.append(current_subset.copy())
            return
        
        # Caso base: passou do target ou chegou ao fim
        if current_sum > target or index >= len(sorted_numbers):
            return
        
        # Poda: se não é possível alcançar o target
        remaining_sum = sum(sorted_numbers[index:])
        if current_sum + remaining_sum < target:
            return
        
        # Inclui o elemento atual
        current_subset.append(sorted_numbers[index])
        backtrack_all(index + 1, current_sum + sorted_numbers[index], current_subset)
        current_subset.pop()
        
        # Não inclui o elemento atual
        backtrack_all(index + 1, current_sum, current_subset)
    
    backtrack_all(0, 0, [])
    
    # Remove soluções duplicadas (mesma soma, mesma composição)
    unique_solutions = []
    seen = set()
    
    for solution in solutions:
        # Ordena a solução para normalizar
        sorted_solution = tuple(sorted(solution))
        if sorted_solution not in seen:
            seen.add(sorted_solution)
            unique_solutions.append(solution)
    
    return unique_solutions


def analyze_subset_sum_complexity(numbers: List[int], target: int) -> dict:
    """
    Analisa a complexidade do problema Subset Sum para os dados fornecidos.
    
    Args:
        numbers: Lista de inteiros positivos
        target: Soma alvo a ser encontrada
        
    Returns:
        Dicionário com métricas de complexidade
    """
    n = len(numbers)
    total_sum = sum(numbers)
    
    analysis = {
        'n': n,
        'target': target,
        'total_sum': total_sum,
        'max_possible_subsets': 2 ** n,
        'target_ratio': target / total_sum if total_sum > 0 else 0,
        'is_feasible': target <= total_sum,
        'estimated_complexity': 'O(2^n)',
        'space_complexity': 'O(n)'
    }
    
    # Análise de podas possíveis
    sorted_numbers = sorted(numbers, reverse=True)
    pruning_opportunities = 0
    
    for i, num in enumerate(sorted_numbers):
        if num > target:
            pruning_opportunities += 1
    
    analysis['pruning_opportunities'] = pruning_opportunities
    analysis['early_termination_possible'] = target == total_sum or target == 0
    
    return analysis


def subset_sum_with_memoization(numbers: List[int], target: int) -> Optional[List[int]]:
    """
    Versão com memoização para evitar recálculos.
    
    Nota: Esta implementação usa mais memória (O(n*target)) mas pode ser
    mais eficiente para problemas com muitas subestruturas sobrepostas.
    
    Args:
        numbers: Lista de inteiros positivos
        target: Soma alvo a ser encontrada
        
    Returns:
        Lista com os elementos que somam target, ou None se não existir solução
    """
    if not numbers or target < 0:
        return None
    
    # Ordena em ordem decrescente (mantém duplicatas)
    sorted_numbers = sorted(numbers, reverse=True)
    
    # Memoização: (index, current_sum) -> resultado
    memo = {}
    
    def backtrack_memoized(index: int, current_sum: int, current_subset: List[int]) -> Optional[List[int]]:
        """
        Função recursiva com memoização.
        """
        # Verifica memoização
        key = (index, current_sum)
        if key in memo:
            if memo[key] is None:
                return None
            else:
                # Reconstrói o subconjunto a partir do resultado memoizado
                return memo[key].copy()
        
        # Caso base: encontrou uma solução
        if current_sum == target:
            memo[key] = current_subset.copy()
            return current_subset.copy()
        
        # Caso base: passou do target ou chegou ao fim
        if current_sum > target or index >= len(sorted_numbers):
            memo[key] = None
            return None
        
        # Poda: se não é possível alcançar o target
        remaining_sum = sum(sorted_numbers[index:])
        if current_sum + remaining_sum < target:
            memo[key] = None
            return None
        
        # Tenta incluir o elemento atual
        current_subset.append(sorted_numbers[index])
        result = backtrack_memoized(index + 1, current_sum + sorted_numbers[index], current_subset)
        if result:
            memo[key] = result
            return result
        
        # Backtrack: remove o elemento e tenta sem ele
        current_subset.pop()
        result = backtrack_memoized(index + 1, current_sum, current_subset)
        memo[key] = result
        return result
    
    return backtrack_memoized(0, 0, [])


# Funções auxiliares para demonstração e análise
def demonstrate_subset_sum_example():
    """
    Demonstra o uso do algoritmo Subset Sum com exemplos.
    """
    examples = [
        ([1, 2, 3, 4, 5], 7),
        ([3, 34, 4, 12, 5, 2], 9),
        ([1, 2, 3, 4, 5], 15),
        ([1, 2, 3, 4, 5], 20),  # Sem solução
        ([1, 1, 1, 1, 1], 3),
        ([10, 20, 30, 40, 50], 100),
    ]
    
    print("=== Demonstração Subset Sum ===")
    
    for numbers, target in examples:
        print(f"\nNúmeros: {numbers}")
        print(f"Target: {target}")
        
        # Solução básica
        solution = subset_sum_backtracking(numbers, target)
        print(f"Solução: {solution}")
        
        # Contagem de soluções
        count = subset_sum_count_solutions(numbers, target)
        print(f"Número de soluções: {count}")
        
        # Análise de complexidade
        analysis = analyze_subset_sum_complexity(numbers, target)
        print(f"Análise: {analysis}")


if __name__ == "__main__":
    demonstrate_subset_sum_example() 