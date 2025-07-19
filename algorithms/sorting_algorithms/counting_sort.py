"""
Counting Sort

Implementar ordenação por contagem estável.
Este algoritmo é O(n + u) onde u é o tamanho do universo de chaves.
Ideal para chaves em faixa limitada com duplicatas.
"""

def counting_sort(arr, min_val=None, max_val=None):
    """
    Ordenação por contagem estável.
    
    Args:
        arr: Lista de inteiros não-negativos
        min_val: Valor mínimo (opcional, será calculado se None)
        max_val: Valor máximo (opcional, será calculado se None)
    
    Returns:
        Lista ordenada
    
    Precondições:
        - Todos os valores são inteiros não-negativos
        - Faixa de valores é razoável (u = O(n))
    """
    if not arr:
        return []
    
    # TODO: Determinar faixa se não fornecida
    # if min_val is None:
    #     min_val = ...
    # if max_val is None:
    #     max_val = ...
    raise NotImplementedError("Implementar determinação da faixa")
    
    # TODO: Calcular tamanho da faixa
    # range_size = ...
    raise NotImplementedError("Implementar cálculo do tamanho da faixa")
    
    # TODO: Inicializar array de contagem
    # count = ...
    raise NotImplementedError("Implementar inicialização do array de contagem")
    
    # TODO: Contar frequência de cada valor
    # for num in arr:
    #     ...
    raise NotImplementedError("Implementar contagem de frequência")
    
    # TODO: Acumular contadores (prefix sum)
    # for i in range(1, range_size):
    #     ...
    raise NotImplementedError("Implementar acumulação de contadores")
    
    # TODO: Construir output estável
    # output = ...
    # for i in range(len(arr)-1, -1, -1):
    #     ...
    raise NotImplementedError("Implementar reconstrução estável")


def counting_sort_simple(arr):
    """
    Versão simplificada do counting sort para valores de 0 a max_val.
    
    Args:
        arr: Lista de inteiros não-negativos
    
    Returns:
        Lista ordenada
    """
    if not arr:
        return []
    
    # TODO: Encontrar valor máximo
    # max_val = ...
    raise NotImplementedError("Implementar busca do valor máximo")
    
    # TODO: Inicializar array de contagem
    # count = ...
    raise NotImplementedError("Implementar inicialização do array de contagem")
    
    # TODO: Contar frequência
    # for num in arr:
    #     ...
    raise NotImplementedError("Implementar contagem de frequência")
    
    # TODO: Reconstruir lista ordenada
    # output = []
    # for i in range(max_val + 1):
    #     ...
    raise NotImplementedError("Implementar reconstrução da lista ordenada")


def counting_sort_objects(arr, key_func):
    """
    Ordenar objetos por chave numérica usando counting sort.
    
    Args:
        arr: Lista de objetos
        key_func: Função que extrai a chave numérica de cada objeto
    
    Returns:
        Lista ordenada dos objetos
    """
    if not arr:
        return []
    
    # TODO: Extrair chaves de todos os objetos
    # keys = ...
    raise NotImplementedError("Implementar extração de chaves")
    
    # TODO: Encontrar chave máxima
    # max_key = ...
    raise NotImplementedError("Implementar busca da chave máxima")
    
    # TODO: Inicializar array de contagem
    # count = ...
    raise NotImplementedError("Implementar inicialização do array de contagem")
    
    # TODO: Contar por chave
    # for key in keys:
    #     ...
    raise NotImplementedError("Implementar contagem por chave")
    
    # TODO: Acumular contadores
    # for i in range(1, max_key + 1):
    #     ...
    raise NotImplementedError("Implementar acumulação de contadores")
    
    # TODO: Reconstruir estável
    # output = ...
    # for i in range(len(arr)-1, -1, -1):
    #     ...
    raise NotImplementedError("Implementar reconstrução estável")


class Student:
    """Classe auxiliar para testar ordenação de objetos"""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.grade == other.grade 