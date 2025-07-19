import pytest
from .sliding_window_median import sliding_window_median


class TestSlidingWindowMedian:
    """Testes para a função sliding_window_median."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        assert sliding_window_median([], 1) == []
    
    def test_k_zero(self):
        """Testa com k = 0."""
        assert sliding_window_median([1, 2, 3], 0) == []
    
    def test_k_greater_than_array_length(self):
        """Testa com k maior que o tamanho do array."""
        assert sliding_window_median([1, 2, 3], 5) == []
    
    def test_k_equals_array_length(self):
        """Testa com k igual ao tamanho do array."""
        result = sliding_window_median([1, 2, 3], 3)
        assert len(result) == 1
        assert result[0] == 2.0
    
    def test_single_element(self):
        """Testa com um único elemento."""
        result = sliding_window_median([5], 1)
        assert result == [5.0]
    
    def test_basic_case(self):
        """Testa caso básico."""
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        result = sliding_window_median(nums, k)
        expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        assert result == expected
    
    def test_window_size_one(self):
        """Testa com janela de tamanho 1."""
        nums = [1, 2, 3, 4, 5]
        result = sliding_window_median(nums, 1)
        expected = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert result == expected
    
    def test_window_size_two(self):
        """Testa com janela de tamanho 2."""
        nums = [1, 2, 3, 4, 5]
        result = sliding_window_median(nums, 2)
        expected = [1.5, 2.5, 3.5, 4.5]
        assert result == expected
    
    def test_negative_numbers(self):
        """Testa com números negativos."""
        nums = [-1, -2, -3, -4, -5]
        k = 3
        result = sliding_window_median(nums, k)
        expected = [-2.0, -3.0, -4.0]
        assert result == expected
    
    def test_duplicate_numbers(self):
        """Testa com números duplicados."""
        nums = [1, 1, 1, 1, 1]
        k = 3
        result = sliding_window_median(nums, k)
        expected = [1.0, 1.0, 1.0]
        assert result == expected
    
    def test_mixed_numbers(self):
        """Testa com números mistos."""
        nums = [1, -1, 2, -2, 3, -3]
        k = 4
        result = sliding_window_median(nums, k)
        expected = [0.0, 0.5, 0.0]
        assert result == expected
    
    def test_large_numbers(self):
        """Testa com números grandes."""
        nums = [1000, 2000, 3000, 4000, 5000]
        k = 3
        result = sliding_window_median(nums, k)
        expected = [2000.0, 3000.0, 4000.0]
        assert result == expected
    
    def test_odd_window_size(self):
        """Testa com janela de tamanho ímpar."""
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 5
        result = sliding_window_median(nums, k)
        expected = [3.0, 4.0, 5.0]
        assert result == expected
    
    def test_even_window_size(self):
        """Testa com janela de tamanho par."""
        nums = [1, 2, 3, 4, 5, 6]
        k = 4
        result = sliding_window_median(nums, k)
        expected = [2.5, 3.5, 4.5]
        assert result == expected
    
    def test_single_window(self):
        """Testa com apenas uma janela possível."""
        nums = [1, 2, 3]
        k = 3
        result = sliding_window_median(nums, k)
        expected = [2.0]
        assert result == expected 