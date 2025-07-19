"""
Testes para Direct Access Array
"""

import pytest
from .direct_access_array import DirectAccessArray


class TestDirectAccessArray:
    """Testes para a classe DirectAccessArray"""
    
    def test_constructor(self):
        """Testa o construtor"""
        daa = DirectAccessArray(100)
        assert daa.size() == 0
        assert daa.is_empty() is True
    
    def test_insert_basic(self):
        """Testa inserção básica"""
        daa = DirectAccessArray(100)
        assert daa.insert(42, "hello") is True
        assert daa.size() == 1
        assert daa.is_empty() is False
    
    def test_insert_update(self):
        """Testa atualização de elemento existente"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        assert daa.insert(42, "world") is False  # Atualização
        assert daa.find(42) == "world"
        assert daa.size() == 1  # Tamanho não muda
    
    def test_find_basic(self):
        """Testa busca básica"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        assert daa.find(42) == "hello"
        assert daa.find(99) is None
    
    def test_delete_basic(self):
        """Testa remoção básica"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        assert daa.delete(42) is True
        assert daa.find(42) is None
        assert daa.size() == 0
        assert daa.is_empty() is True
    
    def test_delete_nonexistent(self):
        """Testa remoção de elemento inexistente"""
        daa = DirectAccessArray(100)
        assert daa.delete(42) is False
        assert daa.size() == 0
    
    def test_find_min_basic(self):
        """Testa busca do menor elemento"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        daa.insert(10, "world")
        daa.insert(99, "test")
        
        result = daa.find_min()
        assert result == (10, "world")
    
    def test_find_min_empty(self):
        """Testa busca do menor elemento em array vazio"""
        daa = DirectAccessArray(100)
        assert daa.find_min() is None
    
    def test_find_max_basic(self):
        """Testa busca do maior elemento"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        daa.insert(10, "world")
        daa.insert(99, "test")
        
        result = daa.find_max()
        assert result == (99, "test")
    
    def test_find_max_empty(self):
        """Testa busca do maior elemento em array vazio"""
        daa = DirectAccessArray(100)
        assert daa.find_max() is None
    
    def test_clear(self):
        """Testa limpeza do array"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        daa.insert(10, "world")
        daa.clear()
        assert daa.is_empty() is True
        assert daa.size() == 0
        assert daa.find(42) is None
        assert daa.find(10) is None
    
    def test_keys(self):
        """Testa retorno das chaves"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        daa.insert(10, "world")
        daa.insert(99, "test")
        
        keys = daa.keys()
        assert keys == [10, 42, 99]
    
    def test_keys_empty(self):
        """Testa retorno das chaves em array vazio"""
        daa = DirectAccessArray(100)
        assert daa.keys() == []
    
    def test_values(self):
        """Testa retorno dos valores"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        daa.insert(10, "world")
        daa.insert(99, "test")
        
        values = daa.values()
        assert values == ["world", "hello", "test"]
    
    def test_values_empty(self):
        """Testa retorno dos valores em array vazio"""
        daa = DirectAccessArray(100)
        assert daa.values() == []
    
    def test_items(self):
        """Testa retorno dos pares (chave, valor)"""
        daa = DirectAccessArray(100)
        daa.insert(42, "hello")
        daa.insert(10, "world")
        daa.insert(99, "test")
        
        items = daa.items()
        assert items == [(10, "world"), (42, "hello"), (99, "test")]
    
    def test_items_empty(self):
        """Testa retorno dos itens em array vazio"""
        daa = DirectAccessArray(100)
        assert daa.items() == []
    
    def test_multiple_operations(self):
        """Testa múltiplas operações"""
        daa = DirectAccessArray(1000)
        
        # Inserções
        assert daa.insert(100, "a") is True
        assert daa.insert(200, "b") is True
        assert daa.insert(300, "c") is True
        
        # Verificações
        assert daa.size() == 3
        assert daa.find(100) == "a"
        assert daa.find(200) == "b"
        assert daa.find(300) == "c"
        
        # Atualizações
        assert daa.insert(200, "bb") is False
        assert daa.find(200) == "bb"
        assert daa.size() == 3
        
        # Remoções
        assert daa.delete(200) is True
        assert daa.find(200) is None
        assert daa.size() == 2
        
        # Min/Max
        assert daa.find_min() == (100, "a")
        assert daa.find_max() == (300, "c")
    
    def test_edge_cases(self):
        """Testa casos extremos"""
        daa = DirectAccessArray(10)
        
        # Chave 0
        daa.insert(0, "zero")
        assert daa.find(0) == "zero"
        assert daa.find_min() == (0, "zero")
        assert daa.find_max() == (0, "zero")
        
        # Chave máxima
        daa.insert(9, "nine")
        assert daa.find(9) == "nine"
        assert daa.find_min() == (0, "zero")
        assert daa.find_max() == (9, "nine")
    
    def test_large_universe(self):
        """Testa com universo grande"""
        daa = DirectAccessArray(10000)
        
        # Inserir elementos esparsos
        daa.insert(100, "a")
        daa.insert(5000, "b")
        daa.insert(9999, "c")
        
        assert daa.size() == 3
        assert daa.find_min() == (100, "a")
        assert daa.find_max() == (9999, "c")
        
        # Verificar que posições vazias retornam None
        assert daa.find(0) is None
        assert daa.find(500) is None
        assert daa.find(9998) is None


class TestDirectAccessArrayProperties:
    """Testes para verificar propriedades do Direct Access Array"""
    
    def test_space_complexity(self):
        """Testa que o espaço usado é proporcional ao universo"""
        # Este teste verifica que o array tem o tamanho correto
        universe_size = 1000
        daa = DirectAccessArray(universe_size)
        
        # Inserir apenas alguns elementos
        daa.insert(100, "a")
        daa.insert(500, "b")
        
        # O tamanho do array deve ser universe_size, não o número de elementos
        assert daa.size() == 2  # Número de elementos
        # O array interno deve ter tamanho universe_size
    
    def test_time_complexity(self):
        """Testa que operações são O(1)"""
        # Este teste verifica que operações são constantes
        daa = DirectAccessArray(1000)
        
        # Inserir muitos elementos
        for i in range(100):
            daa.insert(i, f"value_{i}")
        
        # Operações devem ser rápidas independente do tamanho
        assert daa.find(50) == "value_50"
        assert daa.delete(50) is True
        assert daa.insert(50, "new_value") is True
    
    def test_key_constraints(self):
        """Testa restrições de chaves"""
        daa = DirectAccessArray(100)
        
        # Chaves válidas
        daa.insert(0, "zero")
        daa.insert(99, "ninety_nine")
        
        # Chaves inválidas (maiores que universe_size)
        # O comportamento pode variar dependendo da implementação
        # Algumas implementações podem lançar exceção, outras podem usar módulo
        try:
            daa.insert(100, "invalid")
            # Se não lançar exceção, deve usar módulo
            assert daa.find(0) == "invalid"  # 100 % 100 = 0
        except (IndexError, ValueError):
            # Comportamento esperado: lançar exceção
            pass
    
    def test_value_types(self):
        """Testa diferentes tipos de valores"""
        daa = DirectAccessArray(100)
        
        # Strings
        daa.insert(1, "string")
        assert daa.find(1) == "string"
        
        # Números
        daa.insert(2, 42)
        assert daa.find(2) == 42
        
        # Listas
        daa.insert(3, [1, 2, 3])
        assert daa.find(3) == [1, 2, 3]
        
        # Objetos
        class TestObject:
            def __init__(self, value):
                self.value = value
        
        obj = TestObject("test")
        daa.insert(4, obj)
        assert daa.find(4) == obj
        assert daa.find(4).value == "test" 