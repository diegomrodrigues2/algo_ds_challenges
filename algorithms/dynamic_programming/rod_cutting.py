"""
Problema do Corte de Barras (Rod Cutting)

Dado uma barra de comprimento n e uma tabela de preços p[i] para barras de 
comprimento i, encontre a forma de cortar a barra que maximize o lucro total.

Exemplo:
- Comprimento da barra: 4
- Preços: [0, 1, 5, 8, 9] (preço[0] = 0, preço[1] = 1, etc.)
- Solução ótima: cortar em 2 pedaços de comprimento 2 (lucro = 5 + 5 = 10)
"""

def rod_cutting_recursive(prices, n):
    """
    Solução recursiva para o problema do corte de barras.
    
    Args:
        prices: Lista de preços onde prices[i] é o preço de uma barra de comprimento i
        n: Comprimento da barra a ser cortada
    
    Returns:
        O lucro máximo possível
    """
    if n <= 0:
        return 0
    
    max_profit = 0
    # Para cada possível primeiro corte
    for i in range(1, n + 1):
        # TODO: Implementar a lógica recursiva
        # Calcular o lucro do corte atual + o lucro máximo do restante
        raise NotImplementedError("Implementar a lógica recursiva")
    
    return max_profit


def rod_cutting_dp(prices, n):
    """
    Solução com programação dinâmica (memoização) para o problema do corte de barras.
    
    Args:
        prices: Lista de preços onde prices[i] é o preço de uma barra de comprimento i
        n: Comprimento da barra a ser cortada
    
    Returns:
        O lucro máximo possível
    """
    # TODO: Implementar solução com programação dinâmica
    # Dica: Use uma lista para armazenar os resultados já calculados
    raise NotImplementedError("Implementar solução com programação dinâmica")


def rod_cutting_bottom_up(prices, n):
    """
    Solução bottom-up com programação dinâmica para o problema do corte de barras.
    
    Args:
        prices: Lista de preços onde prices[i] é o preço de uma barra de comprimento i
        n: Comprimento da barra a ser cortada
    
    Returns:
        O lucro máximo possível
    """
    # TODO: Implementar solução bottom-up
    # Dica: Construa a solução iterativamente de baixo para cima
    raise NotImplementedError("Implementar solução bottom-up")


def rod_cutting_with_solution(prices, n):
    """
    Solução que retorna tanto o lucro máximo quanto os cortes ótimos.
    
    Args:
        prices: Lista de preços onde prices[i] é o preço de uma barra de comprimento i
        n: Comprimento da barra a ser cortada
    
    Returns:
        Tupla (lucro_maximo, lista_de_cortes)
    """
    # TODO: Implementar solução que retorna os cortes ótimos
    # Dica: Mantenha um array para rastrear os cortes escolhidos
    raise NotImplementedError("Implementar solução que retorna os cortes ótimos") 