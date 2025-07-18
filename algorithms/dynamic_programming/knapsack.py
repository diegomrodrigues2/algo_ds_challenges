"""
Problema da Mochila (Knapsack Problem)

Dado um conjunto de itens, cada um com um peso e um valor, e uma mochila com 
capacidade máxima, encontre a combinação de itens que maximize o valor total 
sem exceder a capacidade da mochila.

Exemplo:
- Itens: [(peso=1, valor=10), (peso=2, valor=15), (peso=3, valor=20)]
- Capacidade: 5
- Solução ótima: itens 1 e 2 (peso=3, valor=25)
"""

def knapsack_recursive(weights, values, capacity):
    """
    Solução recursiva para o problema da mochila.
    
    Args:
        weights: Lista de pesos dos itens
        values: Lista de valores dos itens
        capacity: Capacidade máxima da mochila
    
    Returns:
        O valor máximo possível
    """
    n = len(weights)
    
    def knapsack_helper(i, remaining_capacity):
        # TODO: Implementar a lógica recursiva
        # Para cada item, decidir se incluir ou não
        raise NotImplementedError("Implementar a lógica recursiva")
    
    return knapsack_helper(0, capacity)


def knapsack_dp(weights, values, capacity):
    """
    Solução com programação dinâmica (memoização) para o problema da mochila.
    
    Args:
        weights: Lista de pesos dos itens
        values: Lista de valores dos itens
        capacity: Capacidade máxima da mochila
    
    Returns:
        O valor máximo possível
    """
    n = len(weights)
    
    # TODO: Implementar solução com programação dinâmica
    # Dica: Use uma matriz 2D para armazenar os resultados
    raise NotImplementedError("Implementar solução com programação dinâmica")


def knapsack_01(weights, values, capacity):
    """
    Problema da mochila 0/1 (cada item pode ser usado no máximo uma vez).
    
    Args:
        weights: Lista de pesos dos itens
        values: Lista de valores dos itens
        capacity: Capacidade máxima da mochila
    
    Returns:
        O valor máximo possível
    """
    # TODO: Implementar solução para mochila 0/1
    # Dica: Similar ao knapsack_dp, mas sem repetição de itens
    raise NotImplementedError("Implementar solução para mochila 0/1")


def knapsack_fractional(weights, values, capacity):
    """
    Problema da mochila fracionária (itens podem ser divididos).
    
    Args:
        weights: Lista de pesos dos itens
        values: Lista de valores dos itens
        capacity: Capacidade máxima da mochila
    
    Returns:
        O valor máximo possível
    """
    # TODO: Implementar solução para mochila fracionária
    # Dica: Use uma abordagem gulosa baseada na razão valor/peso
    raise NotImplementedError("Implementar solução para mochila fracionária")


def knapsack_with_items(weights, values, capacity):
    """
    Solução que retorna tanto o valor máximo quanto os itens selecionados.
    
    Args:
        weights: Lista de pesos dos itens
        values: Lista de valores dos itens
        capacity: Capacidade máxima da mochila
    
    Returns:
        Tupla (valor_maximo, lista_de_indices_dos_itens)
    """
    # TODO: Implementar solução que retorna os itens selecionados
    # Dica: Mantenha um array para rastrear as escolhas feitas
    raise NotImplementedError("Implementar solução que retorna os itens selecionados") 