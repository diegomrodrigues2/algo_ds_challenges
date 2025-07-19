"""
Direct Access Array Sort

Implementar ordenação usando array de acesso direto.
Este algoritmo é O(n + u) onde u é o tamanho do universo de chaves.
Ideal para chaves únicas em faixa limitada.
"""

def direct_access_array_sort(items):
    """
    Ordena uma lista de itens usando array de acesso direto.
    
    Args:
        items: Lista de objetos com atributo 'key' (inteiro)
    
    Returns:
        Lista ordenada dos itens
    
    Precondições:
        - Todos os itens têm chaves únicas
        - Chaves são inteiros não-negativos
        - Faixa de chaves é razoável (u = O(n))
    """
    if not items:
        return []
    
    # TODO: Encontrar o valor máximo das chaves
    # max_key = ...
    raise NotImplementedError("Implementar busca do valor máximo")
    
    # TODO: Criar array de acesso direto
    # direct_array = ...
    raise NotImplementedError("Implementar criação do array de acesso direto")
    
    # TODO: Inserir itens no array de acesso direto
    # Para cada item, colocar em direct_array[item.key] = item
    raise NotImplementedError("Implementar inserção no array de acesso direto")
    
    # TODO: Percorrer array e retornar itens em ordem
    # Retornar apenas as posições que contêm itens
    raise NotImplementedError("Implementar leitura ordenada do array")


class Item:
    """Classe auxiliar para itens com chave"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f"Item({self.key}, {self.value})"
    
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.key == other.key and self.value == other.value


def create_items_from_list(values):
    """Cria lista de Items a partir de lista de valores"""
    return [Item(i, f"value_{i}") for i in values] 