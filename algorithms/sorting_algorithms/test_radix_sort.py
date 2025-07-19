"""
Testes para Radix Sort
"""
import pytest
from .radix_sort import (
    radix_sort, 
    counting_sort_by_digit, 
    get_digit,
    radix_sort_strings,
    counting_sort_strings_by_position,
    msd_radix_sort
)


class TestRadixSort:
    
    def test_empty_list(self):
        """Testa ordenação de lista vazia"""
        result = radix_sort([])
        assert result == []
    
    def test_single_item(self):
        """Testa ordenação de lista com um item"""
        result = radix_sort([5])
        assert result == [5]
    
    def test_sorted_list(self):
        """Testa lista já ordenada"""
        result = radix_sort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted_list(self):
        """Testa lista ordenada em ordem reversa"""
        result = radix_sort([5, 4, 3, 2, 1])
        assert result == [1, 2, 3, 4, 5]
    
    def test_random_order(self):
        """Testa lista em ordem aleatória"""
        result = radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        assert result == [2, 24, 45, 66, 75, 90, 170, 802]
    
    def test_duplicate_values(self):
        """Testa valores duplicados (deve manter ordem relativa)"""
        result = radix_sort([3, 1, 3, 2, 1, 3])
        assert result == [1, 1, 2, 3, 3, 3]
    
    def test_all_same_values(self):
        """Testa lista com todos os valores iguais"""
        result = radix_sort([5, 5, 5, 5, 5])
        assert result == [5, 5, 5, 5, 5]
    
    def test_zero_values(self):
        """Testa valores zero"""
        result = radix_sort([5, 0, 3, 1, 0])
        assert result == [0, 0, 1, 3, 5]
    
    def test_large_numbers(self):
        """Testa números grandes"""
        result = radix_sort([1000, 100, 10, 1, 10000])
        assert result == [1, 10, 100, 1000, 10000]
    
    def test_different_base(self):
        """Testa com base diferente"""
        result = radix_sort([170, 45, 75, 90, 802, 24, 2, 66], base=10)
        assert result == [2, 24, 45, 66, 75, 90, 170, 802]
    
    def test_base_2(self):
        """Testa com base 2 (binária)"""
        result = radix_sort([5, 3, 7, 1, 9], base=2)
        assert result == [1, 3, 5, 7, 9]
    
    def test_negative_values_should_fail(self):
        """Testa que valores negativos causam erro"""
        with pytest.raises((IndexError, ValueError)):
            radix_sort([-1, 2, 3])


class TestCountingSortByDigit:
    """Testes para ordenação por dígito específico"""
    
    def test_empty_list(self):
        """Testa lista vazia"""
        result = counting_sort_by_digit([], 10, 0)
        assert result == []
    
    def test_single_digit(self):
        """Testa números de um dígito"""
        result = counting_sort_by_digit([5, 3, 7, 1, 9], 10, 0)
        assert result == [1, 3, 5, 7, 9]
    
    def test_two_digits(self):
        """Testa números de dois dígitos por dígito menos significativo"""
        result = counting_sort_by_digit([32, 15, 24, 11, 33], 10, 0)
        # Ordenado por dígito das unidades: 11, 32, 33, 24, 15
        assert result == [11, 32, 33, 24, 15]
    
    def test_two_digits_by_tens(self):
        """Testa números de dois dígitos por dígito das dezenas"""
        result = counting_sort_by_digit([32, 15, 24, 11, 33], 10, 1)
        # Ordenado por dígito das dezenas: 11, 15, 24, 32, 33
        assert result == [11, 15, 24, 32, 33]
    
    def test_different_base(self):
        """Testa com base diferente"""
        result = counting_sort_by_digit([5, 3, 7, 1, 9], 5, 0)
        assert result == [1, 3, 5, 7, 9]


class TestGetDigit:
    """Testes para extração de dígitos"""
    
    def test_ones_digit(self):
        """Testa dígito das unidades"""
        assert get_digit(123, 0, 10) == 3
        assert get_digit(456, 0, 10) == 6
        assert get_digit(789, 0, 10) == 9
    
    def test_tens_digit(self):
        """Testa dígito das dezenas"""
        assert get_digit(123, 1, 10) == 2
        assert get_digit(456, 1, 10) == 5
        assert get_digit(789, 1, 10) == 8
    
    def test_hundreds_digit(self):
        """Testa dígito das centenas"""
        assert get_digit(123, 2, 10) == 1
        assert get_digit(456, 2, 10) == 4
        assert get_digit(789, 2, 10) == 7
    
    def test_digit_beyond_number(self):
        """Testa dígito além do tamanho do número"""
        assert get_digit(123, 5, 10) == 0
        assert get_digit(45, 3, 10) == 0
    
    def test_different_base(self):
        """Testa com base diferente"""
        # 123 em base 8 = 1*8² + 7*8¹ + 3*8⁰ = 64 + 56 + 3 = 123
        assert get_digit(123, 0, 8) == 3  # resto da divisão por 8
        assert get_digit(123, 1, 8) == 7  # (123 // 8) % 8 = 15 % 8 = 7
        assert get_digit(123, 2, 8) == 1  # (123 // 64) % 8 = 1 % 8 = 1


class TestRadixSortStrings:
    """Testes para ordenação de strings"""
    
    def test_empty_list(self):
        """Testa lista vazia de strings"""
        result = radix_sort_strings([])
        assert result == []
    
    def test_single_string(self):
        """Testa uma string"""
        result = radix_sort_strings(["hello"])
        assert result == ["hello"]
    
    def test_same_length_strings(self):
        """Testa strings do mesmo comprimento"""
        result = radix_sort_strings(["cat", "bat", "rat", "hat"])
        assert result == ["bat", "cat", "hat", "rat"]
    
    def test_different_length_strings(self):
        """Testa strings de comprimentos diferentes"""
        result = radix_sort_strings(["cat", "bat", "rat", "a", "zoo"])
        assert result == ["a", "bat", "cat", "rat", "zoo"]
    
    def test_with_max_length(self):
        """Testa com comprimento máximo especificado"""
        result = radix_sort_strings(["cat", "bat", "rat"], max_length=3)
        assert result == ["bat", "cat", "rat"]
    
    def test_case_sensitive(self):
        """Testa que é sensível a maiúsculas/minúsculas"""
        result = radix_sort_strings(["Cat", "bat", "Rat", "hat"])
        assert result == ["Cat", "Rat", "bat", "hat"]
    
    def test_numbers_as_strings(self):
        """Testa números como strings"""
        result = radix_sort_strings(["100", "10", "1", "1000"])
        assert result == ["1", "10", "100", "1000"]


class TestCountingSortStringsByPosition:
    """Testes para ordenação de strings por posição"""
    
    def test_empty_list(self):
        """Testa lista vazia"""
        result = counting_sort_strings_by_position([], 0)
        assert result == []
    
    def test_single_string(self):
        """Testa uma string"""
        result = counting_sort_strings_by_position(["hello"], 0)
        assert result == ["hello"]
    
    def test_by_first_character(self):
        """Testa ordenação pelo primeiro caractere"""
        result = counting_sort_strings_by_position(["cat", "bat", "rat", "hat"], 0)
        assert result == ["bat", "cat", "hat", "rat"]
    
    def test_by_second_character(self):
        """Testa ordenação pelo segundo caractere"""
        result = counting_sort_strings_by_position(["cat", "bat", "rat", "hat"], 1)
        # Ordenado por 'a', 'a', 'a', 't'
        assert result == ["cat", "bat", "rat", "hat"]
    
    def test_position_beyond_string(self):
        """Testa posição além do comprimento da string"""
        result = counting_sort_strings_by_position(["cat", "bat", "rat"], 5)
        # Strings curtas são tratadas como tendo caractere '\0' nas posições vazias
        assert result == ["cat", "bat", "rat"]


class TestMSDRadixSort:
    """Testes para MSD Radix Sort"""
    
    def test_empty_list(self):
        """Testa lista vazia"""
        result = msd_radix_sort([])
        assert result == []
    
    def test_single_item(self):
        """Testa um item"""
        result = msd_radix_sort([5])
        assert result == [5]
    
    def test_sorted_list(self):
        """Testa lista já ordenada"""
        result = msd_radix_sort([1, 2, 3, 4, 5])
        assert result == [1, 2, 3, 4, 5]
    
    def test_random_order(self):
        """Testa lista em ordem aleatória"""
        result = msd_radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        assert result == [2, 24, 45, 66, 75, 90, 170, 802]
    
    def test_different_base(self):
        """Testa com base diferente"""
        result = msd_radix_sort([170, 45, 75, 90, 802, 24, 2, 66], base=10)
        assert result == [2, 24, 45, 66, 75, 90, 170, 802]


class TestEdgeCases:
    """Testes para casos extremos"""
    
    def test_very_large_numbers(self):
        """Testa números muito grandes"""
        result = radix_sort([1000000, 100000, 10000, 1000, 100, 10, 1])
        assert result == [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    def test_single_digit_numbers(self):
        """Testa números de um dígito"""
        result = radix_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_all_zeros(self):
        """Testa lista com todos os valores zero"""
        result = radix_sort([0, 0, 0, 0, 0])
        assert result == [0, 0, 0, 0, 0]
    
    def test_powers_of_two(self):
        """Testa potências de 2"""
        result = radix_sort([1, 2, 4, 8, 16, 32, 64, 128, 256, 512])
        assert result == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    
    def test_strings_with_special_characters(self):
        """Testa strings com caracteres especiais"""
        result = radix_sort_strings(["hello", "world", "test", "123", "!@#"])
        assert result == ["!@#", "123", "hello", "test", "world"]


class TestPerformance:
    """Testes de performance"""
    
    def test_large_list_performance(self):
        """Testa performance com lista grande"""
        import time
        
        # Criar lista grande
        large_list = list(range(1000, 0, -1))  # 1000 números em ordem reversa
        
        start_time = time.time()
        result = radix_sort(large_list)
        end_time = time.time()
        
        # Verificar que está ordenado
        assert result == list(range(1, 1001))
        
        # Verificar que não demorou muito (deve ser rápido)
        assert end_time - start_time < 1.0  # menos de 1 segundo
    
    def test_strings_performance(self):
        """Testa performance com strings"""
        import time
        
        # Criar lista de strings
        strings = [f"string_{i:03d}" for i in range(100, 0, -1)]
        
        start_time = time.time()
        result = radix_sort_strings(strings)
        end_time = time.time()
        
        # Verificar que está ordenado
        expected = [f"string_{i:03d}" for i in range(1, 101)]
        assert result == expected
        
        # Verificar que não demorou muito
        assert end_time - start_time < 1.0 