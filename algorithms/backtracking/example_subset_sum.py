#!/usr/bin/env python3
"""
Exemplo de uso do algoritmo Subset Sum.
"""

def subset_sum_backtracking(numbers, target):
    """Implementação básica do Subset Sum."""
    if not numbers or target < 0:
        return None
    
    sorted_numbers = sorted(numbers, reverse=True)
    
    def backtrack(index, current_sum, current_subset):
        if current_sum == target:
            return current_subset.copy()
        
        if current_sum > target or index >= len(sorted_numbers):
            return None
        
        remaining_sum = sum(sorted_numbers[index:])
        if current_sum + remaining_sum < target:
            return None
        
        current_subset.append(sorted_numbers[index])
        result = backtrack(index + 1, current_sum + sorted_numbers[index], current_subset)
        if result:
            return result
        
        current_subset.pop()
        return backtrack(index + 1, current_sum, current_subset)
    
    return backtrack(0, 0, [])

def main():
    """Função principal com exemplos."""
    print("=== Exemplo Subset Sum ===")
    
    # Exemplo 1: Caso simples
    numbers = [1, 2, 3, 4, 5]
    target = 7
    result = subset_sum_backtracking(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Resultado: {result}")
    print(f"Soma: {sum(result) if result else None}")
    print()
    
    # Exemplo 2: Caso sem solução
    numbers = [1, 2, 3, 4, 5]
    target = 20
    result = subset_sum_backtracking(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Resultado: {result}")
    print()
    
    # Exemplo 3: Caso do teste
    numbers = [3, 34, 4, 12, 5, 2]
    target = 9
    result = subset_sum_backtracking(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Resultado: {result}")
    print(f"Soma: {sum(result) if result else None}")
    print()
    
    # Exemplo 4: Com duplicatas
    numbers = [1, 1, 2, 2, 3]
    target = 3
    result = subset_sum_backtracking(numbers, target)
    print(f"Números: {numbers}")
    print(f"Target: {target}")
    print(f"Resultado: {result}")
    print(f"Soma: {sum(result) if result else None}")

if __name__ == "__main__":
    main() 