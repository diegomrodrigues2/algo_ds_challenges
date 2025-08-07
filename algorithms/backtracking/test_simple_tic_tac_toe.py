#!/usr/bin/env python3
"""
Teste simples para verificar se a implementação do Jogo da Velha está funcionando.
"""

def test_basic_functionality():
    """Testa funcionalidade básica."""
    try:
        from tic_tac_toe_minimax import TicTacToeBoard, get_best_move
        
        print("✓ Importação bem-sucedida")
        
        # Testa criação do tabuleiro
        board = TicTacToeBoard(3)
        print("✓ Tabuleiro criado com sucesso")
        
        # Testa movimento
        board.make_move(0, 0)
        print("✓ Movimento realizado com sucesso")
        
        # Testa algoritmo minimax
        best_move = get_best_move(board)
        print(f"✓ Melhor movimento calculado: {best_move}")
        
        print("\n🎉 Todos os testes básicos passaram!")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def test_game_progression():
    """Testa progressão de um jogo simples."""
    try:
        from tic_tac_toe_minimax import TicTacToeBoard, get_best_move
        
        print("\n=== Teste de Progressão de Jogo ===")
        
        board = TicTacToeBoard(3)
        print("Tabuleiro inicial:")
        print(board)
        
        # Primeiro movimento
        best_move = get_best_move(board)
        board.make_move(*best_move)
        print(f"\nApós primeiro movimento {best_move}:")
        print(board)
        
        # Segundo movimento
        best_move = get_best_move(board)
        board.make_move(*best_move)
        print(f"\nApós segundo movimento {best_move}:")
        print(board)
        
        print("✓ Progressão de jogo funcionando!")
        return True
        
    except Exception as e:
        print(f"❌ Erro na progressão: {e}")
        return False


def test_complexity_analysis():
    """Testa análise de complexidade."""
    try:
        from tic_tac_toe_minimax import analyze_minimax_complexity
        
        print("\n=== Teste de Análise de Complexidade ===")
        
        for size in [3, 4]:
            analysis = analyze_minimax_complexity(size)
            print(f"Tabuleiro {size}x{size}:")
            print(f"  Posições: {analysis['total_positions']}")
            print(f"  Viável: {analysis['practical_limit']}")
        
        print("✓ Análise de complexidade funcionando!")
        return True
        
    except Exception as e:
        print(f"❌ Erro na análise: {e}")
        return False


if __name__ == "__main__":
    print("=== Teste Simples: Jogo da Velha com Minimax ===\n")
    
    tests = [
        ("Funcionalidade Básica", test_basic_functionality),
        ("Progressão de Jogo", test_game_progression),
        ("Análise de Complexidade", test_complexity_analysis)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
    
    print(f"\n=== Resultado: {passed}/{total} testes passaram ===")
    
    if passed == total:
        print("🎉 Todos os testes passaram! Implementação funcionando corretamente.")
    else:
        print("⚠️ Alguns testes falharam. Verifique a implementação.") 