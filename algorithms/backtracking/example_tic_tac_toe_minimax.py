"""
Exemplo de Uso: Jogo da Velha com Algoritmo Minimax

Este arquivo demonstra como usar o algoritmo Minimax implementado com backtracking
para resolver o problema do Jogo da Velha generalizado.

Referências:
- Erickson, "Algorithms", Capítulo 2, Seção 2.2, "Game Trees"
- GitHub: t-ROY-coder/Tic-Tac-Toe-Game
- Minimax Algorithm for Game Theory
"""

from typing import List, Dict
import time
from tic_tac_toe_minimax import (
    TicTacToeBoard,
    minimax,
    get_best_move,
    evaluate_board_state,
    play_optimal_game,
    analyze_minimax_complexity
)


def example_basic_minimax():
    """
    Exemplo básico do algoritmo Minimax.
    """
    print("=== Exemplo Básico: Algoritmo Minimax ===\n")
    
    # Cria tabuleiro 3x3
    board = TicTacToeBoard(3)
    print("Tabuleiro inicial:")
    print(board)
    print()
    
    # Determina melhor movimento para X
    best_move = get_best_move(board)
    print(f"Melhor movimento para X: {best_move}")
    print()
    
    # Faz o movimento
    if best_move:
        row, col = best_move
        board.make_move(row, col)
        print("Após movimento ótimo:")
        print(board)
        print()


def example_game_progression():
    """
    Demonstra a progressão de um jogo com movimentos ótimos.
    """
    print("=== Exemplo: Progressão de Jogo ===\n")
    
    board = TicTacToeBoard(3)
    move_count = 0
    
    while not board.is_terminal_state():
        print(f"Movimento {move_count + 1}:")
        print(board)
        print()
        
        # Determina melhor movimento
        best_move = get_best_move(board)
        if best_move is None:
            break
        
        # Faz o movimento
        row, col = best_move
        board.make_move(row, col)
        move_count += 1
    
    # Estado final
    print("Estado final:")
    print(board)
    print()
    
    # Resultado
    if board.winner:
        print(f"Vencedor: {board.winner}")
    else:
        print("Empate!")
    print()


def example_intermediate_states():
    """
    Demonstra como o algoritmo funciona em estados intermediários.
    """
    print("=== Exemplo: Estados Intermediários ===\n")
    
    # Estado 1: X no canto, O no centro
    print("1. Estado após X(0,0) e O(1,1):")
    board = TicTacToeBoard(3)
    board.make_move(0, 0)  # X no canto
    board.make_move(1, 1)  # O no centro
    print(board)
    print()
    
    best_move = get_best_move(board)
    print(f"Melhor movimento para X: {best_move}")
    print()
    
    # Estado 2: Configuração mais complexa
    print("2. Estado mais complexo:")
    board = TicTacToeBoard(3)
    board.make_move(0, 0)  # X
    board.make_move(0, 1)  # O
    board.make_move(1, 1)  # X
    board.make_move(2, 2)  # O
    print(board)
    print()
    
    best_move = get_best_move(board)
    print(f"Melhor movimento para X: {best_move}")
    print()


def example_performance_comparison():
    """
    Compara o desempenho do algoritmo para diferentes tamanhos de tabuleiro.
    """
    print("=== Comparação de Desempenho ===\n")
    
    for size in [3, 4]:
        print(f"Tabuleiro {size}x{size}:")
        
        # Análise de complexidade
        analysis = analyze_minimax_complexity(size)
        print(f"  Posições: {analysis['total_positions']}")
        print(f"  Nós estimados: {analysis['estimated_tree_nodes']}")
        print(f"  Viável: {analysis['practical_limit']}")
        
        # Teste de tempo
        board = TicTacToeBoard(size)
        start_time = time.time()
        best_move = get_best_move(board)
        end_time = time.time()
        
        print(f"  Tempo para primeiro movimento: {end_time - start_time:.4f}s")
        print(f"  Melhor movimento: {best_move}")
        print()


def example_optimal_game_simulation():
    """
    Simula um jogo completo onde ambos os jogadores jogam de forma ótima.
    """
    print("=== Simulação de Jogo Ótimo ===\n")
    
    # Simula jogo 3x3
    game_history = play_optimal_game(3)
    
    print("Histórico do jogo:")
    for i, state in enumerate(game_history):
        print(f"Estado {i}:")
        print(f"  Jogador atual: {state['current_player']}")
        print(f"  Movimentos disponíveis: {state['available_moves']}")
        print(f"  Jogo terminado: {state['game_over']}")
        if state['game_over']:
            print(f"  Resultado: {state['game_result']}")
        print()


def example_complexity_analysis():
    """
    Analisa a complexidade do algoritmo para diferentes cenários.
    """
    print("=== Análise de Complexidade ===\n")
    
    # Análise para diferentes tamanhos
    for size in [3, 4, 5]:
        analysis = analyze_minimax_complexity(size)
        print(f"Tabuleiro {size}x{size}:")
        print(f"  Tamanho: {analysis['board_size']}x{analysis['board_size']}")
        print(f"  Posições totais: {analysis['total_positions']}")
        print(f"  Movimentos máximos: {analysis['max_moves']}")
        print(f"  Nós estimados na árvore: {analysis['estimated_tree_nodes']}")
        print(f"  Classe de complexidade: {analysis['complexity_class']}")
        print(f"  Limite prático: {analysis['practical_limit']}")
        print()
    
    # Notas sobre otimizações
    print("Notas sobre otimizações:")
    for note in analysis['notes']:
        print(f"  - {note}")
    print()


def example_practical_applications():
    """
    Demonstra aplicações práticas do algoritmo Minimax.
    """
    print("=== Aplicações Práticas ===\n")
    
    applications = [
        {
            'name': 'Jogos de Tabuleiro',
            'description': 'Xadrez, Damas, Go - todos usam variações do Minimax',
            'complexity': 'Alta - requer heurísticas para tabuleiros grandes'
        },
        {
            'name': 'Jogos de Estratégia',
            'description': 'Jogos onde dois jogadores se alternam com informação perfeita',
            'complexity': 'Média - depende do tamanho do espaço de estados'
        },
        {
            'name': 'IA em Jogos',
            'description': 'Algoritmo fundamental para criar IAs competitivas',
            'complexity': 'Variável - pode ser otimizado com poda e heurísticas'
        },
        {
            'name': 'Teoria dos Jogos',
            'description': 'Análise de estratégias ótimas em jogos de soma zero',
            'complexity': 'Teórica - base para análise de jogos'
        }
    ]
    
    for app in applications:
        print(f"{app['name']}:")
        print(f"  Descrição: {app['description']}")
        print(f"  Complexidade: {app['complexity']}")
        print()


def example_advanced_features():
    """
    Demonstra recursos avançados do algoritmo.
    """
    print("=== Recursos Avançados ===\n")
    
    # 1. Poda Alpha-Beta
    print("1. Poda Alpha-Beta:")
    print("   - Reduz significativamente o número de nós explorados")
    print("   - Mantém a mesma qualidade de decisão")
    print("   - Especialmente eficaz em jogos com muitos movimentos")
    print()
    
    # 2. Heurísticas
    print("2. Heurísticas:")
    print("   - Funções de avaliação para estados não terminais")
    print("   - Permitem busca em profundidade limitada")
    print("   - Essenciais para jogos complexos")
    print()
    
    # 3. Iterative Deepening
    print("3. Aprofundamento Iterativo:")
    print("   - Busca em profundidades crescentes")
    print("   - Permite controle de tempo")
    print("   - Garante melhor movimento disponível")
    print()


def run_all_examples():
    """
    Executa todos os exemplos em sequência.
    """
    print("=== Demonstração Completa: Jogo da Velha com Minimax ===\n")
    
    examples = [
        ("Exemplo Básico", example_basic_minimax),
        ("Progressão de Jogo", example_game_progression),
        ("Estados Intermediários", example_intermediate_states),
        ("Comparação de Desempenho", example_performance_comparison),
        ("Simulação de Jogo Ótimo", example_optimal_game_simulation),
        ("Análise de Complexidade", example_complexity_analysis),
        ("Aplicações Práticas", example_practical_applications),
        ("Recursos Avançados", example_advanced_features)
    ]
    
    for name, example_func in examples:
        print(f"\n{'='*60}")
        print(f"{name}")
        print(f"{'='*60}")
        try:
            example_func()
        except Exception as e:
            print(f"Erro no exemplo {name}: {e}")
    
    print("\n=== Demonstração Concluída ===")


if __name__ == "__main__":
    run_all_examples() 