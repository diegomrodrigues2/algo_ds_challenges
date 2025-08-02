"""
Exemplo de Implementação Completa do Algoritmo de Exponenciação Rápida

Este arquivo contém uma implementação completa do algoritmo de exponenciação
binária para fins de demonstração e referência. Não deve ser usado nos testes.
"""


def binary_exponentiation(base: int, exponent: int) -> int:
    """Implementação completa da exponenciação binária iterativa."""
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    if exponent == 0:
        return 1
    
    if exponent == 1:
        return base
    
    result = 1
    while exponent > 0:
        if exponent & 1:  # Bit atual é 1
            result *= base
        base *= base      # Quadrar a base
        exponent >>= 1    # Mover para próximo bit
    
    return result


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """Implementação completa da exponenciação modular."""
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
    
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    
    return result


def recursive_exponentiation(base: int, exponent: int) -> int:
    """Implementação completa da exponenciação recursiva."""
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    if exponent == 0:
        return 1
    
    if exponent == 1:
        return base
    
    if exponent % 2 == 0:
        half = recursive_exponentiation(base, exponent // 2)
        return half * half
    else:
        half = recursive_exponentiation(base, (exponent - 1) // 2)
        return base * half * half


def matrix_multiply(A: list, B: list, modulus: int = None) -> list:
    """Multiplica duas matrizes 2x2."""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
            if modulus:
                result[i][j] %= modulus
    return result


def matrix_exponentiation(matrix: list, exponent: int, modulus: int = None) -> list:
    """Implementação completa da exponenciação de matriz."""
    if exponent < 0:
        raise ValueError("Expoente deve ser não-negativo")
    
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Matriz deve ser 2x2")
    
    if exponent == 0:
        return [[1, 0], [0, 1]]  # Matriz identidade
    
    if exponent == 1:
        return matrix
    
    result = [[1, 0], [0, 1]]  # Matriz identidade
    current_matrix = matrix
    
    while exponent > 0:
        if exponent & 1:
            result = matrix_multiply(result, current_matrix, modulus)
        current_matrix = matrix_multiply(current_matrix, current_matrix, modulus)
        exponent >>= 1
    
    return result


def fibonacci_fast(n: int, modulus: int = None) -> int:
    """Implementação completa do Fibonacci rápido."""
    if n < 0:
        raise ValueError("Índice deve ser não-negativo")
    
    if n <= 1:
        return n
    
    # Matriz de Fibonacci: [[1, 1], [1, 0]]
    fib_matrix = [[1, 1], [1, 0]]
    
    # Calcular F(n) usando exponenciação de matriz
    # [F(n+1), F(n)] = [[1, 1], [1, 0]]^n * [1, 0]
    matrix_power = matrix_exponentiation(fib_matrix, n - 1, modulus)
    
    # O resultado é matrix_power[0][0] (F(n))
    return matrix_power[0][0]


def power_mod(base: int, exponent: int, modulus: int) -> int:
    """Interface principal para exponenciação modular."""
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


if __name__ == "__main__":
    # Exemplos de uso
    print("🚀 Testes do Algoritmo de Exponenciação Rápida\n")
    
    # Teste 1: Exponenciação básica
    print("📊 Exponenciação Básica:")
    print(f"   2^10 = {binary_exponentiation(2, 10)}")
    print(f"   3^5 = {binary_exponentiation(3, 5)}")
    print(f"   5^3 = {binary_exponentiation(5, 3)}")
    print()
    
    # Teste 2: Exponenciação modular
    print("📊 Exponenciação Modular:")
    print(f"   2^10 mod 1000 = {modular_exponentiation(2, 10, 1000)}")
    print(f"   3^100 mod 7 = {modular_exponentiation(3, 100, 7)}")
    print(f"   2^100 mod 1000000007 = {modular_exponentiation(2, 100, 1000000007)}")
    print()
    
    # Teste 3: Fibonacci rápido
    print("📊 Fibonacci Rápido:")
    print(f"   F(10) = {fibonacci_fast(10)}")
    print(f"   F(20) = {fibonacci_fast(20)}")
    print(f"   F(100) mod 1000000007 = {fibonacci_fast(100, 1000000007)}")
    print()
    
    # Teste 4: Comparação com exponenciação tradicional
    print("📊 Comparação com Tradicional:")
    base, exp = 2, 10
    traditional = base ** exp
    binary = binary_exponentiation(base, exp)
    print(f"   {base}^{exp} = {traditional}")
    print(f"   Binário: {binary}")
    print(f"   ✅ Correto: {traditional == binary}")
    print()
    
    # Teste 5: Exponenciação de matriz
    print("📊 Exponenciação de Matriz:")
    matrix = [[1, 1], [1, 0]]
    result = matrix_exponentiation(matrix, 5)
    print(f"   [[1, 1], [1, 0]]^5 = {result}")
    print(f"   F(6) = {result[0][0]}, F(5) = {result[0][1]}") 