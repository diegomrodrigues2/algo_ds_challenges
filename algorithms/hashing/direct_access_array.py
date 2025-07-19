"""
Direct Access Array Implementation

Implemente uma estrutura de dados que armazena elementos diretamente
em posições indexadas por suas chaves, permitindo operações O(1).

Complexidade: O(1) para find/insert/delete, mas O(u) de espaço
Onde u = tamanho do universo de chaves
"""

class DirectAccessArray:
    """
    Implementação de Direct Access Array.
    Armazena elementos em posições indexadas por suas chaves.
    """
    
    def __init__(self, universe_size):
        """
        Inicializa o Direct Access Array.
        
        Args:
            universe_size: Tamanho do universo de chaves (u)
            
        Exemplo:
            >>> daa = DirectAccessArray(1000)
            >>> daa.size
            0
        """
        raise NotImplementedError("Implemente o construtor")
    
    def insert(self, key, value):
        """
        Insere um elemento com a chave especificada.
        
        Args:
            key: Chave do elemento (deve ser < universe_size)
            value: Valor a ser armazenado
            
        Returns:
            True se inserido, False se atualizado
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            True
            >>> daa.insert(42, "world")
            False
        """
        raise NotImplementedError("Implemente o método insert")
    
    def find(self, key):
        """
        Busca um elemento pela chave.
        
        Args:
            key: Chave a ser buscada
            
        Returns:
            Valor associado à chave ou None se não encontrado
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.find(42)
            'hello'
            >>> daa.find(99)
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
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.delete(42)
            True
            >>> daa.delete(42)
            False
        """
        raise NotImplementedError("Implemente o método delete")
    
    def find_min(self):
        """
        Encontra o elemento com a menor chave.
        
        Returns:
            Tupla (chave, valor) do menor elemento ou None se vazio
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.insert(10, "world")
            >>> daa.find_min()
            (10, 'world')
        """
        raise NotImplementedError("Implemente o método find_min")
    
    def find_max(self):
        """
        Encontra o elemento com a maior chave.
        
        Returns:
            Tupla (chave, valor) do maior elemento ou None se vazio
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.insert(10, "world")
            >>> daa.find_max()
            (42, 'hello')
        """
        raise NotImplementedError("Implemente o método find_max")
    
    def size(self):
        """
        Retorna o número de elementos armazenados.
        
        Returns:
            Número de elementos
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.size()
            0
            >>> daa.insert(42, "hello")
            >>> daa.size()
            1
        """
        raise NotImplementedError("Implemente o método size")
    
    def is_empty(self):
        """
        Verifica se o array está vazio.
        
        Returns:
            True se vazio, False caso contrário
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.is_empty()
            True
            >>> daa.insert(42, "hello")
            >>> daa.is_empty()
            False
        """
        raise NotImplementedError("Implemente o método is_empty")
    
    def clear(self):
        """
        Remove todos os elementos do array.
        
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.clear()
            >>> daa.is_empty()
            True
        """
        raise NotImplementedError("Implemente o método clear")
    
    def keys(self):
        """
        Retorna todas as chaves armazenadas.
        
        Returns:
            Lista de chaves em ordem crescente
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.insert(10, "world")
            >>> daa.keys()
            [10, 42]
        """
        raise NotImplementedError("Implemente o método keys")
    
    def values(self):
        """
        Retorna todos os valores armazenados.
        
        Returns:
            Lista de valores na ordem das chaves
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.insert(10, "world")
            >>> daa.values()
            ['world', 'hello']
        """
        raise NotImplementedError("Implemente o método values")
    
    def items(self):
        """
        Retorna todos os pares (chave, valor).
        
        Returns:
            Lista de tuplas (chave, valor) em ordem crescente de chaves
            
        Exemplo:
            >>> daa = DirectAccessArray(100)
            >>> daa.insert(42, "hello")
            >>> daa.insert(10, "world")
            >>> daa.items()
            [(10, 'world'), (42, 'hello')]
        """
        raise NotImplementedError("Implemente o método items") 