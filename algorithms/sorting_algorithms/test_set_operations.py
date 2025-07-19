"""
Testes para Set Operations
"""

import pytest
from .set_operations import (
    UnorderedSet, 
    OrderedSet, 
    binary_search
)


class TestBinarySearch:
    """Testes para a função binary_search"""
    
    def test_binary_search_basic(self):
        """Testa busca binária básica"""
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 3) == 2
        assert binary_search(arr, 1) == 0
        assert binary_search(arr, 5) == 4
    
    def test_binary_search_not_found(self):
        """Testa busca binária quando elemento não existe"""
        arr = [1, 2, 3, 4, 5]
        assert binary_search(arr, 6) == -1
        assert binary_search(arr, 0) == -1
    
    def test_binary_search_empty(self):
        """Testa busca binária em array vazio"""
        arr = []
        assert binary_search(arr, 1) == -1
    
    def test_binary_search_single_element(self):
        """Testa busca binária em array com um elemento"""
        arr = [42]
        assert binary_search(arr, 42) == 0
        assert binary_search(arr, 41) == -1
    
    def test_binary_search_duplicates(self):
        """Testa busca binária com elementos duplicados"""
        arr = [1, 2, 2, 2, 3, 4]
        # Pode retornar qualquer índice do elemento 2
        result = binary_search(arr, 2)
        assert result in [1, 2, 3]


class TestUnorderedSet:
    """Testes para a classe UnorderedSet"""
    
    def test_unordered_set_build(self):
        """Testa construção do set não ordenado"""
        s = UnorderedSet()
        s.build([1, 2, 3, 2, 4])
        # Remove duplicatas mas mantém ordem de inserção
        assert len(s.elements) == 4
        assert 1 in s.elements
        assert 2 in s.elements
        assert 3 in s.elements
        assert 4 in s.elements
    
    def test_unordered_set_find(self):
        """Testa busca no set não ordenado"""
        s = UnorderedSet()
        s.build([1, 2, 3, 4])
        assert s.find(3) == 3
        assert s.find(5) is None
        assert s.find(1) == 1
    
    def test_unordered_set_insert(self):
        """Testa inserção no set não ordenado"""
        s = UnorderedSet()
        assert s.insert(1) is True
        assert s.insert(2) is True
        assert s.insert(1) is False  # Já existe
        assert len(s.elements) == 2
    
    def test_unordered_set_delete(self):
        """Testa remoção no set não ordenado"""
        s = UnorderedSet()
        s.build([1, 2, 3, 4])
        assert s.delete(3) is True
        assert s.find(3) is None
        assert s.delete(5) is False
        assert len(s.elements) == 3
    
    def test_unordered_set_find_min_max(self):
        """Testa busca de mínimo e máximo no set não ordenado"""
        s = UnorderedSet()
        s.build([3, 1, 4, 2])
        assert s.find_min() == 1
        assert s.find_max() == 4
    
    def test_unordered_set_length(self):
        """Testa contagem de elementos no set não ordenado"""
        s = UnorderedSet()
        assert s.length() == 0
        s.build([1, 2, 3])
        assert s.length() == 3
        s.delete(2)
        assert s.length() == 2
    
    def test_unordered_set_empty(self):
        """Testa operações em set vazio"""
        s = UnorderedSet()
        assert s.find(1) is None
        assert s.find_min() is None
        assert s.find_max() is None
        assert s.delete(1) is False


class TestOrderedSet:
    """Testes para a classe OrderedSet"""
    
    def test_ordered_set_build(self):
        """Testa construção do set ordenado"""
        s = OrderedSet()
        s.build([3, 1, 4, 2])
        assert s.elements == [1, 2, 3, 4]
    
    def test_ordered_set_find(self):
        """Testa busca no set ordenado"""
        s = OrderedSet()
        s.build([1, 2, 3, 4])
        assert s.find(3) == 3
        assert s.find(5) is None
        assert s.find(1) == 1
    
    def test_ordered_set_insert(self):
        """Testa inserção no set ordenado"""
        s = OrderedSet()
        assert s.insert(3) is True
        assert s.insert(1) is True
        assert s.elements == [1, 3]
        assert s.insert(2) is True
        assert s.elements == [1, 2, 3]
        assert s.insert(1) is False  # Já existe
    
    def test_ordered_set_delete(self):
        """Testa remoção no set ordenado"""
        s = OrderedSet()
        s.build([1, 2, 3, 4])
        assert s.delete(3) is True
        assert s.elements == [1, 2, 4]
        assert s.delete(5) is False
        assert s.elements == [1, 2, 4]
    
    def test_ordered_set_find_min_max(self):
        """Testa busca de mínimo e máximo no set ordenado"""
        s = OrderedSet()
        s.build([3, 1, 4, 2])
        assert s.find_min() == 1
        assert s.find_max() == 4
    
    def test_ordered_set_length(self):
        """Testa contagem de elementos no set ordenado"""
        s = OrderedSet()
        assert s.length() == 0
        s.build([1, 2, 3])
        assert s.length() == 3
        s.delete(2)
        assert s.length() == 2
    
    def test_ordered_set_empty(self):
        """Testa operações em set vazio"""
        s = OrderedSet()
        assert s.find(1) is None
        assert s.find_min() is None
        assert s.find_max() is None
        assert s.delete(1) is False


class TestSetComparison:
    """Testes comparando as duas implementações de Set"""
    
    def test_build_complexity_difference(self):
        """Testa que OrderedSet ordena durante build"""
        unordered = UnorderedSet()
        ordered = OrderedSet()
        
        items = [3, 1, 4, 2]
        unordered.build(items)
        ordered.build(items)
        
        # UnorderedSet mantém ordem de inserção (sem duplicatas)
        # OrderedSet ordena os elementos
        assert unordered.elements != ordered.elements
        assert ordered.elements == [1, 2, 3, 4]
    
    def test_find_performance_difference(self):
        """Testa que ambas implementações retornam os mesmos resultados"""
        unordered = UnorderedSet()
        ordered = OrderedSet()
        
        items = [1, 2, 3, 4, 5]
        unordered.build(items)
        ordered.build(items)
        
        # Ambas devem encontrar os mesmos elementos
        for item in items:
            assert unordered.find(item) == ordered.find(item)
            assert unordered.find(item + 10) == ordered.find(item + 10)
    
    def test_insert_behavior_difference(self):
        """Testa diferença no comportamento de inserção"""
        unordered = UnorderedSet()
        ordered = OrderedSet()
        
        # Inserção sequencial
        unordered.insert(3)
        unordered.insert(1)
        unordered.insert(2)
        
        ordered.insert(3)
        ordered.insert(1)
        ordered.insert(2)
        
        # UnorderedSet mantém ordem de inserção
        # OrderedSet mantém ordem crescente
        assert unordered.elements != ordered.elements
        assert ordered.elements == [1, 2, 3]
    
    def test_min_max_behavior(self):
        """Testa que ambas implementações retornam os mesmos min/max"""
        unordered = UnorderedSet()
        ordered = OrderedSet()
        
        items = [3, 1, 4, 2, 5]
        unordered.build(items)
        ordered.build(items)
        
        assert unordered.find_min() == ordered.find_min()
        assert unordered.find_max() == ordered.find_max()


class TestSetEdgeCases:
    """Testes para casos extremos"""
    
    def test_large_sets(self):
        """Testa sets com muitos elementos"""
        unordered = UnorderedSet()
        ordered = OrderedSet()
        
        items = list(range(100))
        unordered.build(items)
        ordered.build(items)
        
        assert unordered.length() == 100
        assert ordered.length() == 100
        assert unordered.find_min() == 0
        assert ordered.find_min() == 0
        assert unordered.find_max() == 99
        assert ordered.find_max() == 99
    
    def test_duplicate_handling(self):
        """Testa tratamento de duplicatas"""
        unordered = UnorderedSet()
        ordered = OrderedSet()
        
        items = [1, 2, 2, 3, 3, 3, 4]
        unordered.build(items)
        ordered.build(items)
        
        # Ambos devem remover duplicatas
        assert unordered.length() == 4
        assert ordered.length() == 4
        assert ordered.elements == [1, 2, 3, 4]
    
    def test_negative_numbers(self):
        """Testa com números negativos"""
        unordered = UnorderedSet()
        ordered = OrderedSet()
        
        items = [-5, 10, -3, 0, 7, -1]
        unordered.build(items)
        ordered.build(items)
        
        assert unordered.find_min() == -5
        assert ordered.find_min() == -5
        assert unordered.find_max() == 10
        assert ordered.find_max() == 10 