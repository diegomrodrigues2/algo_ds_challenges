"""
Testes para Universal Hash Table
"""

import pytest
from .universal_hash_table import UniversalHashTable


class TestUniversalHashTable:
    """Testes para a classe UniversalHashTable"""
    
    def test_constructor(self):
        """Testa o construtor"""
        ht = UniversalHashTable(10, 100)
        assert ht.size() == 0
        assert ht.is_empty() is True
        assert ht.load_factor() == 0.0
    
    def test_is_prime(self):
        """Testa verificação de primalidade"""
        ht = UniversalHashTable(10, 100)
        assert ht._is_prime(2) is True
        assert ht._is_prime(3) is True
        assert ht._is_prime(7) is True
        assert ht._is_prime(11) is True
        assert ht._is_prime(4) is False
        assert ht._is_prime(6) is False
        assert ht._is_prime(8) is False
        assert ht._is_prime(9) is False
        assert ht._is_prime(1) is False
        assert ht._is_prime(0) is False
    
    def test_next_prime(self):
        """Testa busca do próximo primo"""
        ht = UniversalHashTable(10, 100)
        assert ht._next_prime(10) == 11
        assert ht._next_prime(11) == 13
        assert ht._next_prime(12) == 13
        assert ht._next_prime(13) == 17
        assert ht._next_prime(1) == 2
        assert ht._next_prime(2) == 3
    
    def test_hash_function(self):
        """Testa função hash universal"""
        ht = UniversalHashTable(10, 100)
        
        # Testa que hash está no range correto
        for key in range(100):
            hash_val = ht._hash(key)
            assert 0 <= hash_val < 10
        
        # Testa distribuição (básico)
        hashes = [ht._hash(i) for i in range(20)]
        assert len(set(hashes)) > 1  # Deve ter alguma distribuição
    
    def test_insert_basic(self):
        """Testa inserção básica"""
        ht = UniversalHashTable(10, 100)
        assert ht.insert(42, "hello") is True
        assert ht.size() == 1
        assert ht.is_empty() is False
        assert ht.load_factor() == 0.1
    
    def test_insert_update(self):
        """Testa atualização de elemento existente"""
        ht = UniversalHashTable(10, 100)
        ht.insert(42, "hello")
        assert ht.insert(42, "world") is False  # Atualização
        assert ht.find(42) == "world"
        assert ht.size() == 1  # Tamanho não muda
    
    def test_find_basic(self):
        """Testa busca básica"""
        ht = UniversalHashTable(10, 100)
        ht.insert(42, "hello")
        assert ht.find(42) == "hello"
        assert ht.find(99) is None
    
    def test_delete_basic(self):
        """Testa remoção básica"""
        ht = UniversalHashTable(10, 100)
        ht.insert(42, "hello")
        assert ht.delete(42) is True
        assert ht.find(42) is None
        assert ht.size() == 0
        assert ht.is_empty() is True
        assert ht.load_factor() == 0.0
    
    def test_delete_nonexistent(self):
        """Testa remoção de elemento inexistente"""
        ht = UniversalHashTable(10, 100)
        assert ht.delete(42) is False
        assert ht.size() == 0
    
    def test_clear(self):
        """Testa limpeza da tabela"""
        ht = UniversalHashTable(10, 100)
        ht.insert(42, "hello")
        ht.insert(10, "world")
        ht.clear()
        assert ht.is_empty() is True
        assert ht.size() == 0
        assert ht.find(42) is None
        assert ht.find(10) is None
    
    def test_keys(self):
        """Testa retorno das chaves"""
        ht = UniversalHashTable(10, 100)
        ht.insert(42, "hello")
        ht.insert(10, "world")
        keys = ht.keys()
        assert len(keys) == 2
        assert 42 in keys
        assert 10 in keys
    
    def test_values(self):
        """Testa retorno dos valores"""
        ht = UniversalHashTable(10, 100)
        ht.insert(42, "hello")
        ht.insert(10, "world")
        values = ht.values()
        assert len(values) == 2
        assert "hello" in values
        assert "world" in values
    
    def test_items(self):
        """Testa retorno dos pares (chave, valor)"""
        ht = UniversalHashTable(10, 100)
        ht.insert(42, "hello")
        ht.insert(10, "world")
        items = ht.items()
        assert len(items) == 2
        assert (42, "hello") in items
        assert (10, "world") in items
    
    def test_load_factor(self):
        """Testa cálculo do fator de carga"""
        ht = UniversalHashTable(10, 100)
        assert ht.load_factor() == 0.0
        
        ht.insert(42, "hello")
        assert ht.load_factor() == 0.1
        
        ht.insert(10, "world")
        assert ht.load_factor() == 0.2
    
    def test_max_chain_length(self):
        """Testa comprimento da cadeia mais longa"""
        ht = UniversalHashTable(10, 100)
        assert ht.max_chain_length() == 0
        
        ht.insert(42, "hello")
        assert ht.max_chain_length() == 1
        
        # Se houver colisões, a cadeia pode ser maior
        ht.insert(52, "world")  # Pode colidir dependendo da função hash
        assert ht.max_chain_length() >= 1
    
    def test_multiple_operations(self):
        """Testa múltiplas operações"""
        ht = UniversalHashTable(20, 1000)
        
        # Inserções
        assert ht.insert(100, "a") is True
        assert ht.insert(200, "b") is True
        assert ht.insert(300, "c") is True
        
        # Verificações
        assert ht.size() == 3
        assert ht.find(100) == "a"
        assert ht.find(200) == "b"
        assert ht.find(300) == "c"
        
        # Atualizações
        assert ht.insert(200, "bb") is False
        assert ht.find(200) == "bb"
        assert ht.size() == 3
        
        # Remoções
        assert ht.delete(200) is True
        assert ht.find(200) is None
        assert ht.size() == 2
    
    def test_large_dataset(self):
        """Testa com conjunto grande de dados"""
        ht = UniversalHashTable(100, 10000)
        
        # Inserir muitos elementos
        for i in range(50):
            ht.insert(i, f"value_{i}")
        
        assert ht.size() == 50
        assert ht.load_factor() == 0.5
        
        # Verificar que todos estão lá
        for i in range(50):
            assert ht.find(i) == f"value_{i}"
        
        # Verificar que elementos inexistentes retornam None
        for i in range(50, 100):
            assert ht.find(i) is None
    
    def test_collision_handling(self):
        """Testa tratamento de colisões"""
        ht = UniversalHashTable(5, 100)  # Tabela pequena para forçar colisões
        
        # Inserir elementos que podem colidir
        for i in range(10):
            ht.insert(i, f"value_{i}")
        
        assert ht.size() == 10
        assert ht.load_factor() == 2.0  # Fator de carga > 1
        
        # Verificar que todos os elementos estão acessíveis
        for i in range(10):
            assert ht.find(i) == f"value_{i}"
    
    def test_resize(self):
        """Testa redimensionamento da tabela"""
        ht = UniversalHashTable(5, 100)
        ht.insert(42, "hello")
        ht.insert(10, "world")
        
        # Redimensionar
        ht._resize(10)
        
        # Verificar que elementos ainda estão acessíveis
        assert ht.find(42) == "hello"
        assert ht.find(10) == "world"
        assert ht.size() == 2
        
        # Verificar que fator de carga diminuiu
        assert ht.load_factor() == 0.2


class TestUniversalHashTableProperties:
    """Testes para verificar propriedades do Universal Hash Table"""
    
    def test_universality_property(self):
        """Testa propriedade de universalidade"""
        # Este teste verifica que a função hash distribui bem
        ht = UniversalHashTable(10, 100)
        
        # Contar quantas vezes cada slot é usado
        slot_counts = [0] * 10
        for key in range(100):
            slot = ht._hash(key)
            slot_counts[slot] += 1
        
        # Verificar que nenhum slot está muito sobrecarregado
        # Em uma distribuição uniforme, cada slot deve ter ~10 elementos
        for count in slot_counts:
            assert count > 0  # Todos os slots devem ser usados
            assert count <= 20  # Nenhum slot deve ter mais que 2x a média
    
    def test_randomness(self):
        """Testa que a função hash é aleatória"""
        ht1 = UniversalHashTable(10, 100)
        ht2 = UniversalHashTable(10, 100)
        
        # As funções hash devem ser diferentes (parâmetros aleatórios)
        hashes1 = [ht1._hash(i) for i in range(20)]
        hashes2 = [ht2._hash(i) for i in range(20)]
        
        # Deve haver alguma diferença (não determinístico)
        assert hashes1 != hashes2
    
    def test_space_efficiency(self):
        """Testa eficiência de espaço"""
        ht = UniversalHashTable(100, 10000)
        
        # Inserir poucos elementos
        for i in range(10):
            ht.insert(i, f"value_{i}")
        
        # O espaço usado deve ser proporcional ao tamanho da tabela
        # não ao universo de chaves
        assert ht.size() == 10
        assert ht.load_factor() == 0.1
    
    def test_time_complexity(self):
        """Testa complexidade de tempo"""
        ht = UniversalHashTable(1000, 10000)
        
        # Inserir muitos elementos
        for i in range(500):
            ht.insert(i, f"value_{i}")
        
        # Operações devem ser rápidas
        assert ht.find(250) == "value_250"
        assert ht.delete(250) is True
        assert ht.insert(250, "new_value") is True
    
    def test_prime_parameter(self):
        """Testa que o parâmetro p é primo"""
        ht = UniversalHashTable(10, 100)
        
        # O parâmetro p deve ser primo e maior que universe_size
        assert ht._is_prime(ht.p) is True
        assert ht.p > 100  # universe_size
    
    def test_hash_parameters(self):
        """Testa parâmetros da função hash"""
        ht = UniversalHashTable(10, 100)
        
        # a deve estar no range [1, p-1]
        assert 1 <= ht.a < ht.p
        
        # b deve estar no range [0, p-1]
        assert 0 <= ht.b < ht.p 