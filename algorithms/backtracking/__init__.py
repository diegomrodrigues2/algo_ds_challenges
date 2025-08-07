"""
Módulo de algoritmos de backtracking.

Este módulo contém implementações de algoritmos de backtracking clássicos,
incluindo o problema das N-Rainhas, coloração de grafos, e o Jogo da Velha
com algoritmo Minimax, que é uma aplicação formal do backtracking em árvores de jogo.
"""

# Importações dos algoritmos de backtracking
from .n_queens import n_queens_backtracking, n_queens_all_solutions
from .graph_coloring import (
    graph_coloring_backtracking,
    graph_coloring_optimized,
    graph_coloring_count_solutions,
    graph_coloring_all_solutions,
    graph_coloring_with_memoization,
    analyze_graph_coloring_complexity
)
from .subset_sum import (
    subset_sum_backtracking,
    subset_sum_optimized,
    subset_sum_all_solutions,
    subset_sum_with_memoization
)
from .permutation_generation import (
    generate_permutations_backtracking,
    generate_permutations_iterative,
    generate_permutations_lexicographic,
    generate_permutations_heap
)
from .subset_generation import (
    generate_subsets_backtracking,
    generate_subsets_binary,
    generate_subsets_iterative,
    generate_subsets_recursive
)
from .text_segmentation import (
    text_segmentation_backtracking,
    text_segmentation_optimized,
    text_segmentation_all_solutions
)
from .hamiltonian_path import (
    hamiltonian_path_backtracking,
    hamiltonian_path_optimized,
    hamiltonian_path_all_solutions
)
from .lis_backtracking import (
    longest_increasing_subsequence_backtracking,
    lis_backtracking_optimized,
    lis_backtracking_all_solutions
)
from .obst_backtracking import (
    optimal_binary_search_tree_backtracking,
    obst_backtracking_optimized,
    obst_backtracking_all_solutions
)

# Importações do Jogo da Velha com Minimax
from .tic_tac_toe_minimax import (
    TicTacToeBoard,
    minimax,
    get_best_move,
    evaluate_board_state,
    play_optimal_game,
    analyze_minimax_complexity
)

__all__ = [
    # N-Rainhas
    'n_queens_backtracking',
    'n_queens_all_solutions',
    
    # Coloração de Grafos
    'graph_coloring_backtracking',
    'graph_coloring_optimized',
    'graph_coloring_count_solutions',
    'graph_coloring_all_solutions',
    'graph_coloring_with_memoization',
    'analyze_graph_coloring_complexity',
    
    # Subset Sum
    'subset_sum_backtracking',
    'subset_sum_optimized',
    'subset_sum_all_solutions',
    'subset_sum_with_memoization',
    
    # Geração de Permutações
    'generate_permutations_backtracking',
    'generate_permutations_iterative',
    'generate_permutations_lexicographic',
    'generate_permutations_heap',
    
    # Geração de Subconjuntos
    'generate_subsets_backtracking',
    'generate_subsets_binary',
    'generate_subsets_iterative',
    'generate_subsets_recursive',
    
    # Segmentação de Texto
    'text_segmentation_backtracking',
    'text_segmentation_optimized',
    'text_segmentation_all_solutions',
    
    # Caminho Hamiltoniano
    'hamiltonian_path_backtracking',
    'hamiltonian_path_optimized',
    'hamiltonian_path_all_solutions',
    
    # Longest Increasing Subsequence
    'longest_increasing_subsequence_backtracking',
    'lis_backtracking_optimized',
    'lis_backtracking_all_solutions',
    
    # Optimal Binary Search Tree
    'optimal_binary_search_tree_backtracking',
    'obst_backtracking_optimized',
    'obst_backtracking_all_solutions',
    
    # Jogo da Velha com Minimax
    'TicTacToeBoard',
    'minimax',
    'get_best_move',
    'evaluate_board_state',
    'play_optimal_game',
    'analyze_minimax_complexity'
] 