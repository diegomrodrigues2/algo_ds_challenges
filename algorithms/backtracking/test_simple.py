#!/usr/bin/env python3
"""
Script simples para testar o algoritmo Subset Sum.
"""

from subset_sum import (
    subset_sum_backtracking,
    subset_sum_backtracking_optimized,
    subset_sum_count_solutions,
    subset_sum_all_solutions
)

def test_basic():
    """Testa casos básicos."""
    print("=== Teste Básico ===")
    
    # Teste 1: Caso simples com solução
    numbers = [1, 2, 3, 4, 5]
    target = 7
    result = subset_sum_backtracking(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Resultado: {result}")
    print(f"Soma do resultado: {sum(result) if result else None}")
    print()
    
    # Teste 2: Caso sem solução
    numbers = [1, 2, 3, 4, 5]
    target = 20
    result = subset_sum_backtracking(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Resultado: {result}")
    print()
    
    # Teste 3: Caso do teste que falhou
    numbers = [3, 34, 4, 12, 5, 2]
    target = 9
    result = subset_sum_backtracking_optimized(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Resultado otimizado: {result}")
    print(f"Soma do resultado: {sum(result) if result else None}")
    print()

def test_count_solutions():
    """Testa contagem de soluções."""
    print("=== Teste Contagem de Soluções ===")
    
    numbers = [1, 2, 3, 4, 5]
    target = 7
    count = subset_sum_count_solutions(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Número de soluções: {count}")
    print()

def test_all_solutions():
    """Testa todas as soluções."""
    print("=== Teste Todas as Soluções ===")
    
    numbers = [1, 1, 2, 2, 3]
    target = 3
    solutions = subset_sum_all_solutions(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Número de soluções únicas: {len(solutions)}")
    for i, solution in enumerate(solutions):
        print(f"Solução {i+1}: {solution} (soma: {sum(solution)})")
    print()

if __name__ == "__main__":
    test_basic()
    test_count_solutions()
    test_all_solutions() 