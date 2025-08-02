"""
Algoritmo de Exponenciação Rápida (Binary Exponentiation)

Este módulo implementa o algoritmo de exponenciação rápida, também conhecido como
"exponentiation by squaring" ou "binary exponentiation", que calcula x^n mod m
em tempo O(log n) em vez de O(n).

O algoritmo é baseado na observação de que qualquer expoente n pode ser expresso
como uma soma de potências de 2 (sua representação binária), permitindo calcular
x^n através de multiplicações sucessivas de quadrados.

Referência: Erickson, "Algorithms", Capítulo 1, Seção 1.10, "Exponentiation"
"""


def binary_exponentiation(base: int, exponent: int) -> int:
    """
    Calcula base^exponent usando exponenciação binária.
    
    Args:
        base: Número base
        exponent: Expoente não-negativo
        
    Returns:
        base elevado ao expoente
        
    Example:
        >>> binary_exponentiation(2, 10)
        1024
        >>> binary_exponentiation(3, 5)
        243
    """
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    if exponent == 0:
        return 1
    
    if exponent == 1:
        return base
    
    # TODO: Implementar exponenciação binária iterativa
    # Dica: Use operações bitwise para verificar se o bit atual é 1
    # e quadre a base a cada iteração
    
    raise NotImplementedError("Implementar exponenciação binária")


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """
    Calcula (base^exponent) mod modulus usando exponenciação binária modular.
    
    Esta é a versão mais importante do algoritmo, pois é fundamental para
    criptografia (RSA, Diffie-Hellman) e evita overflow em cálculos grandes.
    
    Args:
        base: Número base
        exponent: Expoente não-negativo
        modulus: Módulo (deve ser positivo)
        
    Returns:
        (base^exponent) mod modulus
        
    Example:
        >>> modular_exponentiation(2, 10, 1000)
        24
        >>> modular_exponentiation(3, 100, 7)
        4
    """
    if modulus <= 0:
        raise ValueError("Módulo deve ser positivo")
    
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    if exponent == 0:
        return 1
    
    # Reduzir base módulo modulus para evitar overflow
    base = base % modulus
    
    if base == 0:
        return 0
    
    # TODO: Implementar exponenciação modular binária
    # Dica: Aplique o módulo a cada multiplicação para manter
    # os números pequenos e evitar overflow
    
    raise NotImplementedError("Implementar exponenciação modular")


def recursive_exponentiation(base: int, exponent: int) -> int:
    """
    Implementação recursiva da exponenciação binária.
    
    Esta versão demonstra a recorrência:
    - x^n = (x^(n/2))^2 se n é par
    - x^n = x * (x^((n-1)/2))^2 se n é ímpar
    
    Args:
        base: Número base
        exponent: Expoente não-negativo
        
    Returns:
        base elevado ao expoente
        
    Example:
        >>> recursive_exponentiation(2, 8)
        256
        >>> recursive_exponentiation(3, 4)
        81
    """
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    if exponent == 0:
        return 1
    
    if exponent == 1:
        return base
    
    # TODO: Implementar versão recursiva
    # Dica: Use divisão inteira e verifique se o expoente é par ou ímpar
    
    raise NotImplementedError("Implementar versão recursiva")


def matrix_exponentiation(matrix: list, exponent: int, modulus: int = None) -> list:
    """
    Calcula matrix^exponent usando exponenciação binária para matrizes.
    
    Útil para resolver relações de recorrência lineares como Fibonacci
    em tempo O(log n).
    
    Args:
        matrix: Matriz 2x2 representada como lista de listas
        exponent: Expoente não-negativo
        modulus: Módulo opcional para aritmética modular
        
    Returns:
        matrix elevada ao expoente
        
    Example:
        >>> matrix_exponentiation([[1, 1], [1, 0]], 5)
        [[8, 5], [5, 3]]
    """
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Matriz deve ser 2x2")
    
    if exponent == 0:
        return [[1, 0], [0, 1]]  # Matriz identidade
    
    if exponent == 1:
        return matrix
    
    # TODO: Implementar exponenciação de matriz
    # Dica: Use multiplicação de matrizes e exponenciação binária
    
    raise NotImplementedError("Implementar exponenciação de matriz")


def fibonacci_fast(n: int, modulus: int = None) -> int:
    """
    Calcula o n-ésimo número de Fibonacci usando exponenciação de matriz.
    
    Usa a relação: [F(n+1), F(n)] = [1, 1; 1, 0]^n * [1, 0]
    
    Args:
        n: Índice do número de Fibonacci (n >= 0)
        modulus: Módulo opcional para evitar overflow
        
    Returns:
        O n-ésimo número de Fibonacci
        
    Example:
        >>> fibonacci_fast(10)
        55
        >>> fibonacci_fast(100, 1000000007)
        687995182
    """
    if n < 0:
        raise ValueError("Índice deve ser não-negativo")
    
    if n <= 1:
        return n
    
    # TODO: Implementar Fibonacci usando exponenciação de matriz
    # Dica: Use a matriz [[1, 1], [1, 0]] e exponenciação binária
    
    raise NotImplementedError("Implementar Fibonacci rápido")


def power_mod(base: int, exponent: int, modulus: int) -> int:
    """
    Interface principal para exponenciação modular.
    
    Calcula (base^exponent) mod modulus de forma eficiente.
    
    Args:
        base: Número base
        exponent: Expoente não-negativo
        modulus: Módulo (deve ser positivo)
        
    Returns:
        (base^exponent) mod modulus
        
    Example:
        >>> power_mod(2, 100, 1000000007)
        976371285
        >>> power_mod(3, 50, 7)
        4
    """
    if modulus <= 0:
        raise ValueError("Módulo deve ser positivo")
    
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    # Casos especiais
    if modulus == 1:
        return 0
    
    if exponent == 0:
        return 1
    
    if base == 0:
        return 0
    
    return modular_exponentiation(base, exponent, modulus) 