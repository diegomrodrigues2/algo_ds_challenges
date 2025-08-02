"""
Testes para o módulo Torre de Hanói.

Este módulo testa todas as funcionalidades implementadas,
incluindo casos básicos, casos extremos e validações.
"""

import pytest
from .tower_of_hanoi import (
    tower_of_hanoi,
    _tower_of_hanoi_helper,
    count_moves,
    tower_of_hanoi_iterative,
    validate_tower_state
)


class TestTowerOfHanoi:
    """Testes para a função principal tower_of_hanoi."""
    
    def test_zero_discs(self):
        """Testa o caso de 0 discos."""
        moves = tower_of_hanoi(0, 'A', 'C', 'B')
        assert moves == []
    
    def test_one_disc(self):
        """Testa o caso de 1 disco."""
        moves = tower_of_hanoi(1, 'A', 'C', 'B')
        assert len(moves) == 1
        assert moves[0] == "Mover disco 1 do pino A para o pino C"
    
    def test_two_discs(self):
        """Testa o caso de 2 discos."""
        moves = tower_of_hanoi(2, 'A', 'C', 'B')
        expected_moves = [
            "Mover disco 1 do pino A para o pino B",
            "Mover disco 2 do pino A para o pino C",
            "Mover disco 1 do pino B para o pino C"
        ]
        assert moves == expected_moves
    
    def test_three_discs(self):
        """Testa o caso de 3 discos."""
        moves = tower_of_hanoi(3, 'A', 'C', 'B')
        assert len(moves) == 7
        
        # Verifica que todos os movimentos são válidos
        for move in moves:
            assert move.startswith("Mover disco")
            assert "do pino" in move
            assert "para o pino" in move
    
    def test_four_discs(self):
        """Testa o caso de 4 discos."""
        moves = tower_of_hanoi(4, 'A', 'C', 'B')
        assert len(moves) == 15
        
        # Verifica que o primeiro e último movimento são corretos
        assert moves[0] == "Mover disco 1 do pino A para o pino B"
        assert moves[-1] == "Mover disco 1 do pino B para o pino C"
    
    def test_different_pin_names(self):
        """Testa com nomes diferentes de pinos."""
        moves = tower_of_hanoi(2, 'X', 'Z', 'Y')
        expected_moves = [
            "Mover disco 1 do pino X para o pino Y",
            "Mover disco 2 do pino X para o pino Z",
            "Mover disco 1 do pino Y para o pino Z"
        ]
        assert moves == expected_moves
    
    def test_negative_discs(self):
        """Testa com número negativo de discos."""
        moves = tower_of_hanoi(-1, 'A', 'C', 'B')
        assert moves == []


class TestTowerOfHanoiHelper:
    """Testes para a função auxiliar _tower_of_hanoi_helper."""
    
    def test_helper_one_disc(self):
        """Testa a função auxiliar com 1 disco."""
        moves = []
        _tower_of_hanoi_helper(1, 'A', 'C', 'B', moves)
        assert moves == ["Mover disco 1 do pino A para o pino C"]
    
    def test_helper_two_discs(self):
        """Testa a função auxiliar com 2 discos."""
        moves = []
        _tower_of_hanoi_helper(2, 'A', 'C', 'B', moves)
        expected_moves = [
            "Mover disco 1 do pino A para o pino B",
            "Mover disco 2 do pino A para o pino C",
            "Mover disco 1 do pino B para o pino C"
        ]
        assert moves == expected_moves
    
    def test_helper_zero_discs(self):
        """Testa a função auxiliar com 0 discos."""
        moves = []
        _tower_of_hanoi_helper(0, 'A', 'C', 'B', moves)
        assert moves == []


class TestCountMoves:
    """Testes para a função count_moves."""
    
    def test_count_moves_small_values(self):
        """Testa o cálculo de movimentos para valores pequenos."""
        assert count_moves(0) == 0
        assert count_moves(1) == 1
        assert count_moves(2) == 3
        assert count_moves(3) == 7
        assert count_moves(4) == 15
        assert count_moves(5) == 31
    
    def test_count_moves_larger_values(self):
        """Testa o cálculo de movimentos para valores maiores."""
        assert count_moves(10) == 1023
        assert count_moves(20) == 1048575
    
    def test_count_moves_formula(self):
        """Testa se a fórmula 2^n - 1 está correta."""
        for n in range(1, 11):
            expected = (2 ** n) - 1
            assert count_moves(n) == expected


class TestTowerOfHanoiIterative:
    """Testes para a versão iterativa."""
    
    def test_iterative_zero_discs(self):
        """Testa a versão iterativa com 0 discos."""
        moves = tower_of_hanoi_iterative(0, 'A', 'C', 'B')
        assert moves == []
    
    def test_iterative_one_disc(self):
        """Testa a versão iterativa com 1 disco."""
        moves = tower_of_hanoi_iterative(1, 'A', 'C', 'B')
        assert len(moves) == 1
        assert moves[0] == "Mover disco 1 do pino A para o pino C"
    
    def test_iterative_two_discs(self):
        """Testa a versão iterativa com 2 discos."""
        moves = tower_of_hanoi_iterative(2, 'A', 'C', 'B')
        expected_moves = [
            "Mover disco 1 do pino A para o pino B",
            "Mover disco 2 do pino A para o pino C",
            "Mover disco 1 do pino B para o pino C"
        ]
        assert moves == expected_moves
    
    def test_iterative_three_discs(self):
        """Testa a versão iterativa com 3 discos."""
        moves = tower_of_hanoi_iterative(3, 'A', 'C', 'B')
        assert len(moves) == 7
    
    def test_iterative_consistency_with_recursive(self):
        """Testa se a versão iterativa produz o mesmo resultado da recursiva."""
        for n in range(1, 5):
            recursive_moves = tower_of_hanoi(n, 'A', 'C', 'B')
            iterative_moves = tower_of_hanoi_iterative(n, 'A', 'C', 'B')
            assert recursive_moves == iterative_moves


class TestValidateTowerState:
    """Testes para a validação de estados das torres."""
    
    def test_valid_initial_state(self):
        """Testa um estado inicial válido."""
        pegs = {'A': [3, 2, 1], 'B': [], 'C': []}
        assert validate_tower_state(pegs) == True
    
    def test_valid_intermediate_state(self):
        """Testa um estado intermediário válido."""
        pegs = {'A': [3], 'B': [2, 1], 'C': []}
        assert validate_tower_state(pegs) == True
    
    def test_valid_final_state(self):
        """Testa um estado final válido."""
        pegs = {'A': [], 'B': [], 'C': [3, 2, 1]}
        assert validate_tower_state(pegs) == True
    
    def test_invalid_state_wrong_order(self):
        """Testa um estado inválido com discos em ordem errada."""
        pegs = {'A': [1, 2, 3], 'B': [], 'C': []}
        assert validate_tower_state(pegs) == False
    
    def test_invalid_state_mixed_order(self):
        """Testa um estado inválido com ordem mista."""
        pegs = {'A': [3, 1, 2], 'B': [], 'C': []}
        assert validate_tower_state(pegs) == False
    
    def test_empty_state(self):
        """Testa um estado vazio."""
        pegs = {'A': [], 'B': [], 'C': []}
        assert validate_tower_state(pegs) == True
    
    def test_single_disk_state(self):
        """Testa um estado com apenas um disco."""
        pegs = {'A': [1], 'B': [], 'C': []}
        assert validate_tower_state(pegs) == True
    
    def test_duplicate_disks(self):
        """Testa um estado com discos duplicados."""
        pegs = {'A': [3, 2, 1], 'B': [1], 'C': []}
        assert validate_tower_state(pegs) == False


class TestEdgeCases:
    """Testes para casos extremos e edge cases."""
    
    def test_large_number_of_discs(self):
        """Testa com um número grande de discos (verifica se não trava)."""
        moves = tower_of_hanoi(10, 'A', 'C', 'B')
        assert len(moves) == 1023
        
        # Verifica que todos os movimentos são válidos
        for move in moves:
            assert "Mover disco" in move
            assert "do pino" in move
            assert "para o pino" in move
    
    def test_same_source_destination(self):
        """Testa quando origem e destino são iguais."""
        moves = tower_of_hanoi(3, 'A', 'A', 'B')
        assert moves == []
    
    def test_all_pins_same(self):
        """Testa quando todos os pinos são iguais."""
        moves = tower_of_hanoi(3, 'A', 'A', 'A')
        assert moves == []
    
    def test_negative_discs_all_functions(self):
        """Testa funções com número negativo de discos."""
        assert tower_of_hanoi(-1, 'A', 'C', 'B') == []
        assert tower_of_hanoi_iterative(-1, 'A', 'C', 'B') == []
        assert count_moves(-1) == 0


class TestPerformance:
    """Testes de performance e complexidade."""
    
    def test_moves_count_correctness(self):
        """Testa se o número de movimentos está correto para vários casos."""
        test_cases = [
            (0, 0), (1, 1), (2, 3), (3, 7), (4, 15), (5, 31), (6, 63)
        ]
        
        for n, expected in test_cases:
            # Testa a função count_moves
            assert count_moves(n) == expected
            
            # Testa se as implementações produzem o número correto de movimentos
            if n > 0:
                recursive_moves = tower_of_hanoi(n, 'A', 'C', 'B')
                iterative_moves = tower_of_hanoi_iterative(n, 'A', 'C', 'B')
                assert len(recursive_moves) == expected
                assert len(iterative_moves) == expected
    
    def test_moves_consistency(self):
        """Testa se as implementações recursiva e iterativa são consistentes."""
        for n in range(1, 6):  # Testa até 5 discos para não ser muito lento
            recursive_moves = tower_of_hanoi(n, 'A', 'C', 'B')
            iterative_moves = tower_of_hanoi_iterative(n, 'A', 'C', 'B')
            assert recursive_moves == iterative_moves


if __name__ == "__main__":
    pytest.main([__file__]) 