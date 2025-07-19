"""
Chaining Hash Table Implementation

Implemente uma tabela hash usando chaining (encadeamento) para resolver
colisões. Cada slot da tabela contém uma lista de elementos.

Complexidade: O(1) esperado para find/insert/delete
Espaço: O(n) onde n é o número de elementos
"""

class ChainingHashTable:
    """
    Implementação de tabela hash com chaining.
    Usa listas para resolver colisões.
    """
    
    def __init__(self, size):
        """
        Inicializa a tabela hash com chaining.
        
        Args:
            size: Tamanho da tabela hash (m)
            
        Exemplo:
            >>> ht = ChainingHashTable(10)
            >>> ht.size()
            0
        """
        raise NotImplementedError("Implemente o construtor")
    
    def _hash(self, key):
        """
        Calcula o hash de uma chave.
        
        Args:
            key: Chave a ser hasheada
            
        Returns:
            Índice na tabela hash
            
        Exemplo:
            >>> ht = ChainingHashTable(10)
            >>> hash_val = ht._hash(42)
            >>> 0 <= hash_val < 10
            True
        """
        raise NotImplementedError("Implemente a função hash")
    
    def insert(self, key, value):
        """
        Insere um par (chave, valor) na tabela.
        
        Args:
            key: Chave do elemento
            value: Valor a ser armazenado
            
        Returns:
            True se inserido, False se atualizado
            
        Exemplo:
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
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
            >>> ht = ChainingHashTable(10)
            >>> ht.max_chain_length()
            0
            >>> ht.insert(42, "hello")
            >>> ht.max_chain_length()
            1
        """
        raise NotImplementedError("Implemente o método max_chain_length")
    
    def chain_lengths(self):
        """
        Retorna uma lista com o comprimento de cada cadeia.
        
        Returns:
            Lista de comprimentos das cadeias
            
        Exemplo:
            >>> ht = ChainingHashTable(5)
            >>> ht.insert(1, "a")
            >>> ht.insert(6, "b")  # Pode colidir com 1
            >>> lengths = ht.chain_lengths()
            >>> len(lengths)
            5
        """
        raise NotImplementedError("Implemente o método chain_lengths")
    
    def _resize(self, new_size):
        """
        Redimensiona a tabela hash.
        
        Args:
            new_size: Novo tamanho da tabela
            
        Exemplo:
            >>> ht = ChainingHashTable(5)
            >>> ht.insert(42, "hello")
            >>> ht._resize(10)
            >>> ht.find(42)
            'hello'
        """
        raise NotImplementedError("Implemente o método _resize")
    
    def contains_key(self, key):
        """
        Verifica se uma chave existe na tabela.
        
        Args:
            key: Chave a verificar
            
        Returns:
            True se a chave existe, False caso contrário
            
        Exemplo:
            >>> ht = ChainingHashTable(10)
            >>> ht.contains_key(42)
            False
            >>> ht.insert(42, "hello")
            >>> ht.contains_key(42)
            True
        """
        raise NotImplementedError("Implemente o método contains_key")
    
    def get(self, key, default=None):
        """
        Busca um valor pela chave, retornando um valor padrão se não encontrado.
        
        Args:
            key: Chave a ser buscada
            default: Valor padrão se chave não encontrada
            
        Returns:
            Valor associado à chave ou default
            
        Exemplo:
            >>> ht = ChainingHashTable(10)
            >>> ht.get(42, "not found")
            'not found'
            >>> ht.insert(42, "hello")
            >>> ht.get(42, "not found")
            'hello'
        """
        raise NotImplementedError("Implemente o método get") 