# Dynamic Programming Algorithms Package

"""
Módulo de algoritmos de programação dinâmica.

Inclui implementações de problemas clássicos como:
- Rod Cutting (corte de barras)
- Knapsack Problem (problema da mochila)
- Longest Common Subsequence (LCS)
- Optimal Binary Search Tree (BST ótima)
- Subset Sum with Memoization (soma de subconjuntos)

Cada algoritmo demonstra diferentes técnicas de PD:
- Memoização (top-down)
- Tabulação (bottom-up)
- Reconstrução de soluções
- Análise de complexidade
"""

from .rod_cutting import (
    rod_cutting_recursive,
    rod_cutting_dp,
    rod_cutting_bottom_up,
    rod_cutting_with_solution
)

from .knapsack import (
    knapsack_recursive,
    knapsack_dp,
    knapsack_01,
    knapsack_fractional,
    knapsack_with_items
)

from .longest_common_subsequence import (
    lcs_recursive,
    lcs_dp,
    lcs_with_string,
    lcs_three_strings,
    lcs_palindrome
)

from .optimal_binary_search_tree import (
    optimal_bst_basic,
    optimal_bst_with_tree,
    optimal_bst_knuth_optimization,
    optimal_bst_space_optimized
)

from .subset_sum_memoization import (
    subset_sum_memoization,
    subset_sum_backtracking,
    subset_sum_tabulation,
    analyze_subset_sum_complexity,
    compare_approaches,
    get_subset_solution,
    count_subset_solutions,
    generate_test_cases,
    benchmark_performance
)

from .text_segmentation_memoization import (
    text_segmentation_memoization,
    text_segmentation_backtracking,
    text_segmentation_tabulation,
    text_segmentation_optimized_memoization,
    analyze_text_segmentation_complexity,
    compare_approaches as compare_text_approaches,
    generate_test_cases as generate_text_test_cases,
    benchmark_performance as benchmark_text_performance
)

from .lis_memoization import (
    lis_memoization,
    lis_backtracking,
    lis_tabulation,
    lis_binary_search,
    lis_with_sequence,
    lis_count_all,
    lis_ending_at_each_index,
    lis_with_constraints,
    analyze_lis_complexity,
    compare_lis_approaches,
    generate_lis_test_cases,
    benchmark_lis_performance
)

__all__ = [
    # Rod Cutting
    'rod_cutting_recursive',
    'rod_cutting_dp',
    'rod_cutting_bottom_up',
    'rod_cutting_with_solution',
    
    # Knapsack
    'knapsack_recursive',
    'knapsack_dp',
    'knapsack_01',
    'knapsack_fractional',
    'knapsack_with_items',
    
    # Longest Common Subsequence
    'lcs_recursive',
    'lcs_dp',
    'lcs_with_string',
    'lcs_three_strings',
    'lcs_palindrome',
    
    # Optimal Binary Search Tree
    'optimal_bst_basic',
    'optimal_bst_with_tree',
    'optimal_bst_knuth_optimization',
    'optimal_bst_space_optimized',
    
    # Subset Sum with Memoization
    'subset_sum_memoization',
    'subset_sum_backtracking',
    'subset_sum_tabulation',
    'analyze_subset_sum_complexity',
    'compare_approaches',
    'get_subset_solution',
    'count_subset_solutions',
    'generate_test_cases',
    'benchmark_performance',
    
    # Text Segmentation with Memoization
    'text_segmentation_memoization',
    'text_segmentation_backtracking',
    'text_segmentation_tabulation',
    'text_segmentation_optimized_memoization',
    'analyze_text_segmentation_complexity',
    'compare_text_approaches',
    'generate_text_test_cases',
    'benchmark_text_performance',
    
    # LIS with Memoization
    'lis_memoization',
    'lis_backtracking',
    'lis_tabulation',
    'lis_binary_search',
    'lis_with_sequence',
    'lis_count_all',
    'lis_ending_at_each_index',
    'lis_with_constraints',
    'analyze_lis_complexity',
    'compare_lis_approaches',
    'generate_lis_test_cases',
    'benchmark_lis_performance'
] 