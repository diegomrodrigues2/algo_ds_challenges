"""
Exemplo de Demonstração: Segmentação de Texto com Memoização

Este exemplo demonstra como usar a implementação do Desafio 22:
Segmentação de Texto com Memoização, mostrando a transição de
backtracking exponencial O(2^n) para programação dinâmica O(n²).

Referências:
- Erickson, "Algorithms", Capítulo 3, Seção 3.3, "Interpunctio Verborum Redux"
- GeeksforGeeks: https://www.geeksforgeeks.org/dsa/word-break-problem-dp-32/
"""

from text_segmentation_memoization import (
    text_segmentation_memoization,
    text_segmentation_backtracking,
    text_segmentation_tabulation,
    text_segmentation_optimized_memoization,
    compare_approaches,
    analyze_text_segmentation_complexity,
    benchmark_performance
)
import time


def demonstrate_basic_usage():
    """Demonstra o uso básico da segmentação de texto."""
    print("=== Demonstração Básica: Segmentação de Texto ===\n")
    
    # Dicionário de palavras válidas
    dictionary = {"i", "like", "gfg", "programming", "algorithms"}
    
    # Casos de teste
    test_cases = [
        "ilike",
        "ilikegfg", 
        "ilikeprogramming",
        "ilikemangoes"
    ]
    
    for text in test_cases:
        print(f"Texto: '{text}'")
        result = text_segmentation_memoization(text, dictionary)
        
        if result:
            print(f"Segmentação: {' '.join(result)}")
        else:
            print("Não é possível segmentar")
        print()


def demonstrate_performance_comparison():
    """Demonstra a comparação de performance entre diferentes abordagens."""
    print("=== Comparação de Performance ===\n")
    
    # Caso de teste que mostra a diferença de performance
    text = "aaaaaaaaaaaaaaaaaaaa"  # 20 'a's
    dictionary = {"a", "aa", "aaa", "aaaa"}
    
    print(f"Texto: '{text}' (tamanho: {len(text)})")
    print(f"Dicionário: {dictionary}")
    print()
    
    # Compara todas as abordagens
    comparison = compare_approaches(text, dictionary)
    
    print("Resultados:")
    for approach, data in comparison['approaches'].items():
        print(f"  {approach.title()}:")
        print(f"    Resultado: {data['result']}")
        print(f"    Tempo: {data['time']:.6f}s")
        print(f"    Complexidade: {data['complexity']}")
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
        analysis = analyze_text_segmentation_complexity(size, 20)
        
        print(f"String de tamanho {size}:")
        print(f"  Complexidade: {analysis['complexity_class']}")
        print(f"  Espaço: {analysis['space_complexity']}")
        print(f"  Melhoria: {analysis['memoization_benefit']}")
        print(f"  Viabilidade: {analysis['practical_viability']}")
        print()
    
    # Mostra análise detalhada para um caso específico
    detailed_analysis = analyze_text_segmentation_complexity(100, 50)
    print("Análise Detalhada (n=100, dicionário=50):")
    print(f"  Definição do estado: {detailed_analysis['subproblem_analysis']['state_definition']}")
    print(f"  Número de estados: {detailed_analysis['subproblem_analysis']['state_count']}")
    print(f"  Subproblemas sobrepostos: {detailed_analysis['subproblem_analysis']['overlapping_subproblems']}")
    print(f"  Estrutura ótima: {detailed_analysis['subproblem_analysis']['optimal_substructure']}")
    print()
    
    print("Técnicas de Otimização:")
    for technique in detailed_analysis['optimization_techniques']:
        print(f"  • {technique}")
    print()
    
    print("Limitações:")
    for limitation in detailed_analysis['limitations']:
        print(f"  • {limitation}")
    print()


def demonstrate_optimization_benefits():
    """Demonstra os benefícios da memoização otimizada."""
    print("=== Benefícios da Memoização Otimizada ===\n")
    
    # Caso onde a ordenação decrescente ajuda
    text = "pineapple"
    dictionary = {"pine", "pineapple", "apple"}
    
    print(f"Texto: '{text}'")
    print(f"Dicionário: {dictionary}")
    print()
    
    # Testa diferentes implementações
    implementations = [
        ("Memoização Normal", text_segmentation_memoization),
        ("Memoização Otimizada", text_segmentation_optimized_memoization),
        ("Tabulação", text_segmentation_tabulation)
    ]
    
    for name, func in implementations:
        start_time = time.time()
        result = func(text, dictionary)
        execution_time = time.time() - start_time
        
        print(f"{name}:")
        print(f"  Resultado: {result}")
        print(f"  Tempo: {execution_time:.6f}s")
        print()
    
    print("Observação: A versão otimizada tenta prefixos maiores primeiro,")
    print("o que pode encontrar soluções mais rapidamente em alguns casos.")


def demonstrate_real_world_scenario():
    """Demonstra um cenário real de uso."""
    print("=== Cenário Real: Segmentação de Texto ===\n")
    
    # Simula um dicionário de palavras em inglês
    english_dictionary = {
        "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog",
        "programming", "algorithms", "dynamic", "programming", "memoization",
        "backtracking", "optimization", "performance", "analysis"
    }
    
    # Texto sem espaços para segmentar
    text = "thequickbrownfoxjumpsoverthelazydog"
    
    print(f"Texto original: 'the quick brown fox jumps over the lazy dog'")
    print(f"Texto sem espaços: '{text}'")
    print(f"Tamanho do dicionário: {len(english_dictionary)}")
    print()
    
    # Tenta segmentar
    result = text_segmentation_memoization(text, english_dictionary)
    
    if result:
        print("Segmentação encontrada:")
        print(f"  {' '.join(result)}")
        print(f"  Número de palavras: {len(result)}")
    else:
        print("Não foi possível segmentar o texto")
    
    print()
    
    # Mostra performance
    start_time = time.time()
    text_segmentation_memoization(text, english_dictionary)
    memoization_time = time.time() - start_time
    
    start_time = time.time()
    text_segmentation_backtracking(text, english_dictionary)
    backtracking_time = time.time() - start_time
    
    print(f"Performance:")
    print(f"  Backtracking: {backtracking_time:.6f}s")
    print(f"  Memoização: {memoization_time:.6f}s")
    print(f"  Melhoria: {backtracking_time/memoization_time:.2f}x mais rápido")


def main():
    """Função principal que executa todas as demonstrações."""
    print("Desafio 22: Segmentação de Texto com Memoização")
    print("=" * 60)
    print()
    
    # Executa todas as demonstrações
    demonstrate_basic_usage()
    demonstrate_performance_comparison()
    demonstrate_complexity_analysis()
    demonstrate_optimization_benefits()
    demonstrate_real_world_scenario()
    
    print("=" * 60)
    print("Demonstração concluída!")
    print()
    print("Principais conceitos demonstrados:")
    print("• Transição de O(2^n) para O(n²) com memoização")
    print("• Estado do subproblema: índice inicial do sufixo")
    print("• Subproblemas sobrepostos e estrutura ótima")
    print("• Benefícios práticos da programação dinâmica")
    print("• Técnicas de otimização (ordenação de tentativas)")


if __name__ == "__main__":
    main() 