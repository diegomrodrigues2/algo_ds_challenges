"""
Testes para o algoritmo de exponenciação rápida (Binary Exponentiation).

Este módulo contém testes abrangentes para validar a implementação
do algoritmo de exponenciação binária, incluindo casos básicos, casos extremos
e comparações com exponenciação tradicional.
"""

import pytest
from .binary_exponentiation import (
    binary_exponentiation,
    modular_exponentiation,
    recursive_exponentiation,
    matrix_exponentiation,
    fibonacci_fast,
    power_mod
)


class TestBinaryExponentiation:
    """Testes para a função binary_exponentiation."""
    
    def test_basic_exponentiation(self):
        """Testa exponenciação básica."""
        assert binary_exponentiation(2, 0) == 1
        assert binary_exponentiation(2, 1) == 2
        assert binary_exponentiation(2, 10) == 1024
        assert binary_exponentiation(3, 5) == 243
        assert binary_exponentiation(5, 3) == 125
    
    def test_power_of_two_exponents(self):
        """Testa expoentes que são potências de 2."""
        assert binary_exponentiation(2, 2) == 4
        assert binary_exponentiation(2, 4) == 16
        assert binary_exponentiation(2, 8) == 256
        assert binary_exponentiation(3, 4) == 81
        assert binary_exponentiation(5, 8) == 390625
    
    def test_large_exponents(self):
        """Testa expoentes grandes."""
        assert binary_exponentiation(2, 20) == 1048576
        assert binary_exponentiation(3, 10) == 59049
        assert binary_exponentiation(10, 5) == 100000
    
    def test_base_one(self):
        """Testa base igual a 1."""
        assert binary_exponentiation(1, 0) == 1
        assert binary_exponentiation(1, 100) == 1
        assert binary_exponentiation(1, 1000) == 1
    
    def test_base_zero(self):
        """Testa base igual a 0."""
        assert binary_exponentiation(0, 0) == 1
        assert binary_exponentiation(0, 1) == 0
        assert binary_exponentiation(0, 10) == 0
    
    def test_negative_exponent(self):
        """Testa expoente negativo."""
        with pytest.raises(ValueError):
            binary_exponentiation(2, -1)
        with pytest.raises(ValueError):
            binary_exponentiation(3, -5)


class TestModularExponentiation:
    """Testes para a função modular_exponentiation."""
    
    def test_basic_modular_exponentiation(self):
        """Testa exponenciação modular básica."""
        assert modular_exponentiation(2, 10, 1000) == 24
        assert modular_exponentiation(3, 100, 7) == 4
        assert modular_exponentiation(5, 3, 13) == 8
        assert modular_exponentiation(2, 5, 10) == 2
    
    def test_small_modulus(self):
        """Testa módulos pequenos."""
        assert modular_exponentiation(2, 10, 5) == 4
        assert modular_exponentiation(3, 5, 7) == 5
        assert modular_exponentiation(4, 3, 6) == 4
    
    def test_large_numbers(self):
        """Testa números grandes."""
        assert modular_exponentiation(2, 100, 1000000007) == 976371285
        assert modular_exponentiation(3, 50, 1000000007) == 930856309
        assert modular_exponentiation(5, 25, 1000000007) == 2265625
    
    def test_zero_base(self):
        """Testa base zero."""
        assert modular_exponentiation(0, 5, 10) == 0
        assert modular_exponentiation(0, 100, 7) == 0
    
    def test_zero_exponent(self):
        """Testa expoente zero."""
        assert modular_exponentiation(5, 0, 10) == 1
        assert modular_exponentiation(100, 0, 7) == 1
    
    def test_modulus_one(self):
        """Testa módulo igual a 1."""
        assert modular_exponentiation(5, 10, 1) == 0
        assert modular_exponentiation(100, 50, 1) == 0
    
    def test_invalid_inputs(self):
        """Testa entradas inválidas."""
        with pytest.raises(ValueError):
            modular_exponentiation(2, -1, 10)
        with pytest.raises(ValueError):
            modular_exponentiation(2, 5, 0)
        with pytest.raises(ValueError):
            modular_exponentiation(2, 5, -5)


class TestRecursiveExponentiation:
    """Testes para a função recursive_exponentiation."""
    
    def test_basic_recursive_exponentiation(self):
        """Testa exponenciação recursiva básica."""
        assert recursive_exponentiation(2, 0) == 1
        assert recursive_exponentiation(2, 1) == 2
        assert recursive_exponentiation(2, 8) == 256
        assert recursive_exponentiation(3, 4) == 81
        assert recursive_exponentiation(5, 3) == 125
    
    def test_even_exponents(self):
        """Testa expoentes pares."""
        assert recursive_exponentiation(2, 2) == 4
        assert recursive_exponentiation(2, 4) == 16
        assert recursive_exponentiation(3, 6) == 729
        assert recursive_exponentiation(5, 4) == 625
    
    def test_odd_exponents(self):
        """Testa expoentes ímpares."""
        assert recursive_exponentiation(2, 3) == 8
        assert recursive_exponentiation(2, 5) == 32
        assert recursive_exponentiation(3, 5) == 243
        assert recursive_exponentiation(5, 5) == 3125
    
    def test_large_exponents(self):
        """Testa expoentes grandes."""
        assert recursive_exponentiation(2, 16) == 65536
        assert recursive_exponentiation(3, 10) == 59049
    
    def test_negative_exponent(self):
        """Testa expoente negativo."""
        with pytest.raises(ValueError):
            recursive_exponentiation(2, -1)


class TestMatrixExponentiation:
    """Testes para a função matrix_exponentiation."""
    
    def test_basic_matrix_exponentiation(self):
        """Testa exponenciação de matriz básica."""
        matrix = [[1, 1], [1, 0]]
        result = matrix_exponentiation(matrix, 5)
        expected = [[8, 5], [5, 3]]
        assert result == expected
    
    def test_identity_matrix(self):
        """Testa exponenciação da matriz identidade."""
        matrix = [[1, 0], [0, 1]]
        result = matrix_exponentiation(matrix, 10)
        assert result == matrix
    
    def test_zero_exponent(self):
        """Testa expoente zero."""
        matrix = [[1, 1], [1, 0]]
        result = matrix_exponentiation(matrix, 0)
        expected = [[1, 0], [0, 1]]
        assert result == expected
    
    def test_exponent_one(self):
        """Testa expoente um."""
        matrix = [[2, 1], [1, 1]]
        result = matrix_exponentiation(matrix, 1)
        assert result == matrix
    
    def test_fibonacci_matrix(self):
        """Testa matriz de Fibonacci."""
        matrix = [[1, 1], [1, 0]]
        # F(6) = 8, F(5) = 5
        result = matrix_exponentiation(matrix, 5)
        expected = [[8, 5], [5, 3]]
        assert result == expected
    
    def test_invalid_matrix(self):
        """Testa matriz inválida."""
        with pytest.raises(ValueError):
            matrix_exponentiation([[1, 2, 3], [4, 5, 6]], 2)
        with pytest.raises(ValueError):
            matrix_exponentiation([[1]], 2)
    
    def test_negative_exponent(self):
        """Testa expoente negativo."""
        matrix = [[1, 1], [1, 0]]
        with pytest.raises(ValueError):
            matrix_exponentiation(matrix, -1)


class TestFibonacciFast:
    """Testes para a função fibonacci_fast."""
    
    def test_basic_fibonacci(self):
        """Testa números de Fibonacci básicos."""
        assert fibonacci_fast(0) == 0
        assert fibonacci_fast(1) == 1
        assert fibonacci_fast(2) == 1
        assert fibonacci_fast(3) == 2
        assert fibonacci_fast(4) == 3
        assert fibonacci_fast(5) == 5
        assert fibonacci_fast(6) == 8
        assert fibonacci_fast(10) == 55
    
    def test_large_fibonacci(self):
        """Testa números de Fibonacci grandes."""
        assert fibonacci_fast(20) == 6765
        assert fibonacci_fast(30) == 832040
    
    def test_fibonacci_with_modulus(self):
        """Testa Fibonacci com módulo."""
        assert fibonacci_fast(100, 1000000007) == 687995182
        assert fibonacci_fast(50, 1000) == 25
        assert fibonacci_fast(25, 100) == 75
    
    def test_negative_index(self):
        """Testa índice negativo."""
        with pytest.raises(ValueError):
            fibonacci_fast(-1)
        with pytest.raises(ValueError):
            fibonacci_fast(-10)


class TestPowerMod:
    """Testes para a função power_mod."""
    
    def test_basic_power_mod(self):
        """Testa power_mod básico."""
        assert power_mod(2, 100, 1000000007) == 976371285
        assert power_mod(3, 50, 7) == 4
        assert power_mod(5, 3, 13) == 8
    
    def test_edge_cases(self):
        """Testa casos extremos."""
        assert power_mod(0, 5, 10) == 0
        assert power_mod(5, 0, 10) == 1
        assert power_mod(5, 10, 1) == 0
    
    def test_large_numbers(self):
        """Testa números grandes."""
        assert power_mod(2, 1000, 1000000007) == 56088
        assert power_mod(3, 500, 1000000007) == 930856309
    
    def test_invalid_inputs(self):
        """Testa entradas inválidas."""
        with pytest.raises(ValueError):
            power_mod(2, -1, 10)
        with pytest.raises(ValueError):
            power_mod(2, 5, 0)
        with pytest.raises(ValueError):
            power_mod(2, 5, -5)


class TestPerformanceComparison:
    """Testes para comparar performance com exponenciação tradicional."""
    
    def test_consistency_with_traditional(self):
        """Testa se o resultado é consistente com exponenciação tradicional."""
        test_cases = [
            (2, 10),
            (3, 5),
            (5, 3),
            (2, 8),
            (3, 4),
        ]
        
        for base, exponent in test_cases:
            expected = base ** exponent
            assert binary_exponentiation(base, exponent) == expected
            assert recursive_exponentiation(base, exponent) == expected
    
    def test_modular_consistency(self):
        """Testa consistência da exponenciação modular."""
        test_cases = [
            (2, 10, 1000),
            (3, 5, 7),
            (5, 3, 13),
            (2, 5, 10),
        ]
        
        for base, exponent, modulus in test_cases:
            expected = pow(base, exponent, modulus)
            assert modular_exponentiation(base, exponent, modulus) == expected
            assert power_mod(base, exponent, modulus) == expected


class TestEdgeCases:
    """Testes para casos extremos e especiais."""
    
    def test_zero_base_edge_cases(self):
        """Testa casos extremos com base zero."""
        assert binary_exponentiation(0, 0) == 1
        assert binary_exponentiation(0, 1) == 0
        assert binary_exponentiation(0, 10) == 0
    
    def test_one_base_edge_cases(self):
        """Testa casos extremos com base um."""
        assert binary_exponentiation(1, 0) == 1
        assert binary_exponentiation(1, 100) == 1
        assert binary_exponentiation(1, 1000) == 1
    
    def test_large_exponents_edge_cases(self):
        """Testa casos extremos com expoentes grandes."""
        assert binary_exponentiation(2, 30) == 1073741824
        assert modular_exponentiation(2, 30, 1000000007) == 73741817
    
    def test_fibonacci_edge_cases(self):
        """Testa casos extremos de Fibonacci."""
        assert fibonacci_fast(0) == 0
        assert fibonacci_fast(1) == 1
        assert fibonacci_fast(2) == 1
        assert fibonacci_fast(40) == 102334155


if __name__ == "__main__":
    pytest.main([__file__]) 