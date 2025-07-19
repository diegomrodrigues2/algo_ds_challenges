"""
Testes para Direct Access Array Sort
"""
import pytest
from .direct_access_array_sort import direct_access_array_sort, Item, create_items_from_list


class TestDirectAccessArraySort:
    
    def test_empty_list(self):
        """Testa ordenação de lista vazia"""
        result = direct_access_array_sort([])
        assert result == []
    
    def test_single_item(self):
        """Testa ordenação de lista com um item"""
        items = [Item(5, "test")]
        result = direct_access_array_sort(items)
        assert result == items
    
    def test_sorted_list(self):
        """Testa lista já ordenada"""
        items = create_items_from_list([1, 2, 3, 4, 5])
        result = direct_access_array_sort(items)
        expected = create_items_from_list([1, 2, 3, 4, 5])
        assert result == expected
    
    def test_reverse_sorted_list(self):
        """Testa lista ordenada em ordem reversa"""
        items = create_items_from_list([5, 4, 3, 2, 1])
        result = direct_access_array_sort(items)
        expected = create_items_from_list([1, 2, 3, 4, 5])
        assert result == expected
    
    def test_random_order(self):
        """Testa lista em ordem aleatória"""
        items = create_items_from_list([3, 1, 4, 1, 5, 9, 2, 6])
        result = direct_access_array_sort(items)
        expected = create_items_from_list([1, 1, 2, 3, 4, 5, 6, 9])
        assert result == expected
    
    def test_duplicate_keys(self):
        """Testa comportamento com chaves duplicadas (deve manter ordem relativa)"""
        items = [
            Item(3, "first_3"),
            Item(1, "first_1"),
            Item(3, "second_3"),
            Item(2, "only_2")
        ]
        result = direct_access_array_sort(items)
        # Deve manter a ordem relativa dos itens com chave 3
        assert result[0].key == 1
        assert result[1].key == 2
        assert result[2].key == 3 and result[2].value == "first_3"
        assert result[3].key == 3 and result[3].value == "second_3"
    
    def test_large_range(self):
        """Testa com faixa grande de chaves"""
        items = create_items_from_list([0, 100, 50, 25, 75])
        result = direct_access_array_sort(items)
        expected = create_items_from_list([0, 25, 50, 75, 100])
        assert result == expected
    
    def test_zero_key(self):
        """Testa chave zero"""
        items = create_items_from_list([5, 0, 3, 1])
        result = direct_access_array_sort(items)
        expected = create_items_from_list([0, 1, 3, 5])
        assert result == expected
    
    def test_consecutive_keys(self):
        """Testa chaves consecutivas"""
        items = create_items_from_list([10, 11, 12, 13, 14])
        result = direct_access_array_sort(items)
        expected = create_items_from_list([10, 11, 12, 13, 14])
        assert result == expected
    
    def test_sparse_keys(self):
        """Testa chaves esparsas"""
        items = create_items_from_list([1, 10, 100, 1000])
        result = direct_access_array_sort(items)
        expected = create_items_from_list([1, 10, 100, 1000])
        assert result == expected
    
    def test_negative_keys_should_fail(self):
        """Testa que chaves negativas causam erro"""
        items = [Item(-1, "negative")]
        with pytest.raises((IndexError, ValueError)):
            direct_access_array_sort(items)
    
    def test_preserves_item_objects(self):
        """Testa que os objetos Item originais são preservados"""
        original_items = [
            Item(3, "custom_value_1"),
            Item(1, "custom_value_2"),
            Item(2, "custom_value_3")
        ]
        result = direct_access_array_sort(original_items)
        
        # Verifica que são os mesmos objetos
        assert result[0] is original_items[1]  # key=1
        assert result[1] is original_items[2]  # key=2
        assert result[2] is original_items[0]  # key=3


class TestItemClass:
    """Testes para a classe Item auxiliar"""
    
    def test_item_creation(self):
        """Testa criação de Item"""
        item = Item(5, "test_value")
        assert item.key == 5
        assert item.value == "test_value"
    
    def test_item_equality(self):
        """Testa igualdade entre Items"""
        item1 = Item(1, "value1")
        item2 = Item(1, "value1")
        item3 = Item(1, "value2")
        item4 = Item(2, "value1")
        
        assert item1 == item2
        assert item1 != item3
        assert item1 != item4
        assert item1 != "not_an_item"
    
    def test_item_repr(self):
        """Testa representação string do Item"""
        item = Item(42, "answer")
        assert repr(item) == "Item(42, answer)"


class TestHelperFunctions:
    """Testes para funções auxiliares"""
    
    def test_create_items_from_list(self):
        """Testa criação de Items a partir de lista"""
        values = [1, 3, 2]
        items = create_items_from_list(values)
        
        assert len(items) == 3
        assert items[0].key == 1 and items[0].value == "value_1"
        assert items[1].key == 3 and items[1].value == "value_3"
        assert items[2].key == 2 and items[2].value == "value_2" 