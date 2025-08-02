"""
Exemplo de uso do módulo de geração de subconjuntos (subset_generation.py).

Este script demonstra como usar as diferentes funções implementadas
no módulo subset_generation.py, incluindo comparações de performance
e casos de uso práticos.
"""

import time
from subset_generation import (
    subset_generation_backtracking,
    subset_generation_iterative_bitmask,
    subset_generation_with_constraints,
    subset_generation_with_sum_constraint,
    subset_generation_with_memoization,
    subset_generation_lexicographic,
    subset_generation_count_only,
    subset_generation_with_duplicates,
    subset_generation_optimized,
    analyze_subset_generation_complexity,
    create_test_subsets
)


def demonstrate_basic_functionality():
    """Demonstra funcionalidade básica de geração de subconjuntos."""
    print("=== Demonstração: Funcionalidade Básica ===\n")
    
    # Teste com conjunto pequeno
    elements = [1, 2, 3]
    print(f"Elementos: {elements}")
    print(f"Número esperado de subconjuntos: {2**len(elements)}")
    
    # Backtracking
    subsets = subset_generation_backtracking(elements)
    print(f"\nSubconjuntos (backtracking): {subsets}")
    print(f"Total: {len(subsets)}")
    
    # Bitmask
    subsets_bitmask = subset_generation_iterative_bitmask(elements)
    print(f"\nSubconjuntos (bitmask): {subsets_bitmask}")
    print(f"Total: {len(subsets_bitmask)}")
    
    # Verificar se são iguais
    print(f"\nResultados idênticos: {subsets == subsets_bitmask}")
    
    # Contagem sem gerar
    count = subset_generation_count_only(elements)
    print(f"Contagem sem gerar: {count}")


def demonstrate_constraints():
    """Demonstra geração de subconjuntos com restrições."""
    print("\n=== Demonstração: Restrições ===\n")
    
    elements = [1, 2, 3, 4]
    print(f"Elementos: {elements}")
    
    # Restrições de tamanho
    print(f"\nSubconjuntos com tamanho 1-2:")
    size_constrained = subset_generation_with_constraints(elements, 1, 2)
    print(f"Resultado: {size_constrained}")
    print(f"Total: {len(size_constrained)}")
    
    # Restrições de soma
    target_sum = 5
    print(f"\nSubconjuntos que somam {target_sum}:")
    sum_constrained = subset_generation_with_sum_constraint(elements, target_sum)
    print(f"Resultado: {sum_constrained}")
    print(f"Total: {len(sum_constrained)}")
    
    # Verificar somas
    for subset in sum_constrained:
        actual_sum = sum(subset)
        print(f"  {subset} = {actual_sum}")


def demonstrate_duplicates():
    """Demonstra geração de subconjuntos com duplicatas."""
    print("\n=== Demonstração: Duplicatas ===\n")
    
    elements_with_duplicates = [1, 1, 2]
    print(f"Elementos com duplicatas: {elements_with_duplicates}")
    
    # Geração normal (pode ter duplicatas)
    normal_subsets = subset_generation_backtracking(elements_with_duplicates)
    print(f"\nSubconjuntos normais: {normal_subsets}")
    print(f"Total: {len(normal_subsets)}")
    
    # Geração com tratamento de duplicatas
    unique_subsets = subset_generation_with_duplicates(elements_with_duplicates)
    print(f"\nSubconjuntos únicos: {unique_subsets}")
    print(f"Total: {len(unique_subsets)}")
    
    # Verificar que não há duplicatas
    subset_strings = [str(sorted(subset)) for subset in unique_subsets]
    unique_strings = set(subset_strings)
    print(f"Subconjuntos únicos verificados: {len(unique_strings) == len(subset_strings)}")


def demonstrate_lexicographic():
    """Demonstra geração lexicográfica."""
    print("\n=== Demonstração: Ordem Lexicográfica ===\n")
    
    elements = [1, 2, 3]
    print(f"Elementos: {elements}")
    
    lexicographic_subsets = subset_generation_lexicographic(elements)
    print(f"Subconjuntos em ordem lexicográfica: {lexicographic_subsets}")
    
    # Verificar ordem
    print("\nVerificando ordem:")
    for i, subset in enumerate(lexicographic_subsets):
        print(f"  {i+1}. {subset}")


def demonstrate_memoization_benefits():
    """Demonstra os benefícios da memoização."""
    print("\n=== Demonstração: Benefícios da Memoização ===\n")
    
    elements = list(range(1, 6))  # [1, 2, 3, 4, 5]
    print(f"Elementos: {elements}")
    print(f"Número esperado de subconjuntos: {2**len(elements)}")
    
    # Medir tempo sem memoização
    start_time = time.time()
    basic_result = subset_generation_backtracking(elements)
    basic_time = time.time() - start_time
    
    # Medir tempo com memoização
    start_time = time.time()
    memo_result = subset_generation_with_memoization(elements)
    memo_time = time.time() - start_time
    
    print(f"Backtracking básico: {len(basic_result)} subconjuntos (tempo: {basic_time:.6f}s)")
    print(f"Com memoização: {len(memo_result)} subconjuntos (tempo: {memo_time:.6f}s)")
    if memo_time > 0:
        print(f"Speedup: {basic_time/memo_time:.2f}x")
    else:
        print("Speedup: N/A (memoized time too small to measure)")
    print(f"Resultados idênticos: {sorted(basic_result) == sorted(memo_result)}")


def demonstrate_performance_comparison():
    """Compara performance de diferentes implementações."""
    print("\n=== Demonstração: Comparação de Performance ===\n")
    
    test_cases = [
        ([1, 2, 3], "Pequeno"),
        ([1, 2, 3, 4], "Médio"),
        ([1, 2, 3, 4, 5], "Grande")
    ]
    
    for elements, size_name in test_cases:
        print(f"\n--- Teste {size_name} ({len(elements)} elementos) ---")
        print(f"Elementos: {elements}")
        print(f"Subconjuntos esperados: {2**len(elements)}")
        
        # Backtracking
        start_time = time.time()
        backtracking_result = subset_generation_backtracking(elements)
        backtracking_time = time.time() - start_time
        
        # Bitmask
        start_time = time.time()
        bitmask_result = subset_generation_iterative_bitmask(elements)
        bitmask_time = time.time() - start_time
        
        # Otimizado
        start_time = time.time()
        optimized_result = subset_generation_optimized(elements)
        optimized_time = time.time() - start_time
        
        print(f"Backtracking: {len(backtracking_result)} subconjuntos ({backtracking_time:.6f}s)")
        print(f"Bitmask: {len(bitmask_result)} subconjuntos ({bitmask_time:.6f}s)")
        print(f"Otimizado: {len(optimized_result)} subconjuntos ({optimized_time:.6f}s)")
        
        # Verificar correção
        all_correct = (
            len(backtracking_result) == len(bitmask_result) == 
            len(optimized_result) == 2**len(elements)
        )
        print(f"Todos corretos: {all_correct}")


def demonstrate_complexity_analysis():
    """Demonstra análise de complexidade."""
    print("\n=== Demonstração: Análise de Complexidade ===\n")
    
    elements = [1, 2, 3, 4]
    print(f"Elementos: {elements}")
    
    analysis = analyze_subset_generation_complexity(elements)
    
    print("Resultados da análise:")
    print(f"  Tamanho da entrada: {analysis['input_size']}")
    print(f"  Subconjuntos esperados: {analysis['expected_count']}")
    print(f"  Subconjuntos gerados: {analysis['actual_count']}")
    print(f"  Todos corretos: {analysis['all_correct']}")
    print(f"  Tempo backtracking: {analysis['backtracking_time']:.6f}s")
    print(f"  Tempo bitmask: {analysis['bitmask_time']:.6f}s")
    print(f"  Tempo memoização: {analysis['memo_time']:.6f}s")
    print(f"  Tempo otimizado: {analysis['optimized_time']:.6f}s")
    
    # Encontrar o mais rápido
    times = {
        'Backtracking': analysis['backtracking_time'],
        'Bitmask': analysis['bitmask_time'],
        'Memoização': analysis['memo_time'],
        'Otimizado': analysis['optimized_time']
    }
    
    fastest = min(times, key=times.get)
    print(f"\nMais rápido: {fastest} ({times[fastest]:.6f}s)")


def demonstrate_test_cases():
    """Demonstra casos de teste."""
    print("\n=== Demonstração: Casos de Teste ===\n")
    
    test_cases = create_test_subsets()
    print(f"Total de casos de teste: {len(test_cases)}")
    
    for i, test_case in enumerate(test_cases):
        print(f"\nCaso {i+1}: {test_case}")
        if test_case:
            count = subset_generation_count_only(test_case)
            print(f"  Subconjuntos esperados: {count}")
            
            # Para casos pequenos, mostrar alguns subconjuntos
            if len(test_case) <= 4:
                subsets = subset_generation_backtracking(test_case)
                print(f"  Primeiros 5 subconjuntos: {subsets[:5]}")
                if len(subsets) > 5:
                    print(f"  ... e mais {len(subsets) - 5} subconjuntos")


def demonstrate_practical_applications():
    """Demonstra aplicações práticas."""
    print("\n=== Demonstração: Aplicações Práticas ===\n")
    
    # Exemplo 1: Seleção de itens com orçamento
    items = [('laptop', 1000), ('phone', 500), ('tablet', 300), ('watch', 200)]
    budget = 1200
    
    print("Exemplo 1: Seleção de itens com orçamento")
    print(f"Itens: {items}")
    print(f"Orçamento: ${budget}")
    
    # Extrair preços
    prices = [price for _, price in items]
    names = [name for name, _ in items]
    
    # Encontrar combinações que cabem no orçamento
    valid_combinations = subset_generation_with_sum_constraint(prices, budget)
    
    print(f"\nCombinações válidas:")
    for combination in valid_combinations:
        total_cost = sum(combination)
        item_names = [names[prices.index(price)] for price in combination]
        print(f"  {item_names} = ${total_cost}")
    
    # Exemplo 2: Seleção de equipes
    players = ['Alice', 'Bob', 'Charlie', 'Diana']
    min_team_size = 2
    max_team_size = 3
    
    print(f"\nExemplo 2: Seleção de equipes")
    print(f"Jogadores: {players}")
    print(f"Tamanho da equipe: {min_team_size}-{max_team_size}")
    
    teams = subset_generation_with_constraints(players, min_team_size, max_team_size)
    
    print(f"\nEquipes possíveis:")
    for team in teams:
        print(f"  {team}")


def main():
    """Função principal que executa todas as demonstrações."""
    print("=== Demonstração Completa: Geração de Subconjuntos ===\n")
    
    try:
        demonstrate_basic_functionality()
        demonstrate_constraints()
        demonstrate_duplicates()
        demonstrate_lexicographic()
        demonstrate_memoization_benefits()
        demonstrate_performance_comparison()
        demonstrate_complexity_analysis()
        demonstrate_test_cases()
        demonstrate_practical_applications()
        
        print("\n=== Demonstração Concluída ===")
        print("Todos os testes foram executados com sucesso!")
        
    except Exception as e:
        print(f"\nErro durante a demonstração: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 