import pytest
from .top_k_frequent import top_k_frequent, top_k_frequent_bucket


class TestTopKFrequent:
    """Testes para as funções top_k_frequent."""
    
    def test_empty_array(self):
        """Testa com array vazio."""
        assert top_k_frequent([], 1) == []
        assert top_k_frequent_bucket([], 1) == []
    
    def test_k_zero(self):
        """Testa com k = 0."""
        assert top_k_frequent([1, 2, 3], 0) == []
        assert top_k_frequent_bucket([1, 2, 3], 0) == []
    
    def test_k_greater_than_array_length(self):
        """Testa com k maior que o tamanho do array."""
        result1 = top_k_frequent([1, 2, 3], 5)
        result2 = top_k_frequent_bucket([1, 2, 3], 5)
        assert set(result1) == {1, 2, 3}
        assert set(result2) == {1, 2, 3}
    
    def test_single_element(self):
        """Testa com um único elemento."""
        assert top_k_frequent([1], 1) == [1]
        assert top_k_frequent_bucket([1], 1) == [1]
    
    def test_all_same_elements(self):
        """Testa com todos os elementos iguais."""
        assert top_k_frequent([1, 1, 1], 1) == [1]
        assert top_k_frequent_bucket([1, 1, 1], 1) == [1]
    
    def test_basic_case(self):
        """Testa caso básico."""
        nums = [1, 1, 1, 2, 2, 3]
        result1 = top_k_frequent(nums, 2)
        result2 = top_k_frequent_bucket(nums, 2)
        assert result1 == [1, 2]
        assert result2 == [1, 2]
    
    def test_three_frequencies(self):
        """Testa com três frequências diferentes."""
        nums = [1, 1, 1, 2, 2, 3]
        result1 = top_k_frequent(nums, 3)
        result2 = top_k_frequent_bucket(nums, 3)
        assert result1 == [1, 2, 3]
        assert result2 == [1, 2, 3]
    
    def test_negative_numbers(self):
        """Testa com números negativos."""
        nums = [-1, -1, -2, -2, -2, 3]
        result1 = top_k_frequent(nums, 2)
        result2 = top_k_frequent_bucket(nums, 2)
        assert result1 == [-2, -1]
        assert result2 == [-2, -1]
    
    def test_large_numbers(self):
        """Testa com números grandes."""
        nums = [1000, 1000, 2000, 2000, 2000, 3000]
        result1 = top_k_frequent(nums, 2)
        result2 = top_k_frequent_bucket(nums, 2)
        assert result1 == [2000, 1000]
        assert result2 == [2000, 1000]
    
    def test_mixed_frequencies(self):
        """Testa com frequências mistas."""
        nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        result1 = top_k_frequent(nums, 3)
        result2 = top_k_frequent_bucket(nums, 3)
        assert result1 == [1, 2, 3]
        assert result2 == [1, 2, 3]
    
    def test_k_equals_one(self):
        """Testa com k = 1."""
        nums = [1, 1, 1, 2, 2, 3]
        result1 = top_k_frequent(nums, 1)
        result2 = top_k_frequent_bucket(nums, 1)
        assert result1 == [1]
        assert result2 == [1]
    
    def test_consistency_between_methods(self):
        """Testa se ambos os métodos produzem o mesmo resultado."""
        nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
        for k in range(1, 5):
            result1 = top_k_frequent(nums, k)
            result2 = top_k_frequent_bucket(nums, k)
            assert result1 == result2 