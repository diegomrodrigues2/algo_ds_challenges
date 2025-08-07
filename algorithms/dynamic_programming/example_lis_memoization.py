"""
Exemplo de Demonstração: LIS com Memoização

Este exemplo demonstra como usar a implementação do Desafio 23:
LIS (Longest Increasing Subsequence) com Memoização, mostrando a transição de
backtracking exponencial O(2^n) para programação dinâmica O(n²).

Referências:
- Erickson, "Algorithms", Capítulo 3, Seção 3.6, "First Recurrence: Is This Next?"
- GeeksforGeeks: https://www.geeksforgeeks.org/dsa/longest-increasing-subsequence-dp-3/
"""

from lis_memoization import (
    lis_memoization,
    lis_backtracking,
    lis_tabulation,
    lis_binary_search,
    compare_lis_approaches,
    analyze_lis_complexity,
    benchmark_lis_performance
)
import time


def demonstrate_basic_usage():
    """Demonstra o uso básico do LIS."""
    print("=== Demonstração Básica: LIS ===\n")
    
    # Casos de teste clássicos
    test_cases = [
        [3, 10, 2, 1, 20],
        [10, 22, 9, 33, 21, 50, 41, 60],
        [30, 20, 10],
        [10, 20, 35, 80],
        [2, 2, 2]
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"Caso {i}: {arr}")
        lis_length = lis_memoization(arr)
        print(f"  Comprimento da LIS: {lis_length}")
        
        # Análise da subsequência
        if lis_length == 1:
            print(f"  Análise: Array decrescente ou elementos iguais")
        elif lis_length == len(arr):
            print(f"  Análise: Array já está em ordem crescente")
        else:
            print(f"  Análise: {lis_length}/{len(arr)} elementos na LIS")
        print()


def demonstrate_performance_comparison():
    """Demonstra a comparação de performance entre diferentes abordagens."""
    print("=== Comparação de Performance ===\n")
    
    # Caso de teste que mostra a diferença de performance
    arr = [5, 1, 6, 2, 7, 3, 8, 4, 9]  # LIS = [1, 2, 3, 4, 9]
    
    print(f"Array: {arr}")
    print(f"Tamanho: {len(arr)}")
    print()
    
    # Compara todas as abordagens
    comparison = compare_lis_approaches(arr)
    
    print("Resultados:")
    for approach, data in comparison['approaches'].items():
        print(f"  {approach.title()}:")
        print(f"    Resultado: {data['result']}")
        print(f"    Tempo: {data['time']:.6f}s")
        print(f"    Complexidade: {data['complexity']}")
        print(f"    Espaço: {data['space']}")
        print()
    
    print("Melhorias de Performance:")
    for improvement, ratio in comparison['performance_improvement'].items():
        print(f"  {improvement}: {ratio}")
    print()


def demonstrate_complexity_analysis():
    """Demonstra a análise de complexidade."""
    print("=== Análise de Complexidade ===\n")
    
    # Analisa diferentes tamanhos de entrada
    sizes = [10, 50, 100, 200]
    
    for size in sizes:
        analysis = analyze_lis_complexity(size)
        
        print(f"Array de tamanho {size}:")
        print(f"  Complexidade: {analysis['complexity_class']}")
        print(f"  Espaço: {analysis['space_complexity']}")
        print(f"  Melhoria: {analysis['memoization_benefit']}")
        print(f"  Viabilidade: {analysis['practical_viability']}")
        print()
    
    # Mostra análise detalhada para um caso específico
    detailed_analysis = analyze_lis_complexity(100)
    print("Análise Detalhada (n=100):")
    print(f"  Definição do estado: {detailed_analysis['subproblem_analysis']['state_definition']}")
    print(f"  Número de estados: {detailed_analysis['subproblem_analysis']['state_count']}")
    print(f"  Subproblemas sobrepostos: {detailed_analysis['subproblem_analysis']['overlapping_subproblems']}")
    print(f"  Estrutura ótima: {detailed_analysis['subproblem_analysis']['optimal_substructure']}")
    print()
    
    print("Técnicas de Otimização:")
    for technique in detailed_analysis['optimization_techniques']:
        print(f"  • {technique}")
    print()
    
    print("Otimizações Futuras:")
    for optimization in detailed_analysis['further_optimizations']:
        print(f"  • {optimization}")
    print()
    
    print("Limitações:")
    for limitation in detailed_analysis['limitations']:
        print(f"  • {limitation}")
    print()


def demonstrate_lis_variations():
    """Demonstra diferentes variações do problema LIS."""
    print("=== Variações do Problema LIS ===\n")
    
    # Array exemplo
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Array base: {arr}")
    print(f"LIS básica: {lis_memoization(arr)}")
    print()
    
    # Diferentes cenários
    scenarios = [
        {
            'name': 'Array Ordenado',
            'array': sorted(arr),
            'description': 'Todo o array é uma LIS'
        },
        {
            'name': 'Array Reverso',
            'array': sorted(arr, reverse=True),
            'description': 'Apenas um elemento forma LIS'
        },
        {
            'name': 'Elementos Duplicados',
            'array': [1, 2, 2, 3, 3, 4],
            'description': 'LIS estritamente crescente'
        },
        {
            'name': 'Valores Negativos',
            'array': [-5, -1, -3, 0, 2, -2, 3],
            'description': 'LIS com números negativos e positivos'
        }
    ]
    
    for scenario in scenarios:
        print(f"{scenario['name']}:")
        print(f"  Array: {scenario['array']}")
        print(f"  LIS: {lis_memoization(scenario['array'])}")
        print(f"  Descrição: {scenario['description']}")
        print()


def demonstrate_memoization_benefits():
    """Demonstra os benefícios específicos da memoização."""
    print("=== Benefícios da Memoização ===\n")
    
    # Array que força muitos subproblemas sobrepostos
    arr = [1, 5, 2, 6, 3, 7, 4, 8, 1, 9]
    
    print(f"Array com subproblemas sobrepostos: {arr}")
    print()
    
    # Múltiplas execuções para demonstrar cache
    print("Executando múltiplas vezes para demonstrar cache:")
    
    times = []
    for i in range(5):
        start_time = time.time()
        result = lis_memoization(arr)
        execution_time = time.time() - start_time
        times.append(execution_time)
        
        print(f"  Execução {i+1}: {execution_time:.6f}s (LIS = {result})")
    
    print(f"\nTempo médio: {sum(times)/len(times):.6f}s")
    print(f"Tempo mínimo: {min(times):.6f}s")
    print(f"Tempo máximo: {max(times):.6f}s")
    
    print("\nObservação: As execuções subsequentes podem ser mais rápidas")
    print("devido ao aquecimento do interpretador Python, não apenas cache.")


def demonstrate_real_world_scenarios():
    """Demonstra cenários do mundo real."""
    print("=== Cenários do Mundo Real ===\n")
    
    # Cenário 1: Preços de ações
    print("1. Análise de Preços de Ações:")
    stock_prices = [100, 80, 60, 70, 60, 75, 85]
    print(f"   Preços diários: {stock_prices}")
    lis_length = lis_memoization(stock_prices)
    print(f"   Maior sequência de alta: {lis_length} dias")
    print(f"   Interpretação: Período mais longo de crescimento contínuo")
    print()
    
    # Cenário 2: Notas de estudante
    print("2. Progresso Acadêmico:")
    grades = [6.5, 7.0, 6.8, 7.5, 8.0, 7.2, 8.5, 9.0]
    print(f"   Notas semestrais: {grades}")
    lis_length = lis_memoization([int(g*10) for g in grades])  # Converte para int
    print(f"   Sequência de melhoria: {lis_length} semestres")
    print(f"   Interpretação: Maior período de progresso contínuo")
    print()
    
    # Cenário 3: Crescimento populacional
    print("3. Crescimento Populacional (em milhares):")
    population = [120, 125, 130, 128, 135, 140, 138, 145, 150]
    print(f"   População anual: {population}")
    lis_length = lis_memoization(population)
    print(f"   Período de crescimento: {lis_length} anos")
    print(f"   Interpretação: Maior período de crescimento sustentado")
    print()
    
    # Cenário 4: Tempos de corrida
    print("4. Tempos de Corrida (em segundos, menor é melhor):")
    race_times = [180, 175, 170, 172, 168, 165, 167, 160]
    # Para tempos, queremos subsequência decrescente, então invertemos
    inverted_times = [-t for t in race_times]
    lis_length = lis_memoization(inverted_times)
    print(f"   Tempos por corrida: {race_times}")
    print(f"   Sequência de melhoria: {lis_length} corridas")
    print(f"   Interpretação: Maior período de melhoria contínua")


def main():
    """Função principal que executa todas as demonstrações."""
    print("Desafio 23: LIS (Longest Increasing Subsequence) com Memoização")
    print("=" * 70)
    print()
    
    # Executa todas as demonstrações
    demonstrate_basic_usage()
    demonstrate_performance_comparison()
    demonstrate_complexity_analysis()
    demonstrate_lis_variations()
    demonstrate_memoization_benefits()
    demonstrate_real_world_scenarios()
    
    print("=" * 70)
    print("Demonstração concluída!")
    print()
    print("Principais conceitos demonstrados:")
    print("• Transição de O(2^n) para O(n²) com memoização")
    print("• Estado do subproblema: (índice_atual, índice_anterior)")
    print("• Subproblemas sobrepostos e estrutura ótima")
    print("• Benefícios práticos da programação dinâmica")
    print("• Aplicações em cenários do mundo real")
    print("• Formulação LISbigger(i, j) de Erickson")


if __name__ == "__main__":
    main()