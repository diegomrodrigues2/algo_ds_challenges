"""
Testes para Jogo da Velha com Algoritmo Minimax

Este arquivo contém testes abrangentes para verificar a correção e eficiência
da implementação do algoritmo Minimax para o Jogo da Velha.

Referências:
- Erickson, "Algorithms", Capítulo 2, Seção 2.2, "Game Trees"
- GitHub: t-ROY-coder/Tic-Tac-Toe-Game
"""

import unittest
import time
from typing import List, Tuple
from tic_tac_toe_minimax import (
    TicTacToeBoard,
    minimax,
    get_best_move,
    evaluate_board_state,
    play_optimal_game,
    analyze_minimax_complexity
)


class TestTicTacToeBoard(unittest.TestCase):
    """
    Testes para a classe TicTacToeBoard.
    """
    
    def test_board_initialization(self):
        """Testa a inicialização do tabuleiro."""
        board = TicTacToeBoard(3)
        self.assertEqual(board.size, 3)
        self.assertEqual(board.current_player, 'X')
        self.assertIsNone(board.winner)
        self.assertFalse(board.game_over)
        
        # Verifica se o tabuleiro está vazio
        for row in board.board:
            for cell in row:
                self.assertEqual(cell, '')
    
    def test_valid_move(self):
        """Testa movimentos válidos."""
        board = TicTacToeBoard(3)
        
        # Movimento válido
        self.assertTrue(board.make_move(0, 0))
        self.assertEqual(board.board[0][0], 'X')
        self.assertEqual(board.current_player, 'O')
    
    def test_invalid_move(self):
        """Testa movimentos inválidos."""
        board = TicTacToeBoard(3)
        
        # Movimento fora dos limites
        self.assertFalse(board.make_move(3, 3))
        self.assertFalse(board.make_move(-1, 0))
        
        # Movimento em posição ocupada
        board.make_move(0, 0)
        self.assertFalse(board.make_move(0, 0))
    
    def test_winning_conditions(self):
        """Testa condições de vitória."""
        board = TicTacToeBoard(3)
        
        # Vitória na linha
        board.make_move(0, 0)  # X
        board.make_move(1, 0)  # O
        board.make_move(0, 1)  # X
        board.make_move(1, 1)  # O
        board.make_move(0, 2)  # X
        
        self.assertTrue(board.game_over)
        self.assertEqual(board.winner, 'X')
    
    def test_diagonal_win(self):
        """Testa vitória na diagonal."""
        board = TicTacToeBoard(3)
        
        # Vitória na diagonal principal
        board.make_move(0, 0)  # X
        board.make_move(0, 1)  # O
        board.make_move(1, 1)  # X
        board.make_move(1, 0)  # O
        board.make_move(2, 2)  # X
        
        self.assertTrue(board.game_over)
        self.assertEqual(board.winner, 'X')
    
    def test_draw_condition(self):
        """Testa condição de empate."""
        board = TicTacToeBoard(3)
        
        # Configuração de empate
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)]
        players = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        
        for (row, col), player in zip(moves, players):
            board.make_move(row, col)
        
        self.assertTrue(board.game_over)
        self.assertIsNone(board.winner)
    
    def test_available_moves(self):
        """Testa obtenção de movimentos disponíveis."""
        board = TicTacToeBoard(3)
        
        # Tabuleiro vazio
        moves = board.get_available_moves()
        self.assertEqual(len(moves), 9)
        
        # Após alguns movimentos
        board.make_move(0, 0)
        board.make_move(1, 1)
        moves = board.get_available_moves()
        self.assertEqual(len(moves), 7)
    
    def test_board_copy(self):
        """Testa cópia do tabuleiro."""
        board = TicTacToeBoard(3)
        board.make_move(0, 0)
        board.make_move(1, 1)
        
        board_copy = board.copy()
        
        # Verifica se são objetos diferentes
        self.assertIsNot(board, board_copy)
        
        # Verifica se o conteúdo é igual
        self.assertEqual(board.board, board_copy.board)
        self.assertEqual(board.current_player, board_copy.current_player)


class TestMinimaxAlgorithm(unittest.TestCase):
    """
    Testes para o algoritmo Minimax.
    """
    
    def test_minimax_basic(self):
        """Testa o algoritmo Minimax básico."""
        board = TicTacToeBoard(3)
        
        # Estado inicial
        value, move = minimax(board, depth=1, maximizing=True)
        self.assertIsInstance(value, int)
        self.assertIsInstance(move, tuple)
        self.assertEqual(len(move), 2)
    
    def test_minimax_terminal_state(self):
        """Testa Minimax em estado terminal."""
        board = TicTacToeBoard(3)
        
        # Cria estado terminal (vitória de X)
        board.make_move(0, 0)  # X
        board.make_move(1, 0)  # O
        board.make_move(0, 1)  # X
        board.make_move(1, 1)  # O
        board.make_move(0, 2)  # X
        
        value, move = minimax(board, depth=1, maximizing=True)
        self.assertEqual(value, 1)  # X vence
        self.assertIsNone(move)  # Não há movimentos em estado terminal
    
    def test_minimax_alpha_beta(self):
        """Testa Minimax com poda Alpha-Beta."""
        board = TicTacToeBoard(3)
        
        value, move = minimax(board, depth=2, alpha=float('-inf'), 
                             beta=float('inf'), maximizing=True)
        
        self.assertIsInstance(value, int)
        self.assertIsInstance(move, tuple)
    
    def test_get_best_move(self):
        """Testa obtenção do melhor movimento."""
        board = TicTacToeBoard(3)
        
        best_move = get_best_move(board)
        self.assertIsInstance(best_move, tuple)
        self.assertEqual(len(best_move), 2)
        
        # Verifica se o movimento é válido
        row, col = best_move
        self.assertTrue(0 <= row < 3)
        self.assertTrue(0 <= col < 3)
    
    def test_get_best_move_terminal(self):
        """Testa obtenção do melhor movimento em estado terminal."""
        board = TicTacToeBoard(3)
        
        # Cria estado terminal
        board.make_move(0, 0)  # X
        board.make_move(1, 0)  # O
        board.make_move(0, 1)  # X
        board.make_move(1, 1)  # O
        board.make_move(0, 2)  # X
        
        best_move = get_best_move(board)
        self.assertIsNone(best_move)


class TestGameAnalysis(unittest.TestCase):
    """
    Testes para análise de jogo.
    """
    
    def test_evaluate_board_state(self):
        """Testa avaliação do estado do tabuleiro."""
        board = TicTacToeBoard(3)
        
        state = evaluate_board_state(board)
        
        self.assertIn('game_over', state)
        self.assertIn('winner', state)
        self.assertIn('current_player', state)
        self.assertIn('available_moves', state)
        self.assertIn('board_state', state)
        
        self.assertFalse(state['game_over'])
        self.assertIsNone(state['winner'])
        self.assertEqual(state['current_player'], 'X')
        self.assertEqual(state['available_moves'], 9)
    
    def test_play_optimal_game(self):
        """Testa simulação de jogo ótimo."""
        game_history = play_optimal_game(3)
        
        self.assertIsInstance(game_history, list)
        self.assertGreater(len(game_history), 0)
        
        # Verifica se o último estado é terminal
        final_state = game_history[-1]
        self.assertTrue(final_state['game_over'])
    
    def test_analyze_complexity(self):
        """Testa análise de complexidade."""
        analysis = analyze_minimax_complexity(3)
        
        self.assertIn('board_size', analysis)
        self.assertIn('total_positions', analysis)
        self.assertIn('max_moves', analysis)
        self.assertIn('estimated_tree_nodes', analysis)
        self.assertIn('complexity_class', analysis)
        self.assertIn('practical_limit', analysis)
        self.assertIn('notes', analysis)
        
        self.assertEqual(analysis['board_size'], 3)
        self.assertEqual(analysis['total_positions'], 9)
        self.assertEqual(analysis['max_moves'], 9)


class TestPerformance(unittest.TestCase):
    """
    Testes de performance.
    """
    
    def test_minimax_performance_3x3(self):
        """Testa performance para tabuleiro 3x3."""
        board = TicTacToeBoard(3)
        
        start_time = time.time()
        best_move = get_best_move(board)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Para tabuleiro 3x3, deve ser rápido (< 1 segundo)
        self.assertLess(execution_time, 1.0)
        self.assertIsInstance(best_move, tuple)
    
    def test_minimax_performance_4x4(self):
        """Testa performance para tabuleiro 4x4."""
        board = TicTacToeBoard(4)
        
        start_time = time.time()
        best_move = get_best_move(board, depth=3)  # Limita profundidade
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Para tabuleiro 4x4 com profundidade limitada, deve ser aceitável
        self.assertLess(execution_time, 10.0)
        self.assertIsInstance(best_move, tuple)


class TestEdgeCases(unittest.TestCase):
    """
    Testes para casos extremos.
    """
    
    def test_empty_board(self):
        """Testa tabuleiro vazio."""
        board = TicTacToeBoard(3)
        
        best_move = get_best_move(board)
        self.assertIsInstance(best_move, tuple)
        
        # O centro é geralmente a melhor jogada inicial
        row, col = best_move
        self.assertTrue((row, col) in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
    
    def test_one_move_left(self):
        """Testa quando resta apenas um movimento."""
        board = TicTacToeBoard(3)
        
        # Preenche quase todo o tabuleiro
        moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
        players = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
        
        for (row, col), player in zip(moves, players):
            board.make_move(row, col)
        
        best_move = get_best_move(board)
        self.assertEqual(best_move, (2, 2))  # Única posição vazia
    
    def test_immediate_win(self):
        """Testa quando há uma vitória imediata disponível."""
        board = TicTacToeBoard(3)
        
        # Configuração onde X pode vencer em um movimento
        board.make_move(0, 0)  # X
        board.make_move(1, 0)  # O
        board.make_move(0, 1)  # X
        board.make_move(1, 1)  # O
        
        best_move = get_best_move(board)
        self.assertEqual(best_move, (0, 2))  # X deve completar a linha
    
    def test_block_opponent_win(self):
        """Testa quando é necessário bloquear vitória do oponente."""
        board = TicTacToeBoard(3)
        
        # Configuração onde O pode vencer se X não bloquear
        board.make_move(0, 0)  # X
        board.make_move(1, 0)  # O
        board.make_move(2, 2)  # X
        board.make_move(1, 1)  # O
        
        best_move = get_best_move(board)
        # X deve bloquear O de completar a diagonal
        self.assertEqual(best_move, (1, 2))


class TestGeneralizedGame(unittest.TestCase):
    """
    Testes para Jogo da Velha generalizado (n x n).
    """
    
    def test_4x4_board(self):
        """Testa tabuleiro 4x4."""
        board = TicTacToeBoard(4)
        
        self.assertEqual(board.size, 4)
        self.assertEqual(len(board.board), 4)
        self.assertEqual(len(board.board[0]), 4)
        
        # Testa movimento válido
        self.assertTrue(board.make_move(0, 0))
        self.assertEqual(board.board[0][0], 'X')
    
    def test_5x5_board(self):
        """Testa tabuleiro 5x5."""
        board = TicTacToeBoard(5)
        
        self.assertEqual(board.size, 5)
        self.assertEqual(len(board.get_available_moves()), 25)
        
        # Testa alguns movimentos
        board.make_move(0, 0)
        board.make_move(2, 2)
        self.assertEqual(len(board.get_available_moves()), 23)
    
    def test_large_board_performance(self):
        """Testa performance em tabuleiros grandes."""
        board = TicTacToeBoard(4)
        
        # Testa com profundidade limitada para evitar timeout
        start_time = time.time()
        best_move = get_best_move(board, depth=2)
        end_time = time.time()
        
        execution_time = end_time - start_time
        self.assertLess(execution_time, 5.0)  # Deve ser rápido com profundidade limitada


def run_performance_benchmark():
    """
    Executa benchmark de performance.
    """
    print("=== Benchmark de Performance ===\n")
    
    sizes = [3, 4]
    depths = [None, 3, 2]
    
    for size in sizes:
        print(f"Tabuleiro {size}x{size}:")
        board = TicTacToeBoard(size)
        
        for depth in depths:
            depth_str = "completa" if depth is None else f"profundidade {depth}"
            start_time = time.time()
            best_move = get_best_move(board, depth)
            end_time = time.time()
            
            execution_time = end_time - start_time
            print(f"  Busca {depth_str}: {execution_time:.4f}s")
        
        print()


def run_comprehensive_tests():
    """
    Executa todos os testes de forma abrangente.
    """
    print("=== Testes Abrangentes: Jogo da Velha com Minimax ===\n")
    
    # Executa testes unitários
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Executa benchmark
    run_performance_benchmark()


if __name__ == "__main__":
    run_comprehensive_tests() 