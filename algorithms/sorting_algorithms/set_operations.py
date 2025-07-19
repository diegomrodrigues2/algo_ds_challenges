"""
Set Operations Implementation

Implemente operações de Set usando arrays ordenados e não ordenados.
Demonstre os trade-offs entre as duas abordagens.

Complexidade:
- Array não ordenado: build O(n), find O(n), insert O(1), delete O(n)
- Array ordenado: build O(n log n), find O(log n), insert O(n), delete O(n)
"""

class UnorderedSet:
    """
    Implementação de Set usando array não ordenado.
    Rápido para inserções, lento para buscas.
    """
    
    def __init__(self):
        """Inicializa um set vazio"""
        self.elements = []
    
    def build(self, items):
        """
        Constrói o set a partir de uma lista de itens.
        
        Args:
            items: Lista de itens para adicionar ao set
            
        Returns:
            None
            
        Exemplo:
            >>> s = UnorderedSet()
            >>> s.build([1, 2, 3, 2, 4])
            >>> s.elements
            [1, 2, 3, 4]
        """
        raise NotImplementedError("Implemente o método build")
    
    def find(self, key):
        """
        Busca um item pela chave.
        
        Args:
            key: Chave a ser buscada
            
        Returns:
            Item encontrado ou None se não encontrado
            
        Exemplo:
            >>> s = UnorderedSet()
            >>> s.build([1, 2, 3, 4])
            >>> s.find(3)
            3
            >>> s.find(5)
            None
        """
        raise NotImplementedError("Implemente o método find")
    
    def insert(self, item):
        """
        Insere um item no set.
        
        Args:
            item: Item a ser inserido
            
        Returns:
            True se inserido, False se já existia
            
        Exemplo:
            >>> s = UnorderedSet()
            >>> s.insert(1)
            True
            >>> s.insert(1)
            False
        """
        raise NotImplementedError("Implemente o método insert")
    
    def delete(self, key):
        """
        Remove um item do set pela chave.
        
        Args:
            key: Chave do item a ser removido
            
        Returns:
            True se removido, False se não encontrado
            
        Exemplo:
            >>> s = UnorderedSet()
            >>> s.build([1, 2, 3, 4])
            >>> s.delete(3)
            True
            >>> s.delete(5)
            False
        """
        raise NotImplementedError("Implemente o método delete")
    
    def find_min(self):
        """
        Encontra o menor elemento do set.
        
        Returns:
            Menor elemento ou None se set vazio
            
        Exemplo:
            >>> s = UnorderedSet()
            >>> s.build([3, 1, 4, 2])
            >>> s.find_min()
            1
        """
        raise NotImplementedError("Implemente o método find_min")
    
    def find_max(self):
        """
        Encontra o maior elemento do set.
        
        Returns:
            Maior elemento ou None se set vazio
            
        Exemplo:
            >>> s = UnorderedSet()
            >>> s.build([3, 1, 4, 2])
            >>> s.find_max()
            4
        """
        raise NotImplementedError("Implemente o método find_max")
    
    def length(self):
        """
        Retorna o número de elementos no set.
        
        Returns:
            Número de elementos
            
        Exemplo:
            >>> s = UnorderedSet()
            >>> s.build([1, 2, 3])
            >>> s.length()
            3
        """
        raise NotImplementedError("Implemente o método length")


class OrderedSet:
    """
    Implementação de Set usando array ordenado.
    Rápido para buscas, lento para inserções.
    """
    
    def __init__(self):
        """Inicializa um set vazio"""
        self.elements = []
    
    def build(self, items):
        """
        Constrói o set a partir de uma lista de itens.
        
        Args:
            items: Lista de itens para adicionar ao set
            
        Returns:
            None
            
        Exemplo:
            >>> s = OrderedSet()
            >>> s.build([3, 1, 4, 2])
            >>> s.elements
            [1, 2, 3, 4]
        """
        raise NotImplementedError("Implemente o método build")
    
    def find(self, key):
        """
        Busca um item pela chave usando busca binária.
        
        Args:
            key: Chave a ser buscada
            
        Returns:
            Item encontrado ou None se não encontrado
            
        Exemplo:
            >>> s = OrderedSet()
            >>> s.build([1, 2, 3, 4])
            >>> s.find(3)
            3
            >>> s.find(5)
            None
        """
        raise NotImplementedError("Implemente o método find")
    
    def insert(self, item):
        """
        Insere um item no set mantendo a ordem.
        
        Args:
            item: Item a ser inserido
            
        Returns:
            True se inserido, False se já existia
            
        Exemplo:
            >>> s = OrderedSet()
            >>> s.insert(3)
            True
            >>> s.insert(1)
            True
            >>> s.elements
            [1, 3]
        """
        raise NotImplementedError("Implemente o método insert")
    
    def delete(self, key):
        """
        Remove um item do set pela chave.
        
        Args:
            key: Chave do item a ser removido
            
        Returns:
            True se removido, False se não encontrado
            
        Exemplo:
            >>> s = OrderedSet()
            >>> s.build([1, 2, 3, 4])
            >>> s.delete(3)
            True
            >>> s.elements
            [1, 2, 4]
        """
        raise NotImplementedError("Implemente o método delete")
    
    def find_min(self):
        """
        Encontra o menor elemento do set.
        
        Returns:
            Menor elemento ou None se set vazio
            
        Exemplo:
            >>> s = OrderedSet()
            >>> s.build([3, 1, 4, 2])
            >>> s.find_min()
            1
        """
        raise NotImplementedError("Implemente o método find_min")
    
    def find_max(self):
        """
        Encontra o maior elemento do set.
        
        Returns:
            Maior elemento ou None se set vazio
            
        Exemplo:
            >>> s = OrderedSet()
            >>> s.build([3, 1, 4, 2])
            >>> s.find_max()
            4
        """
        raise NotImplementedError("Implemente o método find_max")
    
    def length(self):
        """
        Retorna o número de elementos no set.
        
        Returns:
            Número de elementos
            
        Exemplo:
            >>> s = OrderedSet()
            >>> s.build([1, 2, 3])
            >>> s.length()
            3
        """
        raise NotImplementedError("Implemente o método length")


def binary_search(arr, key):
    """
    Implementa busca binária em um array ordenado.
    
    Args:
        arr: Array ordenado
        key: Chave a ser buscada
        
    Returns:
        Índice do elemento encontrado ou -1 se não encontrado
        
    Exemplo:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    raise NotImplementedError("Implemente a busca binária") 