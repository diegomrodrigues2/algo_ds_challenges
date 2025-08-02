"""
Torre de Hanói - Exemplo Canônico da Fé Recursiva

Este módulo implementa o quebra-cabeça clássico da Torre de Hanói,
demonstrando o conceito fundamental da recursão: "fé recursiva".

A solução é baseada na estratégia:
1. Mover recursivamente n-1 discos da origem para o pino auxiliar
2. Mover o disco n da origem para o destino
3. Mover recursivamente n-1 discos do pino auxiliar para o destino

Referência: Erickson, "Algorithms", Capítulo 1, Seção 1.3, "Tower of Hanoi"
"""

from typing import List, Tuple


def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """
    Resolve o quebra-cabeça da Torre de Hanói.
    
    Esta é a implementação canônica que demonstra a "fé recursiva":
    acreditar que a solução para n-1 discos simplesmente funciona.
    
    Args:
        n: Número de discos a serem movidos
        source: Identificador do pino de origem (ex: 'A')
        destination: Identificador do pino de destino (ex: 'B')
        auxiliary: Identificador do pino auxiliar (ex: 'C')
        
    Returns:
        Lista de movimentos no formato "Mover disco X do pino Y para o pino Z"
        
    Example:
        >>> moves = tower_of_hanoi(3, 'A', 'C', 'B')
        >>> print(moves[0])
        Mover disco 1 do pino A para o pino C
        
    Complexidade:
        - Tempo: O(2^n) - exponencial devido à natureza do problema
        - Espaço: O(n) - altura da pilha de recursão
    """
    if n <= 0:
        return []
    
    moves = []
    
    # TODO: Implementar a solução recursiva da Torre de Hanói
    # 
    # A estratégia é:
    # 1. Mover recursivamente n-1 discos da origem para o pino auxiliar
    # 2. Mover o disco n da origem para o destino
    # 3. Mover recursivamente n-1 discos do pino auxiliar para o destino
    #
    # Dica: Use a função auxiliar _tower_of_hanoi_helper para implementar
    # a lógica recursiva e coletar os movimentos
    
    raise NotImplementedError("Implementar a solução recursiva da Torre de Hanói")
    
    return moves


def _tower_of_hanoi_helper(n: int, source: str, destination: str, auxiliary: str, moves: List[str]) -> None:
    """
    Função auxiliar que implementa a lógica recursiva da Torre de Hanói.
    
    Esta função modifica a lista 'moves' adicionando os movimentos necessários.
    
    Args:
        n: Número de discos a serem movidos
        source: Pino de origem
        destination: Pino de destino
        auxiliary: Pino auxiliar
        moves: Lista para armazenar os movimentos
        
    Example:
        >>> moves = []
        >>> _tower_of_hanoi_helper(1, 'A', 'C', 'B', moves)
        >>> moves
        ['Mover disco 1 do pino A para o pino C']
    """
    # TODO: Implementar a lógica recursiva
    # 
    # Caso base: se há apenas 1 disco, mova-o diretamente
    # Caso recursivo: aplique a estratégia de 3 passos
    #
    # Dica: Para n > 1, você precisa fazer 3 chamadas recursivas:
    # 1. Mover n-1 discos da origem para o auxiliar
    # 2. Mover o disco n da origem para o destino
    # 3. Mover n-1 discos do auxiliar para o destino
    
    raise NotImplementedError("Implementar a lógica recursiva")


def count_moves(n: int) -> int:
    """
    Calcula o número mínimo de movimentos necessários para resolver a Torre de Hanói.
    
    A fórmula é: 2^n - 1
    
    Args:
        n: Número de discos
        
    Returns:
        Número mínimo de movimentos
        
    Example:
        >>> count_moves(3)
        7
        >>> count_moves(4)
        15
    """
    # TODO: Implementar o cálculo do número de movimentos
    # 
    # A relação de recorrência é: T(n) = 2*T(n-1) + 1
    # A solução fechada é: T(n) = 2^n - 1
    
    raise NotImplementedError("Implementar o cálculo do número de movimentos")


def tower_of_hanoi_iterative(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """
    Implementação iterativa da Torre de Hanói usando uma pilha.
    
    Esta versão demonstra como converter a recursão em iteração,
    mantendo o mesmo comportamento mas com controle explícito da pilha.
    
    Args:
        n: Número de discos a serem movidos
        source: Identificador do pino de origem
        destination: Identificador do pino de destino
        auxiliary: Identificador do pino auxiliar
        
    Returns:
        Lista de movimentos
        
    Example:
        >>> moves = tower_of_hanoi_iterative(3, 'A', 'C', 'B')
        >>> len(moves)
        7
    """
    if n <= 0:
        return []
    
    moves = []
    stack = [(n, source, destination, auxiliary, False)]
    
    # TODO: Implementar a versão iterativa
    # 
    # Use uma pilha para simular a recursão:
    # - Cada elemento da pilha é uma tupla (n, source, dest, aux, is_moved)
    # - is_moved indica se o disco n já foi movido
    # - Para n > 1, você precisa processar em 3 fases:
    #   1. Primeira chamada recursiva (n-1 discos: source -> aux)
    #   2. Mover disco n (source -> dest)
    #   3. Segunda chamada recursiva (n-1 discos: aux -> dest)
    
    raise NotImplementedError("Implementar a versão iterativa")
    
    return moves


def validate_tower_state(pegs: dict) -> bool:
    """
    Valida se um estado das torres é válido (discos em ordem decrescente).
    
    Args:
        pegs: Dicionário com os pinos e suas listas de discos
              Ex: {'A': [3, 2, 1], 'B': [], 'C': []}
              
    Returns:
        True se o estado é válido, False caso contrário
        
    Example:
        >>> validate_tower_state({'A': [3, 2, 1], 'B': [], 'C': []})
        True
        >>> validate_tower_state({'A': [1, 2, 3], 'B': [], 'C': []})
        False
    """
    # TODO: Implementar validação do estado das torres
    # 
    # Um estado é válido se:
    # - Todos os discos em cada pino estão em ordem decrescente (maior embaixo)
    # - Não há discos duplicados
    # - Todos os discos estão presentes
    
    raise NotImplementedError("Implementar validação do estado das torres") 