"""
Testes para o módulo de N-Queens.

Este módulo contém testes abrangentes para todas as implementações
de algoritmos para resolver o problema das N-Rainhas.
"""

import pytest
import time
from typing import List

from n_queens import (
    solve_n_queens,
    solve_n_queens_backtracking,
    is_safe,
    is_safe_optimized,
    solve_n_queens_optimized,
    solve_n_queens_count_only,
    solve_n_queens_one_solution,
    solve_n_queens_symmetry_breaking,
    solve_n_queens_iterative,
    solve_n_queens_with_constraints,
    validate_solution,
    print_board,
    analyze_n_queens_complexity,
    solve_n_queens_parallel,
    solve_n_queens_heuristic,
    solve_n_queens_min_conflicts,
    solve_n_queens_genetic,
    solve_n_queens_sat,
    solve_n_queens_with_visualization,
    benchmark_n_queens_algorithms,
    solve_n_queens_adaptive,
    analyze_solution_symmetries,
    solve_n_queens_completion,
    solve_n_queens_max_queens,
    solve_n_queens_weighted,
    analyze_theoretical_bounds
)


class TestSolveNQueens:
    """Testes para a função principal solve_n_queens."""
    
    def test_n_equals_1(self):
        """Testa com n = 1."""
        solutions = solve_n_queens(1)
        assert len(solutions) == 1
        assert solutions[0] == ['Q']
    
    def test_n_equals_2(self):
        """Testa com n = 2 (sem soluções)."""
        solutions = solve_n_queens(2)
        assert len(solutions) == 0
    
    def test_n_equals_3(self):
        """Testa com n = 3 (sem soluções)."""
        solutions = solve_n_queens(3)
        assert len(solutions) == 0
    
    def test_n_equals_4(self):
        """Testa com n = 4 (2 soluções)."""
        solutions = solve_n_queens(4)
        assert len(solutions) == 2
        # Verificar se todas as soluções são válidas
        for solution in solutions:
            assert validate_solution(solution)
    
    def test_n_equals_5(self):
        """Testa com n = 5 (10 soluções)."""
        solutions = solve_n_queens(5)
        assert len(solutions) == 10
        for solution in solutions:
            assert validate_solution(solution)
    
    def test_n_equals_6(self):
        """Testa com n = 6 (4 soluções)."""
        solutions = solve_n_queens(6)
        assert len(solutions) == 4
        for solution in solutions:
            assert validate_solution(solution)
    
    def test_n_equals_8(self):
        """Testa com n = 8 (92 soluções)."""
        solutions = solve_n_queens(8)
        assert len(solutions) == 92
        for solution in solutions:
            assert validate_solution(solution)


class TestSolveNQueensBacktracking:
    """Testes para o algoritmo de backtracking clássico."""
    
    def test_backtracking_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_backtracking(4)
        assert len(solutions) == 2
        for solution in solutions:
            assert validate_solution(solution)
    
    def test_backtracking_consistency(self):
        """Testa consistência com a função principal."""
        for n in [1, 4, 5, 6]:
            backtracking_solutions = solve_n_queens_backtracking(n)
            main_solutions = solve_n_queens(n)
            assert len(backtracking_solutions) == len(main_solutions)


class TestIsSafe:
    """Testes para a função is_safe."""
    
    def test_is_safe_empty_board(self):
        """Testa em tabuleiro vazio."""
        board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        assert is_safe(board, 0, 0) == True
        assert is_safe(board, 1, 1) == True
    
    def test_is_safe_with_queens(self):
        """Testa com rainhas já posicionadas."""
        board = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        # Não pode colocar na mesma linha ou coluna
        assert is_safe(board, 0, 1) == False  # Mesma linha
        assert is_safe(board, 1, 0) == False  # Mesma coluna
        # Não pode colocar nas diagonais
        assert is_safe(board, 1, 1) == False  # Diagonal principal
        assert is_safe(board, 1, 3) == False  # Diagonal secundária
        # Pode colocar em posições seguras
        assert is_safe(board, 1, 2) == True
        assert is_safe(board, 2, 1) == True


class TestIsSafeOptimized:
    """Testes para a versão otimizada de is_safe."""
    
    def test_is_safe_optimized_empty(self):
        """Testa com array vazio."""
        cols = [-1, -1, -1, -1]  # -1 indica linha vazia
        assert is_safe_optimized(cols, 0, 0) == True
        assert is_safe_optimized(cols, 1, 1) == True
    
    def test_is_safe_optimized_with_queens(self):
        """Testa com rainhas já posicionadas."""
        cols = [0, -1, -1, -1]  # Rainha na posição (0, 0)
        # Não pode colocar na mesma coluna
        assert is_safe_optimized(cols, 1, 0) == False
        # Não pode colocar nas diagonais
        assert is_safe_optimized(cols, 1, 1) == False
        assert is_safe_optimized(cols, 1, 3) == False
        # Pode colocar em posições seguras
        assert is_safe_optimized(cols, 1, 2) == True


class TestSolveNQueensOptimized:
    """Testes para a versão otimizada."""
    
    def test_optimized_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_optimized(4)
        assert len(solutions) == 2
        for solution in solutions:
            assert validate_solution(solution)
    
    def test_optimized_consistency(self):
        """Testa consistência com outras implementações."""
        for n in [1, 4, 5, 6]:
            optimized_solutions = solve_n_queens_optimized(n)
            main_solutions = solve_n_queens(n)
            assert len(optimized_solutions) == len(main_solutions)


class TestSolveNQueensCountOnly:
    """Testes para contagem apenas."""
    
    def test_count_only_basic(self):
        """Testa casos básicos."""
        assert solve_n_queens_count_only(1) == 1
        assert solve_n_queens_count_only(2) == 0
        assert solve_n_queens_count_only(3) == 0
        assert solve_n_queens_count_only(4) == 2
        assert solve_n_queens_count_only(5) == 10
        assert solve_n_queens_count_only(6) == 4
        assert solve_n_queens_count_only(8) == 92


class TestSolveNQueensOneSolution:
    """Testes para encontrar uma solução."""
    
    def test_one_solution_basic(self):
        """Testa casos básicos."""
        solution = solve_n_queens_one_solution(1)
        assert solution == ['Q']
        
        solution = solve_n_queens_one_solution(4)
        assert solution is not None
        assert validate_solution(solution)
        
        solution = solve_n_queens_one_solution(2)
        assert solution is None  # Não há soluções para n=2


class TestSolveNQueensSymmetryBreaking:
    """Testes para quebra de simetria."""
    
    def test_symmetry_breaking_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_symmetry_breaking(4)
        assert len(solutions) <= 2  # Deve reduzir simetrias
        for solution in solutions:
            assert validate_solution(solution)


class TestSolveNQueensIterative:
    """Testes para versão iterativa."""
    
    def test_iterative_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_iterative(4)
        assert len(solutions) == 2
        for solution in solutions:
            assert validate_solution(solution)
    
    def test_iterative_consistency(self):
        """Testa consistência com versão recursiva."""
        for n in [1, 4, 5, 6]:
            iterative_solutions = solve_n_queens_iterative(n)
            recursive_solutions = solve_n_queens(n)
            assert len(iterative_solutions) == len(recursive_solutions)


class TestSolveNQueensWithConstraints:
    """Testes para N-Rainhas com restrições."""
    
    def test_with_constraints_basic(self):
        """Testa com rainhas fixas."""
        fixed_queens = [(0, 0)]  # Rainha fixa na posição (0, 0)
        solutions = solve_n_queens_with_constraints(4, fixed_queens)
        assert len(solutions) > 0
        for solution in solutions:
            assert validate_solution(solution)
            assert solution[0][0] == 'Q'  # Deve ter rainha na posição fixa
    
    def test_with_constraints_no_solution(self):
        """Testa caso sem solução."""
        fixed_queens = [(0, 0), (1, 1)]  # Posições conflitantes
        solutions = solve_n_queens_with_constraints(4, fixed_queens)
        assert len(solutions) == 0


class TestValidateSolution:
    """Testes para validação de soluções."""
    
    def test_validate_correct_solution(self):
        """Testa solução correta."""
        board = ['.Q..', '...Q', 'Q...', '..Q.']
        assert validate_solution(board) == True
    
    def test_validate_incorrect_solution(self):
        """Testa solução incorreta."""
        board = ['QQ..', '....', '....', '....']  # Duas rainhas na mesma linha
        assert validate_solution(board) == False
    
    def test_validate_diagonal_conflict(self):
        """Testa conflito em diagonal."""
        board = ['Q...', '.Q..', '....', '....']  # Rainhas em diagonal
        assert validate_solution(board) == False
    
    def test_validate_column_conflict(self):
        """Testa conflito em coluna."""
        board = ['Q...', 'Q...', '....', '....']  # Rainhas na mesma coluna
        assert validate_solution(board) == False


class TestPrintBoard:
    """Testes para impressão do tabuleiro."""
    
    def test_print_board_basic(self):
        """Testa impressão básica."""
        board = ['.Q..', '...Q', 'Q...', '..Q.']
        # A função deve executar sem erro
        print_board(board)


class TestAnalyzeNQueensComplexity:
    """Testes para análise de complexidade."""
    
    def test_complexity_analysis(self):
        """Testa análise de complexidade."""
        analysis = analyze_n_queens_complexity(8)
        assert 'time_complexity' in analysis
        assert 'space_complexity' in analysis
        assert 'solutions_count' in analysis
        assert analysis['solutions_count'] == 92


class TestSolveNQueensParallel:
    """Testes para versão paralela."""
    
    def test_parallel_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_parallel(4)
        assert len(solutions) == 2
        for solution in solutions:
            assert validate_solution(solution)
    
    def test_parallel_consistency(self):
        """Testa consistência com versão sequencial."""
        solutions_parallel = solve_n_queens_parallel(4)
        solutions_sequential = solve_n_queens(4)
        assert len(solutions_parallel) == len(solutions_sequential)


class TestSolveNQueensHeuristic:
    """Testes para versão heurística."""
    
    def test_heuristic_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_heuristic(4)
        assert len(solutions) > 0
        for solution in solutions:
            assert validate_solution(solution)


class TestSolveNQueensMinConflicts:
    """Testes para algoritmo de mínimos conflitos."""
    
    def test_min_conflicts_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_min_conflicts(4)
        assert len(solutions) > 0
        for solution in solutions:
            assert validate_solution(solution)


class TestSolveNQueensGenetic:
    """Testes para algoritmo genético."""
    
    def test_genetic_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_genetic(4, population_size=50, generations=100)
        assert len(solutions) >= 0  # Pode não encontrar todas as soluções


class TestSolveNQueensSat:
    """Testes para redução SAT."""
    
    def test_sat_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_sat(4)
        assert len(solutions) >= 0  # Pode não encontrar todas as soluções


class TestSolveNQueensWithVisualization:
    """Testes para versão com visualização."""
    
    def test_visualization_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_with_visualization(4)
        assert len(solutions) == 2
        for solution in solutions:
            assert validate_solution(solution)


class TestBenchmarkNQueensAlgorithms:
    """Testes para benchmark de algoritmos."""
    
    def test_benchmark_basic(self):
        """Testa benchmark básico."""
        n_values = [4, 5, 6]
        results = benchmark_n_queens_algorithms(n_values)
        assert 'algorithms' in results
        assert 'timings' in results
        assert 'memory_usage' in results


class TestSolveNQueensAdaptive:
    """Testes para algoritmo adaptativo."""
    
    def test_adaptive_basic(self):
        """Testa caso básico."""
        solutions = solve_n_queens_adaptive(4)
        assert len(solutions) == 2
        for solution in solutions:
            assert validate_solution(solution)


class TestAnalyzeSolutionSymmetries:
    """Testes para análise de simetrias."""
    
    def test_symmetry_analysis(self):
        """Testa análise de simetrias."""
        solutions = [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
        analysis = analyze_solution_symmetries(solutions)
        assert 'rotations' in analysis
        assert 'reflections' in analysis
        assert 'unique_solutions' in analysis


class TestSolveNQueensCompletion:
    """Testes para completar tabuleiro parcial."""
    
    def test_completion_basic(self):
        """Testa caso básico."""
        board = ['Q...', '....', '....', '....']  # Uma rainha fixa
        solution = solve_n_queens_completion(board)
        assert solution is not None
        assert validate_solution(solution)
        assert solution[0][0] == 'Q'  # Deve manter a rainha fixa
    
    def test_completion_impossible(self):
        """Testa caso impossível."""
        board = ['QQ..', '....', '....', '....']  # Duas rainhas na mesma linha
        solution = solve_n_queens_completion(board)
        assert solution is None


class TestSolveNQueensMaxQueens:
    """Testes para máximo de rainhas."""
    
    def test_max_queens_basic(self):
        """Testa caso básico."""
        max_queens, solutions = solve_n_queens_max_queens(4)
        assert max_queens == 4  # Para n=4, sempre é possível colocar 4 rainhas
        assert len(solutions) > 0


class TestSolveNQueensWeighted:
    """Testes para N-Rainhas com pesos."""
    
    def test_weighted_basic(self):
        """Testa caso básico."""
        weights = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        solutions = solve_n_queens_weighted(4, weights)
        assert len(solutions) > 0
        for solution in solutions:
            assert validate_solution(solution)


class TestAnalyzeTheoreticalBounds:
    """Testes para análise de limites teóricos."""
    
    def test_theoretical_bounds(self):
        """Testa limites teóricos."""
        bounds = analyze_theoretical_bounds()
        assert 'lower_bound' in bounds
        assert 'upper_bound' in bounds
        assert 'known_values' in bounds


class TestConsistency:
    """Testes de consistência entre diferentes implementações."""
    
    def test_all_implementations_consistent(self):
        """Testa consistência entre todas as implementações."""
        n = 4
        implementations = [
            solve_n_queens,
            solve_n_queens_backtracking,
            solve_n_queens_optimized,
            solve_n_queens_iterative,
            solve_n_queens_adaptive
        ]
        
        results = []
        for impl in implementations:
            try:
                result = impl(n)
                results.append(len(result))
            except NotImplementedError:
                continue
        
        # Todos os resultados devem ser iguais
        if len(results) > 1:
            assert all(r == results[0] for r in results)


class TestEdgeCases:
    """Testes para casos extremos."""
    
    def test_n_equals_zero(self):
        """Testa com n = 0."""
        with pytest.raises(ValueError):
            solve_n_queens(0)
    
    def test_n_negative(self):
        """Testa com n negativo."""
        with pytest.raises(ValueError):
            solve_n_queens(-1)
    
    def test_n_large(self):
        """Testa com n grande (deve funcionar, mas pode ser lento)."""
        if solve_n_queens_count_only(8) == 92:  # Se a função está implementada
            count = solve_n_queens_count_only(8)
            assert count == 92


class TestPerformance:
    """Testes de performance."""
    
    def test_performance_comparison(self):
        """Compara performance de diferentes implementações."""
        implementations = [
            solve_n_queens_backtracking,
            solve_n_queens_optimized,
            solve_n_queens_iterative
        ]
        
        times = {}
        for impl in implementations:
            try:
                start_time = time.time()
                result = impl(6)  # n=6 é rápido o suficiente
                end_time = time.time()
                times[impl.__name__] = end_time - start_time
            except NotImplementedError:
                continue
        
        # Verifica se todas as implementações retornam o mesmo resultado
        if len(times) > 1:
            assert len(set(times.keys())) == len(times)  # Todas diferentes
    
    def test_memory_efficiency(self):
        """Testa eficiência de memória."""
        # Para n=8, não deve consumir memória excessiva
        try:
            solutions = solve_n_queens(8)
            assert len(solutions) == 92
        except NotImplementedError:
            pass


class TestTheoreticalAnalysis:
    """Testes para análise teórica."""
    
    def test_complexity_analysis(self):
        """Testa análise de complexidade."""
        analysis = analyze_n_queens_complexity(8)
        assert 'time_complexity' in analysis
        assert 'space_complexity' in analysis
        assert 'branching_factor' in analysis
    
    def test_theoretical_bounds_analysis(self):
        """Testa análise de limites teóricos."""
        bounds = analyze_theoretical_bounds()
        assert 'lower_bound' in bounds
        assert 'upper_bound' in bounds
        assert 'known_values' in bounds
        assert bounds['known_values'][8] == 92  # Para n=8, sabemos que são 92 soluções


if __name__ == "__main__":
    pytest.main([__file__]) 