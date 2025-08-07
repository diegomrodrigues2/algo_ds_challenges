"""
Tic-Tac-Toe Generalizado com Algoritmo Minimax - Backtracking Implementation

Este módulo implementa um solucionador de Jogo da Velha usando o algoritmo Minimax,
que é uma aplicação formal do backtracking em árvores de jogo. O algoritmo explora
todos os movimentos possíveis e determina o movimento ótimo para cada jogador.

Referências:
- Erickson, "Algorithms", Capítulo 2, Seção 2.2, "Game Trees"
- GitHub: t-ROY-coder/Tic-Tac-Toe-Game
- Minimax Algorithm for Game Theory
"""

from typing import List, Optional, Tuple, Dict
import copy
import math


class TicTacToeBoard:
    """
    Representa um tabuleiro de Jogo da Velha generalizado.
    """
    
    def __init__(self, size: int = 3):
        """
        Inicializa um tabuleiro de tamanho n x n.
        
        Args:
            size: Tamanho do tabuleiro (padrão: 3x3)
        """
        self.size = size
        self.board = [['' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'  # X sempre começa
        self.winner = None
        self.game_over = False
    
    def make_move(self, row: int, col: int) -> bool:
        """
        Faz um movimento na posição especificada.
        
        Args:
            row: Linha do movimento
            col: Coluna do movimento
            
        Returns:
            True se o movimento foi válido, False caso contrário
        """
        if (0 <= row < self.size and 0 <= col < self.size and 
            self.board[row][col] == '' and not self.game_over):
            
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            
            # Verifica se o jogo terminou
            self._check_game_over()
            return True
        return False
    
    def _check_game_over(self):
        """
        Verifica se o jogo terminou (vitória ou empate).
        """
        # Verifica vitória
        winner = self._check_winner()
        if winner:
            self.winner = winner
            self.game_over = True
            return
        
        # Verifica empate
        if self._is_board_full():
            self.game_over = True
    
    def _check_winner(self) -> Optional[str]:
        """
        Verifica se há um vencedor no tabuleiro.
        
        Returns:
            'X', 'O' ou None se não há vencedor
        """
        # Verifica linhas
        for row in self.board:
            if all(cell == row[0] and cell != '' for cell in row):
                return row[0]
        
        # Verifica colunas
        for col in range(self.size):
            if all(self.board[row][col] == self.board[0][col] and 
                   self.board[row][col] != '' for row in range(self.size)):
                return self.board[0][col]
        
        # Verifica diagonais
        if all(self.board[i][i] == self.board[0][0] and 
               self.board[i][i] != '' for i in range(self.size)):
            return self.board[0][0]
        
        if all(self.board[i][self.size-1-i] == self.board[0][self.size-1] and 
               self.board[i][self.size-1-i] != '' for i in range(self.size)):
            return self.board[0][self.size-1]
        
        return None
    
    def _is_board_full(self) -> bool:
        """
        Verifica se o tabuleiro está cheio.
        
        Returns:
            True se o tabuleiro está cheio, False caso contrário
        """
        return all(cell != '' for row in self.board for cell in row)
    
    def get_available_moves(self) -> List[Tuple[int, int]]:
        """
        Retorna todas as posições vazias disponíveis.
        
        Returns:
            Lista de tuplas (row, col) com posições vazias
        """
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == '':
                    moves.append((row, col))
        return moves
    
    def is_terminal_state(self) -> bool:
        """
        Verifica se o estado atual é terminal (fim de jogo).
        
        Returns:
            True se é estado terminal, False caso contrário
        """
        return self.game_over
    
    def get_utility(self) -> int:
        """
        Retorna o valor de utilidade do estado terminal.
        
        Returns:
            1 se X vence, -1 se O vence, 0 se empate
        """
        if not self.is_terminal_state():
            return 0
        
        if self.winner == 'X':
            return 1
        elif self.winner == 'O':
            return -1
        else:
            return 0
    
    def copy(self) -> 'TicTacToeBoard':
        """
        Cria uma cópia do tabuleiro atual.
        
        Returns:
            Cópia do tabuleiro
        """
        new_board = TicTacToeBoard(self.size)
        new_board.board = [row[:] for row in self.board]
        new_board.current_player = self.current_player
        new_board.winner = self.winner
        new_board.game_over = self.game_over
        return new_board
    
    def __str__(self) -> str:
        """
        Representação string do tabuleiro.
        """
        result = []
        for i, row in enumerate(self.board):
            row_str = ' | '.join(cell if cell else ' ' for cell in row)
            result.append(f" {row_str} ")
            if i < self.size - 1:
                result.append('-' * (self.size * 4 - 1))
        return '\n'.join(result)


def minimax(board: TicTacToeBoard, depth: int, alpha: float = float('-inf'), 
            beta: float = float('inf'), maximizing: bool = True) -> Tuple[int, Optional[Tuple[int, int]]]:
    """
    Implementa o algoritmo Minimax com poda Alpha-Beta.
    
    O algoritmo explora a árvore de todos os movimentos possíveis e determina
    o movimento ótimo para o jogador atual, assumindo que ambos os jogadores
    jogam de forma ótima.
    
    Args:
        board: Estado atual do tabuleiro
        depth: Profundidade máxima de busca
        alpha: Valor alpha para poda
        beta: Valor beta para poda
        maximizing: True se é o turno do maximizador (X), False para minimizador (O)
        
    Returns:
        Tupla (valor, movimento) onde valor é a avaliação do estado e
        movimento é a posição (row, col) do melhor movimento
    """
    # Caso base: estado terminal ou profundidade máxima
    if board.is_terminal_state() or depth == 0:
        return board.get_utility(), None
    
    available_moves = board.get_available_moves()
    
    if maximizing:
        max_eval = float('-inf')
        best_move = None
        
        for row, col in available_moves:
            # Faz o movimento
            board_copy = board.copy()
            board_copy.make_move(row, col)
            
            # Avalia recursivamente
            eval_score, _ = minimax(board_copy, depth - 1, alpha, beta, False)
            
            # Atualiza melhor movimento
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (row, col)
            
            # Poda Alpha-Beta
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        
        return max_eval, best_move
    
    else:
        min_eval = float('inf')
        best_move = None
        
        for row, col in available_moves:
            # Faz o movimento
            board_copy = board.copy()
            board_copy.make_move(row, col)
            
            # Avalia recursivamente
            eval_score, _ = minimax(board_copy, depth - 1, alpha, beta, True)
            
            # Atualiza melhor movimento
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (row, col)
            
            # Poda Alpha-Beta
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        
        return min_eval, best_move


def get_best_move(board: TicTacToeBoard, depth: int = None) -> Optional[Tuple[int, int]]:
    """
    Determina o melhor movimento para o jogador atual usando Minimax.
    
    Args:
        board: Estado atual do tabuleiro
        depth: Profundidade máxima de busca (padrão: tamanho do tabuleiro)
        
    Returns:
        Tupla (row, col) com o melhor movimento, ou None se não há movimentos
    """
    if depth is None:
        depth = board.size * board.size  # Busca completa para tabuleiros pequenos
    
    if board.is_terminal_state():
        return None
    
    # Determina se é turno do maximizador (X) ou minimizador (O)
    # X sempre começa, então se o número de movimentos é par, é turno do X
    moves_made = sum(1 for row in board.board for cell in row if cell != '')
    maximizing = (moves_made % 2 == 0)  # X joga em turnos pares
    
    _, best_move = minimax(board, depth, maximizing=maximizing)
    return best_move


def evaluate_board_state(board: TicTacToeBoard) -> Dict:
    """
    Avalia o estado atual do tabuleiro e fornece informações detalhadas.
    
    Args:
        board: Estado atual do tabuleiro
        
    Returns:
        Dicionário com informações sobre o estado do jogo
    """
    result = {
        'game_over': board.game_over,
        'winner': board.winner,
        'current_player': board.current_player,
        'available_moves': len(board.get_available_moves()),
        'board_state': [row[:] for row in board.board]
    }
    
    if board.is_terminal_state():
        result['utility'] = board.get_utility()
        result['game_result'] = 'X wins' if board.winner == 'X' else \
                               'O wins' if board.winner == 'O' else 'Draw'
    else:
        result['utility'] = None
        result['game_result'] = 'In progress'
    
    return result


def play_optimal_game(size: int = 3, max_depth: int = None) -> List[Dict]:
    """
    Simula um jogo completo onde ambos os jogadores jogam de forma ótima.
    
    Args:
        size: Tamanho do tabuleiro
        max_depth: Profundidade máxima para busca (padrão: busca completa)
        
    Returns:
        Lista de estados do jogo em cada movimento
    """
    board = TicTacToeBoard(size)
    game_history = []
    
    while not board.is_terminal_state():
        # Registra estado atual
        game_history.append(evaluate_board_state(board))
        
        # Determina melhor movimento
        best_move = get_best_move(board, max_depth)
        
        if best_move is None:
            break
        
        # Faz o movimento
        row, col = best_move
        board.make_move(row, col)
    
    # Adiciona estado final
    game_history.append(evaluate_board_state(board))
    
    return game_history


def analyze_minimax_complexity(size: int) -> Dict:
    """
    Analisa a complexidade do algoritmo Minimax para diferentes tamanhos de tabuleiro.
    
    Args:
        size: Tamanho do tabuleiro
        
    Returns:
        Dicionário com análise de complexidade
    """
    total_positions = size * size
    max_moves = total_positions
    
    # Número de nós na árvore de jogo (aproximação)
    # Para cada nível, o número de nós é aproximadamente o fatorial dos movimentos restantes
    estimated_nodes = 0
    for depth in range(max_moves + 1):
        if depth == 0:
            estimated_nodes += 1
        else:
            # Aproximação: para cada nível, multiplica pelo número de movimentos disponíveis
            moves_at_depth = max_moves - depth + 1
            estimated_nodes += math.factorial(moves_at_depth) if moves_at_depth <= 9 else float('inf')
    
    return {
        'board_size': size,
        'total_positions': total_positions,
        'max_moves': max_moves,
        'estimated_tree_nodes': estimated_nodes,
        'complexity_class': 'O(b^d)' if size <= 4 else 'O(b^d) - Exponential',
        'practical_limit': size <= 4,  # Praticamente limitado a tabuleiros 4x4 ou menores
        'notes': [
            'Complexidade exponencial torna o algoritmo impraticável para tabuleiros grandes',
            'Poda Alpha-Beta pode reduzir significativamente o número de nós explorados',
            'Para tabuleiros 3x3, busca completa é viável',
            'Para tabuleiros maiores, heurísticas são necessárias'
        ]
    }


def demonstrate_minimax_example():
    """
    Demonstra o uso do algoritmo Minimax com exemplos práticos.
    """
    print("=== Demonstração: Jogo da Velha com Minimax ===\n")
    
    # Exemplo 1: Jogo 3x3
    print("1. Jogo 3x3 - Movimento ótimo:")
    board = TicTacToeBoard(3)
    print("Tabuleiro inicial:")
    print(board)
    print()
    
    best_move = get_best_move(board)
    print(f"Melhor movimento para X: {best_move}")
    print()
    
    # Exemplo 2: Estado intermediário
    print("2. Estado intermediário:")
    board = TicTacToeBoard(3)
    board.make_move(0, 0)  # X no canto
    board.make_move(1, 1)  # O no centro
    print("Estado após X(0,0) e O(1,1):")
    print(board)
    print()
    
    best_move = get_best_move(board)
    print(f"Melhor movimento para X: {best_move}")
    print()
    
    # Exemplo 3: Análise de complexidade
    print("3. Análise de Complexidade:")
    for size in [3, 4, 5]:
        analysis = analyze_minimax_complexity(size)
        print(f"Tabuleiro {size}x{size}:")
        print(f"  Posições: {analysis['total_positions']}")
        print(f"  Nós estimados: {analysis['estimated_tree_nodes']}")
        print(f"  Praticamente viável: {analysis['practical_limit']}")
        print()


if __name__ == "__main__":
    demonstrate_minimax_example() 