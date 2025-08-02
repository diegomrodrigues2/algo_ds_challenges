"""
Testes para o algoritmo de Karatsuba de multiplicação rápida.

Este módulo contém testes abrangentes para validar a implementação
do algoritmo de Karatsuba, incluindo casos básicos, casos extremos
e comparações com multiplicação tradicional.
"""

import pytest
from .karatsuba import (
    add_strings,
    subtract_strings,
    remove_leading_zeros,
    karatsuba_multiply,
    multiply_large_numbers
)


class TestAddStrings:
    """Testes para a função add_strings."""
    
    def test_basic_addition(self):
        """Testa adição básica de números."""
        assert add_strings("123", "456") == "579"
        assert add_strings("999", "1") == "1000"
        assert add_strings("0", "0") == "0"
    
    def test_different_lengths(self):
        """Testa adição com números de comprimentos diferentes."""
        assert add_strings("123", "4567") == "4690"
        assert add_strings("4567", "123") == "4690"
        assert add_strings("1", "999") == "1000"
    
    def test_carry_operations(self):
        """Testa operações com carry."""
        assert add_strings("999", "999") == "1998"
        assert add_strings("9999", "1") == "10000"
        assert add_strings("555", "555") == "1110"
    
    def test_large_numbers(self):
        """Testa adição de números grandes."""
        a = "12345678901234567890"
        b = "98765432109876543210"
        expected = "111111111011111111100"
        assert add_strings(a, b) == expected


class TestSubtractStrings:
    """Testes para a função subtract_strings."""
    
    def test_basic_subtraction(self):
        """Testa subtração básica de números."""
        assert subtract_strings("456", "123") == "333"
        assert subtract_strings("1000", "1") == "999"
        assert subtract_strings("123", "123") == "0"
    
    def test_different_lengths(self):
        """Testa subtração com números de comprimentos diferentes."""
        assert subtract_strings("4567", "123") == "4444"
        assert subtract_strings("1000", "999") == "1"
    
    def test_borrow_operations(self):
        """Testa operações com borrow."""
        assert subtract_strings("1000", "1") == "999"
        assert subtract_strings("10000", "1") == "9999"
        assert subtract_strings("555", "556") == "999"  # Resultado negativo não tratado
    
    def test_edge_cases(self):
        """Testa casos extremos de subtração."""
        assert subtract_strings("0", "0") == "0"
        assert subtract_strings("123", "0") == "123"


class TestRemoveLeadingZeros:
    """Testes para a função remove_leading_zeros."""
    
    def test_basic_removal(self):
        """Testa remoção básica de zeros à esquerda."""
        assert remove_leading_zeros("00123") == "123"
        assert remove_leading_zeros("123") == "123"
        assert remove_leading_zeros("0") == "0"
    
    def test_all_zeros(self):
        """Testa strings com apenas zeros."""
        assert remove_leading_zeros("000") == "0"
        assert remove_leading_zeros("00") == "0"
    
    def test_no_leading_zeros(self):
        """Testa strings sem zeros à esquerda."""
        assert remove_leading_zeros("123") == "123"
        assert remove_leading_zeros("1") == "1"


class TestKaratsubaMultiply:
    """Testes para a função karatsuba_multiply."""
    
    def test_single_digit_multiplication(self):
        """Testa multiplicação de dígitos únicos."""
        assert karatsuba_multiply("5", "7") == "35"
        assert karatsuba_multiply("9", "9") == "81"
        assert karatsuba_multiply("0", "5") == "0"
    
    def test_small_numbers(self):
        """Testa multiplicação de números pequenos."""
        assert karatsuba_multiply("12", "34") == "408"
        assert karatsuba_multiply("99", "99") == "9801"
        assert karatsuba_multiply("123", "456") == "56088"
    
    def test_medium_numbers(self):
        """Testa multiplicação de números médios."""
        assert karatsuba_multiply("1234", "5678") == "7006652"
        assert karatsuba_multiply("9999", "9999") == "99980001"
    
    def test_large_numbers(self):
        """Testa multiplicação de números grandes."""
        a = "123456789"
        b = "987654321"
        expected = "121932631112635269"
        assert karatsuba_multiply(a, b) == expected
    
    def test_very_large_numbers(self):
        """Testa multiplicação de números muito grandes."""
        a = "123456789012345678901234567890"
        b = "987654321098765432109876543210"
        # Resultado esperado calculado externamente
        expected = "121932631137021795226185032733622923332237463801111263526900"
        assert karatsuba_multiply(a, b) == expected
    
    def test_numbers_with_leading_zeros(self):
        """Testa multiplicação com zeros à esquerda."""
        assert karatsuba_multiply("00123", "00456") == "56088"
        assert karatsuba_multiply("000", "123") == "0"
    
    def test_power_of_ten_multiplication(self):
        """Testa multiplicação por potências de 10."""
        assert karatsuba_multiply("100", "100") == "10000"
        assert karatsuba_multiply("1000", "1000") == "1000000"


class TestMultiplyLargeNumbers:
    """Testes para a função multiply_large_numbers."""
    
    def test_basic_multiplication(self):
        """Testa multiplicação básica."""
        assert multiply_large_numbers("123", "456") == "56088"
        assert multiply_large_numbers("999", "999") == "998001"
    
    def test_zero_multiplication(self):
        """Testa multiplicação por zero."""
        assert multiply_large_numbers("0", "123") == "0"
        assert multiply_large_numbers("123", "0") == "0"
        assert multiply_large_numbers("0", "0") == "0"
    
    def test_empty_strings(self):
        """Testa strings vazias."""
        assert multiply_large_numbers("", "123") == "0"
        assert multiply_large_numbers("123", "") == "0"
        assert multiply_large_numbers("", "") == "0"
    
    def test_invalid_input(self):
        """Testa entrada inválida."""
        with pytest.raises(ValueError):
            multiply_large_numbers("123a", "456")
        with pytest.raises(ValueError):
            multiply_large_numbers("123", "456b")
        with pytest.raises(ValueError):
            multiply_large_numbers("12.3", "456")
    
    def test_large_numbers(self):
        """Testa números muito grandes."""
        a = "74638463789"
        b = "35284567382"
        expected = "2633585904851937530398"
        assert multiply_large_numbers(a, b) == expected


class TestPerformanceComparison:
    """Testes para comparar performance com multiplicação tradicional."""
    
    def test_consistency_with_traditional(self):
        """Testa se o resultado é consistente com multiplicação tradicional."""
        test_cases = [
            ("123", "456"),
            ("9999", "9999"),
            ("123456789", "987654321"),
            ("1000000", "1000000"),
        ]
        
        for a, b in test_cases:
            # Resultado esperado usando multiplicação tradicional
            expected = str(int(a) * int(b))
            assert karatsuba_multiply(a, b) == expected
            assert multiply_large_numbers(a, b) == expected


class TestEdgeCases:
    """Testes para casos extremos e especiais."""
    
    def test_single_digit_edge_cases(self):
        """Testa casos extremos com dígitos únicos."""
        assert karatsuba_multiply("0", "0") == "0"
        assert karatsuba_multiply("1", "1") == "1"
        assert karatsuba_multiply("9", "9") == "81"
    
    def test_palindrome_numbers(self):
        """Testa números palíndromos."""
        assert karatsuba_multiply("121", "121") == "14641"
        assert karatsuba_multiply("12321", "12321") == "151807041"
    
    def test_repeated_digits(self):
        """Testa números com dígitos repetidos."""
        assert karatsuba_multiply("111", "111") == "12321"
        assert karatsuba_multiply("999", "999") == "998001"
    
    def test_power_of_two_numbers(self):
        """Testa números que são potências de 2."""
        assert karatsuba_multiply("1024", "1024") == "1048576"
        assert karatsuba_multiply("2048", "2048") == "4194304"


if __name__ == "__main__":
    pytest.main([__file__]) 