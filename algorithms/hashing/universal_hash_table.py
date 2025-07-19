"""
Universal Hash Table Implementation

Implemente uma tabela hash usando hashing universal para garantir
distribuição uniforme independente dos dados de entrada.

Complexidade: O(1) esperado para find/insert/delete
Espaço: O(n) onde n é o número de elementos
"""

import random

class UniversalHashTable:
    """
    Implementação de tabela hash com hashing universal.
    Usa a função hash h(k) = ((a*k + b) mod p) mod m
    """
    
    def __init__(self, size, universe_size):
        """
        Inicializa a tabela hash universal.
        
        Args:
            size: Tamanho da tabela hash (m)
            universe_size: Tamanho do universo de chaves (u)
            
        Exemplo:
            >>> ht = UniversalHashTable(100, 1000)
            >>> ht.size
            100
        """
        raise NotImplementedError("Implemente o construtor")
    
    def _next_prime(self, n):
        """
        Encontra o menor primo maior que n.
        
        Args:
            n: Número a partir do qual buscar o próximo primo
            
        Returns:
            Menor primo > n
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht._next_prime(10)
            11
        """
        raise NotImplementedError("Implemente a busca do próximo primo")
    
    def _is_prime(self, num):
        """
        Verifica se um número é primo.
        
        Args:
            num: Número a verificar
            
        Returns:
            True se primo, False caso contrário
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht._is_prime(7)
            True
            >>> ht._is_prime(8)
            False
        """
        raise NotImplementedError("Implemente a verificação de primalidade")
    
    def _hash(self, key):
        """
        Calcula o hash universal de uma chave.
        
        Args:
            key: Chave a ser hasheada
            
        Returns:
            Índice na tabela hash
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> hash_val = ht._hash(42)
            >>> 0 <= hash_val < 10
            True
        """
        raise NotImplementedError("Implemente a função hash universal")
    
    def insert(self, key, value):
        """
        Insere um par (chave, valor) na tabela.
        
        Args:
            key: Chave do elemento
            value: Valor a ser armazenado
            
        Returns:
            True se inserido, False se atualizado
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.insert(42, "hello")
            True
            >>> ht.insert(42, "world")
            False
        """
        raise NotImplementedError("Implemente o método insert")
    
    def find(self, key):
        """
        Busca um valor pela chave.
        
        Args:
            key: Chave a ser buscada
            
        Returns:
            Valor associado à chave ou None se não encontrado
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.insert(42, "hello")
            >>> ht.find(42)
            'hello'
            >>> ht.find(99)
            None
        """
        raise NotImplementedError("Implemente o método find")
    
    def delete(self, key):
        """
        Remove um elemento pela chave.
        
        Args:
            key: Chave do elemento a ser removido
            
        Returns:
            True se removido, False se não encontrado
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.insert(42, "hello")
            >>> ht.delete(42)
            True
            >>> ht.delete(42)
            False
        """
        raise NotImplementedError("Implemente o método delete")
    
    def size(self):
        """
        Retorna o número de elementos na tabela.
        
        Returns:
            Número de elementos
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.size()
            0
            >>> ht.insert(42, "hello")
            >>> ht.size()
            1
        """
        raise NotImplementedError("Implemente o método size")
    
    def is_empty(self):
        """
        Verifica se a tabela está vazia.
        
        Returns:
            True se vazia, False caso contrário
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.is_empty()
            True
            >>> ht.insert(42, "hello")
            >>> ht.is_empty()
            False
        """
        raise NotImplementedError("Implemente o método is_empty")
    
    def clear(self):
        """
        Remove todos os elementos da tabela.
        
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.insert(42, "hello")
            >>> ht.clear()
            >>> ht.is_empty()
            True
        """
        raise NotImplementedError("Implemente o método clear")
    
    def keys(self):
        """
        Retorna todas as chaves na tabela.
        
        Returns:
            Lista de chaves
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.insert(42, "hello")
            >>> ht.insert(10, "world")
            >>> sorted(ht.keys())
            [10, 42]
        """
        raise NotImplementedError("Implemente o método keys")
    
    def values(self):
        """
        Retorna todos os valores na tabela.
        
        Returns:
            Lista de valores
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.insert(42, "hello")
            >>> ht.insert(10, "world")
            >>> sorted(ht.values())
            ['hello', 'world']
        """
        raise NotImplementedError("Implemente o método values")
    
    def items(self):
        """
        Retorna todos os pares (chave, valor).
        
        Returns:
            Lista de tuplas (chave, valor)
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.insert(42, "hello")
            >>> ht.insert(10, "world")
            >>> sorted(ht.items())
            [(10, 'world'), (42, 'hello')]
        """
        raise NotImplementedError("Implemente o método items")
    
    def load_factor(self):
        """
        Calcula o fator de carga da tabela.
        
        Returns:
            Fator de carga (n/m)
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.load_factor()
            0.0
            >>> ht.insert(42, "hello")
            >>> ht.load_factor()
            0.1
        """
        raise NotImplementedError("Implemente o método load_factor")
    
    def max_chain_length(self):
        """
        Retorna o comprimento da cadeia mais longa.
        
        Returns:
            Comprimento da cadeia mais longa
            
        Exemplo:
            >>> ht = UniversalHashTable(10, 100)
            >>> ht.max_chain_length()
            0
            >>> ht.insert(42, "hello")
            >>> ht.max_chain_length()
            1
        """
        raise NotImplementedError("Implemente o método max_chain_length")
    
    def _resize(self, new_size):
        """
        Redimensiona a tabela hash.
        
        Args:
            new_size: Novo tamanho da tabela
            
        Exemplo:
            >>> ht = UniversalHashTable(5, 100)
            >>> ht.insert(42, "hello")
            >>> ht._resize(10)
            >>> ht.find(42)
            'hello'
        """
        raise NotImplementedError("Implemente o método _resize") 