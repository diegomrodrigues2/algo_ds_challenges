"""
Testes para Merge Sort
"""

import pytest
from .merge_sort import (
    merge_sort, 
    merge_sort_inplace, 
    merge, 
    merge_inplace, 
    count_inversions
)


class TestMerge:
    """Testes para a função merge"""
    
    def test_merge_basic(self):
        """Testa merge básico de dois arrays ordenados"""
        left = [1, 3, 5]
        right = [2, 4, 6]
        result = merge(left, right)
        assert result == [1, 2, 3, 4, 5, 6]
    
    def test_merge_different_sizes(self):
        """Testa merge de arrays com tamanhos diferentes"""
        left = [1, 2]
        right = [3, 4, 5]
        result = merge(left, right)
        assert result == [1, 2, 3, 4, 5]
        
        left = [1, 2, 3, 4]
        right = [5]
        result = merge(left, right)
        assert result == [1, 2, 3, 4, 5]
    
    def test_merge_empty_arrays(self):
        """Testa merge com arrays vazios"""
        assert merge([], [1, 2, 3]) == [1, 2, 3]
        assert merge([1, 2, 3], []) == [1, 2, 3]
        assert merge([], []) == []
    
    def test_merge_duplicates(self):
        """Testa merge com elementos duplicados"""
        left = [1, 2, 2, 3]
        right = [2, 3, 4]
        result = merge(left, right)
        assert result == [1, 2, 2, 2, 3, 3, 4]
    
    def test_merge_negative_numbers(self):
        """Testa merge com números negativos"""
        left = [-5, -3, -1]
        right = [-4, -2, 0]
        result = merge(left, right)
        assert result == [-5, -4, -3, -2, -1, 0]


class TestMergeInplace:
    """Testes para a função merge_inplace"""
    
    def test_merge_inplace_basic(self):
        """Testa merge in-place básico"""
        arr = [1, 3, 5, 2, 4, 6]
        merge_inplace(arr, 0, 2, 5)
        assert arr == [1, 2, 3, 4, 5, 6]
    
    def test_merge_inplace_different_sizes(self):
        """Testa merge in-place com subarrays de tamanhos diferentes"""
        arr = [1, 2, 4, 5, 3]
        merge_inplace(arr, 0, 3, 4)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_merge_inplace_duplicates(self):
        """Testa merge in-place com elementos duplicados"""
        arr = [1, 2, 2, 3, 2, 3, 4]
        merge_inplace(arr, 0, 3, 6)
        assert arr == [1, 2, 2, 2, 3, 3, 4]


class TestMergeSort:
    """Testes para a função merge_sort"""
    
    def test_merge_sort_basic(self):
        """Testa ordenação básica"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = merge_sort(arr)
        assert result == [11, 12, 22, 25, 34, 64, 90]
        # Array original não deve ser modificado
        assert arr == [64, 34, 25, 12, 22, 11, 90]
    
    def test_merge_sort_already_sorted(self):
        """Testa ordenação de array já ordenado"""
        arr = [1, 2, 3, 4, 5]
        result = merge_sort(arr)
        assert result == [1, 2, 3, 4, 5]
    
    def test_merge_sort_reverse_sorted(self):
        """Testa ordenação de array em ordem reversa"""
        arr = [5, 4, 3, 2, 1]
        result = merge_sort(arr)
        assert result == [1, 2, 3, 4, 5]
    
    def test_merge_sort_duplicates(self):
        """Testa ordenação com elementos duplicados"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = merge_sort(arr)
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_merge_sort_empty(self):
        """Testa ordenação de array vazio"""
        arr = []
        result = merge_sort(arr)
        assert result == []
    
    def test_merge_sort_single_element(self):
        """Testa ordenação de array com um elemento"""
        arr = [42]
        result = merge_sort(arr)
        assert result == [42]
    
    def test_merge_sort_negative_numbers(self):
        """Testa ordenação com números negativos"""
        arr = [-5, 10, -3, 0, 7, -1]
        result = merge_sort(arr)
        assert result == [-5, -3, -1, 0, 7, 10]
    
    def test_merge_sort_large_array(self):
        """Testa ordenação de array grande"""
        arr = list(range(100, 0, -1))  # 100 a 1 em ordem reversa
        result = merge_sort(arr)
        assert result == list(range(1, 101))  # 1 a 100 em ordem


class TestMergeSortInplace:
    """Testes para a função merge_sort_inplace"""
    
    def test_merge_sort_inplace_basic(self):
        """Testa ordenação in-place básica"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        merge_sort_inplace(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_merge_sort_inplace_already_sorted(self):
        """Testa ordenação in-place de array já ordenado"""
        arr = [1, 2, 3, 4, 5]
        original = arr.copy()
        merge_sort_inplace(arr)
        assert arr == original
    
    def test_merge_sort_inplace_duplicates(self):
        """Testa ordenação in-place com elementos duplicados"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        merge_sort_inplace(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_merge_sort_inplace_empty(self):
        """Testa ordenação in-place de array vazio"""
        arr = []
        merge_sort_inplace(arr)
        assert arr == []
    
    def test_merge_sort_inplace_single_element(self):
        """Testa ordenação in-place de array com um elemento"""
        arr = [42]
        merge_sort_inplace(arr)
        assert arr == [42]
    
    def test_merge_sort_inplace_partial(self):
        """Testa ordenação in-place de parte do array"""
        arr = [5, 4, 3, 2, 1, 9, 8, 7]
        merge_sort_inplace(arr, 0, 4)  # Ordena apenas os primeiros 5 elementos
        assert arr == [1, 2, 3, 4, 5, 9, 8, 7]


class TestCountInversions:
    """Testes para a função count_inversions"""
    
    def test_count_inversions_basic(self):
        """Testa contagem básica de inversões"""
        arr = [2, 4, 1, 3, 5]
        assert count_inversions(arr) == 3
    
    def test_count_inversions_sorted(self):
        """Testa contagem em array ordenado"""
        arr = [1, 2, 3, 4, 5]
        assert count_inversions(arr) == 0
    
    def test_count_inversions_reverse_sorted(self):
        """Testa contagem em array em ordem reversa"""
        arr = [5, 4, 3, 2, 1]
        assert count_inversions(arr) == 10  # n*(n-1)/2 = 5*4/2 = 10
    
    def test_count_inversions_duplicates(self):
        """Testa contagem com elementos duplicados"""
        arr = [2, 2, 2, 2]
        assert count_inversions(arr) == 0  # Elementos iguais não são inversões
    
    def test_count_inversions_empty(self):
        """Testa contagem em array vazio"""
        arr = []
        assert count_inversions(arr) == 0
    
    def test_count_inversions_single_element(self):
        """Testa contagem em array com um elemento"""
        arr = [42]
        assert count_inversions(arr) == 0


class TestMergeSortProperties:
    """Testes para verificar propriedades do Merge Sort"""
    
    def test_merge_sort_stability(self):
        """Testa que Merge Sort é estável"""
        # Criando objetos com valores iguais mas identidades diferentes
        class Item:
            def __init__(self, value, id):
                self.value = value
                self.id = id
            
            def __lt__(self, other):
                return self.value < other.value
            
            def __eq__(self, other):
                return self.value == other.value
        
        arr = [Item(1, 1), Item(2, 1), Item(1, 2), Item(2, 2)]
        result = merge_sort(arr)
        
        # Merge Sort é estável, então a ordem relativa deve ser mantida
        assert [item.value for item in result] == [1, 1, 2, 2]
        # Verifica que a ordem dos IDs foi mantida para valores iguais
        assert result[0].id == 1 and result[1].id == 2  # Ambos têm value=1
        assert result[2].id == 1 and result[3].id == 2  # Ambos têm value=2
    
    def test_merge_sort_not_inplace(self):
        """Testa que merge_sort não modifica o array original"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        original_id = id(arr)
        result = merge_sort(arr)
        # O array original deve ser o mesmo objeto
        assert id(arr) == original_id
        # Mas o resultado deve ser um novo objeto
        assert id(result) != original_id 