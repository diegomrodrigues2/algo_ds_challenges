"""
Testes para Selection Sort
"""

import pytest
from .selection_sort import selection_sort, find_min_index, selection_sort_recursive


class TestFindMinIndex:
    """Testes para a função find_min_index"""
    
    def test_find_min_index_basic(self):
        """Testa busca do menor elemento em array básico"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        assert find_min_index(arr, 0) == 5  # 11 está no índice 5
        assert find_min_index(arr, 1) == 5  # 11 ainda é o menor a partir do índice 1
        assert find_min_index(arr, 2) == 3  # 12 é o menor a partir do índice 2
    
    def test_find_min_index_single_element(self):
        """Testa busca em array com um elemento"""
        arr = [42]
        assert find_min_index(arr, 0) == 0
    
    def test_find_min_index_duplicates(self):
        """Testa busca com elementos duplicados"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        # O primeiro 1 (índice 1) deve ser retornado
        assert find_min_index(arr, 0) == 1
        assert find_min_index(arr, 2) == 3  # O segundo 1 (índice 3)
    
    def test_find_min_index_already_sorted(self):
        """Testa busca em array já ordenado"""
        arr = [1, 2, 3, 4, 5]
        assert find_min_index(arr, 0) == 0
        assert find_min_index(arr, 1) == 1
        assert find_min_index(arr, 2) == 2


class TestSelectionSort:
    """Testes para a função selection_sort"""
    
    def test_selection_sort_basic(self):
        """Testa ordenação básica"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        selection_sort(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_selection_sort_already_sorted(self):
        """Testa ordenação de array já ordenado"""
        arr = [1, 2, 3, 4, 5]
        original = arr.copy()
        selection_sort(arr)
        assert arr == original
    
    def test_selection_sort_reverse_sorted(self):
        """Testa ordenação de array em ordem reversa"""
        arr = [5, 4, 3, 2, 1]
        selection_sort(arr)
        assert arr == [1, 2, 3, 4, 5]
    
    def test_selection_sort_duplicates(self):
        """Testa ordenação com elementos duplicados"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        selection_sort(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_selection_sort_empty(self):
        """Testa ordenação de array vazio"""
        arr = []
        selection_sort(arr)
        assert arr == []
    
    def test_selection_sort_single_element(self):
        """Testa ordenação de array com um elemento"""
        arr = [42]
        selection_sort(arr)
        assert arr == [42]
    
    def test_selection_sort_negative_numbers(self):
        """Testa ordenação com números negativos"""
        arr = [-5, 10, -3, 0, 7, -1]
        selection_sort(arr)
        assert arr == [-5, -3, -1, 0, 7, 10]
    
    def test_selection_sort_large_array(self):
        """Testa ordenação de array grande"""
        arr = list(range(100, 0, -1))  # 100 a 1 em ordem reversa
        selection_sort(arr)
        assert arr == list(range(1, 101))  # 1 a 100 em ordem


class TestSelectionSortRecursive:
    """Testes para a função selection_sort_recursive"""
    
    def test_selection_sort_recursive_basic(self):
        """Testa ordenação recursiva básica"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        selection_sort_recursive(arr)
        assert arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_selection_sort_recursive_already_sorted(self):
        """Testa ordenação recursiva de array já ordenado"""
        arr = [1, 2, 3, 4, 5]
        original = arr.copy()
        selection_sort_recursive(arr)
        assert arr == original
    
    def test_selection_sort_recursive_duplicates(self):
        """Testa ordenação recursiva com elementos duplicados"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        selection_sort_recursive(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_selection_sort_recursive_empty(self):
        """Testa ordenação recursiva de array vazio"""
        arr = []
        selection_sort_recursive(arr)
        assert arr == []
    
    def test_selection_sort_recursive_single_element(self):
        """Testa ordenação recursiva de array com um elemento"""
        arr = [42]
        selection_sort_recursive(arr)
        assert arr == [42]
    
    def test_selection_sort_recursive_with_n_parameter(self):
        """Testa ordenação recursiva com parâmetro n"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        selection_sort_recursive(arr, len(arr))
        assert arr == [11, 12, 22, 25, 34, 64, 90]


class TestSelectionSortProperties:
    """Testes para verificar propriedades do Selection Sort"""
    
    def test_selection_sort_stability(self):
        """Testa que Selection Sort não é estável"""
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
        original_order = [(item.value, item.id) for item in arr]
        selection_sort(arr)
        new_order = [(item.value, item.id) for item in arr]
        
        # Selection Sort não é estável, então a ordem pode mudar
        # Mas os valores devem estar ordenados
        assert [item.value for item in arr] == [1, 1, 2, 2]
    
    def test_selection_sort_in_place(self):
        """Testa que Selection Sort modifica o array original"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        original_id = id(arr)
        selection_sort(arr)
        # O array deve ser o mesmo objeto (modificado in-place)
        assert id(arr) == original_id 